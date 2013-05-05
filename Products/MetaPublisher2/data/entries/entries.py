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

__doc__ = """Entries Component

API for retrieval, mutation and ordering of Entries. An Entry is a singular unit
of data stored. Entries are stored in Storages and are defined by the Storage's
Fields and in EntrySets, which store the result of methods on Entries.

$Id: data/entries/entries.py 7 2013-05-05 18:04:22Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.library import ClassSecurityInfo, DTMLFile, InitializeClass, permission_access_entries, permission_create_entries, permission_change_entries, quote_plus, true

from entry import Entry
from entryfields import EntryFields
from entryorder import EntryOrder
from entrytrees import EntryTrees
from entrygraphs import EntryGraphs
from entrysets import EntrySets
from entrystats import EntryStats


# ============================================================================
# Module Exports

__all__ = [
    'Entries',
]


# ============================================================================
# Entries Mix-In Class

class Entries(Entry, EntryFields, EntrySets, EntryOrder, EntryTrees, EntryGraphs, EntryStats):
    """Entries Mix-In Class"""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # Entries ZMI

    security.declareProtected(permission_access_entries, 'entries_form')

    entries_form = DTMLFile('entries', globals())

    security.declareProtected(permission_create_entries, 'add_entry_form')

    add_entry_form = DTMLFile('add_entry', globals())

    security.declareProtected(permission_create_entries, 'add_entries_form')

    add_entries_form = DTMLFile('add_entries', globals())

    security.declareProtected(permission_change_entries, 'edit_entry_form')

    edit_entry_form = DTMLFile('edit_entry', globals())

    security.declareProtected(permission_change_entries, 'edit_entries_form')

    edit_entries_form = DTMLFile('edit_entries', globals())

    security.declareProtected(permission_change_entries, 'duplicate_entries_form')

    duplicate_entries_form = DTMLFile('duplicate_entries', globals())

    security.declareProtected(permission_change_entries, 'delete_entries_form')

    delete_entries_form = DTMLFile('delete_entries', globals())

    security.declareProtected(permission_change_entries, 'rename_entries_form')

    rename_entries_form = DTMLFile('rename_entries', globals())

    security.declareProtected(permission_change_entries, 'reset_entries_form')

    reset_entries_form = DTMLFile('reset_entries', globals())

    security.declareProtected(permission_change_entries, 'transfer_entries_form')

    transfer_entries_form = DTMLFile('transfer_entries', globals())

    # ------------------------------------------------------------------------
    # Entry Data Processing Helpers

    security.declareProtected(permission_access_entries, 'extract_entry_data')

    def extract_entry_data(self, source, mapping, failsafe=true):
        """Extract the values of the Fields of the specified source from the specified mapping."""

        source = self.get_storage(source)
        return source.extract_entry_data(mapping, failsafe)

    security.declareProtected(permission_access_entries, 'extract_entryfield_data')

    def extract_entryfield_data(self, source, field_id, mapping, failsafe=true):
        """Extract the value of the specified Field of the specified source from the specified mapping"""

        source = self.get_storage(source)
        return source.extract_entryfield_data(field_id, mapping, failsafe)

# ----------------------------------------------------------------------------
# Class Security

InitializeClass(Entries)

# TODO: entries.py - support multi column per field
# TODO: entries.py - specify/implement api for entries without id
# TODO: entries.py - specify/implement api for entries in a tree storage
# TODO: entries.py - specify/implement api for entries in a path storage
