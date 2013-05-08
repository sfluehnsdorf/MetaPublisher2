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

__doc__ = """Widgets Component

!TXT! module info

$Id: publisher/widgets/widgets.py 8 2013-05-08 19:01:56Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.interfaces import IWidgetPluginBase
from Products.MetaPublisher2.library import ClassSecurityInfo, DTMLFile, InitializeClass, permission_manage, permission_manage_frontends, show_future


# ============================================================================
# Module Exports

__all__ = [
    'Widgets',
]


# ============================================================================
# Widgets Component Mix-In Class

class Widgets:
    """!TXT! Widgets Component Mix-In Class"""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # Widget ZMI Forms

    if show_future:

        security.declareProtected(permission_manage_frontends, 'widgets_form')

        widgets_form = DTMLFile('widgets', globals())

    # ------------------------------------------------------------------------
    # Widget Plugin API

    security.declareProtected(permission_manage, 'has_widgetplugins')

    def has_widgetplugins(self):
        """!TXT! Return the specified MetaPublisher2 Widget plugin"""

        return self.has_plugins(IWidgetPluginBase)

    security.declareProtected(permission_manage, 'get_widgetplugin')

    def get_widgetplugin(self, widgetplugin_id):
        """!TXT! Return the specified MetaPublisher2 Widget plugin"""

        return self.get_plugin(widgetplugin_id, IWidgetPluginBase)

    security.declareProtected(permission_manage, 'widgetplugin_ids')

    def widgetplugin_ids(self):
        """!TXT! Return ids of installed MetaPublisher2 Widget plugins"""

        return self.plugin_ids(IWidgetPluginBase)

    security.declareProtected(permission_manage, 'widgetplugin_items')

    def widgetplugin_items(self):
        """!TXT! Return tuples of id, value of installed MetaPublisher2 Widget plugins"""

        return self.plugin_items(IWidgetPluginBase)

    security.declareProtected(permission_manage, 'widgetplugin_values')

    def widgetplugin_values(self):
        """!TXT! Return tuples of id, value of installed MetaPublisher2 Widget plugins"""

        return self.plugin_values(IWidgetPluginBase)

    # ------------------------------------------------------------------------
    # Widget Flag Retrieval

    security.declareProtected(permission_manage, 'get_widgetflags')

    def get_widgetflags(self, frontend_path, widget_id):
        """!TXT! Return tuples of id, boolean states of all Plugin flags"""

        widget = get_widget(self, frontend_path, widget_id)
        return widget.get_widgetflags()

    security.declareProtected(permission_manage, 'get_widgetflag_ids')

    def get_widgetflag_ids(self, frontend_path, widget_id):
        """!TXT! Return the ids of all Plugin flags"""

        widget = get_widget(self, frontend_path, widget_id)
        return widget.get_widgetflag_ids()

    security.declareProtected(permission_manage, 'get_widgetflag')

    def get_widgetflag(self, frontend_path, widget_id, pluginflag_id):
        """!TXT! Return the boolean state of the specified Widget flag if it exists, raises KeyError otherwise"""

        widget = get_widget(self, frontend_path, widget_id)
        return widget.get_pluginflag(pluginflag_id)

    security.declareProtected(permission_manage, 'has_widgetflag')

    def has_widgetflag(self, frontend_path, widget_id, pluginflag_id):
        """!TXT! Return True if the Widget flag exists, False otherwise"""

        widget = get_widget(self, frontend_path, widget_id)
        return widget.has_pluginflag(pluginflag_id)

    # ------------------------------------------------------------------------
    # Widget Matching API

    security.declareProtected(permission_manage_frontends, 'get_fields_for_widget')

    def get_fields_for_widget(self, widget_type_id):
        """!TXT! Return a list of Fields appropriate for the specified Widget type."""

        # TODO: get_fields_for_widget
        raise NotImplemented

    security.declareProtected(permission_manage_frontends, 'get_widgets_for_field')

    def get_widgets_for_field(self, frontend_type_id, field_type_id):
        """!TXT! Return a list of Widgets appropriate for the passed Field type"""

        def sort_widgets(x, y):
            return cmp(x[0], y[0])

        result = []
        for id, plugin in self.widgetplugin_items():
            frontend_type_ids = plugin['instance'].frontend_types
            field_type_ids = plugin['instance'].field_types
            if frontend_type_id in frontend_type_ids and field_type_id in field_type_ids:
                rating = field_type_ids.index(field_type_id)
                result.append((rating, (id, plugin)))
        result.sort(sort_widgets)
        return map(lambda item: item[1], result)

    # ------------------------------------------------------------------------
    # Widget Retrieval API

    security.declareProtected(permission_manage_frontends, 'get_widget')

    def get_widget(self, frontend_path, widget_id):
        """!TXT! Return the specified Frontend's Widget."""

        frontend = self.get_frontend(frontend_path)
        return frontend.get_widget(widget_id)

    security.declareProtected(permission_manage_frontends, 'widget_ids')

    def widget_ids(self, frontend_path):
        """!TXT! Return the ids of Widgets of the specified Frontend."""

        frontend = self.get_frontend(frontend_path)
        return frontend.widget_ids()

    security.declareProtected(permission_manage_frontends, 'widget_items')

    def widget_items(self, frontend_path):
        """!TXT! Return tuples of id, object of the specified Frontend's Widgets."""

        frontend = self.get_frontend(frontend_path)
        return frontend.widget_items()

    security.declareProtected(permission_manage_frontends, 'widget_values')

    def widget_values(self, frontend_path):
        """!TXT! Return the objects of the specified Frontend's Widgets."""

        frontend = self.get_frontend(frontend_path)
        return frontend.widget_values()

    # ------------------------------------------------------------------------
    # Widget Mutation API

    security.declareProtected(permission_manage_frontends, 'add_widget')

    def add_widget(self, frontend_path, widget_type_id, options={}, REQUEST=None, **args):
        """!TXT! Add a new Widget in the specified Frontend with specified type and configuration."""

        # TODO: add_widgets
        raise NotImplemented

    security.declareProtected(permission_manage_frontends, 'edit_widget')

    def edit_widget(self, frontend_path, widget_id, widget_type_id, options={}, REQUEST=None, **args):
        """!TXT! Change the specified Widget's configuration."""

        # !!! widgets.py - implement edit_widget
        raise NotImplemented

    security.declareProtected(permission_manage_frontends, 'delete_widget')

    def delete_widget(self, frontend_path, widget_id, REQUEST=None):
        """!TXT! Delete the specified Widget in the specified Frontend."""

        # TODO: del_widget
        raise NotImplemented

    security.declareProtected(permission_manage_frontends, 'delete_widgets')

    def delete_widgets(self, frontend_path, widget_ids=[], REQUEST=None):
        """!TXT! Delete the specified Widgets in the specified Frontend."""

        # !!! widgets.py - implement del_widgets
        raise NotImplemented

    security.declareProtected(permission_manage_frontends, 'duplicate_widget')

    def duplicate_widget(self, frontend_path, widget_id, REQUEST=None):
        """!TXT! Duplicate the specified Widget in the specified Frontend."""

        # TODO: del_widget
        raise NotImplemented

    security.declareProtected(permission_manage_frontends, 'delete_widgets')

    def delete_widgets(self, frontend_path, widget_ids=[], REQUEST=None):
        """!TXT! Delete the specified Widgets in the specified Frontend."""

        # !!! widgets.py - implement del_widgets
        raise NotImplemented

    security.declareProtected(permission_manage_frontends, 'delete_widget')

    def delete_widget(self, frontend_path, widget_id, REQUEST=None):
        """!TXT! Delete the specified Widget in the specified Frontend."""

        # TODO: del_widget
        raise NotImplemented

    security.declareProtected(permission_manage_frontends, 'delete_widgets')

    def delete_widgets(self, frontend_path, widget_ids=[], REQUEST=None):
        """!TXT! Delete the specified Widgets in the specified Frontend."""

        # !!! widgets.py - implement del_widgets
        raise NotImplemented

    # ------------------------------------------------------------------------
    # Widget Ordering API

    security.declareProtected(permission_manage_frontends, 'get_widget_position')

    def get_widget_position(self, frontend_path, widget_id):
        """!TXT! Return the position of a Widget"""

        # !!! widgets.py - implement get_widget_position
        raise NotImplemented

    security.declareProtected(permission_manage_frontends, 'move_widget_to_position')

    def move_widget_to_position(self, frontend_path, widget_id, position, REQUEST=None):
        """!TXT! Move a Widget to the specified position"""

        # !!! widgets.py - implement move_widget_to_position
        raise NotImplemented

    security.declareProtected(permission_manage_frontends, 'move_widget_to_top')

    def move_widget_to_top(self, frontend_path, widget_id, REQUEST=None):
        """!TXT! Move a Widget to the top"""

        # !!! widgets.py - implement move_widget_top
        raise NotImplemented

    security.declareProtected(permission_manage_frontends, 'move_widget_up')

    def move_widget_up(self, frontend_path, widget_id, REQUEST=None):
        """!TXT! Move a Widget up one position"""

        # !!! widgets.py - implement move_widget_up
        raise NotImplemented

    security.declareProtected(permission_manage_frontends, 'move_widget_down')

    def move_widget_down(self, frontend_path, widget_id, REQUEST=None):
        """!TXT! Move a Widget down one position"""

        # !!! widgets.py - implement move_widget_down
        raise NotImplemented

    security.declareProtected(permission_manage_frontends, 'move_widget_to_bottom')

    def move_widget_to_bottom(self, frontend_path, widget_id):
        """!TXT! Move a Widget to the bottom"""

        # !!! widgets.py - implement move_widget_to_bottom
        raise NotImplemented

# ----------------------------------------------------------------------------
# Class Security

InitializeClass(Widgets)

# !!! widgets.py - form/formlet handler for add_widget
# !!! widgets.py - form/formlet handler for edit_widget
# !!! widgets.py - revise API and comments
#     widgets.py must manage widgets in frontends and widgetsfolder
#     either provide two sets of methods or handle in widgetsfolder if frontend_path is None
# !!! widgets.py - missing add_widget.dtml
# !!! widgets.py - missing delete_widgets.dtml
# !!! widgets.py - missing duplicate_widgets.dtml
# !!! widgets.py - missing edit_widget.dtml
# !!! widgets.py - missing preview_widget.dtml
# !!! widgets.py - missing rename_widgets.dtml
