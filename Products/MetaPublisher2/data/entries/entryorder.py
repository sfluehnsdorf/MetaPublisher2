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

__doc__ = """Entry Order Component

!TXT! module info

$Id: data/entries/entryorder.py 11 2013-05-08 21:41:03Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.library import ClassSecurityInfo, InitializeClass, permission_access_entries, permission_change_entries, quote_plus


# ============================================================================
# Module Exports

__all__ = [
    'EntryOrder',
]


# ============================================================================
# Entry Order Component Mix-In Class

class EntryOrder:
    """!TXT! Entry Order Component Mix-In Class"""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # Entry Order Retrieval API

    # !!! entryorder.py - implement are_entries_sortable OR use flags instead

    security.declareProtected(permission_access_entries, 'get_entry_position')

    def get_entry_position(self, source, entry_id, parent_entry_id=None):
        """!TXT! Return the position of the specified Entry in the specified source."""

        source = self.get_storage(source)
        return source.get_entry_position(entry_id, parent_entry_id)

    security.declareProtected(permission_access_entries, 'get_entry_positions')

    def get_entry_positions(self, source, parent_entry_id=None, entry_ids=None, conditions=None, order_by=None, offset=None, limit=None):
        """!TXT! Return a list of tuples of id, value, position of the specified Entries in the specified source, ordered by a specific EntryField's value and limited to the Entries specified and matching conditions if defined."""

        source = self.get_storage(source)
        return source.get_entry_positions(parent_entry_id, entry_ids, conditions, order_by, offset, limit)

    # ------------------------------------------------------------------------
    # Entry Order Mutation API

    security.declareProtected(permission_change_entries, 'rotate_entries')

    def rotate_entries(self, source, steps, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None, REQUEST=None):
        """!TXT! rotate_entries"""

        source = self.get_storage(source)
        entry_ids = source.rotate_entries(steps, parent_entry_id, entry_ids, entry_positions, conditions)

        if REQUEST:
            self.redirect(REQUEST, 'entries_form', '%d Entries in Storage "%s" rotated by %d steps.' % (len(entry_ids), source.getId(), steps))
        else:
            return entry_ids

    security.declareProtected(permission_change_entries, 'order_entries')

    def order_entries(self, source, order_by, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None, REQUEST=None):
        """!TXT! order_entries"""

        source = self.get_storage(source)
        entry_ids = source.order_entries(order_by, parent_entry_id, entry_ids, entry_positions, conditions)

        if REQUEST:
            self.redirect(REQUEST, 'entries_form', '%d Entries in Storage "%s" reordered.' % (len(entry_ids), source.getId()))
        else:
            return entry_ids

    security.declareProtected(permission_change_entries, 'shuffle_entries')

    def shuffle_entries(self, source, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None, REQUEST=None):
        """!TXT! shuffle_entries"""

        source = self.get_storage(source)
        entry_ids = source.shuffle_entries(parent_entry_id, entry_ids, entry_positions, conditions)

        if REQUEST:
            self.redirect(REQUEST, 'entries_form', '%d Entries in Storage "%s" shuffled.' % (len(entry_ids), source.getId()))
        else:
            return entry_ids

    security.declareProtected(permission_change_entries, 'reverse_entries')

    def reverse_entries(self, source, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None, REQUEST=None):
        """!TXT! reverse_entries"""

        source = self.get_storage(source)
        entry_ids = source.reverse_entries(parent_entry_id, entry_ids, entry_positions, conditions)

        if REQUEST:
            self.redirect(REQUEST, 'entries_form', '%d Entries in Storage "%s" reversed order.' % (len(entry_ids), source.getId()))
        else:
            return entry_ids

    security.declareProtected(permission_change_entries, 'move_entry')

    def move_entry(self, source, position, parent_entry_id=None, entry_id=None, entry_position=None, REQUEST=None):
        """!TXT! Move the specified Entry in the specified source to the specified position."""

        source = self.get_storage(source)
        source.move_entry(position, parent_entry_id, entry_id, entry_position)

        self.redirect(REQUEST, 'entries_form', 'Entry "%s" in Storage "%s" moved to position %d.' % (entry_id, source.getId(), position))

    security.declareProtected(permission_change_entries, 'move_entry_to_top')

    def move_entry_to_top(self, source, parent_entry_id=None, entry_id=None, entry_position=None, REQUEST=None):
        """!TXT! Move the specified Entry in the specified source to the top."""

        source = self.get_storage(source)
        source.move_entry_to_top(parent_entry_id, entry_id, entry_position)

        self.redirect(REQUEST, 'entries_form', 'Entry "%s" in Storage "%s" moved to top.' % (entry_id, source.getId()))

    security.declareProtected(permission_change_entries, 'move_entry_up')

    def move_entry_up(self, source, parent_entry_id=None, entry_id=None, entry_position=None, REQUEST=None):
        """!TXT! Move the specified Entry in the specified source up one position."""

        source = self.get_storage(source)
        source.move_entry_up(parent_entry_id, entry_id, entry_position)

        self.redirect(REQUEST, 'entries_form', 'Entry "%s" in Storage "%s" moved up.' % (entry_id, source.getId()))

    security.declareProtected(permission_change_entries, 'move_entry_down')

    def move_entry_down(self, source, parent_entry_id=None, entry_id=None, entry_position=None, REQUEST=None):
        """!TXT! Move the specified Entry in the specified source down one position."""

        source = self.get_storage(source)
        source.move_entry_down(parent_entry_id, entry_id, entry_position)

        self.redirect(REQUEST, 'entries_form', 'Entry "%s" in Storage "%s" moved down.' % (entry_id, source.getId()))

    security.declareProtected(permission_change_entries, 'move_entry_to_bottom')

    def move_entry_to_bottom(self, source, parent_entry_id=None, entry_id=None, entry_position=None, REQUEST=None):
        """!TXT! Move the specified Entry in the specified source to the bottom."""

        source = self.get_storage(source)
        source.move_entry_to_bottom(parent_entry_id, entry_id, entry_position)

        self.redirect(REQUEST, 'entries_form', 'Entry "%s" in Storage "%s" moved to bottom.' % (entry_id, source.getId()))

    security.declareProtected(permission_change_entries, 'move_entries')

    def move_entries(self, source, position, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None, REQUEST=None):
        """!TXT! move_entries"""

        source = self.get_storage(source)
        entry_ids = source.move_entries(position, parent_entry_id, entry_ids, entry_positions, conditions)

        if REQUEST:
            self.redirect(REQUEST, 'entries_form', '%d Entries in Storage "%s" moved to position %s.' % (len(entry_ids), source.getId(), position))
        else:
            return entry_ids

    security.declareProtected(permission_change_entries, 'move_entries_to_top')

    def move_entries_to_top(self, source, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None, REQUEST=None):
        """!TXT! move_entries_to_top"""

        source = self.get_storage(source)
        entry_ids = source.move_entries_to_top(parent_entry_id, entry_ids, entry_positions, conditions)

        if REQUEST:
            self.redirect(REQUEST, 'entries_form', '%d Entries in Storage "%s" moved to top.' % (len(entry_ids), source.getId()))
        else:
            return entry_ids

    security.declareProtected(permission_change_entries, 'move_entries_up')

    def move_entries_up(self, source, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None, REQUEST=None):
        """!TXT! move_entries_up"""

        source = self.get_storage(source)
        entry_ids = source.move_entries_up(parent_entry_id, entry_ids, entry_positions, conditions)

        if REQUEST:
            self.redirect(REQUEST, 'entries_form', '%d Entries in Storage "%s" moved up' % (len(entry_ids), source.getId()))
        else:
            return entry_ids

    security.declareProtected(permission_change_entries, 'move_entries_down')

    def move_entries_down(self, source, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None, REQUEST=None):
        """!TXT! move_entries_down"""

        source = self.get_storage(source)
        entry_ids = source.move_entries_down(parent_entry_id, entry_ids, entry_positions, conditions)

        if REQUEST:
            self.redirect(REQUEST, 'entries_form', '%d Entries in Storage "%s" moved down.' % (len(entry_ids), source.getId()))
        else:
            return entry_ids

    security.declareProtected(permission_change_entries, 'move_entries_to_bottom')

    def move_entries_to_bottom(self, source, parent_entry_id=None, entry_ids=None, entry_positions=None, conditions=None, REQUEST=None):
        """!TXT! move_entries_to_bottom"""

        source = self.get_storage(source)
        entry_ids = source.move_entries_to_bottom(parent_entry_id, entry_ids, entry_positions, conditions)

        if REQUEST:
            self.redirect(REQUEST, 'entries_form', '%d Entries in Storage "%s" moved to bottom.' % (len(entry_ids), source.getId()))
        else:
            return entry_ids

# ----------------------------------------------------------------------------
# Class Security

InitializeClass(EntryOrder)
