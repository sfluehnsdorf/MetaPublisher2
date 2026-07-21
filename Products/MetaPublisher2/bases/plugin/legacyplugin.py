"""Legacy Plugin Base.

NOTE: This class is provided for backward compatibility and should not be of
interest to you!

It defines a plugin identifier and maps old style plugin detail attributes. It
must preceed the plugin type base class in inheritance order to function
properly.
"""


from Products.MetaPublisher2.library.common import (
    ClassSecurityInfo, ComputedAttribute, InitializeClass)


# ==============================================================================
# Module Exports

__all__ = [
    'LegacyPluginBase',
]


# ============================================================================
# Legacy Plugin Identifiers

all_plugintypes = [
    'ZMP2StoragePlugin', 'ZMP2FieldPlugin', 'ZMP2InterfacePlugin',
    'ZMP2WidgetPlugin']


# ============================================================================
# Legacy Plugin Base Class

class LegacyPluginBase:
    """Legacy Plugin Base Class."""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # Legacy Plugin Identity Attributes

    isZMP2Plugin = 1

    # ------------------------------------------------------------------------
    # Legacy Plugin Information Attributes

    pluginName = 'Unknown Plugin Type'

    pluginAuthor = 'Unknown Author'

    pluginVersion = 'Unknown Version'

    pluginInfo = 'No description available.'

    # ------------------------------------------------------------------------
    # Plugin Information Attributes Remapping

    plugin_name = ComputedAttribute(lambda self: self.pluginName)

    plugin_author = ComputedAttribute(lambda self: self.pluginAuthor)

    plugin_version = ComputedAttribute(lambda self: self.pluginVersion)

    plugin_info = ComputedAttribute(lambda self: self.pluginInfo)


# ----------------------------------------------------------------------------
# initialize class security


InitializeClass(LegacyPluginBase)
