"""MetaPublisher2 - Plugins Component.

Plugin service, providing access to all installed Product classess based on
the MetaPublisher2's Plugin base class. Retrieval can be limited to one or
more Plugin interfaces.
"""


from Products.MetaPublisher2.interfaces import IPluginBase
from Products.MetaPublisher2.library.application import permission_manage
from Products.MetaPublisher2.library.common import (
    ClassSecurityInfo, DTMLFile, false, InitializeClass, Products, true)


# ============================================================================
# Module Exports

__all__ = [
    'Plugins',
]


# ============================================================================
# Plugins Component Mix-In Class

class Plugins:
    """Plugins Component Mix-In Class."""

    security = ClassSecurityInfo()

    # --------------------------------------------------------------------------
    # Plugins ZMI Forms

    security.declareProtected(permission_manage, 'plugins_form')

    plugins_form = DTMLFile('plugins', globals())

    # --------------------------------------------------------------------------
    # Plugins Retrieval API

    security.declareProtected(permission_manage, 'get_plugin')

    def get_plugin(self, plugin_id, interfaces=[]):
        """Return registry mapping of the specified MetaPublisher2 plugin."""
        for id, plugin in self.plugin_items(interfaces):
            if id == plugin_id:
                return plugin
        raise KeyError("!TXT! No plugin named '%s'" % plugin_id)

    security.declareProtected(permission_manage, 'has_plugins')

    def has_plugins(self, interfaces=[]):
        """Return True if any MetaPublisher2 plugins are installed."""
        return self.plugin_ids(interfaces) and true or false

    security.declareProtected(permission_manage, 'list_plugins')

    def list_plugins(self, plugin_type=None):
        """Return a filtered list of plugins for the ZMI form."""
        result = []
        for plugin in (
            not plugin_type and
            self.plugin_values() or
            filter(
                lambda plugin: (
                    plugin['plugin_details']['plugin_type'] == plugin_type),
                self.plugin_values())
        ):
            plugin.update(plugin['plugin_details'])
            plugin['icon'] = plugin['instance'].icon
            result.append(plugin)
        return result

    security.declareProtected(permission_manage, 'list_plugin_types')

    def list_plugin_types(self):
        """Return a filtered list of plugins for the ZMI form."""
        result = []
        for plugin in self.plugin_values():
            plugin_type = plugin['plugin_details']['plugin_type']
            if plugin_type not in result:
                result.append(plugin_type)
        return result

    security.declareProtected(permission_manage, 'plugin_ids')

    def plugin_ids(self, interfaces=[]):
        """Return the ids of installed plugins."""
        return map(lambda item: item[0], self.plugin_items(interfaces))

    security.declareProtected(permission_manage, 'plugin_items')

    def plugin_items(self, interfaces=[]):
        """Return tuples of id, registry mapping of installed plugins."""
        if not interfaces:
            interfaces = [IPluginBase, ]
        if not isinstance(interfaces, list):
            interfaces = [interfaces, ]

        result = []
        for item in Products.meta_types:
            for item_interface in item.get('interfaces', None):
                for interface in interfaces:
                    if (
                        interface is item_interface or
                        item_interface.extends(interface)
                    ):
                        instance = item['instance']('dummy')
                        data = item.copy()
                        data['plugin_details'] = (
                            instance.get_plugin_specification())
                        candidate = (
                            item['product'] + '.' + item['name'], data)
                        if candidate not in result:
                            result.append(candidate)
        return result

    security.declareProtected(permission_manage, 'plugin_values')

    def plugin_values(self, interfaces=[]):
        """Return the registry mapping of installed plugins."""
        return map(lambda item: item[1], self.plugin_items(interfaces))


# ------------------------------------------------------------------------------
# Class Security

InitializeClass(Plugins)
