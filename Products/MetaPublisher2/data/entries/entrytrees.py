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

__doc__ = """Entry Trees Component

!TXT! module info

$Id: data/entries/entrytrees.py 10 2013-05-08 21:41:53Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.library import ClassSecurityInfo, InitializeClass, permission_access_entries, permission_change_entries, false


# ============================================================================
# Module Exports

__all__ = [
    'EntryTrees',
]


# ============================================================================
# Entry Trees Component Mix-In Class

class EntryTrees:
    """!TXT! Entry Trees Component Mix-In Class"""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # Single Root Entry Retrieval API

    security.declareProtected(permission_access_entries, 'is_root_entry')

    def is_root_entry(self, source, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT! is_root_entry"""

        source = self.get_storage(source)
        return source.is_root_entry(tree_field_id, parent_entry_id, entry_id, entry_position)

    security.declareProtected(permission_access_entries, 'root_entry_id')

    def root_entry_id(self, source, tree_field_id=None):
        """!TXT! root_entry_id"""

        source = self.get_storage(source)
        return source.root_entry_id(tree_field_id)

    security.declareProtected(permission_access_entries, 'root_entry_item')

    def root_entry_item(self, source, tree_field_id=None):
        """!TXT! root_entry_item"""

        source = self.get_storage(source)
        return source.root_entry_item(tree_field_id)

    security.declareProtected(permission_access_entries, 'root_entry_value')

    def root_entry_value(self, source, tree_field_id=None):
        """!TXT! root_entry_value"""

        source = self.get_storage(source)
        return source.root_entry_value(tree_field_id)

    # ------------------------------------------------------------------------
    # Multiple Root Entry Retrieval API

    security.declareProtected(permission_access_entries, 'is_top_entry')

    def is_top_entry(self, source, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT! is_top_entry"""

        source = self.get_storage(source)
        return source.is_top_entry(tree_field_id, parent_entry_id, entry_id, entry_position)

    security.declareProtected(permission_access_entries, 'top_entry_ids')

    def top_entry_ids(self, source, tree_field_id=None):
        """!TXT! top_entry_ids"""

        source = self.get_storage(source)
        return source.top_entry_ids(tree_field_id)

    security.declareProtected(permission_access_entries, 'top_entry_items')

    def top_entry_items(self, source, tree_field_id=None):
        """!TXT! top_entry_items"""

        source = self.get_storage(source)
        return source.top_entry_items(tree_field_id)

    security.declareProtected(permission_access_entries, 'top_entry_values')

    def top_entry_values(self, source, tree_field_id=None):
        """!TXT! get_root_entry_values"""

        source = self.get_storage(source)
        return source.top_entry_values(tree_field_id)

    # ------------------------------------------------------------------------
    # Node Type Retrieval API

    security.declareProtected(permission_access_entries, 'is_entry_branch')

    def is_entry_branch(self, source, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT! is_entry_branch"""

        source = self.get_storage(source)
        return source.is_entry_branch(tree_field_id, parent_entry_id, entry_id, entry_position)

    security.declareProtected(permission_access_entries, 'is_entry_leaf')

    def is_entry_leaf(self, source, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT! is_entry_leaf"""

        source = self.get_storage(source)
        return source.is_entry_leaf(tree_field_id, parent_entry_id, entry_id, entry_position)

    security.declareProtected(permission_access_entries, 'are_entries_branches')

    def are_entries_branches(self, source, tree_field_id=None, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None):
        """!TXT! are_entries_branches"""

        source = self.get_storage(source)
        return source.are_entries_branches(tree_field_id, parent_entry_id, entry_ids, entry_positions, conditions)

    security.declareProtected(permission_access_entries, 'are_entries_leaves')

    def are_entries_leaves(self, source, tree_field_id=None, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None):
        """!TXT! are_entries_leaves"""

        source = self.get_storage(source)
        return source.are_entries_leaves(tree_field_id, parent_entry_id, entry_ids, entry_positions, conditions)

    security.declareProtected(permission_access_entries, 'entry_branch_ids')

    def entry_branch_ids(self, source, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None, conditions=None, max_levels=None):
        """!TXT! entry_branch_ids"""

        source = self.get_storage(source)
        return source.entry_branch_ids(tree_field_id, parent_entry_id, entry_id, entry_position, conditions, max_levels)

    security.declareProtected(permission_access_entries, 'entry_branch_items')

    def entry_branch_items(self, source, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None, conditions=None, max_levels=None):
        """!TXT! entry_branch_items"""

        source = self.get_storage(source)
        return source.entry_branch_items(tree_field_id, parent_entry_id, entry_id, entry_position, conditions, max_levels)

    security.declareProtected(permission_access_entries, 'entry_branch_values')

    def entry_branch_values(self, source, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None, conditions=None, max_levels=None):
        """!TXT! entry_branch_values"""

        source = self.get_storage(source)
        return source.entry_branch_values(tree_field_id, parent_entry_id, entry_id, entry_position, conditions, max_levels)

    security.declareProtected(permission_access_entries, 'entry_leaf_ids')

    def entry_leaf_ids(self, source, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None, conditions=None, max_levels=None):
        """!TXT! entry_leaf_ids"""

        source = self.get_storage(source)
        return source.entry_leaf_ids(tree_field_id, parent_entry_id, entry_id, entry_position, conditions, max_levels)

    security.declareProtected(permission_access_entries, 'entry_leaf_items')

    def entry_leaf_items(self, source, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None, max_levels=None):
        """!TXT! entry_leaf_items"""

        source = self.get_storage(source)
        return source.entry_leaf_items(tree_field_id, parent_entry_id, entry_id, entry_position, conditions, max_levels)

    security.declareProtected(permission_access_entries, 'entry_leaf_values')

    def entry_leaf_values(self, source, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None, max_levels=None):
        """!TXT! entry_leaf_values"""

        source = self.get_storage(source)
        return source.entry_leaf_values(tree_field_id, parent_entry_id, entry_id, entry_position, conditions, max_levels)

    # ------------------------------------------------------------------------
    # Entry Relationship Retrieval API

    security.declareProtected(permission_access_entries, 'is_ancestor')

    def is_ancestor(self, source, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None, other_parent_entry_id=None, other_entry_id=None, other_entry_position=None, of_level=None, max_levels=None):
        """!TXT! is_ancestor"""

        source = self.get_storage(source)
        return source.is_ancestor(tree_field_id, parent_entry_id, entry_id, entry_position, other_parent_entry_id, other_entry_id, other_entry_position, of_level, max_levels)

    security.declareProtected(permission_access_entries, 'is_parent')

    def is_parent(self, source, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None, other_parent_entry_id=None, other_entry_id=None, other_entry_position=None):
        """!TXT! is_parent"""

        source = self.get_storage(source)
        return source.is_parent(tree_field_id, parent_entry_id, entry_id, entry_position, other_parent_entry_id, other_entry_id, other_entry_position)

    security.declareProtected(permission_access_entries, 'is_sibling')

    def is_sibling(self, source, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None, other_parent_entry_id=None, other_entry_id=None, other_entry_position=None):
        """!TXT! is_sibling"""

        source = self.get_storage(source)
        return source.is_sibling(tree_field_id, parent_entry_id, entry_id, entry_position, other_parent_entry_id, other_entry_id, other_entry_position)

    security.declareProtected(permission_access_entries, 'is_child')

    def is_child(self, source, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None, other_parent_entry_id=None, other_entry_id=None, other_entry_position=None):
        """!TXT! is_child"""

        source = self.get_storage(source)
        return source.is_child(tree_field_id, parent_entry_id, entry_id, entry_position, other_parent_entry_id, other_entry_id, other_entry_position)

    security.declareProtected(permission_access_entries, 'is_descendant')

    def is_descendant(self, source, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None, other_parent_entry_id=None, other_entry_id=None, other_entry_position=None, of_level=None, max_levels=None):
        """!TXT! is_descendant"""

        source = self.get_storage(source)
        return source.is_descendant(tree_field_id, parent_entry_id, entry_id, entry_position, other_parent_entry_id, other_entry_id, other_entry_position, of_level, max_levels)

    # ------------------------------------------------------------------------
    # Entry Ancestor Retrieval API

    security.declareProtected(permission_access_entries, 'is_descendant')

    def count_ancestor_entries(self, source, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None, max_levels=None, include_ancestor_siblings=false):
        """!TXT! count_ancestor_entries"""

        source = self.get_storage(source)
        return source.count_ancestor_entries(tree_field_id, parent_entry_id, entry_id, entry_position, max_levels=max_levels, include_ancestor_siblings=include_ancestor_siblings)

    def ancestor_entry_ids(self, source, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None, max_levels=None, include_ancestor_siblings=false):
        """!TXT! ancestor_entry_ids"""

        source = self.get_storage(source)
        return source.ancestor_entry_ids(tree_field_id, parent_entry_id, entry_id, entry_position, max_levels=max_levels, include_ancestor_siblings=include_ancestor_siblings)

    def ancestor_entry_items(self, source, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None, max_levels=None, include_ancestor_siblings=false):
        """!TXT! ancestor_entry_items"""

        source = self.get_storage(source)
        return source.ancestor_entry_items(tree_field_id, parent_entry_id, entry_id, entry_position, max_levels=max_levels, include_ancestor_siblings=include_ancestor_siblings)

    def ancestor_entry_values(self, source, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None, max_levels=None, include_ancestor_siblings=false):
        """!TXT! ancestor_entry_values"""

        source = self.get_storage(source)
        return source.ancestor_entry_values(tree_field_id, parent_entry_id, entry_id, entry_position, max_levels=max_levels, include_ancestor_siblings=include_ancestor_siblings)

    # ------------------------------------------------------------------------
    # Entry Parent Retrieval API

    def get_parent_entry(self, source, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT! get_parent_entry"""

        source = self.get_storage(source)
        return source.get_parent_entry(tree_field_id, parent_entry_id, entry_id, entry_position)

    def get_parent_entry_id(self, source, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT! get_parent_entry_id"""

        source = self.get_storage(source)
        return source.get_parent_entry_id(tree_field_id, parent_entry_id, entry_id, entry_position)

    def get_parent_entry_item(self, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT! get_parent_entry_item"""

        source = self.get_storage(source)
        return source.get_parent_entry_item(tree_field_id, parent_entry_id, entry_id, entry_position)

    # ------------------------------------------------------------------------
    # Entry Sibling Retrieval API

    def count_sibling_entries(self, source, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT! count_sibling_entries"""

        source = self.get_storage(source)
        return source.count_sibling_entries(tree_field_id, parent_entry_id, entry_id, entry_position)

    def has_sibling_entries(self, source, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT! has_sibling_entries"""

        source = self.get_storage(source)
        return source.has_sibling_entries(tree_field_id, parent_entry_id, entry_id, entry_position)

    def sibling_entry_ids(self, source, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT! sibling_entry_ids"""

        source = self.get_storage(source)
        return source.sibling_entry_ids(tree_field_id, parent_entry_id, entry_id, entry_position)

    def sibling_entry_items(self, source, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT! sibling_entry_items"""

        source = self.get_storage(source)
        return source.sibling_entry_items(tree_field_id, parent_entry_id, entry_id, entry_position)

    def sibling_entry_values(self, source, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT! sibling_entry_values"""

        source = self.get_storage(source)
        return source.sibling_entry_values(tree_field_id, parent_entry_id, entry_id, entry_position)

    # ------------------------------------------------------------------------
    # Entry Child Retrieval API

    def count_children_entries(self, source, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT! count_children_entries"""

        source = self.get_storage(source)
        return source.count_descendant_entries(tree_field_id, parent_entry_id, entry_id, entry_position)

    def has_children_entries(self, source, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT! has_children_entries"""

        source = self.get_storage(source)
        return source.has_descendant_entries(tree_field_id, parent_entry_id, entry_id, entry_position)

    def children_entry_ids(self, source, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT! children_entry_ids"""

        source = self.get_storage(source)
        return source.children_entry_ids(tree_field_id, parent_entry_id, entry_id, entry_position)

    def children_entry_items(self, source, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT! children_entry_items"""

        source = self.get_storage(source)
        return source.children_entry_items(tree_field_id, parent_entry_id, entry_id, entry_position)

    def children_entry_values(self, source, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None):
        """!TXT! children_entry_values"""

        source = self.get_storage(source)
        return source.children_entry_values(tree_field_id, parent_entry_id, entry_id, entry_position)

    # ------------------------------------------------------------------------
    # Entry Descendant Retrieval API

    def count_descendant_entries(self, source, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None, max_levels=None):
        """!TXT! count_descendant_entries"""

        source = self.get_storage(source)
        return source.count_descendant_entries(tree_field_id, parent_entry_id, entry_id, entry_position, max_levels)

    def descendant_entry_ids(self, source, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None, max_levels=None):
        """!TXT! descendant_entry_ids"""

        source = self.get_storage(source)
        return source.descendant_entry_ids(tree_field_id, parent_entry_id, entry_id, entry_position, max_levels)

    def descendant_entry_items(self, source, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None, max_levels=None):
        """!TXT! descendant_entry_items"""

        source = self.get_storage(source)
        return source.descendant_entry_items(tree_field_id, parent_entry_id, entry_id, entry_position, max_levels)

    def descendant_entry_values(self, source, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None, max_levels=None):
        """!TXT! descendant_entry_values"""

        source = self.get_storage(source)
        return source.descendant_entry_values(tree_field_id, parent_entry_id, entry_id, entry_position, max_levels)

    # ------------------------------------------------------------------------
    # Entry Tree Mutation API

    def move_entry_branch(self, source, tree_field_id=None, destination_entry_id=None, parent_entry_id=None, entry_id=None, entry_position=None, REQUEST=None):
        """!TXT! move_entry_branch"""

        source = self.get_storage(source)
        entry_ids, entry_positions = source.move_entry_branch(tree_field_id, destination_entry_id, parent_entry_id, entry_id, entry_position)

        if REQUEST:
            self.redirect(REQUEST, 'entries_form', '!TXT! %d Entries in Storage "%s" moved.' % (len(entry_ids), source.getId()))
        else:
            return entry_ids, entry_positions

    def move_entry_branches(self, source, tree_field_id=None, destination_entry_id=None, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None, REQUEST=None):
        """!TXT! move_entry_branches"""

        source = self.get_storage(source)
        entry_ids, entry_positions = source.move_entry_branches(tree_field_id, destination_entry_id, parent_entry_id, entry_ids, entry_positions, conditions)

        if REQUEST:
            self.redirect(REQUEST, 'entries_form', '!TXT! %d Entries in Storage "%s" moved.' % (len(entry_ids), source.getId()))
        else:
            return entry_ids, entry_positions

    def flatten_entry_branch(self, source, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None, max_levels=None, REQUEST=None):
        """!TXT! flatten_entry_branch"""

        source = self.get_storage(source)
        entry_ids, entry_positions = source.flatten_entry_branch(tree_field_id, parent_entry_id, entry_id, entry_position, max_levels)

        if REQUEST:
            self.redirect(REQUEST, 'entries_form', '!TXT! %d Entries in Storage "%s" flattened.' % (len(entry_ids), source.getId()))
        else:
            return entry_ids, entry_positions

    def flatten_entry_branches(self, source, tree_field_id=None, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None, max_levels=None, REQUEST=None):
        """!TXT! flatten_entry_branches"""

        source = self.get_storage(source)
        entry_ids, entry_positions = source.flatten_entry_branches(tree_field_id, parent_entry_id, entry_ids, entry_positions, conditions, max_levels)

        if REQUEST:
            self.redirect(REQUEST, 'entries_form', '!TXT! %d Entries in Storage "%s" flattened.' % (len(entry_ids), source.getId()))
        else:
            return entry_ids, entry_positions

    def crop_entry_branch(self, source, tree_field_id=None, parent_entry_id=None, entry_id=None, entry_position=None, REQUEST=None):
        """!TXT! crop_entry_branch"""

        source = self.get_storage(source)
        entry_ids, entry_positions = source.crop_entry_branch(tree_field_id, parent_entry_id, entry_id, entry_position, max_levels)

        if REQUEST:
            self.redirect(REQUEST, 'entries_form', '!TXT! %d Entries in Storage "%s" cropped.' % (len(entry_ids), source.getId()))
        else:
            return entry_ids, entry_positions

    def crop_entry_branches(self, source, tree_field_id=None, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None, REQUEST=None):
        """!TXT! crop_entry_branches"""

        source = self.get_storage(source)
        entry_ids, entry_positions = source.crop_entry_branches(tree_field_id, parent_entry_id, entry_ids, entry_positions, conditions)

        if REQUEST:
            self.redirect(REQUEST, 'entries_form', '!TXT! %d Entries in Storage "%s" cropped.' % (len(entry_ids), source.getId()))
        else:
            return entry_ids, entry_positions

# ----------------------------------------------------------------------------
# Class Security

InitializeClass(EntryTrees)
