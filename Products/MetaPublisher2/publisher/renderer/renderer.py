# -*- coding: iso-8859-15 -*-
# ============================================================================
#
#                         M e t a  P u b l i s h e r  2
#
# ----------------------------------------------------------------------------
# Copyright (c) 2002-2013, Sebastian Lühnsdorf - Web-Solutions and others
# For more information see the README.txt file or visit www.metapulisher.org
# ----------------------------------------------------------------------------
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).
#
# A copy of the ZPL should accompany this distribution.
#
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE
#
# ============================================================================

__doc__ = """Renderer Component

API and ZMI services for rendering Frontends. A previously defined Frontend must
be rendered for it to be publically viewable. A Frontend only stores the
definition of the final public interface as such is not publically viewable.
Users can choose the destination for the public interface, relative to the
MetaPublisher 2 instance.

$Id: publisher/renderer/renderer.py 13 2013-05-10 23:03:58Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.library import ClassSecurityInfo, DTMLFile, false, InitializeClass, manage_addPythonScript, permission_publish_frontends, RenderError, show_future, true


# ============================================================================
# Module Exports

__all__ = [
    'Renderer',
]


# ============================================================================
# Renderer Component Mix-In Class

class Renderer:
    """!TXT! Renderer Component Mix-In Class"""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # Renderer ZMI Forms

    if show_future:

        security.declareProtected(permission_publish_frontends, 'renderer_form')

        renderer_form = DTMLFile('renderer', globals())

    # ------------------------------------------------------------------------
    # Renderer Retrieval API

    security.declareProtected(permission_publish_frontends, 'is_frontend_modified')

    def is_frontend_modified(self, frontend_path):
        """!TXT! Return True if the specified Frontend has been changed since last rendering, False if not and None if Frontend is unrendered."""

        frontend = self.get_frontend(frontend_path)
        if hasattr(frontend, 'is_frontend_modified'):
            return frontend.is_frontend_modified()
        return None

    security.declareProtected(permission_publish_frontends, 'is_frontend_renderable')

    def is_frontend_renderable(self, frontend_path):
        """!TXT! Return True if the specified Frontend can be rendered, False otherwise."""

        frontend = self.get_frontend(frontend_path)
        if hasattr(frontend, 'is_frontend_renderable'):
            return frontend.is_frontend_renderable()
        return false

    security.declareProtected(permission_publish_frontends, 'get_rendering_errors')

    def get_rendering_errors(self, frontend_path):
        """!TXT! Return a list of errors of the specified Frontend."""

        frontend = self.get_frontend(frontend_path)
        if hasattr(frontend, 'get_rendering_errors'):
            return frontend.get_rendering_errors()
        return []

    # ------------------------------------------------------------------------
    # Renderer Mutation API

    security.declareProtected(permission_publish_frontends, 'render_frontends')

    def render_frontends(self, ids, destination, acquired_destination_path=None, arbitrary_destination_path=None, create_folder=false, create_folder_id=None, overwrite='fail', REQUEST=None):
        """!TXT! Render Interface objects"""

        rendered_frontends = []

        # determine ids
        if ids == '*':
            ids = self.frontend_paths()

        # determine destination
        render_base = self.get_MetaPublisher2()
        if destination == 'inside':
            get_MetaPublisher2_code = '''container.get_MetaPublisher2()'''
        elif destination == 'parent':
            render_base = render_base.aq_parent
            get_MetaPublisher2_code = '''container[ '%s' ]''' % self.get_MetaPublisher2().getId()
        elif destination == 'acquired':
            if not acquired_destination_path:
                raise ValueError('!TXT! Path for acquired destination must be specified.')
            render_base = render_base.aq_parent
            for id in acquired_destination_path.split('/'):
                if id:
                    render_base = render_base._getOb(id)
            get_MetaPublisher2_code = '''container[ '%s' ]''' % self.get_MetaPublisher2().getId()
        elif destination == 'arbitrary':
            if not arbitrary_destination_path:
                raise ValueError('!TXT! Path for arbitrary destination must be specified.')
            render_base = self.getPhysicalRoot()
            for id in arbitrary_destination_path.split('/'):
                if id:
                    render_base = render_base._getOb(id)
            get_MetaPublisher2_code = '''container.getPhysicalRoot()'''
            for id in self.get_MetaPublisher2_url()[len(self.getPhysicalRoot().absolute_url()) + 1:].split('/'):
                get_MetaPublisher2_code = get_MetaPublisher2_code + '.' + id
        else:
            raise ValueError('!TXT! Unknown destination mode "%s".' % destination)

        # check overwrite mode
        if not overwrite in ['fail', 'none', 'all', 'replace']:
            raise ValueError('!TXT! Unknown overwrite mode "%s".' % overwrite)

        # create destination Folder
        if create_folder:
            if not create_folder_id:
                raise ValueError('!TXT! Id for Folder must be specified.')
            if create_folder_id in render_base.objectIds():
                if overwrite == 'fail':
                    raise RenderError('!TXT! Folder "%s" already exists.' % create_folder_id)
                elif overwrite == 'replace':
                    render_base.manage_delObject(create_folder_id)
                    render_base.manage_addFolder(create_folder_id)
            else:
                render_base.manage_addFolder(create_folder_id)
            render_base = render_base._getOb(create_folder_id)
        elif overwrite == 'replace':
            for id, object in render_base.objectItems():
                if not(id == 'acl_users' or object.meta_type.startswith('MetaPublisher2')):
                    render_base.manage_delObject(id)

        # create MetaPublisher2 instance retrieval method
        do_render = true
        if 'get_MetaPublisher2' in render_base.objectIds():
            if overwrite == 'fail':
                raise RenderError('!TXT! MetaPublisher2 instance retrieval method with id "get_MetaPublisher" already exists.')
            elif overwrite == 'none':
                do_render = false
            elif overwrite == 'all':
                render_base.manage_delObject('get_MetaPublisher2')
        if do_render:
            manage_addPythonScript(render_base, 'get_MetaPublisher2')
            render_base._getOb('get_MetaPublisher2').ZPythonScript_edit('', 'return %s' % get_MetaPublisher2_code)
            rendered_frontends.append('get_MetaPublisher2')

        # render all specified objects
        for id in ids:

            # retrieve object to render
            frontend = self.get_frontend(id)
            object_base = render_base
            path = id.split('/')
            if len(path) > 1:
                for path_id in path[: -1]:
                    if path_id:
                        object_base = object_base._getOb(path_id)

            # object is Frontend plugin
            if IFrontendPluginBase.providedBy(found_object):
                do_render = true
                rendering_ids = frontend.rendering_ids()
                for rendering_id in rendering_ids:
                    if rendering_id in object_base.objectIds():
                        if overwrite == 'fail':
                            raise RenderError('!TXT! An object with id "%s" already exists.' % rendering_id)
                        elif overwrite == 'none':
                            do_render = false
                        elif overwrite == 'all':
                            render_base.manage_delObject(rendering_id)
                if do_render:
                    frontend.render_frontend(object_base)
                    rendered_frontends.append(id)

            # object is OFS object
            else:

                # only copy if object was not already recursively copied
                if not id in rendered_frontends:
                    frontend_id = frontend.getId()
                    do_render = true
                    if overwrite == 'fail':
                        raise RenderError('!TXT! An object with id "%s" already exists.' % frontend_id)
                    elif overwrite == 'none':
                        do_render = false
                    elif overwrite == 'all':
                        render_base.manage_delObject('get_MetaPublisher2')
                    if do_render:

                        # copy the object and its content
                        object_base.manage_pasteObjects(frontend.aq_parent.manage_copyObjects(frontend_id))
                        rendered_object = object_base._getOb(frontend_id)

                        # iterate through all subobjects
                        for found_id, found_object in rendered_object.ZopeFind(rendered_object, search_sub=1):

                            # delete Frontend plugins (they must be rendered)
                            if IFrontendPluginBase.providedBy(found_object):
                                parent_object = found_object.aq_parent
                                parent_object.manage_delObject(found_id.split('/')[-1])

                                # old render stuff
                                #parent_object = rendered_object
                                #path = found_id.split('/')
                                #if len(path) > 1:
                                #    for path_id in path[ : -1 ]:
                                #        if path_id:
                                #            parent_object = parent_object._getOb(path_id)
                                #parent_object.manage_delObjects([ path[ -1 ], ])

                            # append OFS objects to list of rendered frontends
                            else:
                                rendered_frontends.append(id + '/' + found_id)

                        rendered_frontends.append(id)

        self.redirect(
            REQUEST,
            'frontends_form',
            message='!TXT! %d Frontends rendered.' % (rendered_frontends and len(rendered_frontends) or 'No')
        )

# ----------------------------------------------------------------------------
# Class Security

InitializeClass(Renderer)

# !!! renderer.py - remove code to 2.4
# TODO renderer.py - revise api and make use of new api
# TODO renderer.py - refactor and break up rendering method
