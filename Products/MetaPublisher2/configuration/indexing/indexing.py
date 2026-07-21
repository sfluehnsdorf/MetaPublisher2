"""MetaPublisher2 - Indexing Component.

API and ZMI for managing Indexers and Indexes. The indexing service creates one
Indexer per Storage and can index one or more Fields of the Storage. An Indexer
can be a Zope based ZCatalog or a Storage specific indexing mechanism. If the
Indexer requires special calls, these are also handled by the Storage.
"""


from Products.MetaPublisher2.library.application import (
    permission_access_configuration, permission_change_configuration)
from Products.MetaPublisher2.library.common import (
    ClassSecurityInfo, DTMLFile, InitializeClass)
from Products.MetaPublisher2.library.compatibility import show_future


# =============================================================================
# Module Exports


__all__ = [
    'Indexing',
]


# =============================================================================
# Indexing Component Mix-In Class

class Indexing:
    """Indexing Component Mix-In Class."""

    security = ClassSecurityInfo()

    # -------------------------------------------------------------------------
    # Indexing ZMI

    if show_future:

        security.declareProtected(
            permission_access_configuration, 'indexing_form')

        indexing_form = DTMLFile('indexing', globals())

    # -------------------------------------------------------------------------
    # Indexer Plugins

    # -------------------------------------------------------------------------
    # Indexer Retrieval API

    security.declareProtected(permission_access_configuration, 'get_indexer')

    def get_indexer(self, indexer_id):
        """Return the ids of Storages with an associated Indexer."""
        raise NotImplementedError
        # storage = self.get_storage(storage_id)
        # return storage.get_indexer()

    security.declareProtected(permission_access_configuration, 'indexer_ids')

    def indexer_ids(self):
        """Return the ids of Storages with an associated Indexer."""
        return map(lambda t: t[0], self.indexer_items())

    security.declareProtected(permission_access_configuration, 'indexer_items')

    def indexer_items(self):
        """Return tuples of id, specification of Storages' Indexers."""
        raise NotImplementedError
        # result = []
        # for storage_id, storage in self.storage_items():
        #     if storage.has_indexer():
        #         result.append((storage_id, storage.get_indexer()))
        # return result

    security.declareProtected(
        permission_access_configuration, 'indexer_values')

    def indexer_values(self):
        """Return the specifications of Storages' Indexers."""
        return map(lambda t: t[1], self.indexer_items())

    # -------------------------------------------------------------------------
    # Indexer Mutation API

    security.declareProtected(permission_change_configuration, 'add_indexer')

    def add_indexer(self, storage_id, options={}, REQUEST=None, **args):
        """Add an Indexer for the specified Storage with the configuration."""
        raise NotImplementedError
        # options.update(args)
        # storage = self.get_storage(storage_id)
        # storage.add_indexer(options)

    def delete_indexer(self, storage_id, REQUEST=None):
        """Delete the Indexer of the specified Storage."""
        raise NotImplementedError
        # storage = self.get_storage(storage_id)
        # storage.delete_indexer()

    def delete_indexers(self, storage_ids=[], REQUEST=None):
        """Delete the Indexers of the specified Storages."""
        raise NotImplementedError
        # for storage_id in storage_ids:
        #     storage = self.get_storage(storage_id)
        #     storage.delete_indexer()

    def edit_indexer(self, storage_id, options={}, REQUEST=None, **args):
        """Change the specified Storage's Indexer's configuration."""
        raise NotImplementedError
        # options.update(args)
        # storage = self.get_storage(storage_id)
        # storage.edit_indexer(options)

    # !!! duplicate_indexer
    # !!! duplicate_indexers
    # !!! rename_indexer
    # !!! rename_indexers

    # -------------------------------------------------------------------------
    # Index Retrieval API

    def get_index(self, storage_id, field_id):
        """Return the specification for the specified Storage's Field index."""
        raise NotImplementedError
        # storage = self.get_storage(storage_id)
        # return storage.get_index(field_id)

    def index_ids(self, storage_id):
        """Return the ids of the Storage's Fields with an associated Index."""
        raise NotImplementedError
        # storage = self.get_storage(storage_id)
        # return storage.index_ids()

    def index_items(self, storage_id):
        """Return tuples of id, specification of Indexes of the Storage."""
        raise NotImplementedError
        # storage = self.get_storage(storage_id)
        # return storage.index_items()

    def index_values(self, storage_id):
        """Return the specifications of Indexes of the Storage."""
        raise NotImplementedError
        # storage = self.get_storage(storage_id)
        # return storage.index_values()

    # -------------------------------------------------------------------------
    # Index Mutation API

    def add_index(self, storage_id, field_id, REQUEST=None):
        """Add an Index for the specified Storage's Field."""
        raise NotImplementedError
        # options.update(args)
        # storage = self.get_storage(storage_id)
        # storage.add_index(field_id, options)

    def delete_index(self, storage_id, field_id, REQUEST=None):
        """Delete the Index of the specified Storage's Field."""
        raise NotImplementedError
        # storage = self.get_storage(storage_id)
        # storage.delete_index(field_id)

    def delete_indexes(self, storage_id, field_ids=[], REQUEST=None):
        """Delete the Indexes of the specified Storage's Fields."""
        raise NotImplementedError
        # storage = self.get_storage(storage_id)
        # storage.delete_indexes(field_ids)

    def edit_index(self, storage_id, field_id, REQUEST=None):
        """Change the specified Storage's Field's Index's configuration."""
        raise NotImplementedError
        # options.update(args)
        # storage = self.get_storage(storage_id)
        # storage.edit_index(field_id, options)

    # !!! duplicate_index
    # !!! duplicate_indexes
    # !!! rename_index
    # !!! rename_indexes

    # -------------------------------------------------------------------------
    # Entry Indexing API

    security.declareProtected(permission_change_configuration, 'index_entry')

    def index_entry(self, storage_id, entry_id, REQUEST=None):
        """Index the Storage's Entry, updating any index data for the Entry."""
        raise NotImplementedError

    security.declareProtected(permission_change_configuration, 'index_entries')

    def index_entries(self, storage_id, entry_ids=[], REQUEST=None):
        """Index the Storage's Entries, updating any existing index data."""
        raise NotImplementedError

    security.declareProtected(permission_change_configuration, 'index_storage')

    def index_storage(self, storage_id, REQUEST=None):
        """Index Entries of the Storage, updating any existing index data."""
        raise NotImplementedError

    security.declareProtected(
        permission_change_configuration, 'index_storages')

    def index_storages(self, REQUEST=None):
        """Index all Entries of all Storages, updating any index data."""
        raise NotImplementedError

    security.declareProtected(permission_change_configuration, 'unindex_entry')

    def unindex_entry(self, storage_id, entry_id, REQUEST=None):
        """Remove index data of the specified Storage's Entry."""
        raise NotImplementedError

    security.declareProtected(
        permission_change_configuration, 'unindex_entries')

    def unindex_entries(self, storage_id, entry_ids, REQUEST=None):
        """Remove index data of the specified Storage's Entries."""
        raise NotImplementedError

    security.declareProtected(
        permission_change_configuration, 'unindex_storage')

    def unindex_storage(self, storage_id, REQUEST=None):
        """Remove index data of all Entries of the specified Storage."""
        raise NotImplementedError

    security.declareProtected(
        permission_change_configuration, 'unindex_storages')

    def unindex_storages(self, REQUEST=None):
        """Remove index data of all Entries of the all Storages."""
        raise NotImplementedError


# -----------------------------------------------------------------------------
# Class Security


InitializeClass(Indexing)


# !!! indexing.py - implement
