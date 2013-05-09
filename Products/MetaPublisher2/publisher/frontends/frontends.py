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

__doc__ = """Frontends Component

API and ZMI services for managing Frontends. Frontends store the definition of
the public interface for the MetaPublisher 2. Once they are rendered, they
provide a public interface to the functions of the MetaPublisher 2, such as
Entry management. Frontends can be added, edited, deleted, renamed and moved as
well as retrieved, listed and tested for existence.

$Id: publisher/frontends/frontends.py 17 2013-05-08 23:43:57Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.interfaces import IFrontendPluginBase
from Products.MetaPublisher2.library import ClassSecurityInfo, DTMLFile, false, InitializeClass, permission_manage, permission_manage_frontends, true


# ============================================================================
# Module Exports

__all__ = [
    'Frontends',
]


# ============================================================================
# Frontends Component Mix-In Class

class Frontends:
    """!TXT! Frontends Component Mix-In Class"""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # Frontend ZMI Forms

    security.declareProtected(permission_manage_frontends, 'frontends_form')

    frontends_form = DTMLFile('frontends', globals())

    security.declareProtected(permission_manage_frontends, 'add_frontend_form')

    add_frontend_form = DTMLFile('add_frontend', globals())

    security.declareProtected(permission_manage_frontends, 'duplicate_frontends_form')

    duplicate_frontends_form = DTMLFile('duplicate_frontends', globals())

    security.declareProtected(permission_manage_frontends, 'delete_frontends_form')

    delete_frontends_form = DTMLFile('delete_frontends', globals())

    security.declareProtected(permission_manage_frontends, 'edit_frontend_form')

    edit_frontend_form = DTMLFile('edit_frontend', globals())

    security.declareProtected(permission_manage_frontends, 'move_frontends_form')

    move_frontends_form = DTMLFile('move_frontends', globals())

    security.declareProtected(permission_manage_frontends, 'rename_frontends_form')

    rename_frontends_form = DTMLFile('rename_frontends', globals())

    # ------------------------------------------------------------------------
    # Frontend Plugins

    security.declareProtected(permission_manage, 'has_frontendplugins')

    def has_frontendplugins(self):
        """!TXT! Return the specified MetaPublisher2 Frontend plugin"""

        return self.has_plugins(IFrontendPluginBase)

    security.declareProtected(permission_manage, 'get_frontendplugin')

    def get_frontendplugin(self, frontendplugin_id):
        """!TXT! Return the specified MetaPublisher2 Frontend plugin"""

        return self.get_plugin(frontendplugin_id, IFrontendPluginBase)

    security.declareProtected(permission_manage, 'frontendplugin_ids')

    def frontendplugin_ids(self):
        """!TXT! Return ids of installed MetaPublisher2 Frontend plugins"""

        return self.plugin_ids(IFrontendPluginBase)

    security.declareProtected(permission_manage, 'frontendplugin_items')

    def frontendplugin_items(self):
        """!TXT! Return tuples of id, value of installed MetaPublisher2 Frontend plugins"""

        return self.plugin_items(IFrontendPluginBase)

    security.declareProtected(permission_manage, 'frontendplugin_values')

    def frontendplugin_values(self):
        """!TXT! Return tuples of id, value of installed MetaPublisher2 Frontend plugins"""

        return self.plugin_values(IFrontendPluginBase)

    # ------------------------------------------------------------------------
    # Frontend Flag Retrieval

    security.declareProtected(permission_manage, 'get_frontendflags')

    def get_frontendflags(self, frontend_path):
        """!TXT! Return tuples of id, boolean states of all Plugin flags"""

        frontend = get_frontend(self, frontend_path)
        return frontend.get_frontendflags()

    security.declareProtected(permission_manage, 'get_frontendflag_ids')

    def get_frontendflag_ids(self, frontend_path):
        """!TXT! Return the ids of all Plugin flags"""

        frontend = get_frontend(self, frontend_path)
        return frontend.get_frontendflag_ids()

    security.declareProtected(permission_manage, 'get_frontendflag')

    def get_frontendflag(self, frontend_path, pluginflag_id):
        """!TXT! Return the boolean state of the specified Frontend flag if it exists, raises KeyError otherwise"""

        frontend = get_frontend(self, frontend_path)
        return frontend.get_pluginflag(pluginflag_id)

    security.declareProtected(permission_manage, 'has_frontendflag')

    def has_frontendflag(self, frontend_path, pluginflag_id):
        """!TXT! Return True if the Frontend flag exists, False otherwise"""

        frontend = get_frontend(self, frontend_path)
        return frontend.has_pluginflag(pluginflag_id)

    # -------------------------------------------------------------
    # Frontends Retrieval API

    def _traverse_frontend_path(self, path):
        """!TXT!"""

        path_object = self.frontends
        if path:
            for id in path.split('/'):
                path_object = path_object._getOb(id)
        return path_object

    security.declareProtected(permission_manage_frontends, 'has_frontends')

    def has_frontends(self):
        """!TXT!"""

        return self.frontend_paths() and true or false

    security.declareProtected(permission_manage_frontends, 'has_frontend')

    def has_frontend(self, path):
        """!TXT!"""

        try:
            self._traverse_frontend_path(path)
            return true
        except:
            return false

    security.declareProtected(permission_manage_frontends, 'frontendpath_paths')

    def frontendpath_paths(self):
        """!TXT!"""

        return map(lambda item: item[0], self.frontendpath_items())

    security.declareProtected(permission_manage_frontends, 'frontendpath_items')

    def frontendpath_items(self):
        """!TXT!"""

        paths = []
        paths_append = paths.append
        for path, frontend in self.frontend_items():
            if getattr(frontend, 'isPrincipiaFolderish', None) and not IPluginBase.providedBy(frontend):
                paths_append((path, frontend))
        return paths

    security.declareProtected(permission_manage_frontends, 'frontendpath_values')

    def frontendpath_values(self):
        """!TXT!"""

        return map(lambda item: item[1], self.frontendpath_items())

    security.declareProtected(permission_manage_frontends, 'frontend_paths')

    def frontend_paths(self, path=None, recursive=true):
        """!TXT! Return the paths of Frontends."""

        return map(lambda item: item[0], self.frontend_items(path, recursive))

    security.declareProtected(permission_manage_frontends, 'frontend_items')

    def frontend_items(self, path=None, recursive=true):
        """!TXT!"""

        def sort_items(x, y):
            return cmp(x[0], y[0])

        result = []
        result_append = result.append
        base = self._traverse_frontend_path(path)
        top = self.frontends
        prefix_len = len(top.absolute_url()) + 1
        frontends = top.objectValues()
        while frontends:
            frontend = frontends.pop()
            if not IFrontendPluginBase.providedBy(frontend):
                frontends = frontends + list(frontend.objectValues())
            if not IWidgetPluginBase.providedBy(frontend):
                result_append((frontend.absolute_url()[prefix_len:], frontend))
        result.sort(sort_items)
        return result

    security.declareProtected(permission_manage_frontends, 'frontend_values')

    def frontend_values(self, path=None, recursive=true):
        """!TXT!"""

        return map(lambda item: item[1], self.frontend_items(path, recursive))

    security.declareProtected(permission_manage_frontends, 'get_frontend')

    def get_frontend(self, path):
        """!TXT!"""

        return self._traverse_frontend_path(path)

    security.declareProtected(permission_manage_frontends, 'get_frontend_path')

    def get_frontend_path(self, frontend):
        """!TXT! get frontend object's path"""

        # !!! frontends.py - implement get_frontend_path

        raise NotImplemented

    security.declareProtected(permission_manage_frontends, 'get_frontend_parent')

    def get_frontend_parent(self, frontend):
        """!TXT! Return the specified Frontend's parent object. If object is a string, it will be normalized and the last path element removed."""

        # !!! frontends.py - implement get_frontend_parent

        raise NotImplemented

    security.declareProtected(permission_manage_frontends, 'get_frontend_parent_path')

    def get_frontend_parent_path(self, frontend):
        """!TXT! Return the specified Frontend's parent object. If object is a string, it will be normalized and the last path element removed."""

        # !!! frontends.py - implement get_frontend_parent_path

        raise NotImplemented

    security.declareProtected(permission_manage_frontends, 'get_frontend_parents')

    def get_frontend_parents(self, frontend):
        """!TXT! Return the specified Frontend's parent objects. If object is a string, it will be normalized and the last path element removed."""

        # !!! frontends.py - implement get_frontend_parents

        raise NotImplemented

    security.declareProtected(permission_manage_frontends, 'get_frontend_rendering_ids')

    def get_frontend_rendering_ids(self, path):
        """!TXT! Return a list of all ids generated by rendering the specified Frontend."""

        frontend = self.get_frontend(path)
        return frontend.get_frontend_rendering_ids()

    # ------------------------------------------------------------------------
    # Frontend Mutation API

    security.declareProtected(permission_manage_frontends, 'add_frontend_type')

    # !!! frontends.py - update add_frontend_type to new mechanism
    # !!! frontends.py - check add_frontend_type if add factory can redirect properly to frontends_form

    def add_frontend_type(self, REQUEST=None):
        """!TXT! Add a new Frontend in the specified path with specified id and configuration."""

        path = self.get_app_url() + '/frontends' + REQUEST.get('path', '')
        frontend_type = REQUEST.get('frontend_type', '')
        if frontend_type == 'OFS':
            REQUEST.RESPONSE.redirect(path + REQUEST.get('ofs_object_type'))

        else:
            try:
                frontendplugin = self.get_plugin(REQUEST.get('frontend_type'))
                REQUEST.RESPONSE.redirect(path + frontendplugin['action'])
            except:
                self.redirect(REQUEST, 'frontends_form', '!TXT! Invalid Frontend Type')

    security.declareProtected(permission_manage_frontends, 'add_frontend')

    # !!! frontends.py - implement add_frontend

    def add_frontend(self, path, frontend_path, frontend_type_id, options={}, REQUEST=None, **args):
        """!TXT! Add a new Frontend in the specified path with specified id and configuration."""

        raise NotImplemented

    security.declareProtected(permission_manage_frontends, 'delete_frontend')

    def delete_frontend(self, path, REQUEST=None):
        """!TXT!"""

        path, frontend_id = path.rsplit('/', 1)
        base = self.get_frontend_parent(path)
        base.manage_delObjects(frontend_id)
        self.redirect(
            REQUEST,
            'frontends_form',
            message='!TXT! Frontend "%s" at "%s" deleted.' % (frontend_id, path, new_id),
            update_menu=true,
        )

    security.declareProtected(permission_manage_frontends, 'delete_frontends')

    def delete_frontends(self, paths=[], REQUEST=None):
        """!TXT!"""

        if not paths:
            raise ValueError('!TXT! No Frontends specified')
        delete_frontend = self.delete_frontend
        for path in paths:
            delete_frontend(path)
        self.redirect(
            REQUEST,
            'frontends_form',
            message='!TXT! %d Frontends deleted.' % len(paths),
            update_menu=true,
        )

    security.declareProtected(permission_manage_frontends, 'duplicate_frontend')

    def duplicate_frontend(self, path, new_id=None, REQUEST=None):
        """!TXT!"""

        path, frontend_id = path.rsplit('/', 1)
        base = _traverse_frontend_path(path)
        if not new_id:
            ids = base.objectIds()
            new_id = 'copy_of_%s' % frontend_id
            counter = 2
            while new_id in ids:
                new_id = 'copy_%d_of_%s' % (counter, frontend_id)
                counter = counter + 1
        base.manage_clone(frontend_id, new_id)
        self.redirect(
            REQUEST,
            'frontends_form',
            message='!TXT! Frontend "%s" at "%s" duplicated as "%s"' % (frontend_id, path, new_id),
            update_menu=true,
        )
        return new_id

    security.declareProtected(permission_manage_frontends, 'duplicate_frontends')

    def duplicate_frontends(self, paths, new_ids=[], REQUEST=None):
        """!TXT!"""

        if not paths:
            raise ValueError('No Frontends specified')
        elif not new_ids:
            new_ids = [None] * len(paths)
        elif len(paths) != len(new_ids):
            raise ValueError("!TXT! Number of old and new ids for duplicating Frontends mismatch.")
        result_ids = []
        result_ids_append = result.append
        duplicate_frontend = self.duplicate_frontend
        for index in range(len(paths)):
            result_ids_append(duplicate_frontend(paths[index], new_ids[index]))
        self.redirect(
            REQUEST,
            'frontends_form',
            message='!TXT! %d Frontends duplicated.' % len(result_ids),
            update_menu=true,
        )
        return result_ids

    security.declareProtected(permission_manage_frontends, 'edit_frontend')

    # !!! frontends.py - implement edit_frontend

    def edit_frontend(self, frontend_path, options={}, REQUEST=None, **args):
        """!TXT! Change the specified Frontend's configuration."""

        raise NotImplemented

    security.declareProtected(permission_manage_frontends, 'move_frontend')

    # !!! frontends.py - implement move_frontend

    def move_frontend(self, frontend_path, destination_path, REQUEST=None):
        """!TXT! Move the specified Frontend to a new container."""

        raise NotImplemented

    security.declareProtected(permission_manage_frontends, 'move_frontends')

    # !!! frontends.py - implement move_frontends

    def move_frontends(self, frontend_paths, destination_path, REQUEST=None):
        """!TXT! Move the specified Frontends to a new container."""

        raise NotImplemented

    security.declareProtected(permission_manage_frontends, 'rename_frontend')

    def rename_frontend(self, path, new_id, REQUEST=None):
        """!TXT! Rename the specified Frontend."""

        path, frontend_id = path.rsplit('/', 1)
        base = _traverse_frontend_path(path)
        base.manage_renameObject(frontend_id, new_id)
        self.redirect(
            REQUEST,
            'frontends_form',
            message='!TXT! Frontend "%s" at "%s" renamed to "%s".' % (frontend_id, path, new_id),
            update_menu=true,
        )
        return new_id

    security.declareProtected(permission_manage_frontends, 'rename_frontends')

    def rename_frontends(self, paths, new_ids, REQUEST=None):
        """!TXT! Rename the specified Frontends. Both id lists must have the same length or ValueError is raised."""

        if not paths:
            raise ValueError('!TXT! No Frontends specified')
        elif len(paths) != len(new_ids):
            raise ValueError("!TXT! Number of old and new ids for renaming Frontends mismatch.")
        result_ids = []
        result_ids_append = result.append
        rename_frontend = self.rename_frontend
        for index in range(len(paths)):
            result_ids_append(rename_frontend(paths[index], new_ids[index]))
        self.redirect(
            REQUEST,
            'frontends_form',
            message='!TXT! %d Frontends renamed.' % len(frontend_ids),
            update_menu=true,
        )
        return result_ids

# ----------------------------------------------------------------------------
# Class Security

InitializeClass(Frontends)

# !!! frontends.py - form/formlet handler for add_frontend
# !!! frontends.py - form/formlet handler for edit_frontend
# TODO frontends.py - implement frontend preview
