"""MetaPublisher2 - Legacy Widget Plugin Base."""


from Products.MetaPublisher2.bases.plugin.legacyplugin import LegacyPluginBase
from Products.MetaPublisher2.library.common import (
    ClassSecurityInfo, ComputedAttribute, InitializeClass)

from widget import WidgetPluginBase


# ============================================================================
# Module Exports

__all__ = [
    'LegacyWidgetPlugin',
]


# ============================================================================
# Legacy Widget Plugin Base Class

class LegacyWidgetPlugin(LegacyPluginBase, WidgetPluginBase):
    """Legacy Widget Plugin Base Class."""

    security = ClassSecurityInfo()

    # --------------------------------------------------------------------------

    isZMP2WidgetPlugin = 1

    icon = 'misc_/MetaPublisher2/Widget.gif'

    fieldTypeIds = []

    formTypeIds = []

    formTypeId = ''

    field_types = ComputedAttribute(lambda self: self.fieldTypeIds)

    frontend_types = ComputedAttribute(lambda self: self.formTypeIds)

    frontend_type = ComputedAttribute(lambda self: self.formTypeId)

    # -------------------------------------------------------------------------
    # Plugin Identity API

    getWidgetObject = WidgetPluginBase.get_plugin_instance

    getWidgetId = WidgetPluginBase.get_plugin_id

    getWidgetURL = WidgetPluginBase.get_plugin_url

    # -------------------------------------------------------------------------

    def get_immutable_pluginflag_ids(self):
        """Return list of Plugin flag ids.

        Return list of Plugin flag ids, which are either constants or set by an
        external source and may not be altered by MetaPublisher2 or its users.
        """
        # !!! bases/widget/legacywidget.py -  get_immutable_pluginflag_ids
        return []

    def get_mutable_pluginflag_ids(self):
        """Return list of Plugin flag ids.

        Return list of Plugin flag ids, which may be altered by MetaPublisher2
        and its users.
        """
        # !!! bases/widget/legacywidget.py -  get_mutable_pluginflag_ids
        return []

    # -------------------------------------------------------------------------

    def setWidgetData(self, data={}):
        """Return a dictionary describing this widget."""
        raise NotImplementedError

    def getWidgetData(self, form_type_id):
        """Return a dictionary describing this widget."""
        raise NotImplementedError


# ------------------------------------------------------------------------------
# initialize class security


InitializeClass(LegacyWidgetPlugin)


# !!! bases/widget/legacywidget.py - revise and update legacy api
