"""MetaPublisher2."""


from Products.MetaPublisher2.library.application import permission_manage
from Products.MetaPublisher2.library.common import (
    ClassSecurityInfo, DTMLFile, InitializeClass)
from Products.MetaPublisher2.library.compatibility import show_future


# ============================================================================
# Module Exports

__all__ = [
    'Events',
]


# ============================================================================
# Events Component Mix-In Class

class Events:
    """Events Component Mix-In Class."""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # Events ZMI Form

    if show_future:

        security.declareProtected(permission_manage, 'events_form')

        events_form = DTMLFile('events', globals())


# ----------------------------------------------------------------------------
# Class Security

InitializeClass(Events)

# TODO events.py - implement
