"""MetaPublisher2 - EntrySet Base."""


from Products.MetaPublisher2.bases.entrycontainer import EntryContainer
from Products.MetaPublisher2.interfaces import IEntrySet
from Products.MetaPublisher2.library.common import (
    ClassSecurityInfo, implements, InitializeClass)


# ============================================================================
# Module Exports

__all__ = [
    'EntrySet',
]


# ============================================================================
# Entry Set Base Class

class EntrySet(EntryContainer):
    """Entry Set Base Class."""

    security = ClassSecurityInfo()

    implements(IEntrySet)


# ----------------------------------------------------------------------------
# initialize class security


InitializeClass(EntrySet)


# !!! bases/entryset/entryset.py - define api
# !!! bases/entryset/entryset.py - implement source/storage handling
# !!! bases/entryset/entryset.py - implement live linking
# !!! bases/entryset/entryset.py - implement query storage
