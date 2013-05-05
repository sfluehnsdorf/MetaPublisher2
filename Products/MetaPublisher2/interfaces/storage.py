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

__doc__ = """Storage Plugin Interface

$Id: interfaces/storage.py 1 2012-02-17 15:45:00Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from zope.interface import Interface


# ============================================================================
# Module Exports

__all__ = [
    'IStoragePluginBase',
]


# ============================================================================
# Storage Plugin Base Interface

class IStoragePluginBase(Interface):
    """Storage Plugin Base Interface"""

    # ------------------------------------------------------------------------
    # Storage Mutation API

    def add_storage(options):
        """!TXT!"""

    def edit_storage(options):
        """!TXT!"""

    def before_duplicate(new_id):
        """!TXT!"""

    def after_duplicate(old_id):
        """!TXT!"""

    def before_rename(new_id):
        """!TXT!"""

    def after_rename(old_id):
        """!TXT!"""

    def before_delete():
        """!TXT!"""

    # ------------------------------------------------------------------------
    # Identifiers Retrieval API

    def last_entry_id():
        """!TXT!"""

    def new_entry_id():
        """!TXT!"""

    # ------------------------------------------------------------------------
    # Fields Retrieval API

    def count_fields():
        """!TXT!"""

    def field_ids():
        """!TXT!"""

    def field_items():
        """!TXT!"""

    def field_values():
        """!TXT!"""

    def get_field(field_id):
        """!TXT!"""

    def get_field_default():
        """!TXT!"""

    def has_all_fields(field_ids=None, field_types=None):
        """!TXT!"""

    def has_any_fields(field_ids=None, field_types=None):
        """!TXT!"""

    def has_field(field_id):
        """!TXT!"""

    # ------------------------------------------------------------------------
    # Fields Mutation API

    def before_add_field(field_id, field_type_id, options):
        """!TXT!"""

    def after_add_field(field_id, field_type_id, options):
        """!TXT!"""

    def delete_field(field_id):
        """!TXT!"""

    def delete_fields(field_ids):
        """!TXT!"""

    def duplicate_field(field_id, new_id):
        """!TXT!"""

    def duplicate_fields(field_ids, new_ids):
        """!TXT!"""

    def edit_field(field_id, options):
        """!TXT!"""

    def rename_field(field_id, new_id):
        """!TXT!"""

    def rename_fields(field_ids, new_ids):
        """!TXT!"""

    def set_field_default(field_id, value):
        """!TXT!"""

    # ------------------------------------------------------------------------
    # Primary Field API

    def is_primary_field(field_id):
        """!TXT!"""

    def primary_field_ids():
        """!TXT!"""

    def primary_field_items():
        """!TXT!"""

    def primary_field_values():
        """!TXT!"""

    def set_primary_field(field_id):
        """!TXT!"""

    def unset_primary_field(field_id):
        """!TXT!"""

    # ------------------------------------------------------------------------
    # Field Ordering API

    def get_field_position(field_id):
        """!TXT!"""

    def move_field_to_position(field_id, position):
        """!TXT!"""

    def move_field_to_top(field_id):
        """!TXT!"""

    def move_field_up(field_id):
        """!TXT!"""

    def move_field_down(field_id):
        """!TXT!"""

    def move_field_to_bottom(field_id):
        """!TXT!"""

# !!! interfaces/storage.py - review api
