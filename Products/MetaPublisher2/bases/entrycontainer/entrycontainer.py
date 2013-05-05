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

__doc__ = """EntryContainer Base

!TXT! module info

$Id: bases/entrycontainer/entrycontainer.py 1 2012-02-17 15:45:00Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.interfaces import IEntryContainer
from Products.MetaPublisher2.library.common import ClassSecurityInfo, implements, InitializeClass, true, false


# ============================================================================
# Module Exports

__all__ = [
    'EntryContainer',
]


# ============================================================================
# Entry Container Base

class EntryContainer:
    """Entry Container Base"""

    security = ClassSecurityInfo()

    implements(IEntryContainer)

    # ------------------------------------------------------------------------
    # Entry Data Processing Helpers

    def extract_entry_data(self, mapping, failsafe=true):
        """!TXT!"""

        raise NotImplemented

    def extract_entryfield_data(self, field_id, mapping, failsafe=true):
        """!TXT!"""

        raise NotImplemented

    # ------------------------------------------------------------------------
    # Single Entry Retrieval API

    def get_entry(self, parent_entry_id=None, entry_id=None, entry_position=None, field_ids=None, failsafe=false, bound=true):
        """!TXT!"""

        raise NotImplemented

    # ------------------------------------------------------------------------
    # Multiple Entry Retrieval API

    def entry_ids(self, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None, order_by=None, offset=None, limit=None, bound=None):
        """!TXT!"""

        raise NotImplemented

    def entry_items(self, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None, field_ids=None, order_by=None, offset=None, limit=None, bound=None):
        """!TXT!"""

        raise NotImplemented

    def entry_values(self, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None, field_ids=None, order_by=None, offset=None, limit=None, bound=None):
        """!TXT!"""

        raise NotImplemented

    # --------------------------------------------------------------------------
    # Entry Statistics Retrieval API

    def count_entries(self, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None):
        """!TXT!"""

        raise NotImplemented

    # --------------------------------------------------------------------------
    # Entry Existence Retrieval API

    def has_all_entries(self, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None):
        """!TXT!"""

        raise NotImplemented

    def has_any_entries(self, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None):
        """!TXT!"""

        raise NotImplemented

    def has_entry(self, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT!"""

        raise NotImplemented

    # ------------------------------------------------------------------------
    # Entry Creation Mutation API

    def add_entry(self, parent_entry_id=None, entry_id=None, entry_position=None, data={}, **args):
        """!TXT!"""

        raise NotImplemented

    def add_entry_to_top(self, parent_entry_id=None, entry_id=None, data={}, **args):
        """!TXT!"""

        raise NotImplemented

    def add_entry_to_bottom(self, parent_entry_id=None, entry_id=None, data={}, **args):
        """!TXT!"""

        raise NotImplemented

    def add_entry_somewhere(self, parent_entry_id=None, entry_id=None, data={}, **args):
        """!TXT!"""

        raise NotImplemented

    def add_entries(self, entries, parent_entry_id=None):
        """!TXT!"""

        raise NotImplemented

    def add_entries_to_top(self, entries, parent_entry_id=None):
        """!TXT!"""

        raise NotImplemented

    def add_entries_to_bottom(self, entries, parent_entry_id=None):
        """!TXT!"""

        raise NotImplemented

    def add_entries_somewhere(self, entries, parent_entry_id=None):
        """!TXT!"""

        raise NotImplemented

    def duplicate_entry(self, parent_entry_id=None, entry_id=None, entry_position=None, new_id=None):
        """!TXT!"""

        raise NotImplemented

    def duplicate_entries(self, parent_entry_id=None, entry_ids=[], entry_positions=[], conditions=None, new_ids=None):
        """!TXT!"""

        raise NotImplemented

    def set_entry(self, parent_entry_id=None, entry_id=None, entry_position=None, data={}, **args):
        """!TXT!"""

        raise NotImplemented

    # ------------------------------------------------------------------------
    # Entry Modification Mutation API

    def edit_entry(self, parent_entry_id=None, entry_id=None, entry_position=None, data={}, **args):
        """!TXT!"""

        raise NotImplemented

    def edit_entries(self, parent_entry_id=None, entry_ids=[], entry_positions=[], conditions=None, data={}, **args):
        """!TXT!"""

        raise NotImplemented

    def rename_entry(self, parent_entry_id=None, entry_id=None, entry_position=None, new_id=None):
        """!TXT!"""

        raise NotImplemented

    def rename_entries(self, parent_entry_id=None, entry_ids=[], entry_positions=[], conditions=None, new_ids=None):
        """!TXT!"""

        raise NotImplemented

    def reset_entry(self, parent_entry_id=None, entry_id=None, entry_position=None, field_ids=None):
        """!TXT!"""

        raise NotImplemented

    def reset_entries(self, parent_entry_id=None, entry_ids=[], entry_positions=[], conditions=None, field_ids=None):
        """!TXT!"""

        raise NotImplemented

    # ------------------------------------------------------------------------
    # Entry Deletion Mutation API

    def clear_entries(self):
        """!TXT!"""

        raise NotImplemented

    def delete_entry(self, parent_entry_id=None, entry_id=None, entry_position=None, failsafe=false):
        """!TXT!"""

        raise NotImplemented

    def delete_entries(self, parent_entry_id=None, entry_ids=[], entry_positions=[], conditions=None, failsafe=false):
        """!TXT!"""

        raise NotImplemented

    def pop_first_entry(self, parent_entry_id=None, conditions=None):
        """!TXT!"""

        raise NotImplemented

    def pop_last_entry(self, parent_entry_id=None, conditions=None):
        """!TXT!"""

        raise NotImplemented

    def pop_random_entry(self, parent_entry_id=None, conditions=None):
        """!TXT!"""

        raise NotImplemented

    # ------------------------------------------------------------------------
    # EntryField Retrieval API

    def get_entryfield(self, field_id, default=None, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT!"""

        raise NotImplemented

    def count_entryfields(self, field_id, value, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None):
        """!TXT!"""

        raise NotImplemented

    def count_unique_entryfields(self, field_id, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None):
        """!TXT!"""

        raise NotImplemented

    def has_any_entryfields(self, field_id, value, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None):
        """!TXT!"""

        raise NotImplemented

    def has_all_entryfields(self, field_id, value, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None):
        """!TXT!"""

        raise NotImplemented

    def has_entryfield(self, field_id, entry_id):
        """!TXT!"""

        raise NotImplemented

    def get_unique_entryfields(self, field_id, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None):
        """!TXT!"""

        raise NotImplemented

    # ------------------------------------------------------------------------
    # EntryField Mutation API

    def reset_entryfield(self, field_id, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT!"""

        raise NotImplemented

    def reset_entryfields(self, field_id, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None):
        """!TXT!"""

        raise NotImplemented

    def set_entryfield(self, field_id, value, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT!"""

        raise NotImplemented

    def set_entryfields(self, field_id, value, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None):
        """!TXT!"""

        raise NotImplemented

    # ------------------------------------------------------------------------
    # EntrySet Creation API

    def get_entryset(self, field_ids=None, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None, order_by=None, offset=None, limit=None, bound=true, lazy=true, live=false):
        """!TXT!"""

        raise NotImplemented

    def join_entries(self, right_source, join_type='inner', join_conditions=None, field_ids=None, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None, order_by=None, offset=None, limit=None, left_field_ids=None, left_parent_entry_id=None, left_entry_ids=[], left_entry_positions=[], left_conditions=None, left_order_by=None, left_offset=None, left_limit=None, right_field_ids=None, right_parent_entry_id=None, right_entry_ids=[], right_entry_positions=[], right_conditions=None, right_order_by=None, right_offset=None, right_limit=None, bound=true, lazy=true, live=True):
        """!TXT!"""

        raise NotImplemented

    # !!! bases/entrycontainer/entrycontainer.py - review/revise API for select_entries
    def select_entries(self, fields=None, joins=None, conditions=None, order_by=None, offset=None, limit=None, bound=true, live=True):
        """!TXT!"""

        raise NotImplemented

    # ------------------------------------------------------------------------
    # EntrySet Retrieval API

    def is_entryset(self):
        """!TXT!"""

        raise NotImplemented

    def is_entryset_live(self):
        """!TXT!"""

        raise NotImplemented

    def is_entryset_lazy(self):
        """!TXT!"""

        raise NotImplemented

    def is_entryset_bound(self):
        """!TXT!"""

        raise NotImplemented

    def is_source_storage(self):
        """!TXT!"""

        raise NotImplemented

    def get_source_storages(self):
        """!TXT!"""

        raise NotImplemented

    # ------------------------------------------------------------------------
    # EntrySet Mutation API

    def commit_entryset(self):
        """!TXT!"""

        raise NotImplemented

    def reload_entryset(self):
        """!TXT!"""

        raise NotImplemented

    def refresh_entryset(self, field_ids, entry_ids=None, entry_positions=None, conditions=None):
        """!TXT!"""

        raise NotImplemented

    # ------------------------------------------------------------------------
    # Set Theory Retrieval API

    def is_member(self, entry, fields=None, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None):
        """!TXT!"""

        raise NotImplemented

    def is_disjoint(self, other_source, field_ids=None, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None, other_field_ids=None, other_parent_entry_id=None, other_entry_ids=None, other_entry_positions=None, other_conditions=None):
        """!TXT!"""

        raise NotImplemented

    def is_subset(self, other_source, field_ids=None, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None, other_field_ids=None, other_parent_entry_id=None, other_entry_ids=None, other_entry_positions=None, other_conditions=None):
        """!TXT!"""

        raise NotImplemented

    def is_true_subset(self, other_source, field_ids=None, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None, other_field_ids=None, other_parent_entry_id=None, other_entry_ids=[], other_entry_positions=[], other_conditions=None):
        """!TXT!"""

        raise NotImplemented

    def is_superset(self, other_source, field_ids=None, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None, other_field_ids=None, other_parent_entry_id=None, other_entry_ids=[], other_entry_positions=[], other_conditions=None):
        """!TXT!"""

        raise NotImplemented

    def is_true_superset(self, other_source, field_ids=None, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None, other_field_ids=None, other_parent_entry_id=None, other_entry_ids=[], other_entry_positions=[], other_conditions=None):
        """!TXT!"""

        raise NotImplemented

    # ------------------------------------------------------------------------
    # Set Theory Mutation API

    def intersection(self, other_source, field_ids=None, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None, other_field_ids=None, other_parent_entry_id=None, other_entry_ids=[], other_entry_positions=[], other_conditions=None):
        """!TXT!"""

        raise NotImplemented

    def difference(self, other_source, field_ids=None, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None, other_field_ids=None, other_parent_entry_id=None, other_entry_ids=[], other_entry_positions=[], other_conditions=None):
        """!TXT!"""

        raise NotImplemented

    def symmetric_difference(self, other_source, field_ids=None, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None, other_field_ids=None, other_parent_entry_id=None, other_entry_ids=[], other_entry_positions=[], other_conditions=None):
        """!TXT!"""

        raise NotImplemented

    def union(self, other_source, field_ids=None, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None, other_field_ids=None, other_parent_entry_id=None, other_entry_ids=[], other_entry_positions=[], other_conditions=None):
        """!TXT!"""

        raise NotImplemented

    # ------------------------------------------------------------------------
    # Entry Order Retrieval API

    def get_entry_position(self, entry_id, parent_entry_id=None):
        """!TXT!"""

        raise NotImplemented

    def get_entry_positions(self, parent_entry_id=None, entry_ids=None, conditions=None, order_by=None, offset=None, limit=None):
        """!TXT!"""

        raise NotImplemented

    # ------------------------------------------------------------------------
    # Entry Order Mutation API

    def rotate_entries(self, steps, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None):
        """!TXT!"""

        raise NotImplemented

    def order_entries(self, order_by, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None):
        """!TXT!"""

        raise NotImplemented

    def shuffle_entries(self, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None):
        """!TXT!"""

        raise NotImplemented

    def reverse_entries(self, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None):
        """!TXT!"""

        raise NotImplemented

    def move_entry(self, position, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT!"""

        raise NotImplemented

    def move_entry_to_top(self, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT!"""

        raise NotImplemented

    def move_entry_up(self, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT!"""

        raise NotImplemented

    def move_entry_down(self, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT!"""

        raise NotImplemented

    def move_entry_to_bottom(self, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT!"""

        raise NotImplemented

    def move_entries(self, position, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None):
        """!TXT!"""

        raise NotImplemented

    def move_entries_to_top(self, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None):
        """!TXT!"""

        raise NotImplemented

    def move_entries_up(self, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None):
        """!TXT!"""

        raise NotImplemented

    def move_entries_down(self, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None):
        """!TXT!"""

        raise NotImplemented

    def move_entries_to_bottom(self, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None):
        """!TXT!"""

        raise NotImplemented

    # ------------------------------------------------------------------------
    # Single Root Entry Retrieval API

    def is_root_entry(self, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT!"""

        raise NotImplemented

    def root_entry_id(self):
        """!TXT!"""

        raise NotImplemented

    def root_entry_item(self):
        """!TXT!"""

        raise NotImplemented

    def root_entry_value(self):
        """!TXT!"""

        raise NotImplemented

    # ------------------------------------------------------------------------
    # Multiple Root Entry Retrieval API

    def is_top_entry(self, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT!"""

        raise NotImplemented

    def top_entry_ids(self):
        """!TXT!"""

        raise NotImplemented

    def top_entry_items(self):
        """!TXT!"""

        raise NotImplemented

    def top_entry_values(self):
        """!TXT!"""

        raise NotImplemented

    # ------------------------------------------------------------------------
    # Node Type Retrieval API

    def is_entry_branch(self, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT!"""

        raise NotImplemented

    def is_entry_leaf(self, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT!"""

        raise NotImplemented

    def are_entries_branches(self, tree_field_id=None, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None):
        """!TXT!"""

        raise NotImplemented

    def are_entries_leaves(self, tree_field_id=None, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None):
        """!TXT!"""

        raise NotImplemented

    def entry_branch_ids(self, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None, conditions=None, max_levels=None):
        """!TXT!"""

        raise NotImplemented

    def entry_branch_items(self, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None, conditions=None, max_levels=None):
        """!TXT!"""

        raise NotImplemented

    def entry_branch_values(self, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None, conditions=None, max_levels=None):
        """!TXT!"""

        raise NotImplemented

    def entry_leaf_id(self, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None, conditions=None, max_levels=None):
        """!TXT!"""

        raise NotImplemented

    def entry_leaf_items(self, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None, max_levels=None):
        """!TXT!"""

        raise NotImplemented

    def entry_leaf_values(self, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None, max_levels=None):
        """!TXT!"""

        raise NotImplemented

    # ------------------------------------------------------------------------
    # Entry Relationship Retrieval API

    def is_ancestor(self, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None, other_parent_entry_id=None, other_entry_id=None, other_entry_position=None, of_level=None, max_levels=None):
        """!TXT!"""

        raise NotImplemented

    def is_parent(self, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None, other_parent_entry_id=None, other_entry_id=None, other_entry_position=None):
        """!TXT!"""

        raise NotImplemented

    def is_sibling(self, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None, other_parent_entry_id=None, other_entry_id=None, other_entry_position=None):
        """!TXT!"""

        raise NotImplemented

    def is_child(self, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None, other_parent_entry_id=None, other_entry_id=None, other_entry_position=None):
        """!TXT!"""

        raise NotImplemented

    def is_descendant(self, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None, other_parent_entry_id=None, other_entry_id=None, other_entry_position=None, of_level=None, max_levels=None):
        """!TXT!"""

        raise NotImplemented

    # ------------------------------------------------------------------------
    # Entry Ancestor Retrieval API

    def count_ancestor_entries(self, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None, max_levels=None, include_ancestor_siblings=false):
        """!TXT!"""

        raise NotImplemented

    def ancestor_entry_ids(self, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None, max_levels=None, include_ancestor_siblings=false):
        """!TXT!"""

        raise NotImplemented

    def ancestor_entry_items(self, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None, max_levels=None, include_ancestor_siblings=false):
        """!TXT!"""

        raise NotImplemented

    def ancestor_entry_values(self, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None, max_levels=None, include_ancestor_siblings=false):
        """!TXT!"""

        raise NotImplemented

    # ------------------------------------------------------------------------
    # Entry Parent Retrieval API

    def get_parent_entry(self, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT!"""

        raise NotImplemented

    def get_parent_entry_id(self, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT!"""

        raise NotImplemented

    def get_parent_entry_item(self, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT!"""

        raise NotImplemented

    # ------------------------------------------------------------------------
    # Entry Sibling Retrieval API

    def count_sibling_entries(self, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT!"""

        raise NotImplemented

    def has_sibling_entries(self, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT!"""

        raise NotImplemented

    def sibling_entry_ids(self, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT!"""

        raise NotImplemented

    def sibling_entry_items(self, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT!"""

        raise NotImplemented

    def sibling_entry_values(self, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT!"""

        raise NotImplemented

    # ------------------------------------------------------------------------
    # Entry Child Retrieval API

    def count_children_entries(self, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT!"""

        raise NotImplemented

    def has_children_entries(self, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT!"""

        raise NotImplemented

    def children_entry_ids(self, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT!"""

        raise NotImplemented

    def children_entry_items(self, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT!"""

        raise NotImplemented

    def children_entry_values(self, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT!"""

        raise NotImplemented

    # ------------------------------------------------------------------------
    # Entry Descendant Retrieval API

    def count_descendant_entries(self, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None, max_levels=None):
        """!TXT!"""

        raise NotImplemented

    def descendant_entry_ids(self, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None, max_levels=None):
        """!TXT!"""

        raise NotImplemented

    def descendant_entry_items(self, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None, max_levels=None):
        """!TXT!"""

        raise NotImplemented

    def descendant_entry_values(self, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None, max_levels=None):
        """!TXT!"""

        raise NotImplemented

    # ------------------------------------------------------------------------
    # Entry Tree Mutation API

    def move_entry_branch(self, tree_field_id=None, destination_entry_id=None, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT!"""

        raise NotImplemented

    def move_entry_branches(self, tree_field_id=None, destination_entry_id=None, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None):
        """!TXT!"""

        raise NotImplemented

    def flatten_entry_branch(self, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None, max_levels=None):
        """!TXT!"""

        raise NotImplemented

    def flatten_entry_branches(self, tree_field_id=None, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None, max_levels=None):
        """!TXT!"""

        raise NotImplemented

    def crop_entry_branch(self, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT!"""

        raise NotImplemented

    def crop_entry_branches(self, tree_field_id=None, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None):
        """!TXT!"""

        raise NotImplemented

    # ------------------------------------------------------------------------
    # Entry Stats Retrieval

    def stat_entry(self, entry_id):
        """!TXT!"""

        raise NotImplemented

    def stat_entries(self, entry_ids=None, conditions=None):
        """!TXT!"""

        raise NotImplemented

    def get_entry_stat_size(self, entry_id):
        """!TXT!"""

        raise NotImplemented

    def get_entry_stat_ctime(self, entry_id):
        """!TXT!"""

        raise NotImplemented

    def get_entry_stat_cuser(self, entry_id):
        """!TXT!"""

        raise NotImplemented

    def get_entry_stat_mtime(self, entry_id):
        """!TXT!"""

        raise NotImplemented

    def get_entry_stat_muser(self, entry_id):
        """!TXT!"""

        raise NotImplemented

    def get_entry_stat_atime(self, entry_id):
        """!TXT!"""

        raise NotImplemented

    def get_entry_stat_auser(self, entry_id):
        """!TXT!"""

        raise NotImplemented

    # ------------------------------------------------------------------------
    # Entry Stats Retrieval

    def touch_entry(self, entry_id):
        """!TXT!"""

        raise NotImplemented

    def touch_entries(self, entry_ids=None, conditions=None):
        """!TXT!"""

        raise NotImplemented

    def access_entry(self, entry_id):
        """!TXT!"""

        raise NotImplemented

    def access_entries(self, entry_ids=None, conditions=None):
        """!TXT!"""

        raise NotImplemented

# ----------------------------------------------------------------------------
# initialize class security

InitializeClass(EntryContainer)

# !!! bases/entrycontainer/entrycontainer.py - review api
# !!! bases/entrycontainer/entrycontainer.py - implement backdrop/failsafe code
