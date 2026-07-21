"""MetaPublisher2 - Widgets Component."""


from Products.MetaPublisher2.interfaces import IWidgetPluginBase
from Products.MetaPublisher2.library.application import (
    permission_manage, permission_manage_frontends)
from Products.MetaPublisher2.library.common import (
    ClassSecurityInfo, DTMLFile, InitializeClass)
from Products.MetaPublisher2.library.compatibility import show_future


# ============================================================================
# Module Exports

__all__ = [
    'Widgets',
]


# ============================================================================
# Widgets Component Mix-In Class

class Widgets:
    """Widgets Component Mix-In Class."""

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
        """Return the specified MetaPublisher2 Widget plugin."""
        return self.has_plugins(IWidgetPluginBase)

    security.declareProtected(permission_manage, 'get_widgetplugin')

    def get_widgetplugin(self, widgetplugin_id):
        """Return the specified MetaPublisher2 Widget plugin."""
        return self.get_plugin(widgetplugin_id, IWidgetPluginBase)

    security.declareProtected(permission_manage, 'widgetplugin_ids')

    def widgetplugin_ids(self):
        """Return ids of Widget plugins."""
        return self.plugin_ids(IWidgetPluginBase)

    security.declareProtected(permission_manage, 'widgetplugin_items')

    def widgetplugin_items(self):
        """Return tuples of id, value of Widget plugins."""
        return self.plugin_items(IWidgetPluginBase)

    security.declareProtected(permission_manage, 'widgetplugin_values')

    def widgetplugin_values(self):
        """Return tuples of id, value of Widget plugins."""
        return self.plugin_values(IWidgetPluginBase)

    # ------------------------------------------------------------------------
    # Widget Flag Retrieval

    security.declareProtected(permission_manage, 'get_widgetflags')

    def get_widgetflags(self, frontend_path, widget_id):
        """Return tuples of id, boolean states of all Plugin flags."""
        widget = self.get_widget(self, frontend_path, widget_id)
        return widget.get_widgetflags()

    security.declareProtected(permission_manage, 'get_widgetflag_ids')

    def get_widgetflag_ids(self, frontend_path, widget_id):
        """Return the ids of all Plugin flags."""
        widget = self.get_widget(self, frontend_path, widget_id)
        return widget.get_widgetflag_ids()

    security.declareProtected(permission_manage, 'get_widgetflag')

    def get_widgetflag(self, frontend_path, widget_id, pluginflag_id):
        """Return state of the Widget flag if it exists."""
        widget = self.get_widget(self, frontend_path, widget_id)
        return widget.get_pluginflag(pluginflag_id)

    security.declareProtected(permission_manage, 'has_widgetflag')

    def has_widgetflag(self, frontend_path, widget_id, pluginflag_id):
        """Return True if the Widget flag exists, False otherwise."""
        widget = self.get_widget(self, frontend_path, widget_id)
        return widget.has_pluginflag(pluginflag_id)

    # ------------------------------------------------------------------------
    # Widget Matching API

    security.declareProtected(
        permission_manage_frontends, 'get_fields_for_widget')

    def get_fields_for_widget(self, widget_type_id):
        """Return a list of Fields appropriate for the Widget type."""
        # TODO widgets.py - implement get_fields_for_widget
        raise NotImplementedError

    security.declareProtected(
        permission_manage_frontends, 'get_widgets_for_field')

    def get_widgets_for_field(self, frontend_type_id, field_type_id):
        """Return a list Widgets appropriate for the passed Field type."""

        def sort_widgets(x, y):
            return cmp(x[0], y[0])

        result = []
        for id, plugin in self.widgetplugin_items():
            frontend_type_ids = plugin['instance'].frontend_types
            field_type_ids = plugin['instance'].field_types
            if (
                frontend_type_id in frontend_type_ids and
                field_type_id in field_type_ids
            ):
                rating = field_type_ids.index(field_type_id)
                result.append((rating, (id, plugin)))
        result.sort(sort_widgets)
        return map(lambda item: item[1], result)

    # ------------------------------------------------------------------------
    # Widget Retrieval API

    security.declareProtected(permission_manage_frontends, 'get_widget')

    def get_widget(self, frontend_path, widget_id):
        """Return the specified Frontend's Widget."""
        frontend = self.get_frontend(frontend_path)
        return frontend.get_widget(widget_id)

    security.declareProtected(permission_manage_frontends, 'widget_ids')

    def widget_ids(self, frontend_path):
        """Return the ids of Widgets of the specified Frontend."""
        frontend = self.get_frontend(frontend_path)
        return frontend.widget_ids()

    security.declareProtected(permission_manage_frontends, 'widget_items')

    def widget_items(self, frontend_path):
        """Return tuples of id, object of the specified Frontend's Widgets."""
        frontend = self.get_frontend(frontend_path)
        return frontend.widget_items()

    security.declareProtected(permission_manage_frontends, 'widget_values')

    def widget_values(self, frontend_path):
        """Return the objects of the specified Frontend's Widgets."""
        frontend = self.get_frontend(frontend_path)
        return frontend.widget_values()

    # ------------------------------------------------------------------------
    # Widget Mutation API

    security.declareProtected(permission_manage_frontends, 'add_widget')

    def add_widget(
        self, frontend_path, widget_type_id, options={}, REQUEST=None, **args
    ):
        """Add a new Widget in the specified Frontend."""
        # TODO widgets.py - implement add_widgets
        raise NotImplementedError

    security.declareProtected(permission_manage_frontends, 'edit_widget')

    def edit_widget(
        self, frontend_path, widget_id, widget_type_id, options={},
        REQUEST=None, **args
    ):
        """Change the specified Widget's configuration."""
        # TODO widgets.py - implement edit_widget
        raise NotImplementedError

    security.declareProtected(permission_manage_frontends, 'delete_widget')

    def delete_widget(self, frontend_path, widget_id, REQUEST=None):
        """Delete the specified Widget in the specified Frontend."""
        # TODO widgets.py - implement delete_widget
        raise NotImplementedError

    security.declareProtected(permission_manage_frontends, 'delete_widgets')

    def delete_widgets(self, frontend_path, widget_ids=[], REQUEST=None):
        """Delete the specified Widgets in the specified Frontend."""
        # TODO widgets.py - implement delete_widgets
        raise NotImplementedError

    security.declareProtected(permission_manage_frontends, 'duplicate_widget')

    def duplicate_widget(self, frontend_path, widget_id, new_id, REQUEST=None):
        """Duplicate the specified Widget in the specified Frontend."""
        # TODO widgets.py - implement duplicate_widget
        raise NotImplementedError

    security.declareProtected(permission_manage_frontends, 'duplicate_widgets')

    def duplicate_widgets(
        self, frontend_path, widget_ids, new_ids, REQUEST=None
    ):
        """Duplicate the specified Widgets in the specified Frontend."""
        # TODO widgets.py - implement duplicate_widgets
        raise NotImplementedError

    security.declareProtected(permission_manage_frontends, 'rename_widget')

    def rename_widget(self, frontend_path, widget_id, new_id, REQUEST=None):
        """Rename the specified Widget in the specified Frontend."""
        # TODO widgets.py - implement rename_widget
        raise NotImplementedError

    security.declareProtected(permission_manage_frontends, 'rename_widgets')

    def rename_widgets(self, frontend_path, widget_ids, new_ids, REQUEST=None):
        """Rename the specified Widgets in the specified Frontend."""
        # TODO widgets.py - implement rename_widgets
        raise NotImplementedError

    # ------------------------------------------------------------------------
    # Widget Ordering API

    security.declareProtected(
        permission_manage_frontends, 'get_widget_position')

    def get_widget_position(self, frontend_path, widget_id):
        """Return the position of a Widget."""
        # TODO widgets.py - implement get_widget_position
        raise NotImplementedError

    security.declareProtected(
        permission_manage_frontends, 'move_widget_to_position')

    def move_widget_to_position(
        self, frontend_path, widget_id, position, REQUEST=None
    ):
        """Move a Widget to the specified position."""
        # TODO widgets.py - implement move_widget_to_position
        raise NotImplementedError

    security.declareProtected(
        permission_manage_frontends, 'move_widget_to_top')

    def move_widget_to_top(self, frontend_path, widget_id, REQUEST=None):
        """Move a Widget to the top."""
        # TODO widgets.py - implement move_widget_top
        raise NotImplementedError

    security.declareProtected(permission_manage_frontends, 'move_widget_up')

    def move_widget_up(self, frontend_path, widget_id, REQUEST=None):
        """Move a Widget up one position."""
        # TODO widgets.py - implement move_widget_up
        raise NotImplementedError

    security.declareProtected(permission_manage_frontends, 'move_widget_down')

    def move_widget_down(self, frontend_path, widget_id, REQUEST=None):
        """Move a Widget down one position."""
        # TODO widgets.py - implement move_widget_down
        raise NotImplementedError

    security.declareProtected(
        permission_manage_frontends, 'move_widget_to_bottom')

    def move_widget_to_bottom(self, frontend_path, widget_id):
        """Move a Widget to the bottom."""
        # TODO widgets.py - implement move_widget_to_bottom
        raise NotImplementedError


# ----------------------------------------------------------------------------
# Class Security

InitializeClass(Widgets)

# TODO widgets.py - form/formlet handler for add_widget
# TODO widgets.py - form/formlet handler for edit_widget
# TODO widgets.py - revise API and comments
#      widgets.py must manage widgets in frontends and widgetsfolder
#      either provide two sets of methods or handle in widgetsfolder if
#      frontend_path is None
# TODO widgets.py - missing add_widget.dtml
# TODO widgets.py - missing delete_widgets.dtml
# TODO widgets.py - missing duplicate_widgets.dtml
# TODO widgets.py - missing edit_widget.dtml
# TODO widgets.py - missing preview_widget.dtml
# TODO widgets.py - missing rename_widgets.dtml
