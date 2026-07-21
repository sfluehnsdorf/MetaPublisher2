"""MetaPublisher2 - Application Plugin Registry.

The plugin registry automatises Zope Product registration for a range of
plugins and handles auomatic registration for related pluginbases supporting
this feature.
"""


# ============================================================================
# Module Exports


__all__ = [
    'PluginRegistry',
]


# ============================================================================
# PluginRegistry Class

class PluginRegistry:
    """PluginRegistry Class."""

    def __init__(self, context, prefix):
        """Initialize instance."""
        self.context = context
        self.prefix = prefix
        self.pluginbases = []

    def register_plugin(self, pluginclass):
        """Register a plugin."""
        context = None  # TODO: how to get context after Zope init
        context.register(
            pluginclass,
            meta_type='%s_%s' % (self.prefix, pluginclass.plugin_subtype),
            constructors=(pluginclass.zmi_add_form, ),
            container_filter=pluginclass.container_filter,
        )
        self.pluginbases.append(pluginclass.plugin_subtype)

    def register_plugins(self, pluginclasses):
        """Register plugins."""
        for pluginclass in pluginclasses:
            self.register_plugin(pluginclass)

    def autoregister_plugins(self):
        """Automatically register plugins."""
        for pluginbase, baseclasses, modifiers in (
            self._get_plugin_autoregistries()
        ):
            pluginclass = type('%s_%s' % (
                self.prefix, pluginbase.plugin_subtype), baseclasses, {})
            for name, attribute in modifiers:
                setattr(pluginclass, name, attribute)
            # !!! pluginregistry.py - add pluginclass to ... ?
            self.register_plugin(
                pluginclass,
                meta_type='%s %s' % (
                    pluginbase.plugin_type, pluginbase.plugin_subtype),
                constructors=pluginbase.constructors,
                container_filter=pluginbase.container_filter,
            )

    def _get_plugin_autoregistries(self):
        """Repeat until no more autoregistries can be matched."""
        result = []
        registered_pluginbases = self.pluginbases
        for pluginbase in self._get_pluginbases():
            if pluginbase not in registered_pluginbases:
                for autoregistry in pluginbase._autoregistries:
                    if autoregistry['dependencies'].issubset(
                        registered_pluginbases
                    ):
                        result.append((
                            pluginbase, [pluginbase, ] +
                            autoregistry['baseclasses'],
                            autoregistry['modifiers']))
                        break
        return result

    def _get_pluginbases(self):
        """Return pluginbase classes."""
        result = []  # TODO
        return result


'''
TODO
- handle updates with actual implementation (needs to update existing data
  structures - must be able to read)
- autoregsitered plugins must be marked (base/interface, i.e.
  plugin/autoregister.py)
- replace type specific identifiers (field_type, storage_type, etc. with
  generic plugin_subtype)
- use plugin_subtype if it makes sense...
'''
