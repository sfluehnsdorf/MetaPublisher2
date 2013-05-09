# -*- coding: iso-8859-15 -*-
# ============================================================================
#
#                         M e t a  P u b l i s h e r  2
#
# ----------------------------------------------------------------------------
# Copyright (c) 2002-2013, Sebastian Lühnsdorf - Web-Solutions and others
# For more information see the README.txt file or visit www.metapulisher.org
# ----------------------------------------------------------------------------
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).
#
# A copy of the ZPL should accompany this distribution.
#
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE
#
# ============================================================================

__doc__ = """Indexing Component

API and ZMI for managing Indexers and Indexes. The indexing service creates one
Indexer per Storage and can index one or more Fields of the Storage. An Indexer
can be a Zope based ZCatalog or a Storage specific indexing mechanism. If the
Indexer requires special calls, these are also handled by the Storage.

$Id: configuration/indexing/indexing.py 8 2013-05-09 00:02:46Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.library import ClassSecurityInfo, DTMLFile, InitializeClass, permission_access_configuration, permission_change_configuration, show_future


# ============================================================================
# Module Exports

__all__ = [
    'Indexing',
]


# ============================================================================
# Indexing Component Mix-In Class

class Indexing:
    """!TXT! Indexing Component Mix-In Class"""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # Indexing ZMI

    if show_future:

        security.declareProtected(permission_access_configuration, 'indexing_form')

        indexing_form = DTMLFile('indexing', globals())

    # ------------------------------------------------------------------------
    # Indexer Plugins

    # ------------------------------------------------------------------------
    # Indexer Retrieval API

    security.declareProtected(permission_access_configuration, 'get_indexer')

    def get_indexer(self, indexer_id):
        """!TXT! Return the ids of Storages with an associated Indexer."""

        raise NotImplementedError
        #storage = self.get_storage(storage_id)
        #return storage.get_indexer()

    security.declareProtected(permission_access_configuration, 'indexer_ids')

    def indexer_ids(self):
        """!TXT! Return the ids of Storages with an associated Indexer."""

        return map(lambda t: t[0], self.indexer_items())

    security.declareProtected(permission_access_configuration, 'indexer_items')

    def indexer_items(self):
        """!TXT! Return tuples of id, specification of Storages' Indexers."""

        raise NotImplementedError
        #result = []
        #for storage_id, storage in self.storage_items():
        #    if storage.has_indexer():
        #        result.append((storage_id, storage.get_indexer()))
        #return result

    security.declareProtected(permission_access_configuration, 'indexer_values')

    def indexer_values(self):
        """!TXT! Return the specifications of Storages' Indexers."""

        return map(lambda t: t[1], self.indexer_items())

    # ------------------------------------------------------------------------
    # Indexer Mutation API

    security.declareProtected(permission_change_configuration, 'add_indexer')

    def add_indexer(self, storage_id, options={}, REQUEST=None, **args):
        """!TXT! Add an Indexer for the specified Storage with the specified configuration."""

        raise NotImplementedError
        #options.update(args)
        #storage = self.get_storage(storage_id)
        #storage.add_indexer(options)

    def delete_indexer(self, storage_id, REQUEST=None):
        """!TXT! Delete the Indexer of the specified Storage."""

        raise NotImplementedError
        #storage = self.get_storage(storage_id)
        #storage.delete_indexer()

    def delete_indexers(self, storage_ids=[], REQUEST=None):
        """!TXT! Delete the Indexers of the specified Storages."""

        raise NotImplementedError
        #for storage_id in storage_ids:
        #    storage = self.get_storage(storage_id)
        #    storage.delete_indexer()

    def edit_indexer(self, storage_id, options={}, REQUEST=None, **args):
        """!TXT! Change the specified Storage's Indexer's configuration."""

        raise NotImplementedError
        #options.update(args)
        #storage = self.get_storage(storage_id)
        #storage.edit_indexer(options)

    # ------------------------------------------------------------------------
    # Index Retrieval API

    def get_index(self, storage_id, field_id):
        """!TXT! Return the specification for the specified Storage's Field index."""

        raise NotImplementedError
        #storage = self.get_storage(storage_id)
        #return storage.get_index(field_id)

    def index_ids(self, storage_id):
        """!TXT! Return the ids of the specified Storage's Fields with an associated Index."""

        raise NotImplementedError
        #storage = self.get_storage(storage_id)
        #return storage.index_ids()

    def index_items(self, storage_id):
        """!TXT! Return tuples of id, specification of Indexes the specified Storages' Fields."""

        raise NotImplementedError
        #storage = self.get_storage(storage_id)
        #return storage.index_items()

    def index_values(self, storage_id):
        """!TXT! Return the specifications of Indexes the specified Storages' Fields."""

        raise NotImplementedError
        #storage = self.get_storage(storage_id)
        #return storage.index_values()

    # ------------------------------------------------------------------------
    # Index Mutation API

    def add_index(self, storage_id, field_id, REQUEST=None):
        """!TXT! Add an Index for the specified Storage's Field with the specified configuration."""

        raise NotImplementedError
        options.update(args)

        storage = self.get_storage(storage_id)
        storage.add_index(field_id, options)

    def delete_index(self, storage_id, field_id, REQUEST=None):
        """!TXT! Delete the Index of the specified Storage's Field."""

        raise NotImplementedError
        storage = self.get_storage(storage_id)
        storage.delete_index(field_id)

    def delete_indexes(self, storage_id, field_ids=[], REQUEST=None):
        """!TXT! Delete the Indexes of the specified Storage's Fields."""

        raise NotImplementedError
        storage = self.get_storage(storage_id)
        storage.delete_indexes(field_ids)

    def edit_index(self, storage_id, field_id, REQUEST=None):
        """!TXT! Change the specified Storage's Field's Index's configuration."""

        raise NotImplementedError
        options.update(args)

        storage = self.get_storage(storage_id)
        storage.edit_index(field_id, options)

    # ------------------------------------------------------------------------
    # Entry Indexing API

    security.declareProtected(permission_change_configuration, 'index_entry')

    def index_entry(self, storage_id, entry_id, REQUEST=None):
        """!TXT! Index the specified Storage's Entry, updating an existing index data for the Entry."""

        raise NotImplementedError

    security.declareProtected(permission_change_configuration, 'index_entries')

    def index_entries(self, storage_id, entry_ids=[], REQUEST=None):
        """!TXT! Index the specified Storage's Entries, updating any existing index data."""

        raise NotImplementedError

    security.declareProtected(permission_change_configuration, 'index_storage')

    def index_storage(self, storage_id, REQUEST=None):
        """!TXT! Index all Entries of the specified Storage, updating any existing index data."""

        raise NotImplementedError

    security.declareProtected(permission_change_configuration, 'index_storages')

    def index_storages(self, REQUEST=None):
        """!TXT! Index all Entries of all Storages, updating any existing index data."""

        raise NotImplementedError

    security.declareProtected(permission_change_configuration, 'unindex_entry')

    def unindex_entry(self, storage_id, entry_id, REQUEST=None):
        """!TXT! Remove index data of the specified Storage's Entry."""

        raise NotImplementedError

    security.declareProtected(permission_change_configuration, 'unindex_entries')

    def unindex_entries(self, storage_id, entry_ids, REQUEST=None):
        """!TXT! Remove index data of the specified Storage's Entries."""

        raise NotImplementedError

    security.declareProtected(permission_change_configuration, 'unindex_storage')

    def unindex_storage(self, storage_id, REQUEST=None):
        """!TXT! Remove index data of all Entries of the specified Storage."""

        raise NotImplementedError

    security.declareProtected(permission_change_configuration, 'unindex_storages')

    def unindex_storages(self, REQUEST=None):
        """!TXT! Remove index data of all Entries of the all Storages."""

        raise NotImplementedError

# ----------------------------------------------------------------------------
# Class Security

InitializeClass(Indexing)

# TODO indexing.py - implement
