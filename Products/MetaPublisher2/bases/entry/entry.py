"""MetaPublisher2 - Entry Base."""


from Products.MetaPublisher2.interfaces import IEntry
from Products.MetaPublisher2.library.common import (
    ClassSecurityInfo, implements, InitializeClass)


# ============================================================================
# Module Exports

__all__ = [
    'Entry',
]


# ============================================================================
# Entry Base Class

class Entry:
    """Entry Base Class."""

    security = ClassSecurityInfo()

    implements(IEntry)


# ----------------------------------------------------------------------------
# initialize class security

InitializeClass(Entry)

# !!! bases/entry/entry.py - define api
# !!! bases/entry/entry.py - implement backdrop/failsafe code
