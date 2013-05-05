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

__doc__ = """Storage Base

!TXT! module info

$Id: bases/storage/storage.py 5 2013-05-05 18:01:53Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.bases.entrycontainer import EntryContainer
from Products.MetaPublisher2.bases.plugin import PluginBase
from Products.MetaPublisher2.interfaces import IStoragePluginBase
from Products.MetaPublisher2.library.application import permission_access_configuration, permission_change_configuration, permission_zmi
from Products.MetaPublisher2.library.common import ClassSecurityInfo, ComputedAttribute, DTMLFile, implements, InitializeClass, OrderedFolder
from Products.MetaPublisher2.library.userinterface import UserInterface


# ==============================================================================
# Module Exports

__all__ = [
    'StoragePluginBase',
]


# ============================================================================
# Storage Plugin Base

class StoragePluginBase(EntryContainer, UserInterface, PluginBase, OrderedFolder):
    """Storage Plugin Base"""

    security = ClassSecurityInfo()

    implements(IStoragePluginBase)

    # ------------------------------------------------------------------------
    # Storage Attributes

    icon = 'misc_/MetaPublisher2/storage.png'

    _properties = PluginBase._properties + (
        {'id': 'storage_type', 'type': 'string', 'mode': ''},
    )

    # ------------------------------------------------------------------------
    # Storage Plugin Description

    plugin_type = 'Storage'

    storage_type = None

    # ------------------------------------------------------------------------
    # Storage Specification

    security.declareProtected(permission_access_configuration, 'get_plugin_specification')

    def get_plugin_specification(self):
        """Return a dictionary describing this Storage"""

        options = PluginBase.get_plugin_specification(self)
        options.update({
            'storage_type': self.storage_type,
        })
        return options

    # ------------------------------------------------------------------------
    # Storage Identity API

    security.declareProtected(permission_access_configuration, 'get_storage_instance')

    get_storage_instance = PluginBase.get_plugin_instance

    security.declareProtected(permission_access_configuration, 'get_storage_id')

    get_storage_id = PluginBase.get_plugin_id

    security.declareProtected(permission_access_configuration, 'get_storage_url')

    get_storage_url = PluginBase.get_plugin_url

    # ------------------------------------------------------------------------
    # Storage ZMI

    security.declareProtected(permission_change_configuration, 'add_storage_formlet')

    add_storage_formlet = DTMLFile('storageplugin_add', globals())

    security.declareProtected(permission_change_configuration, 'edit_storage_formlet')

    edit_storage_formlet = DTMLFile('storageplugin_edit', globals())

    # ------------------------------------------------------------------------
    # Storage Retrieval API

    def get_status(self):
        """!TXT!"""

        # DEVELOPER: IMPORTANT - get_status !TXT!
        pass

    # ------------------------------------------------------------------------
    # Storage Mutation API

    def add_storage(self, options):
        """!TXT!"""

        # DEVELOPER: IMPORTANT - add_storage !TXT! maybe auto set properties as placeholder
        pass

    def edit_storage(self, options):
        """!TXT!"""

        # DEVELOPER: IMPORTANT - edit_storage !TXT! maybe auto set properties as placeholder
        pass

    def before_duplicate(self, new_id):
        """!TXT!"""

        # DEVELOPER: OPTIONAL - before_duplicate !TXT!
        pass

    def after_duplicate(self, old_id):
        """!TXT!"""

        # DEVELOPER: OPTIONAL - after_duplicate !TXT!
        pass

    def before_rename(self, new_id):
        """!TXT!"""

        # DEVELOPER: OPTIONAL - before_rename !TXT!
        pass

    def after_rename(self, old_id):
        """!TXT!"""

        # DEVELOPER: OPTIONAL - after_rename !TXT!
        pass

    def before_delete(self):
        """!TXT!"""

        # DEVELOPER: OPTIONAL - before_delete !TXT!
        pass

    def is_source_storage(self):
        """!TXT!"""

        return true

    def get_source_storages(self):
        """!TXT!"""

        return []

    # ------------------------------------------------------------------------
    # Identifiers Retrieval API

    def last_entry_id(self):
        """!TXT! read last entry id from property"""

        pass

    def new_entry_id(self):
        """!TXT! create temporary solution (code exists), store in property for last_entry_id"""

        pass

    # ------------------------------------------------------------------------
    # Fields Retrieval API

    def count_fields(self):
        """!TXT!"""

        pass

    def field_ids(self):
        """!TXT!"""

        pass

    def field_items(self):
        """!TXT!"""

        pass

    def field_values(self):
        """!TXT!"""

        pass

    def get_field(self, field_id):
        """!TXT!"""

        pass

    def get_field_default(self, field_id):
        """!TXT!"""

        pass

    def has_all_fields(self, field_ids=None, field_types=None):
        """!TXT!"""

        pass

    def has_any_fields(self, field_ids=None, field_types=None):
        """!TXT!"""

        pass

    def has_field(self, field_id):
        """!TXT!"""

        pass

    # ------------------------------------------------------------------------
    # Fields Mutation API

    def before_add_field(self, field_id, field_type_id, options):
        """!TXT!"""

        pass

    def after_add_field(self, field_id, field_type_id, options):
        """!TXT!"""

        pass

    def delete_field(self, field_id):
        """!TXT!"""

        pass

    def delete_fields(self, field_ids):
        """!TXT!"""

        pass

    def duplicate_field(self, field_id, new_id):
        """!TXT!"""

        pass

    def duplicate_fields(self, field_ids, new_ids):
        """!TXT!"""

        pass

    def edit_field(self, field_id, options):
        """!TXT!"""

        pass

    def rename_field(self, field_id, new_id):
        """!TXT!"""

        pass

    def rename_fields(self, field_ids, new_ids):
        """!TXT!"""

        pass

    def set_field_default(self, field_id, value):
        """!TXT!"""

        pass

    # ------------------------------------------------------------------------
    # Primary Field API

    def is_primary_field(self, field_id):
        """!TXT!"""

        pass

    def primary_field_ids(self):
        """!TXT!"""

        pass

    def primary_field_items(self):
        """!TXT!"""

        pass

    def primary_field_values(self):
        """!TXT!"""

        pass

    def set_primary_field(self, field_id):
        """!TXT!"""

        pass

    def unset_primary_field(self, field_id):
        """!TXT!"""

        pass

    # ------------------------------------------------------------------------
    # Field Ordering API

    def get_field_position(self, field_id):
        """!TXT!"""

        pass

    def move_field_to_position(self, field_id, position):
        """!TXT!"""

        pass

    def move_field_to_top(self, field_id):
        """!TXT!"""

        pass

    def move_field_up(self, field_id):
        """!TXT!"""

        pass

    def move_field_down(self, field_id):
        """!TXT!"""

        pass

    def move_field_to_bottom(self, field_id):
        """!TXT!"""

        pass

# ----------------------------------------------------------------------------
# initialize class security

InitializeClass(StoragePluginBase)

# !!! bases/storage/storage.py - define api, including before_ and after_ handlers (see legacystorage.py for default implementations)
# !!! bases/storage/storage.py - define zmi (with developer notes regarding choice of form and formlet)
# !!! bases/storage/storage.py - create unreadable_storage.py
# !!! bases/storage/storage.py - create unwriteable_storage.py
# !!! bases/storage/storage.py - create unconfigurable_storage.py
