"""MetaPublisher2 - Exports Component.

Export service for Entries into various types of files either for the
filesystem or download. Users can choose the Storage and match the Fields in
the Storage to data slots in the file.
"""


from Products.MetaPublisher2.library.application import (
    permission_export_entries)
from Products.MetaPublisher2.library.common import (
    ClassSecurityInfo, DTMLFile, InitializeClass)
from Products.MetaPublisher2.library.compatibility import show_future


# ============================================================================
# Module Exports

__all__ = [
    'Exports',
]


# ============================================================================
# Exports Component Mix-In Class

class Exports:
    """Exports Component Mix-In Class."""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # Exports ZMI

    if show_future:

        security.declareProtected(permission_export_entries, 'exports_form')

        exports_form = DTMLFile('exports', globals())


# ----------------------------------------------------------------------------
# Class Security


InitializeClass(Exports)


# TODO exports.py - implement
