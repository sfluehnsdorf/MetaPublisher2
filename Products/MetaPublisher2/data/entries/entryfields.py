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

__doc__ = """EntryFields Component

$Id: data/entries/entryfields.py 11 2012-08-09 19:48:00Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.library import ClassSecurityInfo, InitializeClass, permission_access_entries, permission_change_entries


# ============================================================================
# Module Exports

__all__ = [
    'EntryFields',
]


# ============================================================================
# EntryFields Mix-In Class

class EntryFields:
    """EntryFields Mix-In Class"""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # EntryField Retrieval API

    security.declareProtected(permission_access_entries, 'get_entryfield')

    def get_entryfield(self, source, field_id, default=None, parent_entry_id=None, entry_id=None, entry_position=None):
        """Return the specified Entry's Field's value"""

        source = self.get_storage(source)
        return source.get_entryfield(field_id, default, parent_entry_id, entry_id, entry_position)

    # !!! entryfields.py - implement get_entryfields

    # !!! entryfields.py - implement get_entryfields_mapping

    security.declareProtected(permission_access_entries, 'count_entryfields')

    def count_entryfields(self, source, field_id, value, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None):
        """Count the number of Entries, with a specific Field's value"""

        source = self.get_storage(source)
        return source.count_entryfields(field_id, value, parent_entry_id, entry_ids, entry_positions, conditions)

    security.declareProtected(permission_access_entries, 'count_unique_entryfields')

    def count_unique_entryfields(self, source, field_id, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None):
        """Return a mapping with the number of Entries for each unique value of a specific Field's value"""

        source = self.get_storage(source)
        return source.count_unique_entryfields(field_id, parent_entry_id, entry_ids, entry_positions, conditions)

    security.declareProtected(permission_access_entries, 'has_any_entryfields')

    def has_any_entryfields(self, source, field_id, value, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None):
        """Return True if any of the specified Entries have the specified value in the specified Field, limited to the Entries specified and matching conditions if defined."""

        source = self.get_storage(source)
        return source.has_any_entryfields(field_id, value, parent_entry_id, entry_ids, entry_positions, conditions)

    security.declareProtected(permission_access_entries, 'has_all_entryfields')

    def has_all_entryfields(self, source, field_id, value, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None):
        """Return True if all of the specified Entries have the specified value in the specified Field, limited to the Entries specified and matching conditions if defined."""

        source = self.get_storage(source)
        return source.has_all_entryfields(field_id, value, parent_entry_id, entry_ids, entry_positions, conditions)

    security.declareProtected(permission_access_entries, 'has_entryfield')

    def has_entryfield(self, source, field_id, entry_id):
        """Return True if the specified EntryField exists and has a value different from None."""

        source = self.get_storage(source)
        return source.has_entryfield(field_id, entry_id)

    security.declareProtected(permission_access_entries, 'get_unique_entryfields')

    def get_unique_entryfields(self, source, field_id, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None):
        """Return a list of unique values stored in the specified Field, limited to the Entries specified and matching conditions if defined."""

        source = self.get_storage(source)
        return source.get_unique_entryfields(field_id, parent_entry_id, entry_ids, entry_positions, conditions)

    # ------------------------------------------------------------------------
    # EntryField Mutation API

    security.declareProtected(permission_change_entries, 'reset_entryfield')

    def reset_entryfield(self, source, field_id, parent_entry_id=None, entry_id=None, entry_position=None):
        """Reset the specified Field of the specified Entry to its default value."""

        source = self.get_storage(source)
        source.reset_entryfield(field_id, parent_entry_id, entry_id, entry_position)

    security.declareProtected(permission_change_entries, 'reset_entryfields')

    def reset_entryfields(self, source, field_id, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None):
        """Reset the specified Field of the specified Entries, matching conditions if defined, to its default value."""

        source = self.get_storage(source)
        source.reset_entryfields(field_id, parent_entry_id, entry_ids, entry_positions, conditions)

    security.declareProtected(permission_change_entries, 'set_entryfield')

    def set_entryfield(self, source, field_id, value, parent_entry_id=None, entry_id=None, entry_position=None):
        """Set the value of the specified Field of the specified Entry."""

        source = self.get_storage(source)
        source.set_entryfield(field_id, parent_entry_id, entry_id, entry_position)

    security.declareProtected(permission_change_entries, 'set_entryfields')

    def set_entryfields(self, source, field_id, value, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None):
        """Set the values of the specified Field of the specified Entries, matching conditions if defined."""

        source = self.get_storage(source)
        source.set_entryfields(field_id, value, parent_entry_id, entry_ids, entry_positions, conditions)

# ----------------------------------------------------------------------------
# Class Security

InitializeClass(EntryFields)
