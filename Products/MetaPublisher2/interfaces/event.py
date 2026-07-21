"""MetaPublisher2 - Event Plugin Interface."""


from zope.interface import Interface


# ============================================================================
# Module Exports

__all__ = [
    'IEventPluginBase',
]


# ============================================================================
# Event Plugin Base Interface

class IEventPluginBase(Interface):
    """Event Plugin Base Interface."""

    pass

# TODO interfaces/event.py - implement
