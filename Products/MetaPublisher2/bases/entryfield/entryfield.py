"""MetaPublisher2 - Entry Field Base."""


from Products.MetaPublisher2.interfaces import IEntryField
from Products.MetaPublisher2.library.common import (
    ClassSecurityInfo, implements, InitializeClass)


# ============================================================================
# Module Exports

__all__ = [
    'EntryField',
]


# ============================================================================
# Entry Field Base Class

class EntryField:
    """Entry Field Base Class."""

    security = ClassSecurityInfo()

    implements(IEntryField)


# ----------------------------------------------------------------------------
# initialize class security


InitializeClass(EntryField)


# !!! bases/entryfield/entryfield.py - define api
# !!! bases/entryfield/entryfield.py - implement backdrop/failsafe code
