"""MetaPublisher2 - Transfers Component."""


from Products.MetaPublisher2.library.application import (
    permission_access_entries)
from Products.MetaPublisher2.library.common import (
    ClassSecurityInfo, DTMLFile, InitializeClass)
from Products.MetaPublisher2.library.compatibility import show_future


# ============================================================================
# Module Exports

__all__ = [
    'Transfers',
]


# ============================================================================
# Transfers Component Mix-In Class

class Transfers:
    """Transfer Component Mix-In Class."""

    security = ClassSecurityInfo()

    # -----------------------------------------------------------------------
    # !TXT!

    if show_future:

        security.declareProtected(permission_access_entries, 'transfers_form')

        transfers_form = DTMLFile('transfers', globals())


# ----------------------------------------------------------------------------
# Class Security


InitializeClass(Transfers)


# TODO transfers.py - implement
