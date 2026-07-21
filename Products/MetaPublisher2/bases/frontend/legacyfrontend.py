"""MetaPublisher2 - Legacy Frontend Plugin Base."""


import Products
from Products.MetaPublisher2.bases.plugin.legacyplugin import LegacyPluginBase
from Products.MetaPublisher2.library.common import (
    ClassSecurityInfo, InitializeClass)

from frontend import FrontendPluginBase


# ============================================================================
# Module Exports

__all__ = [
    'LegacyFrontendPlugin',
]


# ============================================================================
# Legacy Frontend Plugin Base Class

class LegacyFrontendPlugin(LegacyPluginBase, FrontendPluginBase):
    """Legacy Frontend Plugin Base Class."""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # !TXT!

    isZMP2InterfacePlugin = 1

    icon = 'misc_/MetaPublisher2/Interface.gif'

    # ------------------------------------------------------------------------
    # !TXT!

    getInterfaceObject = FrontendPluginBase.get_plugin_instance

    getInterfaceId = FrontendPluginBase.get_plugin_id

    getInterfaceURL = FrontendPluginBase.get_plugin_url

    # ------------------------------------------------------------------------
    # !TXT!

    def get_immutable_pluginflag_ids(self):
        """Return list of Plugin flag ids.

        Return list of Plugin flag ids, which are either constants or set by
        an external source and may not be altered by MetaPublisher2 or its
        users.
        """
        # !!! bases/frontend/legacyfrontend.py -  get_immutable_pluginflag_ids
        return []

    def get_mutable_pluginflag_ids(self):
        """Return list of Plugin flag ids.

        Return list of Plugin flag ids, which may be altered by MetaPublisher2
        and its users.
        """
        # !!! bases/frontend/legacyfrontend.py -  get_immutable_pluginflag_ids
        return []

    # ------------------------------------------------------------------------
    # !TXT!

    def all_meta_types(self, interfaces=None):
        """TODO: Docstring for all_meta_types."""
        result = FrontendPluginBase.all_meta_types(interfaces)
        for product in Products.meta_types:
            if (
                product.get('visibility', None) == 'ZMP2WidgetPlugin' and
                not (product in result)
            ):
                result.append(product)
        return result

    # ------------------------------------------------------------------------
    # !TXT!

    def renderingIds(self):
        """Return list ids for objects created on rendering."""
        raise NotImplementedError

    def rendering_ids(self):
        """Return list ids for objects created on rendering."""
        self.renderingIds()

    # ------------------------------------------------------------------------
    # !TXT!

    def renderInterface(self, destination, **options):
        """Render the Interface."""
        raise NotImplementedError


# ----------------------------------------------------------------------------
# initialize class security

InitializeClass(LegacyFrontendPlugin)

# !!! bases/frontend/legacyfrontend.py - revise and update legacy api
