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

Plugin service, providing access to all installed Product classess based on the
MetaPublisher2's Plugin base class. Retrieval can be limited to one or more
Plugin interfaces.

$Id: system/plugins/plugins.py 12 2013-05-05 18:00:31Z sfluehnsdorf $
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
# Plugins Mix-In Class

class Plugins:
    """Plugins Mix-In Class"""

    security = ClassSecurityInfo()

    # --------------------------------------------------------------------------
    # Plugins ZMI Forms

    security.declareProtected(permission_manage, 'plugins_form')

    plugins_form = DTMLFile('plugins', globals())

    # --------------------------------------------------------------------------
    # Plugins Retrieval API

    security.declareProtected(permission_manage, 'get_plugin')

    def get_plugin(self, plugin_id, interfaces=[]):
        """Return the registry mapping of the specified MetaPublisher2 plugin"""

        for id, plugin in self.plugin_items(interfaces):
            if id == plugin_id:
                return plugin
        raise KeyError("No plugin named '%s'" % plugin_id)

    security.declareProtected(permission_manage, 'has_plugins')

    def has_plugins(self, interfaces=[]):
        """Return True if any MetaPublisher2 plugins are installed"""

        return self.plugin_ids(interfaces) and true or false

    security.declareProtected(permission_manage, 'list_plugins')

    def list_plugins(self, plugin_type, order_by, reverse_order):
        """Return a filtered and sorted plugin list for the ZMI form."""

        if plugin_type:
            result = []
            for id, data in self.plugin_items():
                if data['plugin_details']['plugin_type'] == plugin_type:
                    result.append((id, data))
            return result
        else:
            result = self.plugin_items()

        if order_by == 'plugin':
            def sort_items(x, y):
                return cmp(x[1]['name'], y[1]['name'])
            result.sort(sort_items)
        elif order_by == 'type':
            def sort_items(x, y):
                return cmp(x[1]['plugin_details']['plugin_type'], y[1]['plugin_details']['plugin_type'])
            result.sort(sort_items)
        elif order_by == 'version':
            def sort_items(x, y):
                return cmp(x[1]['plugin_details']['plugin_version'], y[1]['plugin_details']['plugin_version'])
            result.sort(sort_items)
        else:
            def sort_items(x, y):
                return cmp((x[1]['product'], x[1]['name']), (y[1]['product'], y[1]['name']))
            result.sort(sort_items)

        if reverse_order:
            result.reverse()

        return result

    security.declareProtected(permission_manage, 'plugin_ids')

    def plugin_ids(self, interfaces=[]):
        """Return the ids of installed MetaPublisher2 plugins"""

        return map(lambda item: item[0], self.plugin_items(interfaces))

    security.declareProtected(permission_manage, 'plugin_items')

    def plugin_items(self, interfaces=[]):
        """Return tuples of id, registry mapping of installed MetaPublisher2 plugins"""

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
        """Return the registry mapping of installed MetaPublisher2 plugins"""

        return map(lambda item: item[1], self.plugin_items(interfaces))

# ------------------------------------------------------------------------------
# Class Security

InitializeClass(Plugins)
