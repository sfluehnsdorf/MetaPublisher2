"""MetaPublisher2 - Entry Container Base."""


from Products.MetaPublisher2.interfaces import IEntryContainer
from Products.MetaPublisher2.library.common import (
    ClassSecurityInfo, implements, InitializeClass, true, false)


# ============================================================================
# Module Exports

__all__ = [
    'EntryContainer',
]


# ============================================================================
# Entry Container Base Class

class EntryContainer:
    """Entry Container Base Class."""

    security = ClassSecurityInfo()

    implements(IEntryContainer)

    # ------------------------------------------------------------------------
    # Entry Data Processing Helpers

    def extract_entry_data(self, mapping, failsafe=true):
        """TODO: Docstring for extract_entry_data."""
        raise NotImplementedError

    def extract_entryfield_data(self, field_id, mapping, failsafe=true):
        """TODO: Docstring for extract_entryfield_data."""
        raise NotImplementedError

    # ------------------------------------------------------------------------
    # Single Entry Retrieval API

    def get_entry(
        self, parent_entry_id=None, entry_id=None, entry_position=None,
        field_ids=None, failsafe=false, bound=true
    ):
        """TODO: Docstring for get_entry."""
        raise NotImplementedError

    # ------------------------------------------------------------------------
    # Multiple Entry Retrieval API

    def entry_ids(
        self, parent_entry_id=None, entry_ids=None, entry_positions=None,
        conditions=None, order_by=None, offset=None, limit=None, bound=None
    ):
        """TODO: Docstring for entry_ids."""
        raise NotImplementedError

    def entry_items(
        self, parent_entry_id=None, entry_ids=None, entry_positions=None,
        conditions=None, field_ids=None, order_by=None, offset=None,
        limit=None, bound=None
    ):
        """TODO: Docstring for entry_items."""
        raise NotImplementedError

    def entry_values(
        self, parent_entry_id=None, entry_ids=None, entry_positions=None,
        conditions=None, field_ids=None, order_by=None, offset=None,
        limit=None, bound=None
    ):
        """TODO: Docstring for entry_values."""
        raise NotImplementedError

    # --------------------------------------------------------------------------
    # Entry Statistics Retrieval API

    def count_entries(
        self, parent_entry_id=None, entry_ids=None, entry_positions=None,
        conditions=None
    ):
        """TODO: Docstring for count_entries."""
        raise NotImplementedError

    # --------------------------------------------------------------------------
    # Entry Existence Retrieval API

    def has_all_entries(
        self, parent_entry_id=None, entry_ids=None, entry_positions=None,
        conditions=None
    ):
        """TODO: Docstring for has_all_entries."""
        raise NotImplementedError

    def has_any_entries(
        self, parent_entry_id=None, entry_ids=None, entry_positions=None,
        conditions=None
    ):
        """TODO: Docstring for has_any_entries."""
        raise NotImplementedError

    def has_entry(
        self, parent_entry_id=None, entry_id=None, entry_position=None
    ):
        """TODO: Docstring for has_entry."""
        raise NotImplementedError

    # ------------------------------------------------------------------------
    # Entry Creation Mutation API

    def add_entry(
        self, parent_entry_id=None, entry_id=None, entry_position=None,
        data={}, **args
    ):
        """TODO: Docstring for add_entry."""
        raise NotImplementedError

    def add_entry_to_top(
        self, parent_entry_id=None, entry_id=None, data={}, **args
    ):
        """TODO: Docstring for add_entry_to_top."""
        raise NotImplementedError

    def add_entry_to_bottom(
        self, parent_entry_id=None, entry_id=None, data={}, **args
    ):
        """TODO: Docstring for add_entry_to_bottom."""
        raise NotImplementedError

    def add_entry_somewhere(
        self, parent_entry_id=None, entry_id=None, data={}, **args
    ):
        """TODO: Docstring for add_entry_somewhere."""
        raise NotImplementedError

    def add_entries(self, entries, parent_entry_id=None):
        """TODO: Docstring for add_entries."""
        raise NotImplementedError

    def add_entries_to_top(self, entries, parent_entry_id=None):
        """TODO: Docstring for add_entries_to_top."""
        raise NotImplementedError

    def add_entries_to_bottom(self, entries, parent_entry_id=None):
        """TODO: Docstring for add_entries_to_bottom."""
        raise NotImplementedError

    def add_entries_somewhere(self, entries, parent_entry_id=None):
        """TODO: Docstring for add_entries_somewhere."""
        raise NotImplementedError

    def duplicate_entry(
        self, parent_entry_id=None, entry_id=None, entry_position=None,
        new_id=None
    ):
        """TODO: Docstring for duplicate_entry."""
        raise NotImplementedError

    def duplicate_entries(
        self, parent_entry_id=None, entry_ids=[], entry_positions=[],
        conditions=None, new_ids=None
    ):
        """TODO: Docstring for duplicate_entries."""
        raise NotImplementedError

    def set_entry(
        self, parent_entry_id=None, entry_id=None, entry_position=None,
        data={}, **args
    ):
        """TODO: Docstring for set_entry."""
        raise NotImplementedError

    # ------------------------------------------------------------------------
    # Entry Modification Mutation API

    def edit_entry(
        self, parent_entry_id=None, entry_id=None, entry_position=None,
        data={}, **args
    ):
        """TODO: Docstring for edit_entry."""
        raise NotImplementedError

    def edit_entries(
        self, parent_entry_id=None, entry_ids=[], entry_positions=[],
        conditions=None, data={}, **args
    ):
        """TODO: Docstring for edit_entries."""
        raise NotImplementedError

    def rename_entry(
        self, parent_entry_id=None, entry_id=None, entry_position=None,
        new_id=None
    ):
        """TODO: Docstring for rename_entry."""
        raise NotImplementedError

    def rename_entries(
        self, parent_entry_id=None, entry_ids=[], entry_positions=[],
        conditions=None, new_ids=None
    ):
        """TODO: Docstring for rename_entries."""
        raise NotImplementedError

    def reset_entry(
        self, parent_entry_id=None, entry_id=None, entry_position=None,
        field_ids=None
    ):
        """TODO: Docstring for reset_entry."""
        raise NotImplementedError

    def reset_entries(
        self, parent_entry_id=None, entry_ids=[], entry_positions=[],
        conditions=None, field_ids=None
    ):
        """TODO: Docstring for reset_entries."""
        raise NotImplementedError

    # ------------------------------------------------------------------------
    # Entry Deletion Mutation API

    def clear_entries(self):
        """TODO: Docstring for clear_entries."""
        raise NotImplementedError

    def delete_entry(
        self, parent_entry_id=None, entry_id=None, entry_position=None,
        failsafe=false
    ):
        """TODO: Docstring for delete_entry."""
        raise NotImplementedError

    def delete_entries(
        self, parent_entry_id=None, entry_ids=[], entry_positions=[],
        conditions=None, failsafe=false
    ):
        """TODO: Docstring for delete_entries."""
        raise NotImplementedError

    def pop_first_entry(self, parent_entry_id=None, conditions=None):
        """TODO: Docstring for pop_first_entry."""
        raise NotImplementedError

    def pop_last_entry(self, parent_entry_id=None, conditions=None):
        """TODO: Docstring for pop_last_entry."""
        raise NotImplementedError

    def pop_random_entry(self, parent_entry_id=None, conditions=None):
        """TODO: Docstring for pop_random_entry."""
        raise NotImplementedError

    # ------------------------------------------------------------------------
    # EntryField Retrieval API

    def get_entryfield(
        self, field_id, default=None, parent_entry_id=None, entry_id=None,
        entry_position=None
    ):
        """TODO: Docstring for get_entryfield."""
        raise NotImplementedError

    def count_entryfields(
        self, field_id, value, parent_entry_id=None, entry_ids=None,
        entry_positions=None, conditions=None
    ):
        """TODO: Docstring for count_entryfields."""
        raise NotImplementedError

    def count_unique_entryfields(
        self, field_id, parent_entry_id=None, entry_ids=None,
        entry_positions=None, conditions=None
    ):
        """TODO: Docstring for count_unique_entryfields."""
        raise NotImplementedError

    def has_any_entryfields(
        self, field_id, value, parent_entry_id=None, entry_ids=None,
        entry_positions=None, conditions=None
    ):
        """TODO: Docstring for has_any_entryfields."""
        raise NotImplementedError

    def has_all_entryfields(
        self, field_id, value, parent_entry_id=None, entry_ids=None,
        entry_positions=None, conditions=None
    ):
        """TODO: Docstring for has_all_entryfields."""
        raise NotImplementedError

    def has_entryfield(self, field_id, entry_id):
        """TODO: Docstring for has_entryfield."""
        raise NotImplementedError

    def get_unique_entryfields(
        self, field_id, parent_entry_id=None, entry_ids=None,
        entry_positions=None, conditions=None
    ):
        """TODO: Docstring for get_unique_entryfields."""
        raise NotImplementedError

    # ------------------------------------------------------------------------
    # EntryField Mutation API

    def reset_entryfield(
        self, field_id, parent_entry_id=None, entry_id=None,
        entry_position=None
    ):
        """TODO: Docstring for reset_entryfield."""
        raise NotImplementedError

    def reset_entryfields(
        self, field_id, parent_entry_id=None, entry_ids=None,
        entry_positions=None, conditions=None
    ):
        """TODO: Docstring for reset_entryfields."""
        raise NotImplementedError

    def set_entryfield(
        self, field_id, value, parent_entry_id=None, entry_id=None,
        entry_position=None
    ):
        """TODO: Docstring for set_entryfield."""
        raise NotImplementedError

    def set_entryfields(
        self, field_id, value, parent_entry_id=None, entry_ids=None,
        entry_positions=None, conditions=None
    ):
        """TODO: Docstring for set_entryfields."""
        raise NotImplementedError

    # ------------------------------------------------------------------------
    # EntrySet Creation API

    def get_entryset(
        self, field_ids=None, parent_entry_id=None, entry_ids=None,
        entry_positions=None, conditions=None, order_by=None, offset=None,
        limit=None, bound=true, lazy=true, live=false
    ):
        """TODO: Docstring for get_entryset."""
        raise NotImplementedError

    def join_entries(
        self, right_source, join_type='inner', join_conditions=None,
        field_ids=None, parent_entry_id=None, entry_ids=None,
        entry_positions=None, conditions=None, order_by=None, offset=None,
        limit=None, left_field_ids=None, left_parent_entry_id=None,
        left_entry_ids=[], left_entry_positions=[], left_conditions=None,
        left_order_by=None, left_offset=None, left_limit=None,
        right_field_ids=None, right_parent_entry_id=None, right_entry_ids=[],
        right_entry_positions=[], right_conditions=None, right_order_by=None,
        right_offset=None, right_limit=None, bound=true, lazy=true, live=True
    ):
        """TODO: Docstring for join_entries."""
        raise NotImplementedError

    # !!! bases/entrycontainer/entrycontainer.py - review/revise API for
    # select_entries
    def select_entries(
        self, fields=None, joins=None, conditions=None, order_by=None,
        offset=None, limit=None, bound=true, live=True
    ):
        """TODO: Docstring for select_entries."""
        raise NotImplementedError

    # ------------------------------------------------------------------------
    # EntrySet Retrieval API

    def is_entryset(self):
        """TODO: Docstring for is_entryset."""
        raise NotImplementedError

    def is_entryset_live(self):
        """TODO: Docstring for is_entryset_live."""
        raise NotImplementedError

    def is_entryset_lazy(self):
        """TODO: Docstring for is_entryset_lazy."""
        raise NotImplementedError

    def is_entryset_bound(self):
        """TODO: Docstring for is_entryset_bound."""
        raise NotImplementedError

    def is_source_storage(self):
        """TODO: Docstring for is_source_storage."""
        raise NotImplementedError

    def get_source_storages(self):
        """TODO: Docstring for get_source_storages."""
        raise NotImplementedError

    # ------------------------------------------------------------------------
    # EntrySet Mutation API

    def commit_entryset(self):
        """TODO: Docstring for commit_entryset."""
        raise NotImplementedError

    def reload_entryset(self):
        """TODO: Docstring for reload_entryset."""
        raise NotImplementedError

    def refresh_entryset(
        self, field_ids, entry_ids=None, entry_positions=None, conditions=None
    ):
        """TODO: Docstring for )."""
        raise NotImplementedError

    # ------------------------------------------------------------------------
    # Set Theory Retrieval API

    def is_member(
        self, entry, fields=None, parent_entry_id=None, entry_ids=None,
        entry_positions=None, conditions=None
    ):
        """TODO: Docstring for is_member."""
        raise NotImplementedError

    def is_disjoint(
        self, other_source, field_ids=None, parent_entry_id=None,
        entry_ids=None, entry_positions=None, conditions=None,
        other_field_ids=None, other_parent_entry_id=None, other_entry_ids=None,
        other_entry_positions=None, other_conditions=None
    ):
        """TODO: Docstring for is_disjoint."""
        raise NotImplementedError

    def is_subset(
        self, other_source, field_ids=None, parent_entry_id=None,
        entry_ids=None, entry_positions=None, conditions=None,
        other_field_ids=None, other_parent_entry_id=None, other_entry_ids=None,
        other_entry_positions=None, other_conditions=None
    ):
        """TODO: Docstring for is_subset."""
        raise NotImplementedError

    def is_true_subset(
        self, other_source, field_ids=None, parent_entry_id=None,
        entry_ids=None, entry_positions=None, conditions=None,
        other_field_ids=None, other_parent_entry_id=None, other_entry_ids=[],
        other_entry_positions=[], other_conditions=None
    ):
        """TODO: Docstring for is_true_subset."""
        raise NotImplementedError

    def is_superset(
        self, other_source, field_ids=None, parent_entry_id=None,
        entry_ids=None, entry_positions=None, conditions=None,
        other_field_ids=None, other_parent_entry_id=None, other_entry_ids=[],
        other_entry_positions=[], other_conditions=None
    ):
        """TODO: Docstring for is_superset."""
        raise NotImplementedError

    def is_true_superset(
        self, other_source, field_ids=None, parent_entry_id=None,
        entry_ids=None, entry_positions=None, conditions=None,
        other_field_ids=None, other_parent_entry_id=None, other_entry_ids=[],
        other_entry_positions=[], other_conditions=None
    ):
        """TODO: Docstring for is_true_superset."""
        raise NotImplementedError

    # ------------------------------------------------------------------------
    # Set Theory Mutation API

    def intersection(
        self, other_source, field_ids=None, parent_entry_id=None,
        entry_ids=None, entry_positions=None, conditions=None,
        other_field_ids=None, other_parent_entry_id=None, other_entry_ids=[],
        other_entry_positions=[], other_conditions=None
    ):
        """TODO: Docstring for intersection."""
        raise NotImplementedError

    def difference(
        self, other_source, field_ids=None, parent_entry_id=None,
        entry_ids=None, entry_positions=None, conditions=None,
        other_field_ids=None, other_parent_entry_id=None, other_entry_ids=[],
        other_entry_positions=[], other_conditions=None
    ):
        """TODO: Docstring for difference."""
        raise NotImplementedError

    def symmetric_difference(
        self, other_source, field_ids=None, parent_entry_id=None,
        entry_ids=None, entry_positions=None, conditions=None,
        other_field_ids=None, other_parent_entry_id=None, other_entry_ids=[],
        other_entry_positions=[], other_conditions=None
    ):
        """TODO: Docstring for symmetric_difference."""
        raise NotImplementedError

    def union(
        self, other_source, field_ids=None, parent_entry_id=None,
        entry_ids=None, entry_positions=None, conditions=None,
        other_field_ids=None, other_parent_entry_id=None, other_entry_ids=[],
        other_entry_positions=[], other_conditions=None
    ):
        """TODO: Docstring for union."""
        raise NotImplementedError

    # ------------------------------------------------------------------------
    # Entry Order Retrieval API

    def get_entry_position(self, entry_id, parent_entry_id=None):
        """TODO: Docstring for get_entry_position."""
        raise NotImplementedError

    def get_entry_positions(
        self, parent_entry_id=None, entry_ids=None, conditions=None,
        order_by=None, offset=None, limit=None
    ):
        """TODO: Docstring for get_entry_positions."""
        raise NotImplementedError

    # ------------------------------------------------------------------------
    # Entry Order Mutation API

    def rotate_entries(
        self, steps, parent_entry_id=None, entry_ids=None,
        entry_positions=None, conditions=None
    ):
        """TODO: Docstring for rotate_entries."""
        raise NotImplementedError

    def order_entries(
        self, order_by, parent_entry_id=None, entry_ids=None,
        entry_positions=None, conditions=None
    ):
        """TODO: Docstring for order_entries."""
        raise NotImplementedError

    def shuffle_entries(
        self, parent_entry_id=None, entry_ids=None, entry_positions=None,
        conditions=None
    ):
        """TODO: Docstring for shuffle_entries."""
        raise NotImplementedError

    def reverse_entries(
        self, parent_entry_id=None, entry_ids=None, entry_positions=None,
        conditions=None
    ):
        """TODO: Docstring for reverse_entries."""
        raise NotImplementedError

    def move_entry(
        self, position, parent_entry_id=None, entry_id=None,
        entry_position=None
    ):
        """TODO: Docstring for move_entry."""
        raise NotImplementedError

    def move_entry_to_top(
        self, parent_entry_id=None, entry_id=None, entry_position=None
    ):
        """TODO: Docstring for move_entry_to_top."""
        raise NotImplementedError

    def move_entry_up(
        self, parent_entry_id=None, entry_id=None, entry_position=None
    ):
        """TODO: Docstring for move_entry_up."""
        raise NotImplementedError

    def move_entry_down(
        self, parent_entry_id=None, entry_id=None, entry_position=None
    ):
        """TODO: Docstring for move_entry_down."""
        raise NotImplementedError

    def move_entry_to_bottom(
        self, parent_entry_id=None, entry_id=None, entry_position=None
    ):
        """TODO: Docstring for move_entry_to_bottom."""
        raise NotImplementedError

    def move_entries(
        self, position, parent_entry_id=None, entry_ids=None,
        entry_positions=None, conditions=None
    ):
        """TODO: Docstring for move_entries."""
        raise NotImplementedError

    def move_entries_to_top(
        self, parent_entry_id=None, entry_ids=None, entry_positions=None,
        conditions=None
    ):
        """TODO: Docstring for )."""
        raise NotImplementedError

    def move_entries_up(
        self, parent_entry_id=None, entry_ids=None, entry_positions=None,
        conditions=None
    ):
        """TODO: Docstring for )."""
        raise NotImplementedError

    def move_entries_down(
        self, parent_entry_id=None, entry_ids=None, entry_positions=None,
        conditions=None
    ):
        """TODO: Docstring for )."""
        raise NotImplementedError

    def move_entries_to_bottom(
        self, parent_entry_id=None, entry_ids=None, entry_positions=None,
        conditions=None
    ):
        """TODO: Docstring for )."""
        raise NotImplementedError

    # ------------------------------------------------------------------------
    # Single Root Entry Retrieval API

    def is_root_entry(
        self, tree_field_id=None, parent_entry_id=None, entry_id=None,
        entry_position=None
    ):
        """TODO: Docstring for )."""
        raise NotImplementedError

    def root_entry_id(self):
        """TODO: Docstring for root_entry_id."""
        raise NotImplementedError

    def root_entry_item(self):
        """TODO: Docstring for root_entry_item."""
        raise NotImplementedError

    def root_entry_value(self):
        """TODO: Docstring for root_entry_value."""
        raise NotImplementedError

    # ------------------------------------------------------------------------
    # Multiple Root Entry Retrieval API

    def is_top_entry(
        self, tree_field_id=None, parent_entry_id=None, entry_id=None,
        entry_position=None
    ):
        """TODO: Docstring for )."""
        raise NotImplementedError

    def top_entry_ids(self):
        """TODO: Docstring for top_entry_ids."""
        raise NotImplementedError

    def top_entry_items(self):
        """TODO: Docstring for top_entry_items."""
        raise NotImplementedError

    def top_entry_values(self):
        """TODO: Docstring for top_entry_values."""
        raise NotImplementedError

    # ------------------------------------------------------------------------
    # Node Type Retrieval API

    def is_entry_branch(
        self, tree_field_id=None, parent_entry_id=None, entry_id=None,
        entry_position=None
    ):
        """TODO: Docstring for )."""
        raise NotImplementedError

    def is_entry_leaf(
        self, tree_field_id=None, parent_entry_id=None, entry_id=None,
        entry_position=None
    ):
        """TODO: Docstring for )."""
        raise NotImplementedError

    def are_entries_branches(
        self, tree_field_id=None, parent_entry_id=None, entry_ids=None,
        entry_positions=None, conditions=None
    ):
        """TODO: Docstring for )."""
        raise NotImplementedError

    def are_entries_leaves(
        self, tree_field_id=None, parent_entry_id=None, entry_ids=None,
        entry_positions=None, conditions=None
    ):
        """TODO: Docstring for )."""
        raise NotImplementedError

    def entry_branch_ids(
        self, tree_field_id=None, parent_entry_id=None, entry_id=None,
        entry_position=None, conditions=None, max_levels=None
    ):
        """TODO: Docstring for )."""
        raise NotImplementedError

    def entry_branch_items(
        self, tree_field_id=None, parent_entry_id=None, entry_id=None,
        entry_position=None, conditions=None, max_levels=None
    ):
        """TODO: Docstring for )."""
        raise NotImplementedError

    def entry_branch_values(
        self, tree_field_id=None, parent_entry_id=None, entry_id=None,
        entry_position=None, conditions=None, max_levels=None
    ):
        """TODO: Docstring for )."""
        raise NotImplementedError

    def entry_leaf_id(
        self, tree_field_id=None, parent_entry_id=None, entry_id=None,
        entry_position=None, conditions=None, max_levels=None
    ):
        """TODO: Docstring for )."""
        raise NotImplementedError

    def entry_leaf_items(
        self, tree_field_id=None, parent_entry_id=None, entry_id=None,
        entry_position=None, max_levels=None
    ):
        """TODO: Docstring for )."""
        raise NotImplementedError

    def entry_leaf_values(
        self, tree_field_id=None, parent_entry_id=None, entry_id=None,
        entry_position=None, max_levels=None
    ):
        """TODO: Docstring for )."""
        raise NotImplementedError

    # ------------------------------------------------------------------------
    # Entry Relationship Retrieval API

    def is_ancestor(
        self, tree_field_id=None, parent_entry_id=None, entry_id=None,
        entry_position=None, other_parent_entry_id=None, other_entry_id=None,
        other_entry_position=None, of_level=None, max_levels=None
    ):
        """TODO: Docstring for )."""
        raise NotImplementedError

    def is_parent(
        self, tree_field_id=None, parent_entry_id=None, entry_id=None,
        entry_position=None, other_parent_entry_id=None, other_entry_id=None,
        other_entry_position=None
    ):
        """TODO: Docstring for )."""
        raise NotImplementedError

    def is_sibling(
        self, tree_field_id=None, parent_entry_id=None, entry_id=None,
        entry_position=None, other_parent_entry_id=None, other_entry_id=None,
        other_entry_position=None
    ):
        """TODO: Docstring for )."""
        raise NotImplementedError

    def is_child(
        self, tree_field_id=None, parent_entry_id=None, entry_id=None,
        entry_position=None, other_parent_entry_id=None, other_entry_id=None,
        other_entry_position=None
    ):
        """TODO: Docstring for )."""
        raise NotImplementedError

    def is_descendant(
        self, tree_field_id=None, parent_entry_id=None, entry_id=None,
        entry_position=None, other_parent_entry_id=None, other_entry_id=None,
        other_entry_position=None, of_level=None, max_levels=None
    ):
        """TODO: Docstring for )."""
        raise NotImplementedError

    # ------------------------------------------------------------------------
    # Entry Ancestor Retrieval API

    def count_ancestor_entries(
        self, tree_field_id=None, parent_entry_id=None, entry_id=None,
        entry_position=None, max_levels=None, include_ancestor_siblings=false
    ):
        """TODO: Docstring for )."""
        raise NotImplementedError

    def ancestor_entry_ids(
        self, tree_field_id=None, parent_entry_id=None, entry_id=None,
        entry_position=None, max_levels=None, include_ancestor_siblings=false
    ):
        """TODO: Docstring for )."""
        raise NotImplementedError

    def ancestor_entry_items(
        self, tree_field_id=None, parent_entry_id=None, entry_id=None,
        entry_position=None, max_levels=None, include_ancestor_siblings=false
    ):
        """TODO: Docstring for )."""
        raise NotImplementedError

    def ancestor_entry_values(
        self, tree_field_id=None, parent_entry_id=None, entry_id=None,
        entry_position=None, max_levels=None, include_ancestor_siblings=false
    ):
        """TODO: Docstring for )."""
        raise NotImplementedError

    # ------------------------------------------------------------------------
    # Entry Parent Retrieval API

    def get_parent_entry(
        self, tree_field_id=None, parent_entry_id=None, entry_id=None,
        entry_position=None
    ):
        """TODO: Docstring for )."""
        raise NotImplementedError

    def get_parent_entry_id(
        self, tree_field_id=None, parent_entry_id=None, entry_id=None,
        entry_position=None
    ):
        """TODO: Docstring for )."""
        raise NotImplementedError

    def get_parent_entry_item(
        self, tree_field_id=None, parent_entry_id=None, entry_id=None,
        entry_position=None
    ):
        """TODO: Docstring for )."""
        raise NotImplementedError

    # ------------------------------------------------------------------------
    # Entry Sibling Retrieval API

    def count_sibling_entries(
        self, tree_field_id=None, parent_entry_id=None, entry_id=None,
        entry_position=None
    ):
        """TODO: Docstring for )."""
        raise NotImplementedError

    def has_sibling_entries(
        self, tree_field_id=None, parent_entry_id=None, entry_id=None,
        entry_position=None
    ):
        """TODO: Docstring for )."""
        raise NotImplementedError

    def sibling_entry_ids(
        self, tree_field_id=None, parent_entry_id=None, entry_id=None,
        entry_position=None
    ):
        """TODO: Docstring for )."""
        raise NotImplementedError

    def sibling_entry_items(
        self, tree_field_id=None, parent_entry_id=None, entry_id=None,
        entry_position=None
    ):
        """TODO: Docstring for )."""
        raise NotImplementedError

    def sibling_entry_values(
        self, tree_field_id=None, parent_entry_id=None, entry_id=None,
        entry_position=None
    ):
        """TODO: Docstring for )."""
        raise NotImplementedError

    # ------------------------------------------------------------------------
    # Entry Child Retrieval API

    def count_children_entries(
        self, tree_field_id=None, parent_entry_id=None, entry_id=None,
        entry_position=None
    ):
        """TODO: Docstring for )."""
        raise NotImplementedError

    def has_children_entries(
        self, tree_field_id=None, parent_entry_id=None, entry_id=None,
        entry_position=None
    ):
        """TODO: Docstring for )."""
        raise NotImplementedError

    def children_entry_ids(
        self, tree_field_id=None, parent_entry_id=None, entry_id=None,
        entry_position=None
    ):
        """TODO: Docstring for )."""
        raise NotImplementedError

    def children_entry_items(
        self, tree_field_id=None, parent_entry_id=None, entry_id=None,
        entry_position=None
    ):
        """TODO: Docstring for )."""
        raise NotImplementedError

    def children_entry_values(
        self, tree_field_id=None, parent_entry_id=None, entry_id=None,
        entry_position=None
    ):
        """TODO: Docstring for )."""
        raise NotImplementedError

    # ------------------------------------------------------------------------
    # Entry Descendant Retrieval API

    def count_descendant_entries(
        self, tree_field_id=None, parent_entry_id=None, entry_id=None,
        entry_position=None, max_levels=None
    ):
        """TODO: Docstring for )."""
        raise NotImplementedError

    def descendant_entry_ids(
        self, tree_field_id=None, parent_entry_id=None, entry_id=None,
        entry_position=None, max_levels=None
    ):
        """TODO: Docstring for )."""
        raise NotImplementedError

    def descendant_entry_items(
        self, tree_field_id=None, parent_entry_id=None, entry_id=None,
        entry_position=None, max_levels=None
    ):
        """TODO: Docstring for )."""
        raise NotImplementedError

    def descendant_entry_values(
        self, tree_field_id=None, parent_entry_id=None, entry_id=None,
        entry_position=None, max_levels=None
    ):
        """TODO: Docstring for )."""
        raise NotImplementedError

    # ------------------------------------------------------------------------
    # Entry Tree Mutation API

    def move_entry_branch(
        self, tree_field_id=None, destination_entry_id=None,
        parent_entry_id=None, entry_id=None, entry_position=None
    ):
        """TODO: Docstring for )."""
        raise NotImplementedError

    def move_entry_branches(
        self, tree_field_id=None, destination_entry_id=None,
        parent_entry_id=None, entry_ids=None, entry_positions=None,
        conditions=None
    ):
        """TODO: Docstring for )."""
        raise NotImplementedError

    def flatten_entry_branch(
        self, tree_field_id=None, parent_entry_id=None, entry_id=None,
        entry_position=None, max_levels=None
    ):
        """TODO: Docstring for )."""
        raise NotImplementedError

    def flatten_entry_branches(
        self, tree_field_id=None, parent_entry_id=None, entry_ids=None,
        entry_positions=None, conditions=None, max_levels=None
    ):
        """TODO: Docstring for )."""
        raise NotImplementedError

    def crop_entry_branch(
        self, tree_field_id=None, parent_entry_id=None, entry_id=None,
        entry_position=None
    ):
        """TODO: Docstring for )."""
        raise NotImplementedError

    def crop_entry_branches(
        self, tree_field_id=None, parent_entry_id=None, entry_ids=None,
        entry_positions=None, conditions=None
    ):
        """TODO: Docstring for )."""
        raise NotImplementedError

    # ------------------------------------------------------------------------
    # Entry Stats Retrieval

    def stat_entry(self, entry_id):
        """TODO: Docstring for stat_entry."""
        raise NotImplementedError

    def stat_entries(self, entry_ids=None, conditions=None):
        """TODO: Docstring for stat_entries."""
        raise NotImplementedError

    def get_entry_stat_size(self, entry_id):
        """TODO: Docstring for get_entry_stat_size."""
        raise NotImplementedError

    def get_entry_stat_ctime(self, entry_id):
        """TODO: Docstring for get_entry_stat_ctime."""
        raise NotImplementedError

    def get_entry_stat_cuser(self, entry_id):
        """TODO: Docstring for get_entry_stat_cuser."""
        raise NotImplementedError

    def get_entry_stat_mtime(self, entry_id):
        """TODO: Docstring for get_entry_stat_mtime."""
        raise NotImplementedError

    def get_entry_stat_muser(self, entry_id):
        """TODO: Docstring for get_entry_stat_muser."""
        raise NotImplementedError

    def get_entry_stat_atime(self, entry_id):
        """TODO: Docstring for get_entry_stat_atime."""
        raise NotImplementedError

    def get_entry_stat_auser(self, entry_id):
        """TODO: Docstring for get_entry_stat_auser."""
        raise NotImplementedError

    # ------------------------------------------------------------------------
    # Entry Stats Retrieval

    def touch_entry(self, entry_id):
        """TODO: Docstring for touch_entry."""
        raise NotImplementedError

    def touch_entries(self, entry_ids=None, conditions=None):
        """TODO: Docstring for touch_entries."""
        raise NotImplementedError

    def access_entry(self, entry_id):
        """TODO: Docstring for access_entry."""
        raise NotImplementedError

    def access_entries(self, entry_ids=None, conditions=None):
        """TODO: Docstring for access_entries."""
        raise NotImplementedError


# ----------------------------------------------------------------------------
# initialize class security

InitializeClass(EntryContainer)

# !!! bases/entrycontainer/entrycontainer.py - review api
# !!! bases/entrycontainer/entrycontainer.py - implement backdrop/failsafe code
