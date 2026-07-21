"""MetaPublisher2 - Search Component.

Keyword search for Entries in a Storage, allowing to define search conditions
with a variety of conditions, provided by Field plugins.
"""


from Products.MetaPublisher2.library.application import (
    permission_access_entries)
from Products.MetaPublisher2.library.common import (
    ClassSecurityInfo, DTMLFile, InitializeClass)


# =============================================================================
# Module Exports

__all__ = [
    'Search',
]


# =============================================================================
# Search Component Mix-In Class

class Search:
    """Search Component Mix-In Class."""

    security = ClassSecurityInfo()

    # -------------------------------------------------------------------------
    # Search ZMI

    security.declareProtected(permission_access_entries, 'search_form')

    search_form = DTMLFile('search', globals())


# -----------------------------------------------------------------------------
# Class Security


InitializeClass(Search)


# !!! search.py - implement
