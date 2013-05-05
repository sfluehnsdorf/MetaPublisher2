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

__doc__ = """EntrySets Component

!TXT! module info

$Id: data/entries/entrysets.py 8 2013-05-05 18:01:53Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.library import ClassSecurityInfo, InitializeClass, permission_access_entries, permission_change_entries, true, false


# ============================================================================
# Module Exports

__all__ = [
    'EntrySets',
]


# ============================================================================
# EntrySets Mix-In Class

class EntrySets:
    """EntrySets Mix-In Class"""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # EntrySet Creation API

    security.declareProtected(permission_access_entries, 'get_entryset')

    def get_entryset(self, source, field_ids=None, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None, order_by=None, offset=None, limit=None, bound=true, lazy=true, live=false):
        """
        Retrieve Entries from a source

        Return an EntrySet with the Entries of the specified source, ordered by
        a specific EntryField's value and limited to the Entries specified by
        ids or positions and matching conditions if defined.

        source
          the id of a Storage, a Storage or an EntrySet to retrieve the Entries
          from.

        field_ids
          the ids of the Fields, that will be returned. A 2-tuple identifies the
          Field with the first item and specifies an alias for it with the
          second item. If undefined or 'primary' string will return all primary
          Fields. If '*' string will return all Fields.

        parent_entry_id
          the parent Entry that the specified Entry is searched in. If no parent
          Entry is specified, the root Entry is used.

        entry_ids
          the unique ids identifying the Entries. If specified, entry_positions
          must be None or a ValueError exception will be raised.

        entry_positions
          the position identifying the Entries. If specified, entry_ids must be
          None or a ValueError exception will be raised.

        conditions
          one or more filter expression that limit the Entries to return.

        order_by
          one or more Field id to order on or order expression used to sort the
          Entries.

        offset
          the index of the first Entry to return from the total result set. Must
          be an integer greater or equal to zero.

        limit
          the maxinum number of Entries to return. Must be an integer greater or
          equal to zero.

        bound
          if True, the returned EntrySet is bound to the source, referencing the
          origin of the Entries in the EntrySet.

        lazy
          if True, Entries and EntryFields are loaded from the source as needed.
          The EntrySet must be bound for lazy retrieval.

        live
          if True, the returned EntrySet is live and all changes to it affect
          the source's Entries immediately.
        """

        source = self.get_storage(source)
        return source.get_entryset(field_ids, parent_entry_id, entry_ids, entry_positions, conditions, order_by, offset, limit, bound, live)

    security.declareProtected(permission_access_entries, 'join_entries')

    def join_entries(self, left_source, right_source, join_type='inner', join_conditions=None, field_ids=None, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None, order_by=None, offset=None, limit=None, left_field_ids=None, left_parent_entry_id=None, left_entry_ids=[], left_entry_positions=[], left_conditions=None, left_order_by=None, left_offset=None, left_limit=None, right_field_ids=None, right_parent_entry_id=None, right_entry_ids=[], right_entry_positions=[], right_conditions=None, right_order_by=None, right_offset=None, right_limit=None, bound=true, lazy=true, live=True):
        """
        Join the Entries of two sources

        Return an EntrySet with the Entries resulting from the join of the two
        specified sources, using the specified join type and matching the
        specified conditions if defined and .

        left_source
          the id of a Storage, a Storage or an EntrySet to retrieve the Entries
          from for the left side of the join.

        right_source
          the id of a Storage, a Storage or an EntrySet to retrieve the Entries
          from for the right side of the join.

        join_conditions

        join_type
          the type of the join to apply. Valid values are 'inner', 'left',
          'right', 'full' and 'cartesian'.

        field_ids
          the ids of the Fields, that will be returned. A 2-tuple identifies the
          Field with the first item and specifies an alias for it with the
          second item. If undefined or 'primary' string will return all primary
          Fields. If '*' string will return all Fields.

          !TXT!

          To avoid ambiguities, a Field id can be prefixed with a source
          Storage's id or the 'left' and 'right' identifier, seperated from the Field's id by a period, for example 'mystorage.id' or 'left.id'

        parent_entry_id
        entry_ids
        entry_positions
        conditions
        order_by
        offset
        limit
          modifiers for the resulting Entries. See get_entryset() for details.

        left_field_ids
        left_parent_entry_id
        left_entry_ids
        left_entry_positions
        left_conditions
        left_order_by
        left_offset
        left_limit
          modifiers for the left source's Entries.

        right_field_ids
        right_parent_entry_id
        right_entry_ids
        right_entry_positions
        right_conditions
        right_order_by
        right_offset
        right_limit
          modifiers for the right source's Entries.

        bound
          if True, the returned EntrySet is bound to the source, referencing the
          origin of the Entries in the EntrySet.

        lazy
          if True, Entries and EntryFields are loaded from the source as needed.
          The EntrySet must be bound for lazy retrieval.

        live
          if True, the returned EntrySet is live and all changes to it affect
          the source's Entries immediately.
        """

        source = self.get_storage(source)
        return source.join_entries(right_source, join_type, join_conditions, field_ids, parent_entry_id, entry_ids, entry_positions, conditions, order_by, offset, limit, left_field_ids, left_parent_entry_id, left_entry_ids, left_entry_positions, left_conditions, left_order_by, left_offset, left_limit, right_field_ids, right_parent_entry_id, right_entry_ids, right_entry_positions, right_conditions, right_order_by, right_offset, right_limit, bound, lazy, live)

    security.declareProtected(permission_access_entries, 'select_entries')

    # !!! entrysets.py - revise select_entries api
    def select_entries(self, source, fields=None, joins=None, conditions=None, order_by=None, offset=None, limit=None, bound=true, live=True):
        """
        Retrieve Entries from one or more sources

        Return an EntrySet with the Entries from the specified source, joined
        with the specified sources matching optional conditions, ordered by a
        specific EntryField's value.

        source
          the id of a Storage, a Storage or an EntrySet to retrieve the Entries
          from.

        fields
          the ids of the Fields, that will be returned. A 2-tuple identifies the
          Field with the first item and specifies an alias for it with the
          second item. Instead of a Field id an expression may be defined with
          an alias. If undefined or 'primary' string will return all primary
          Fields. If '*' string will return all Fields.

A Field id can be prefixed with a source Storage's id or a source's index in the list of sources,
seperated from the Field's by a period, for example 'mystorage.id' or '0.id'

!TXT! seperate storage from field with '.' ??? - may be used in some storage types, space might be better OR tuple (but how to diff from alias?)

          If undefined or the '*' string, will return all primary Fields. If the
          list of Fields is ambiguous a !TXT! error is raised.

        joins
          list of strings or 2-tuples identifying the types of joins to apply
          with optional conditions. Supported types of joins are 'inner',
          'left', 'right' and 'outer'. The default join type for two sources is
          an inner join.
        """

        source = self.get_storage(source)
        return source.select_entries(fields, joins, conditions, order_by, offset, limit, bound, live)

    # --------------------------------------------------------------------------
    # EntrySet Retrieval API

    security.declareProtected(permission_access_entries, 'is_entryset')

    def is_entryset(self, source):
        """!TXT! Return true, if the specified source is an EntrySet."""

        source = self.get_storage(source)
        return source.is_entryset()

    security.declareProtected(permission_access_entries, 'is_entryset_live')

    def is_entryset_live(self, source):
        """!TXT! Return true, if all changes to the EntrySet affect the Storage immediately (non transactional/no commit needed) - this may be ambigious if bound to more than one Storage."""

        source = self.get_storage(source)
        return source.is_entryset_live()

    security.declareProtected(permission_access_entries, 'is_entryset_lazy')

    def is_entryset_lazy(self, source):
        """!TXT! Return true, if all Entries and EntryFields are loaded from the source as needed, False otherwise. This implies that the source is bound to a Storage."""

        source = self.get_storage(source)
        return source.is_entryset_lazy()

    security.declareProtected(permission_access_entries, 'is_entryset_bound')

    def is_entryset_bound(self, source):
        """Return True if the specified source is bound to one or more Storages, meaning that the EntrySet indicates the sources (Storages) for Fields and their values, False otherwise."""

        source = self.get_storage(source)
        return source.is_entryset_bound()

    security.declareProtected(permission_access_entries, 'is_source_storage')

    def is_source_storage(self, source):

        source = self.get_storage(source)
        return source.is_source_storage()

    security.declareProtected(permission_access_entries, 'get_source_storages')

    def get_source_storages(self, source):
        """Return the list of all Storages, the specified source is bound to. If the source is unbound or a Storage, the result is None."""

        source = self.get_storage(source)
        return source.get_source_storages()

    # ------------------------------------------------------------------------
    # EntrySet Mutation API

    security.declareProtected(permission_change_entries, 'commit_entryset')

    def commit_entryset(self, source):
        """Save all changes made to the specified source. If the source is an EntrySet changed are saved to the bound Storages. If the source is a transactional Storage, it will commit changes to the connected storage engine."""

        source = self.get_storage(source)
        return source.commit_entryset()

    security.declareProtected(permission_change_entries, 'reload_entryset')

    def reload_entryset(self, source):
        """Remove and reload all Entries of the EntrySet from the bound Storages, by calling the conditions used to populate the EntrySet again. If no method to reload the EntrySet exists, an !TXT! exception is raised."""

        source = self.get_storage(source)
        return source.reload_entryset()

    security.declareProtected(permission_change_entries, 'refresh_entryset')

    def refresh_entryset(self, source, field_ids, entry_ids=None, entry_positions=None, conditions=None):
        """Reload the values for all EntryFields stored in the EntrySet from the bound Storages, limited to, if defined, the Entries specified by ids, position and matching conditions. If an Entry no longer exists in the bound Storage, it will remain in the EntrySet untouched."""

        source = self.get_storage(source)
        return source.refresh_entryset(field_ids, entry_ids, entry_positions, conditions)

    # ------------------------------------------------------------------------
    # Set Theory Retrieval API

    security.declareProtected(permission_access_entries, 'is_member')

    def is_member(self, source, entry, fields=None, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None):
        """
        Return True if the entry is a member of the Storage.

        Test if the an Entry with the specified Fields' values exists in the
        specified source.

        source
          the id of a Storage, a Storage or an EntrySet to test the Entry
          against.

        entry
          an Entry or a mapping that must contain at least the Fields tested for
          in the specified source.

        fields
          list of Fields to consider for testing. A string represents a Field
          with the same id in the Entry and the source. A 2-tuple identifies
          the Field in the Entry with the first item and the Field in the source
          with the second item, mapping the two differently named Fields to each
          other. Instead of a Field id an expression may be defined. If
          undefined or 'primary' string specifies all primary Fields. If '*'
          string specifies all Fields. For both of these cases the Fields' ids
          must be identical in both Entry and source.

        parent_entry_id
          optionally and for hierarchical Storages only, this identifies the
          the root in the source.

        entry_ids
          optionally specifies which Entries from the source with matching ids
          to limit to.

        entry_positions
          optionally specifies which Entries from the source with matching
          positions to limit to.

        conditions
          optionally specifies one or more filters to apply to Entries from the
          source.
        """

        source = self.get_storage(source)
        return source.is_member(entry, field_ids, parent_entry_id, entry_ids, entry_positions, conditions)

    security.declareProtected(permission_access_entries, 'is_disjoint')

    def is_disjoint(self, source, other_source, field_ids=None, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None, other_field_ids=None, other_parent_entry_id=None, other_entry_ids=None, other_entry_positions=None, other_conditions=None):
        """Return True if the Storage has no Entries in common with the other Storage."""

        source = self.get_storage(source)
        other_source = self.get_storage(other_source)
        return source.is_disjoint(other_source, field_ids, parent_entry_id, entry_ids, entry_positions, conditions, other_field_ids, other_parent_entry_id, other_entry_ids, other_entry_positions, other_conditions)

    security.declareProtected(permission_access_entries, 'is_subset')

    def is_subset(self, source, other_source, field_ids=None, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None, other_field_ids=None, other_parent_entry_id=None, other_entry_ids=None, other_entry_positions=None, other_conditions=None):
        """Return True if all Entries from the Storage is in the other Storage."""

        source = self.get_storage(source)
        other_source = self.get_storage(other_source)
        return source.is_subset(other_source, field_ids, parent_entry_id, entry_ids, entry_positions, conditions, other_field_ids, other_parent_entry_id, other_entry_ids, other_entry_positions, other_conditions)

    security.declareProtected(permission_access_entries, 'is_true_subset')

    def is_true_subset(self, source, other_source, field_ids=None, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None, other_field_ids=None, other_parent_entry_id=None, other_entry_ids=[], other_entry_positions=[], other_conditions=None):
        """Return True if all Entries from the Storage are in the other Storage, but both Storages are not identical."""

        source = self.get_storage(source)
        other_source = self.get_storage(other_source)
        return source.is_true_subset(other_source, field_ids, parent_entry_id, entry_ids, entry_positions, conditions, other_field_ids, other_parent_entry_id, other_entry_ids, other_entry_positions, other_conditions)

    security.declareProtected(permission_access_entries, 'is_superset')

    def is_superset(self, source, other_source, field_ids=None, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None, other_field_ids=None, other_parent_entry_id=None, other_entry_ids=[], other_entry_positions=[], other_conditions=None):
        """Return True if all Entries from the Storage is in the other Storage."""

        source = self.get_storage(source)
        other_source = self.get_storage(other_source)
        return source.is_superset(other_source, field_ids, parent_entry_id, entry_ids, entry_positions, conditions, other_field_ids, other_parent_entry_id, other_entry_ids, other_entry_positions, other_conditions)

    security.declareProtected(permission_access_entries, 'is_true_superset')

    def is_true_superset(self, source, other_source, field_ids=None, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None, other_field_ids=None, other_parent_entry_id=None, other_entry_ids=[], other_entry_positions=[], other_conditions=None):
        """Return True if all Entries from the Storage is in the other Storage, but both Storages are not identical."""

        source = self.get_storage(source)
        other_source = self.get_storage(other_source)
        return source.is_true_superset(other_source, field_ids, parent_entry_id, entry_ids, entry_positions, conditions, other_field_ids, other_parent_entry_id, other_entry_ids, other_entry_positions, other_conditions)

    # ------------------------------------------------------------------------
    # Set Theory Mutation API

    security.declareProtected(permission_change_entries, 'intersection')

    def intersection(self, source, other_source, field_ids=None, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None, other_field_ids=None, other_parent_entry_id=None, other_entry_ids=[], other_entry_positions=[], other_conditions=None):
        """Return an EntrySet with Entries common to both sources."""

        source = self.get_storage(source)
        other_source = self.get_storage(other_source)
        return source.intersection(other_source, field_ids, parent_entry_id, entry_ids, entry_positions, conditions, other_field_ids, other_parent_entry_id, other_entry_ids, other_entry_positions, other_conditions)

    security.declareProtected(permission_change_entries, 'difference')

    def difference(self, source, other_source, field_ids=None, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None, other_field_ids=None, other_parent_entry_id=None, other_entry_ids=[], other_entry_positions=[], other_conditions=None):
        """Return an EntrySet with Entries in the source that are not in the other source."""

        source = self.get_storage(source)
        other_source = self.get_storage(other_source)
        return source.difference(other_source, field_ids, parent_entry_id, entry_ids, entry_positions, conditions, other_field_ids, other_parent_entry_id, other_entry_ids, other_entry_positions, other_conditions)

    security.declareProtected(permission_change_entries, 'symmetric_difference')

    def symmetric_difference(self, source, other_source, field_ids=None, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None, other_field_ids=None, other_parent_entry_id=None, other_entry_ids=[], other_entry_positions=[], other_conditions=None):
        """Return an EntrySet with Entries in either the source or the other source but not in both."""

        source = self.get_storage(source)
        other_source = self.get_storage(other_source)
        return source.symmetric_difference(other_source, field_ids, parent_entry_id, entry_ids, entry_positions, conditions, other_field_ids, other_parent_entry_id, other_entry_ids, other_entry_positions, other_conditions)

    security.declareProtected(permission_change_entries, 'union')

    def union(self, source, other_source, field_ids=None, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None, other_field_ids=None, other_parent_entry_id=None, other_entry_ids=[], other_entry_positions=[], other_conditions=None):
        """Return an EntrySet with Entries from two sources."""

        source = self.get_storage(source)
        other_source = self.get_storage(other_source)
        return source.union(other_source, field_ids, parent_entry_id, entry_ids, entry_positions, conditions, other_field_ids, other_parent_entry_id, other_entry_ids, other_entry_positions, other_conditions)

# ----------------------------------------------------------------------------
# Class Security

InitializeClass(EntrySets)
