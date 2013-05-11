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

__doc__ = """Plugins Component

Plugin service, providing access to all installed Product classess based on
the MetaPublisher2's Plugin base class. Retrieval can be limited to one or
more Plugin interfaces.

$Id: system/plugins/plugins.py 15 2013-05-11 00:18:05Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.interfaces import IPluginBase
from Products.MetaPublisher2.library import ClassSecurityInfo, DTMLFile, false, InitializeClass, permission_manage, Products, true


# ============================================================================
# Module Exports

__all__ = [
    'Plugins',
]


# ============================================================================
# Plugins Component Mix-In Class

class Plugins:
    """!TXT! Plugins Component Mix-In Class"""

    security = ClassSecurityInfo()

    # --------------------------------------------------------------------------
    # Plugins ZMI Forms

    security.declareProtected(permission_manage, 'plugins_form')

    plugins_form = DTMLFile('plugins', globals())

    # --------------------------------------------------------------------------
    # Plugins Retrieval API

    security.declareProtected(permission_manage, 'get_plugin')

    def get_plugin(self, plugin_id, interfaces=[]):
        """!TXT! Return the registry mapping of the specified MetaPublisher2 plugin"""

        for id, plugin in self.plugin_items(interfaces):
            if id == plugin_id:
                return plugin
        raise KeyError("!TXT! No plugin named '%s'" % plugin_id)

    security.declareProtected(permission_manage, 'has_plugins')

    def has_plugins(self, interfaces=[]):
        """!TXT! Return True if any MetaPublisher2 plugins are installed"""

        return self.plugin_ids(interfaces) and true or false

    security.declareProtected(permission_manage, 'list_plugins')

    def list_plugins(self, plugin_type=None):
        """!TXT! Return a filtered list of plugins for the ZMI form."""

        result = []
        for plugin in not(plugin_type) and self.plugin_values() or filter(lambda plugin: plugin['plugin_details']['plugin_type'] == plugin_type, self.plugin_values()):
            plugin.update(plugin['plugin_details'])
            plugin['icon'] = plugin['instance'].icon
            result.append(plugin)
        return result

    security.declareProtected(permission_manage, 'list_plugin_types')

    def list_plugin_types(self):
        """!TXT! Return a filtered list of plugins for the ZMI form."""

        result = []
        for plugin in self.plugin_values():
            plugin_type = plugin['plugin_details']['plugin_type']
            if not plugin_type in result:
                result.append(plugin_type)
        return result

    security.declareProtected(permission_manage, 'plugin_ids')

    def plugin_ids(self, interfaces=[]):
        """!TXT! Return the ids of installed MetaPublisher2 plugins"""

        return map(lambda item: item[0], self.plugin_items(interfaces))

    security.declareProtected(permission_manage, 'plugin_items')

    def plugin_items(self, interfaces=[]):
        """!TXT! Return tuples of id, registry mapping of installed MetaPublisher2 plugins"""

        if not(interfaces):
            interfaces = [IPluginBase, ]
        if not isinstance(interfaces, list):
            interfaces = [interfaces, ]

        result = []
        for item in Products.meta_types:
            for item_interface in item.get('interfaces', None):
                for interface in interfaces:
                    if interface is item_interface or item_interface.extends(interface):
                        instance = item['instance']('dummy')
                        data = item.copy()
                        data['plugin_details'] = instance.get_plugin_specification()
                        candidate = (item['product'] + '.' + item['name'], data)
                        if not(candidate in result):
                            result.append(candidate)
        return result

    security.declareProtected(permission_manage, 'plugin_values')

    def plugin_values(self, interfaces=[]):
        """!TXT! Return the registry mapping of installed MetaPublisher2 plugins"""

        return map(lambda item: item[1], self.plugin_items(interfaces))

# ------------------------------------------------------------------------------
# Class Security

InitializeClass(Plugins)
