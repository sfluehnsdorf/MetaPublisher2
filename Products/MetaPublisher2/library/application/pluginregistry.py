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

__doc__ = """Application Plugin Registry

The plugin registry automatises Zope Product registration for a range of plugins
and handles auomatic registration for related pluginbases supporting this
feature.

$Id: library/application/pluginregistry.py 4 2012-02-17 15:45:00Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Exports

__all__ = [
    'PluginRegistry',
]


# ============================================================================
# PluginRegistry Class

class PluginRegistry:
    """PluginRegistry Class"""

    def __init__(self, context, prefix):
        self.context = context
        self.prefix = prefix
        self.pluginbases = []

    def register_plugin(self, pluginclass):
        context.register(
            pluginclass,
            meta_type='%s_%s' % (self.prefix, pluginbase.plugin_subtype),
            constructors=(pluginbase.zmi_add_form, ),
            container_filter=pluginbase.container_filter,
        )
        self.pluginbases.append(pluginclass.plugin_subtype)

    def register_plugins(self, basepath):
        for pluginclass in pluginclasses:
            register_plugin(pluginclass)

    def autoregister_plugins(self):
        for pluginbase, baseclasses, modifiers in self._get_plugin_autoregistries():
            pluginclass = type('%s_%s' % (prefix, pluginbase.plugin_subtype), baseclasses, {})
            for name, attribute in modifiers:
                setattr(pluginclass, name, attribute)
            # !!! pluginregistry.py - add pluginclass to ... ?
            self.register_plugin(
                pluginclass,
                meta_type='%s %s' % (prefix, pluginbase.plugin_type, pluginbase.plugin_subtype),
                constructors=pluginbase.constructors,
                container_filter=pluginbase.container_filter,
            )

    # !!! pluginregistry.py - repeat until no more autoregistries can be matched...
    def _get_plugin_autoregistries(self):
        result = []
        registered_pluginbases = self.pluginbases
        for pluginbase in self._get_pluginbases():
            if not pluginbase in registered_pluginbases:
                for autoregistry in pluginbase._autoregistries:
                    if autoregistry['dependencies'].issubset(registered_pluginbases):
                        result.append((pluginbase, [pluginbase, ] + autoregistry['baseclasses'], autoregistry['modifiers']))
                        break
        return result

    # !!! pluginregistry.py - return pluginbase classes (currently not implemented)
    def _get_pluginbases(self):
        result = []
        return result

# !!! pluginregistry.py - handle updates with actual implementation (needs to update existing data structures - must be able to read)
# !!! pluginregistry.py - autoregsitered plugins must be marked (base/interface, i.e. plugin/autoregister.py)
# !!! pluginregistry.py - replace type specific identifiers (field_type, storage_type, etc. with generic plugin_subtype)
# !!! pluginregistry.py - use plugin_subtype if it makes sense...
