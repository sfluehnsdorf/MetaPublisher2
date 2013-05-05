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

__doc__ = """Entry Component

!TXT! module info

$Id: data/entries/entry.py 10 2013-05-05 18:01:53Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.library import ClassSecurityInfo, InitializeClass, permission_access_entries, permission_change_entries, permission_create_entries, false, true, quote_plus


# ============================================================================
# Module Exports

__all__ = [
    'Entry',
]


# ============================================================================
# Entry Mix-In Class

class Entry:
    """Entry Mix-In Class"""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # Single Entry Retrieval API

    security.declareProtected(permission_access_entries, 'get_entry')

    def get_entry(self, source, parent_entry_id=None, entry_id=None, entry_position=None, field_ids=None, failsafe=false, bound=true):
        """
        Retrieve a single Entry

        Return the specified EntryFields of the Entry specified by either id or
        position from the specified source. Unless failsafe is True, raises
        KeyError if the specified Entry does not exist.

        source
          the id of a Storage, a Storage or an EntrySet to retrieve the Entry
          from.

        parent_entry_id
          the parent Entry that the specified Entry is searched in. If no parent
          Entry is specified, the root Entry is used.

        entry_id
          the unique id identifying the Entry. If specified, entry_position must
          be None or a ValueError exception will be raised.

        entry_position
          the position identifying the Entry. If specified, entry_id must be
          None or a ValueError exception will be raised.

        field_ids
          the ids of the Fields, that will be returned. A 2-tuple identifies the
          Field with the first item and specifies an alias for it with the
          second item. Instead of a Field id an expression may be defined with
          an alias. If undefined or 'primary' string will return all primary
          Fields. If '*' string will return all Fields.

        failsafe
          Flag, that if True causes no KeyError exception to be raised, should
          the specified Entry not exist.

        bound
          Flag, that if True will bind the Entry to its source, causing all
          changes to its values to be stored in the source as well.
        """

        source = self.get_storage(source)
        return source.get_entry(parent_entry_id, entry_id, field_ids, failsafe, bound)

    # ------------------------------------------------------------------------
    # Multiple Entry Retrieval API

    security.declareProtected(permission_access_entries, 'entry_ids')

    def entry_ids(self, source, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None, order_by=None, offset=None, limit=None, bound=None):
        """Return the ids of Entries of the specified source, ordered by a specific EntryField's value and limited to the Entries specified by ids or positions and matching conditions if defined."""

        source = self.get_storage(source)
        return source.entry_ids(parent_entry_id, entry_ids, entry_positions, conditions, order_by, offset, limit, bound)

    security.declareProtected(permission_access_entries, 'entry_items')

    def entry_items(self, source, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None, field_ids=None, order_by=None, offset=None, limit=None, bound=None):
        """Return a list of tuples of id, Entry of the Entries of the specified source, ordered by a specific EntryField's value and limited to the Entries specified by ids or positions and matching conditions if defined. If the Fields to return are undefined, all primary Fields will be returned."""

        source = self.get_storage(source)
        return source.entry_items(parent_entry_id, entry_ids, entry_positions, conditions, field_ids, order_by, offset, limit, bound)

    security.declareProtected(permission_access_entries, 'entry_values')

    def entry_values(self, source, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None, field_ids=None, order_by=None, offset=None, limit=None, bound=None):
        """Return a list of Entries of the specified source, ordered by a specific EntryField's value and limited to the Entries specified by ids or positions and matching conditions if defined. If the Fields to return are undefined, all primary Fields will be returned."""

        source = self.get_storage(source)
        return source.entry_values(parent_entry_id, entry_ids, entry_positions, conditions, field_ids, order_by, offset, limit, bound)

    # ------------------------------------------------------------------------
    # Entry Statistics Retrieval API

    security.declareProtected(permission_access_entries, 'count_entries')

    def count_entries(self, source, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None):
        """Return the number of Entries of the specified source, limited to the Entries specified by ids or positions and filtered by conditions if defined."""

        source = self.get_storage(source)
        return source.count_entries(parent_entry_id, entry_ids, entry_positions, conditions)

    # ------------------------------------------------------------------------
    # Entry Existence Retrieval API

    security.declareProtected(permission_access_entries, 'has_all_entries')

    def has_all_entries(self, source, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None):
        """Return True if all Entries exist in the specified source, limited to the Entries specified by ids or positions and matching conditions if specified, False otherwise."""

        source = self.get_storage(source)
        return source.has_all_entries(parent_entry_id, entry_ids, entry_positions, conditions)

    security.declareProtected(permission_access_entries, 'has_any_entries')

    def has_any_entries(self, source, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None):
        """Return True if any Entries exist in the specified source, limited to the Entries specified by ids or positions and matching conditions if defined, False otherwise."""

        source = self.get_storage(source)
        return source.has_any_entries(parent_entry_id, entry_ids, entry_positions, conditions)

    security.declareProtected(permission_access_entries, 'has_entry')

    def has_entry(self, source, parent_entry_id=None, entry_id=None, entry_position=None):
        """Return True if the Entry specified by id or position exists in the specified source, False otherwise."""

        source = self.get_storage(source)
        return source.has_entry(parent_entry_id, entry_id, entry_position)

    # ------------------------------------------------------------------------
    # Entry Creation Mutation API

    security.declareProtected(permission_create_entries, 'add_entry')

    def add_entry(self, source, parent_entry_id=None, entry_id=None, entry_position=None, data={}, REQUEST=None, **args):
        """Add a new Entry to the specified source with the specified id and/or position and the specified data. If no id is specified and the source expects an id, it will be automatically generated. If no position is specified and the source, the Entry will be added to the default position."""

        data.update(args)
        if REQUEST:
            data.update(REQUEST.form)
        source = self.get_storage(source)
        entry_id, entry_position = source.add_entry(parent_entry_id, entry_id, entry_position, data)

        if REQUEST:
            self.redirect(REQUEST, 'entries_form', 'Entry %s%sadded to Storage "%s".' % (entry_id and '"%s" ' % entry_id or '', entry_position is not None and 'at position %d ' % entry_position or '', source.getId()))
        else:
            return entry_id, entry_position

    security.declareProtected(permission_create_entries, 'add_entry_continued')

    def add_entry_continued(self, source, parent_entry_id=None, entry_id=None, entry_position=None, data={}, REQUEST=None, **args):
        """Convenience method to add a new Entry and redirect to the add form."""

        data.update(args)
        if REQUEST:
            data.update(REQUEST.form)
        entry_id, entry_position = self.add_entry(parent_entry_id, entry_id, entry_position, data)

        if REQUEST:
            self.redirect(REQUEST, 'add_entry_form', 'Entry %s%sadded to Storage "%s".' % (entry_id and '"%s" ' % entry_id or '', entry_position is not None and 'at position %d ' % entry_position or '', source.getId()))
        else:
            return entry_id, entry_position

    security.declareProtected(permission_create_entries, 'add_entry_to_top')

    def add_entry_to_top(self, source, parent_entry_id=None, entry_id=None, data={}, REQUEST=None, **args):
        """Convenience method to add a new Entry to the beginning of the source."""

        data.update(args)
        if REQUEST:
            data.update(REQUEST.form)
        source = self.get_storage(source)
        entry_id, entry_position = source.add_entry_to_top(parent_entry_id, entry_id, data)

        if REQUEST:
            self.redirect(REQUEST, 'entries_form', 'Entry %sadded to the top of Storage "%s".' % (entry_id and '"%s" ' % entry_id or '', source.getId()))
        else:
            return entry_id, entry_position

    security.declareProtected(permission_create_entries, 'add_entry_to_bottom')

    def add_entry_to_bottom(self, source, parent_entry_id=None, entry_id=None, data={}, REQUEST=None, **args):
        """Convenience method to add a new Entry to the end of the source."""

        data.update(args)
        if REQUEST:
            data.update(REQUEST.form)
        source = self.get_storage(source)
        entry_id, entry_position = source.add_entry_to_bottom(parent_entry_id, entry_id, data)

        if REQUEST:
            self.redirect(REQUEST, 'entries_form', 'Entry %sadded to the end of Storage "%s".' % (entry_id and '"%s" ' % entry_id or '', source.getId()))
        else:
            return entry_id, entry_position

    security.declareProtected(permission_create_entries, 'add_entry_somewhere')

    def add_entry_somewhere(self, source, parent_entry_id=None, entry_id=None, data={}, REQUEST=None, **args):
        """Convenience method to add a new Entry at a random position in the source."""

        data.update(args)
        if REQUEST:
            data.update(REQUEST.form)
        source = self.get_storage(source)
        entry_id, entry_position = source.add_entry_somewhere(parent_entry_id, entry_id, data)

        if REQUEST:
            self.redirect(REQUEST, 'entries_form', 'Entry %s%sadded to Storage "%s".' % (entry_id and '"%s" ' % entry_id or '', entry_position is not None and 'at position %d ' % entry_position or '', source.getId()))
        else:
            return entry_id, entry_position

    security.declareProtected(permission_create_entries, 'add_entries')

    def add_entries(self, source, entries, parent_entry_id=None, REQUEST=None):
        """!TXT! add_entries"""

        source = self.get_storage(source)
        entry_ids, entry_positions = source.add_entries(parent_entry_id, entries)

        if REQUEST:
            self.redirect(REQUEST, 'entries_form', '%d Entries %sadded to Storage "%s".' % (len(entry_ids), entry_id and '"%s" ' % entry_id or '', source.getId()))
        else:
            return entry_ids, entry_positions

    # !!! entry.py - implement add_entries_continued

    security.declareProtected(permission_create_entries, 'add_entries_to_top')

    def add_entries_to_top(self, source, entries, parent_entry_id=None, REQUEST=None):
        """!TXT! add_entries_to_top"""

        source = self.get_storage(source)
        entry_ids, entry_positions = source.add_entries_to_top(parent_entry_id, entries)

        if REQUEST:
            # !!! entry.py - add_entries_to_top redirect
            pass
        else:
            return entry_ids, entry_positions

    security.declareProtected(permission_create_entries, 'add_entries_to_bottom')

    def add_entries_to_bottom(self, source, entries, parent_entry_id=None, REQUEST=None):
        """!TXT! add_entries_to_bottom"""

        source = self.get_storage(source)
        entry_ids, entry_positions = source.add_entries_to_bottom(parent_entry_id, entries)

        if REQUEST:
            # !!! entry.py - add_entries_to_bottom redirect
            pass
        else:
            return entry_ids, entry_positions

    security.declareProtected(permission_create_entries, 'add_entries_somewhere')

    def add_entries_somewhere(self, source, entries, parent_entry_id=None, REQUEST=None):
        """!TXT! add_entries_to_bottom"""

        source = self.get_storage(source)
        entry_ids, entry_positions = source.add_entries_somewhere(parent_entry_id, entries)

        if REQUEST:
            # !!! entry.py - add_entries_to_somewhere redirect
            pass
        else:
            return entry_ids, entry_positions

    security.declareProtected(permission_create_entries, 'duplicate_entry')

    def duplicate_entry(self, source, parent_entry_id=None, entry_id=None, entry_position=None, new_id=None, REQUEST=None):
        """Duplicate the Entry, specified by id or position, in the specified storage, automatically generating a new id if not specified"""

        source = self.get_storage(source)
        new_id, new_position = source.duplicate_entry(parent_entry_id, entry_id, entry_position, new_id)

        if REQUEST:
            self.redirect(REQUEST, 'entries_form', 'Entry %s%sin Storage "%s" duplicated%s%s.' % (entry_id and '"%s" ' % entry_id or '', entry_position is not None and 'at position %d ' % entry_position or '', source.getId(), new_id and ' as "%s"' % new_id, new_position is not None and ' at position %d' % new_position or ''))
        else:
            return new_id, new_position

    security.declareProtected(permission_create_entries, 'duplicate_entries')

    def duplicate_entries(self, source, parent_entry_id=None, entry_ids=[], entry_positions=[], conditions=None, new_ids=None, REQUEST=None):
        """Duplicate the Entries, specified by ids or positions, in the specified storage, matching conditions if defined, automatically generating new ids if not specified. If the new ids are specfied, both id lists must have the same length or ValueError is raised."""

        source = self.get_storage(source)
        new_ids, new_positions = source.duplicate_entries(parent_entry_id, entry_ids, entry_positions, conditions, new_ids)

        if REQUEST:
            self.redirect(REQUEST, 'entries_form', '%d Entries duplicated in Storage "%s".' % (len(new_ids), source.getId()))
        else:
            return new_ids, new_positions

    security.declareProtected(permission_change_entries, 'set_entry')

    def set_entry(self, source, parent_entry_id=None, entry_id=None, entry_position=None, data={}, REQUEST=None, **args):
        """Add or edit an Entry of the specified Storage"""

        data.update(args)
        if REQUEST:
            data.update(REQUEST.form)
        source = self.get_storage(source)
        entry_id, entry_position = source.set_entry(parent_entry_id, entry_id, entry_position, data)

        if REQUEST:
            self.redirect(REQUEST, 'entries_form', 'Entry %s%sset in Storage "%s".' % (entry_id and '"%s" ' % entry_id or '', entry_position is not None and 'at position %d ' % entry_position or '', source.getId()))
        else:
            return entry_id, entry_position

    # ------------------------------------------------------------------------
    # Entry Modification Mutation API

    security.declareProtected(permission_change_entries, 'edit_entry')

    def edit_entry(self, source, parent_entry_id=None, entry_id=None, entry_position=None, data={}, REQUEST=None, **args):
        """Edit an Entry of the specified source with the specified id and/or position and the specified data."""

        data.update(args)
        if REQUEST:
            data.update(REQUEST.form)
        source = self.get_storage(source)
        entry_id, entry_position = source.edit_entry(parent_entry_id, entry_id, entry_position, data)

        if REQUEST:
            self.redirect(REQUEST, 'entries_form', 'Entry %s%sin Storage "%s" changed.' % (entry_id and '"%s" ' % entry_id or '', entry_position is not None and 'at position %d ' % entry_position or '', source.getId()))
        else:
            return entry_id, entry_position

    security.declareProtected(permission_change_entries, 'edit_entry_continued')

    def edit_entry_continued(self, source, parent_entry_id=None, entry_id=None, entry_position=None, data={}, REQUEST=None, **args):
        """Edit an Entry of the specified Storage and redirect to the add form."""

        data.update(args)
        if REQUEST:
            data.update(REQUEST.form)
        entry_id, entry_position = edit_entry(source, parent_entry_id, entry_id, entry_position, data)

        if REQUEST:
            self.redirect(REQUEST, 'edit_entry_form', 'Entry %s%sin Storage "%s" changed.' % (entry_id and '"%s" ' % entry_id or '', entry_position is not None and 'at position %d ' % entry_position or '', source.getId()))
        else:
            return entry_id, entry_position

    security.declareProtected(permission_change_entries, 'edit_entries')

    def edit_entries(self, source, parent_entry_id=None, entry_ids=[], entry_positions=[], conditions=None, data={}, REQUEST=None, **args):
        """Edit Entries of the specified Storage with the specified data, identified by the specified ids and/or positions, matching conditions if defined"""

        data.update(args)
        if REQUEST:
            data.update(REQUEST.form)
        source = self.get_storage(source)
        entry_ids, entry_positions = source.edit_entries(parent_entry_id, entry_ids, entry_positions, conditions, data)

        if REQUEST:
            self.redirect(REQUEST, 'entries_form', '%d Entries in Storage "%s" changed.' % (len(entry_ids), source.getId()))
        else:
            return entry_ids, entry_positions

    # !!! entry.py - implement edit_entries_continued

    security.declareProtected(permission_change_entries, 'rename_entry')

    def rename_entry(self, source, parent_entry_id=None, entry_id=None, entry_position=None, new_id=None, REQUEST=None):
        """Rename the specified Entry of the specified Storage, automatically generating a new id if not specified."""

        source = self.get_storage(source)
        new_id = source.rename_entry(parent_entry_id, entry_id, entry_position, new_id)

        if REQUEST:
            self.redirect(REQUEST, 'entries_form', 'Entry %s%sin Storage "%s" renamed to "%s".' % (entry_id and '"%s" ' % entry_id or '', entry_position is not None and 'at position %d ' % entry_position or '', source.getId(), new_id))
        else:
            return new_id

    security.declareProtected(permission_change_entries, 'rename_entries')

    def rename_entries(self, source, parent_entry_id=None, entry_ids=[], entry_positions=[], conditions=None, new_ids=None, REQUEST=None):
        """Rename the specified Entries of the specified Storage, automatically generating new ids if not specified, matching conditions if defined. If the new ids are specified, both id lists must have the same length."""

        source = self.get_storage(source)
        entry_ids, new_ids = source.rename_entries(parent_entry_id, entry_ids, entry_positions, conditions, new_ids)

        if REQUEST:
            self.redirect(REQUEST, 'entries_form', '%d Entries renamed in Storage "%s".' % (len(new_ids), source.getId()))
        else:
            return entry_ids, new_ids

    security.declareProtected(permission_change_entries, 'reset_entry')

    def reset_entry(self, source, parent_entry_id=None, entry_id=None, entry_position=None, field_ids=None, REQUEST=None):
        """Reset either all or only the specified Fields of the specified Entry to default values."""

        source = self.get_storage(source)
        entry_id, entry_position = source.reset_entry(parent_entry_id, entry_id, entry_position, field_ids)

        if REQUEST:
            self.redirect(REQUEST, 'entries_form', 'Entry %s%sin Storage "%s" resetted to default values.' % (entry_id and '"%s" ' % entry_id or '', entry_position is not None and 'at position %d ' % entry_position or '', source.getId()))
        else:
            return entry_id, entry_position

    security.declareProtected(permission_change_entries, 'reset_entries')

    def reset_entries(self, source, parent_entry_id=None, entry_ids=[], entry_positions=[], conditions=None, field_ids=None, REQUEST=None):
        """Reset either all or only the specified Fields of the specified Entries, matching conditions if defined, to default values."""

        source = self.get_storage(source)
        entry_ids, entry_positions = source.reset_entries(parent_entry_id, entry_ids, entry_positions, conditions, field_ids)

        if REQUEST is not None:
            self.redirect(REQUEST, 'entries_form', '%d Entries in Storage "%s" resetted to default values.' % (len(entry_ids), source.getId()))
        else:
            return entry_ids, entry_positions

    # ------------------------------------------------------------------------
    # Entry Deletion Mutation API

    security.declareProtected(permission_change_entries, 'clear_entries')

    def clear_entries(self, source, REQUEST=None):
        """Delete all Entries in the specified source."""

        source = self.get_storage(source)
        entry_ids, entry_positions = self.clear_entries()

        if REQUEST:
            self.redirect(REQUEST, 'entries_form', 'All %d Entries deleted from Storage "%s".' % (len(entry_ids), source.getId()))
        else:
            return entry_ids, entry_positions

    security.declareProtected(permission_change_entries, 'delete_entry')

    def delete_entry(self, source, parent_entry_id=None, entry_id=None, entry_position=None, failsafe=false, REQUEST=None):
        """Delete an Entry from the specified Storage. Either an Entry's id or position must be specified. Unless failsafe is True, raises KeyError if the specified Entry does not exist."""

        source = self.get_storage(source)
        entry_id, entry_position = source.delete_entry(parent_entry_id, entry_id, entry_position, failsafe)

        if REQUEST:
            self.redirect(REQUEST, 'entries_form', 'Entry %s%sdeleted from Storage "%s".' % (entry_id and '"%s" ' % entry_id or '', entry_position is not None and 'at position %d ' % entry_position or '', source.getId()))
        else:
            return entry_id, entry_position

    security.declareProtected(permission_change_entries, 'delete_entries')

    def delete_entries(self, source, parent_entry_id=None, entry_ids=[], entry_positions=[], conditions=None, failsafe=false, REQUEST=None):
        """Delete the Entries, matching conditions if defined, from the specified Storage. Either Entries' ids or positions must be specified. Unless failsafe is True, raises KeyError if any of the specified Entries does not exist."""

        source = self.get_storage(source)
        entry_ids, entry_positions = source.delete_entries(parent_entry_id, entry_ids, entry_positions, conditions, failsafe)

        if REQUEST:
            self.redirect(REQUEST, 'entries_form', '%d Entries deleted from Storage "%s".' % (len(entry_ids), source.getId()))
        else:
            return entry_ids, entry_positions

    security.declareProtected(permission_change_entries, 'pop_first_entry')

    def pop_first_entry(self, source, parent_entry_id=None, conditions=None, REQUEST=None):
        """Convenience method to delete and return the Entry at the beginning of the source."""

        source = self.get_storage(source)
        entry_id, entry_position, entry = source.pop_first_entry(parent_entry_id, conditions)

        if REQUEST:
            self.redirect(REQUEST, 'entries_form', 'Entry %s%sdeleted from Storage "%s".' % (entry_id and '"%s" ' % entry_id or '', entry_position is not None and 'at position %d ' % entry_position or '', source.getId()))
        else:
            return entry_id, entry_position, entry

    security.declareProtected(permission_change_entries, 'pop_last_entry')

    def pop_last_entry(self, source, parent_entry_id=None, conditions=None, REQUEST=None):
        """Convenience method to delete and return the Entry at the end of the source."""

        source = self.get_storage(source)
        entry_id, entry_position, entry = source.pop_last_entry(parent_entry_id, conditions)

        if REQUEST:
            self.redirect(REQUEST, 'entries_form', 'Entry %s%sdeleted from Storage "%s".' % (entry_id and '"%s" ' % entry_id or '', entry_position is not None and 'at position %d ' % entry_position or '', source.getId()))
        else:
            return entry_id, entry_position, entry

    security.declareProtected(permission_change_entries, 'pop_random_entry')

    def pop_random_entry(self, source, parent_entry_id=None, conditions=None, REQUEST=None):
        """Convenience method to delete and return the Entry at a random position in the source."""

        source = self.get_storage(source)
        entry_id, entry_position, entry = source.pop_random_entry(parent_entry_id, conditions)

        if REQUEST:
            self.redirect(REQUEST, 'entries_form', 'Entry %s%sdeleted from Storage "%s".' % (entry_id and '"%s" ' % entry_id or '', entry_position is not None and 'at position %d ' % entry_position or '', source.getId()))
        else:
            return entry_id, entry_position, entry

# ----------------------------------------------------------------------------
# Class Security

InitializeClass(Entry)

# TODO: include **options parameter to support special tree and graph options OR define additional parameters (
#       delete_entry() with exclude_self=false, include_descendants=false, max_descendant_levels=None
#       delete_entries() with exclude_selves=false, include_ancestors=false, include_ancestor_siblings=false, max_ancestor_levels=None, include_descendants=false, max_descendant_levels=None
#       - ascend=false, ascend_levels=0, descend=false, descend_levels=0

# !!! entry.py - use list_entries_formlet where applicable
