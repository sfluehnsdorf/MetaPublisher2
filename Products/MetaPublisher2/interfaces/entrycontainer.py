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

__doc__ = """EntryContainer Interface

!TXT! module info

$Id: interfaces/entrycontainer.py 3 2013-05-07 17:48:57Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from zope.interface import Interface
#from zope.interface import Attribute
#from zope.schema import Bool, BytesLine, List, Tuple, URI

from Products.MetaPublisher2.library.common import false, true


# ============================================================================
# Module Exports

__all__ = [
    'IEntryContainer',
]


# ==============================================================================
# EntryContainer Class Interface

class IEntryContainer(Interface):
    """EntryContainer Class Interface"""

    # ------------------------------------------------------------------------
    # Entry Data Processing Helpers

    def extract_entry_data(mapping, failsafe=true):
        """!TXT!"""

    def extract_entryfield_data(field_id, mapping, failsafe=true):
        """!TXT!"""

    # ------------------------------------------------------------------------
    # Single Entry Retrieval API

    def get_entry(parent_entry_id=None, entry_id=None, entry_position=None, field_ids=None, failsafe=false, bound=true):
        """!TXT!"""

    # ------------------------------------------------------------------------
    # Multiple Entry Retrieval API

    def entry_ids(parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None, order_by=None, offset=None, limit=None, bound=true):
        """!TXT!"""

    def entry_items(parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None, field_ids=None, order_by=None, offset=None, limit=None, bound=true):
        """!TXT!"""

    def entry_values(parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None, field_ids=None, order_by=None, offset=None, limit=None, bound=true):
        """!TXT!"""

    # ------------------------------------------------------------------------
    # Entry Statistics Retrieval API

    def count_entries(parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None):
        """!TXT!"""

    # ------------------------------------------------------------------------
    # Entry Existence Retrieval API

    def has_all_entries(parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None):
        """!TXT!"""

    def has_any_entries(parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None):
        """!TXT!"""

    def has_entry(parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT!"""

    # ------------------------------------------------------------------------
    # Entry Creation Mutation API

    def add_entry(parent_entry_id=None, entry_id=None, entry_position=None, data={}, **args):
        """!TXT!"""

    def add_entry_to_top(parent_entry_id=None, entry_id=None, data={}, **args):
        """!TXT!"""

    def add_entry_to_bottom(parent_entry_id=None, entry_id=None, data={}, **args):
        """!TXT!"""

    def add_entry_somewhere(parent_entry_id=None, entry_id=None, data={}, **args):
        """!TXT!"""

    def add_entries(entries, parent_entry_id=None):
        """!TXT!"""

    def add_entries_to_top(entries, parent_entry_id=None):
        """!TXT!"""

    def add_entries_to_bottom(entries, parent_entry_id=None):
        """!TXT!"""

    def add_entries_somewhere(entries, parent_entry_id=None):
        """!TXT!"""

    def duplicate_entry(parent_entry_id=None, entry_id=None, entry_position=None, new_id=None):
        """!TXT!"""

    def duplicate_entries(parent_entry_id=None, entry_ids=[], entry_positions=[], conditions=None, new_ids=None):
        """!TXT!"""

    def set_entry(parent_entry_id=None, entry_id=None, entry_position=None, data={}, **args):
        """!TXT!"""

    # ------------------------------------------------------------------------
    # Entry Modification Mutation API

    def edit_entry(parent_entry_id=None, entry_id=None, entry_position=None, data={}, **args):
        """!TXT!"""

    def edit_entries(parent_entry_id=None, entry_ids=[], entry_positions=[], conditions=None, data={}, **args):
        """!TXT!"""

    def rename_entry(parent_entry_id=None, entry_id=None, entry_position=None, new_id=None):
        """!TXT!"""

    def rename_entries(parent_entry_id=None, entry_ids=[], entry_positions=[], conditions=None, new_ids=None):
        """!TXT!"""

    def reset_entry(parent_entry_id=None, entry_id=None, entry_position=None, field_ids=None):
        """!TXT!"""

    def reset_entries(parent_entry_id=None, entry_ids=[], entry_positions=[], conditions=None, field_ids=None):
        """!TXT!"""

    # ------------------------------------------------------------------------
    # Entry Deletion Mutation API

    def clear_entries():
        """!TXT!"""

    def delete_entry(parent_entry_id=None, entry_id=None, entry_position=None, failsafe=false):
        """!TXT!"""

    def delete_entries(parent_entry_id=None, entry_ids=[], entry_positions=[], conditions=None, failsafe=false):
        """!TXT!"""

    def pop_first_entry(parent_entry_id=None, conditions=None):
        """!TXT!"""

    def pop_last_entry(parent_entry_id=None, conditions=None):
        """!TXT!"""

    def pop_random_entry(parent_entry_id=None, conditions=None):
        """!TXT!"""

    # ------------------------------------------------------------------------
    # EntryField Retrieval API

    def get_entryfield(field_id, default=None, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT!"""

    def count_entryfields(field_id, value, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None):
        """!TXT!"""

    def count_unique_entryfields(field_id, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None):
        """!TXT!"""

    def has_any_entryfields(field_id, value, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None):
        """!TXT!"""

    def has_all_entryfields(field_id, value, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None):
        """!TXT!"""

    def has_entryfield(field_id, entry_id):
        """!TXT!"""

    def get_unique_entryfields(field_id, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None):
        """!TXT!"""

    # ------------------------------------------------------------------------
    # EntryField Mutation API

    def reset_entryfield(field_id, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT!"""

    def reset_entryfields(field_id, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None):
        """!TXT!"""

    def set_entryfield(field_id, value, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT!"""

    def set_entryfields(field_id, value, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None):
        """!TXT!"""

    # ------------------------------------------------------------------------
    # EntrySet Creation API

    def get_entryset(field_ids=None, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None, order_by=None, offset=None, limit=None, bound=true, lazy=true, live=false):
        """!TXT!"""

    def join_entries(
        right_source, join_type='inner', join_conditions=None, field_ids=None,
        parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None, order_by=None, offset=None, limit=None,
        left_field_ids=None, left_parent_entry_id=None, left_entry_ids=[], left_entry_positions=[], left_conditions=None, left_order_by=None, left_offset=None, left_limit=None,
        right_field_ids=None, right_parent_entry_id=None, right_entry_ids=[], right_entry_positions=[], right_conditions=None, right_order_by=None, right_offset=None, right_limit=None,
        bound=true, lazy=true, live=True
    ):
        """!TXT!"""

    # !!! interfaces/entrycontainer.py - check API of select_entries
    def select_entries(fields=None, joins=None, conditions=None, order_by=None, offset=None, limit=None, bound=true, live=True):
        """!TXT!"""

    # ------------------------------------------------------------------------
    # EntrySet Retrieval API

    def is_entryset():
        """!TXT!"""

    def is_entryset_live():
        """!TXT!"""

    def is_entryset_lazy():
        """!TXT!"""

    def is_entryset_bound():
        """!TXT!"""

    def is_source_storage():
        """!TXT!"""

    def get_source_storages():
        """!TXT!"""

    # ------------------------------------------------------------------------
    # EntrySet Mutation API

    def commit_entryset():
        """!TXT!"""

    def reload_entryset():
        """!TXT!"""

    def refresh_entryset(field_ids, entry_ids=None, entry_positions=None, conditions=None):
        """!TXT!"""

    # ------------------------------------------------------------------------
    # Set Theory Retrieval API

    def is_member(entry, fields=None, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None):
        """!TXT!"""

    def is_disjoint(other_source, field_ids=None, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None, other_field_ids=None, other_parent_entry_id=None, other_entry_ids=None, other_entry_positions=None, other_conditions=None):
        """!TXT!"""

    def is_subset(other_source, field_ids=None, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None, other_field_ids=None, other_parent_entry_id=None, other_entry_ids=None, other_entry_positions=None, other_conditions=None):
        """!TXT!"""

    def is_true_subset(other_source, field_ids=None, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None, other_field_ids=None, other_parent_entry_id=None, other_entry_ids=[], other_entry_positions=[], other_conditions=None):
        """!TXT!"""

    def is_superset(other_source, field_ids=None, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None, other_field_ids=None, other_parent_entry_id=None, other_entry_ids=[], other_entry_positions=[], other_conditions=None):
        """!TXT!"""

    def is_true_superset(other_source, field_ids=None, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None, other_field_ids=None, other_parent_entry_id=None, other_entry_ids=[], other_entry_positions=[], other_conditions=None):
        """!TXT!"""

    # ------------------------------------------------------------------------
    # Set Theory Mutation API

    def intersection(other_source, field_ids=None, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None, other_field_ids=None, other_parent_entry_id=None, other_entry_ids=[], other_entry_positions=[], other_conditions=None):
        """!TXT!"""

    def difference(other_source, field_ids=None, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None, other_field_ids=None, other_parent_entry_id=None, other_entry_ids=[], other_entry_positions=[], other_conditions=None):
        """!TXT!"""

    def symmetric_difference(other_source, field_ids=None, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None, other_field_ids=None, other_parent_entry_id=None, other_entry_ids=[], other_entry_positions=[], other_conditions=None):
        """!TXT!"""

    def union(other_source, field_ids=None, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None, other_field_ids=None, other_parent_entry_id=None, other_entry_ids=[], other_entry_positions=[], other_conditions=None):
        """!TXT!"""

    # ------------------------------------------------------------------------
    # Entry Order Retrieval API

    def get_entry_position(entry_id, parent_entry_id=None):
        """!TXT!"""

    def get_entry_positions(parent_entry_id=None, entry_ids=None, conditions=None, order_by=None, offset=None, limit=None):
        """!TXT!"""

    # ------------------------------------------------------------------------
    # Entry Order Mutation API

    def rotate_entries(steps, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None):
        """!TXT!"""

    def order_entries(order_by, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None):
        """!TXT!"""

    def shuffle_entries(parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None):
        """!TXT!"""

    def reverse_entries(parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None):
        """!TXT!"""

    def move_entry(position, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT!"""

    def move_entry_to_top(parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT!"""

    def move_entry_up(parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT!"""

    def move_entry_down(parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT!"""

    def move_entry_to_bottom(parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT!"""

    def move_entries(position, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None):
        """!TXT!"""

    def move_entries_to_top(parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None):
        """!TXT!"""

    def move_entries_up(parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None):
        """!TXT!"""

    def move_entries_down(parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None):
        """!TXT!"""

    def move_entries_to_bottom(parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None):
        """!TXT!"""

    # ------------------------------------------------------------------------
    # Single Root Entry Retrieval API

    def is_root_entry(tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT!"""

    def root_entry_id():
        """!TXT!"""

    def root_entry_item():
        """!TXT!"""

    def root_entry_value():
        """!TXT!"""

    # ------------------------------------------------------------------------
    # Multiple Root Entry Retrieval API

    def is_top_entry(tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT!"""

    def top_entry_ids():
        """!TXT!"""

    def top_entry_items():
        """!TXT!"""

    def top_entry_values():
        """!TXT!"""

    # ------------------------------------------------------------------------
    # Node Type Retrieval API

    def is_entry_branch(tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT!"""

    def is_entry_leaf(tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT!"""

    def are_entries_branches(tree_field_id=None, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None):
        """!TXT!"""

    def are_entries_leaves(tree_field_id=None, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None):
        """!TXT!"""

    def entry_branch_ids(tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None, conditions=None, max_levels=None):
        """!TXT!"""

    def entry_branch_items(tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None, conditions=None, max_levels=None):
        """!TXT!"""

    def entry_branch_values(tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None, conditions=None, max_levels=None):
        """!TXT!"""

    def entry_leaf_id(tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None, conditions=None, max_levels=None):
        """!TXT!"""

    def entry_leaf_items(tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None, max_levels=None):
        """!TXT!"""

    def entry_leaf_values(tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None, max_levels=None):
        """!TXT!"""

    # ------------------------------------------------------------------------
    # Entry Relationship Retrieval API

    def is_ancestor(tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None, other_parent_entry_id=None, other_entry_id=None, other_entry_position=None, of_level=None, max_levels=None):
        """!TXT!"""

    def is_parent(tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None, other_parent_entry_id=None, other_entry_id=None, other_entry_position=None):
        """!TXT!"""

    def is_sibling(tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None, other_parent_entry_id=None, other_entry_id=None, other_entry_position=None):
        """!TXT!"""

    def is_child(tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None, other_parent_entry_id=None, other_entry_id=None, other_entry_position=None):
        """!TXT!"""

    def is_descendant(tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None, other_parent_entry_id=None, other_entry_id=None, other_entry_position=None, of_level=None, max_levels=None):
        """!TXT!"""

    # ------------------------------------------------------------------------
    # Entry Ancestor Retrieval API

    def count_ancestor_entries(tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None, max_levels=None, include_ancestor_siblings=false):
        """!TXT!"""

    def ancestor_entry_ids(tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None, max_levels=None, include_ancestor_siblings=false):
        """!TXT!"""

    def ancestor_entry_items(tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None, max_levels=None, include_ancestor_siblings=false):
        """!TXT!"""

    def ancestor_entry_values(tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None, max_levels=None, include_ancestor_siblings=false):
        """!TXT!"""

    # ------------------------------------------------------------------------
    # Entry Parent Retrieval API

    def get_parent_entry(tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT!"""

    def get_parent_entry_id(tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT!"""

    def get_parent_entry_item(tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT!"""

    # ------------------------------------------------------------------------
    # Entry Sibling Retrieval API

    def count_sibling_entries(tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT!"""

    def has_sibling_entries(tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT!"""

    def sibling_entry_ids(tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT!"""

    def sibling_entry_items(tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT!"""

    def sibling_entry_values(tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT!"""

    # ------------------------------------------------------------------------
    # Entry Child Retrieval API

    def count_children_entries(tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT!"""

    def has_children_entries(tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT!"""

    def children_entry_ids(tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT!"""

    def children_entry_items(tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT!"""

    def children_entry_values(tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT!"""

    # ------------------------------------------------------------------------
    # Entry Descendant Retrieval API

    def count_descendant_entries(tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None, max_levels=None):
        """!TXT!"""

    def descendant_entry_ids(tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None, max_levels=None):
        """!TXT!"""

    def descendant_entry_items(tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None, max_levels=None):
        """!TXT!"""

    def descendant_entry_values(tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None, max_levels=None):
        """!TXT!"""

    # ------------------------------------------------------------------------
    # Entry Tree Mutation API

    def move_entry_branch(tree_field_id=None, destination_entry_id=None, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT!"""

    def move_entry_branches(tree_field_id=None, destination_entry_id=None, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None):
        """!TXT!"""

    def flatten_entry_branch(tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None, max_levels=None):
        """!TXT!"""

    def flatten_entry_branches(tree_field_id=None, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None, max_levels=None):
        """!TXT!"""

    def crop_entry_branch(tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT!"""

    def crop_entry_branches(tree_field_id=None, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None):
        """!TXT!"""

    # ------------------------------------------------------------------------
    # Entry Stats Retrieval

    def stat_entry(entry_id):
        """!TXT!"""

    def stat_entries(entry_ids=None, conditions=None):
        """!TXT!"""

    def get_entry_stat_size(entry_id):
        """!TXT!"""

    def get_entry_stat_ctime(entry_id):
        """!TXT!"""

    def get_entry_stat_cuser(entry_id):
        """!TXT!"""

    def get_entry_stat_mtime(entry_id):
        """!TXT!"""

    def get_entry_stat_muser(entry_id):
        """!TXT!"""

    def get_entry_stat_atime(entry_id):
        """!TXT!"""

    def get_entry_stat_auser(entry_id):
        """!TXT!"""

    # ------------------------------------------------------------------------
    # Entry Stats Retrieval

    def touch_entry(entry_id):
        """!TXT!"""

    def touch_entries(entry_ids=None, conditions=None):
        """!TXT!"""

    def access_entry(entry_id):
        """!TXT!"""

    def access_entries(entry_ids=None, conditions=None):
        """!TXT!"""

# !!! interfaces/entrycontainer.py - review api
