"""MetaPublisher2 - Imports Component.

Import service for Entries from various types of files either in the filesystem
or uploaded. Users can choose the destination Storage and match the data in the
file to the Fields in the Storage.
"""


from Products.MetaPublisher2.library.application import (
    permission_import_entries)
from Products.MetaPublisher2.library.common import (
    ClassSecurityInfo, DTMLFile, InitializeClass)
from Products.MetaPublisher2.library.compatibility import show_future


# =============================================================================
# Module Exports


__all__ = [
    'Imports',
]


# =============================================================================
# Imports Component Mix-In Class


class Imports:
    """Imports Component Mix-In Class."""

    security = ClassSecurityInfo()

    # -------------------------------------------------------------------------
    # Imports ZMI

    if show_future:

        security.declareProtected(permission_import_entries, 'imports_form')

        imports_form = DTMLFile('imports', globals())

    # -------------------------------------------------------------------------
    # Imports API

    security.declareProtected(permission_import_entries, 'import_entries')

    def import_entries(self, file, storage_id, field_map={}, REQUEST=None):
        """Import entries into a storage.

        Import entries from the specified local file into the specified
        Storage, mapping the data to the Storage's Field according the
        specified field map.
        """
        raise NotImplementedError

    security.declareProtected(permission_import_entries, 'upload_entries')

    def upload_entries(self, file, storage_id, field_map={}, REQUEST=None):
        """Upload a data file for entry import to a local file."""
        raise NotImplementedError

    def _inspect_entry_import(self, filename):
        """Inspect a data file for importing.

        Inspect a data file for importing, returning the file format and
        available data for mapping it to a Storage's Fields.
        """
        raise NotImplementedError


# -----------------------------------------------------------------------------
# Class Security


InitializeClass(Imports)


# TODO imports.py - implement
