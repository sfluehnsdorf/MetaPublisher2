"""MetaPublisher2 - Cache Plugin Interface."""


from zope.interface import Interface


# ============================================================================
# Module Exports

__all__ = [
    'ICachePluginBase',
]


# ============================================================================
# Cache Plugin Base Interface

class ICachePluginBase(Interface):
    """Cache Plugin Base Interface."""

    pass

# TODO interfaces/cache.py - implement
