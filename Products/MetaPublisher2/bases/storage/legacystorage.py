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

__doc__ = """Legacy Storage Base

!TXT! module info

$Id: bases/storage/legacystorage.py 14 2012-02-17 15:45:00Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.bases.plugin.legacyplugin import LegacyPluginBase
from Products.MetaPublisher2.library.common import ClassSecurityInfo, ComputedAttribute, DTMLFile, false, InitializeClass, true
from Products.MetaPublisher2.library.compatibility.deprecation import deprecated_method

from storage import StoragePluginBase


# ==============================================================================
# Module Exports

__all__ = [
    'LegacyStoragePlugin',
]


# ============================================================================
# Legacy Storage Plugin Base

class LegacyStoragePlugin(LegacyPluginBase, StoragePluginBase):
    """Legacy Storage Plugin Base"""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # !TXT!

    isZMP2StoragePlugin = 1

    # ------------------------------------------------------------------------
    # Plugin Identity API

    getStorageObject = StoragePluginBase.get_plugin_instance

    getStorageId = StoragePluginBase.get_plugin_id

    getStorageURL = StoragePluginBase.get_plugin_url

    # ------------------------------------------------------------------------
    # !TXT!

    def get_immutable_pluginflag_ids(self):
        """Return list of Plugin flag ids, which are either constants or set by an external source and may not be altered by MetaPublisher2 or its users"""

        # !!! bases/storage/legacystorage.py -  get_immutable_pluginflag_ids
        return []

    def get_mutable_pluginflag_ids(self):
        """Return list of Plugin flag ids, which may be altered by MetaPublisher2 and its users"""

        # !!! bases/storage/legacystorage.py -  get_mutable_pluginflag_ids
        return []

    # ------------------------------------------------------------------------
    # !TXT!

    def all_meta_types(self, interfaces=None):

        result = StoragePluginBase.all_meta_types(interfaces)
        for product in Products.meta_types:
            if product.get('visibility', None) == 'ZMP2FieldPlugin' and not(product in result):
                result.append(product)
        return result

    # ------------------------------------------------------------------------
    # Storage Configuration

    manage_configureStorageForm = DTMLFile('storageplugin_edit', globals())

    def manage_configureStorage(self, REQUEST=None):
        """Change Storage's configuration parameters"""

        self.title = REQUEST.get('title', '')

        self.redirect(REQUEST, 'storages_form', 'Changes saved')

    def storage_getOptions(self):
        """Return a list of the Storage's configuration parameters"""

        raise NotImplementedError

    # ------------------------------------------------------------------------
    # Entry Retrieval

    def storage_entryIds(self):
        """Return ids of Entries of the specified Storage"""

        raise NotImplementedError

    def storage_entryItems(self):
        """Return tuples of id, value of Entries of the specified Storage"""

        raise NotImplementedError

    def storage_entryValues(self):
        """Return values of Entries of the specified Storage"""

        raise NotImplementedError

    def storage_getEntry(self, entry_id):
        """Return the specified Entry as a mapping object"""

        raise NotImplementedError

    # ------------------------------------------------------------------------
    # Entry Mutation

    def storage_addEntry(self, entry_id, data):
        """Add a new Entry in the specified Storage"""

        raise NotImplementedError

    def storage_delEntry(self, entry_id):
        """Delete an Entry from the specified Storage"""

        raise NotImplementedError

    def storage_delEntries(self, entry_ids=[]):
        """Delete Entries from the specified Storage"""

        raise NotImplementedError

    def storage_editEntry(self, entry_id, data):
        """Edit an Entry of the specified Storage"""

        raise NotImplementedError

    def storage_renameEntry(self, entry_id, new_id):
        """Rename an Entry"""

        raise NotImplementedError

    # --------------------------------------------------------------------------
    # EntryFields

    def storage_getEntryField(self, entry_id, field_id, default=None):
        """Return the specified Entry's Field's value"""

        raise NotImplementedError

    def storage_setEntryField(self, entry_id, field_id, value):
        """Set the specified Entry's Field's value"""

        raise NotImplementedError

    # --------------------------------------------------------------------------
    # EntryOrder

    def storage_getEntryPosition(self, entry_id):
        """Return the position of an Entry"""

        raise NotImplementedError

    def storage_moveEntryToPosition(self, entry_id, position):
        """Move an Entry to the specified position"""

        raise NotImplementedError

    def storage_moveEntryTop(self, entry_id):
        """Move an Entry to the top"""

        raise NotImplementedError

    def storage_moveEntryUp(self, entry_id):
        """Move an Entry up one position"""

        raise NotImplementedError

    def storage_moveEntryDown(self, entry_id):
        """Move an Entry down one position"""

        raise NotImplementedError

    def storage_moveEntryBottom(self, entry_id):
        """Move an Entry to the bottom"""

        raise NotImplementedError

    # ------------------------------------------------------------------------
    # Storage Mutation API

    def add_storage(self, options):
        """!TXT!"""

        deprecated_method('')

        # DEVELOPER: IMPORTANT - add_storage !TXT! - maybe auto set properties as placeholder
        pass

    def edit_storage(self, options):
        """!TXT!"""

        deprecated_method('')

        # DEVELOPER: IMPORTANT - edit_storage !TXT!  - maybe auto set properties as placeholder
        pass

    def before_duplicate(self, new_id):
        """!TXT!"""

        deprecated_method('')

        # DEVELOPER: OPTIONAL - before_duplicate !TXT!
        pass

    def after_duplicate(self, old_id):
        """!TXT!"""

        deprecated_method('')

        # DEVELOPER: OPTIONAL - after_duplicate !TXT!
        pass

    def before_rename(self, new_id):
        """!TXT!"""

        deprecated_method('')

        # DEVELOPER: OPTIONAL - before_rename !TXT!
        pass

    def after_rename(self, old_id):
        """!TXT!"""

        deprecated_method('')

        # DEVELOPER: OPTIONAL - after_rename !TXT!
        pass

    def before_delete(self):
        """!TXT!"""

        deprecated_method('')

        # DEVELOPER: OPTIONAL - before_delete !TXT!
        pass

    # ------------------------------------------------------------------------
    # Identifiers Retrieval API

    def last_entry_id(self):
        """!TXT!"""

        deprecated_method('')

        #  last_entry_id - read last entry id from property
        pass

    def new_entry_id(self):
        """!TXT!"""

        deprecated_method('')

        #  new_entry_id - create temporary solution (code exists), store in property for last_entry_id
        pass

    # ------------------------------------------------------------------------
    # Fields Retrieval API

    def count_fields(self):
        """!TXT!"""

        return len(self.field_ids())

    def field_ids(self):
        """!TXT!"""

        deprecated_method('storage_fieldIds')
        return self.storage_fieldIds()

    def storage_fieldIds(self):
        """Return ids of Fields of the specified Storage"""

        raise NotImplementedError

    def field_items(self):
        """!TXT!"""

        deprecated_method('storage_fieldItems')
        return self.storage_fieldItems()

    def storage_fieldItems(self):
        """Return tuples of id, value of Fields of the specified Storage"""

        raise NotImplementedError

    def field_values(self):
        """!TXT!"""

        deprecated_method('storage_fieldValues')
        return self.storage_fieldValues()

    def storage_fieldValues(self):
        """Return values of Fields of the specified Storage"""

        raise NotImplementedError

    def get_field(self, field_id):
        """!TXT!"""

        deprecated_method('storage_getField')
        return self.storage_getField(field_id)

    def storage_getField(self, field_id):
        """Return the specified Field of the Storage"""

        raise NotImplementedError

    def get_field_default(self, field_id):
        """!TXT!"""

        try:
            field = self.get_field(field_id)
            return field.default
        except:
            return None

    def has_all_fields(self, field_ids=None, field_types=None):
        """!TXT!"""

        deprecated_method('')

        pass

    def has_any_fields(self, field_ids=None, field_types=None):
        """!TXT!"""

        deprecated_method('')

        pass

    def has_field(self, field_id):
        """!TXT!"""

        if field_id in self.field_ids():
            return true
        return false

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

        deprecated_method('storage_delField')
        self.storage_delField(field_id)

    def storage_delField(self, field_id):
        """Delete the specified Field from the Storage"""

        raise NotImplementedError

    def delete_fields(self, field_ids):
        """!TXT!"""

        deprecated_method('storage_delFields')
        self.storage_delFields(field_ids)

    def storage_delFields(self, field_id=[]):
        """Delete the specified Fields from the Storage"""

        raise NotImplementedError

    def duplicate_field(self, field_id, new_id):
        """!TXT!"""

        deprecated_method('')
        pass

    def duplicate_fields(self, field_ids, new_ids):
        """!TXT!"""

        deprecated_method('')
        pass

    def edit_field(self, field_id, options):
        """!TXT!"""

        deprecated_method('')
        pass

    def rename_field(self, field_id, new_id):
        """!TXT!"""

        deprecated_method('storage_renameField')
        self.storage_renameField(field_id, new_id)

    def storage_renameField(self, field_id, new_id):
        """Rename a Field"""

        raise NotImplementedError

    def rename_fields(self, field_ids, new_ids):
        """!TXT!"""

        rename_field = self._rename_field
        for index in range(len(self.field_ids())):
            rename_field(field_ids[index], new_ids[index])

    def set_field_default(self, field_id, value):
        """!TXT!"""

        deprecated_method('')

        pass

    # ------------------------------------------------------------------------
    # Primary Field API

    def is_primary_field(self, field_id):
        """!TXT!"""

        deprecated_method('')
        pass

    def primary_field_ids(self):
        """!TXT!"""

        deprecated_method('')
        pass

    def primary_field_items(self):
        """!TXT!"""

        deprecated_method('')
        pass

    def primary_field_values(self):
        """!TXT!"""

        deprecated_method('')
        pass

    def set_primary_field(self, field_id):
        """!TXT!"""

        deprecated_method('')
        pass

    def unset_primary_field(self, field_id):
        """!TXT!"""

        deprecated_method('')
        pass

    # ------------------------------------------------------------------------
    # Field Ordering API

    def get_field_position(self, field_id):
        """!TXT!"""

        return self.field_ids().index(field_ids)

    def move_field_to_position(self, field_id, position):
        """!TXT!"""

        old_position = self.get_field_position(field_id)
        if old_position < position:
            method = self.move_field_up
        else:
            method = self.move_field_down
        for step in range(abs(position - old_position)):
            method(field_id)

    def move_field_to_top(self, field_id):
        """!TXT!"""

        deprecated_method('storage_moveFieldTop')
        self.storage_moveFieldTop(field_id)

    def storage_moveFieldTop(self, field_id):
        """Move a Field to the top"""

        raise NotImplementedError

    def move_field_up(self, field_id):
        """!TXT!"""

        deprecated_method('storage_moveFieldUp')
        self.storage_moveFieldUp(field_id)

    def storage_moveFieldUp(self, field_id):
        """Move a Field up one position"""

        raise NotImplementedError

    def move_field_down(self, field_id):
        """!TXT!"""

        deprecated_method('storage_moveFieldDown')
        self.storage_moveFieldDown(field_id)

    def storage_moveFieldDown(self, field_id):
        """Move a Field down one position"""

        raise NotImplementedError

    def move_field_to_bottom(self, field_id):
        """!TXT!"""

        deprecated_method('storage_moveFieldBottom')
        self.storage_moveFieldBottom(field_id)

    def storage_moveFieldBottom(self, field_id):
        """Move a Field to the bottom"""

        raise NotImplementedError

    # ------------------------------------------------------------------------
    # Storage Identity

    def get_storage(self):
        """!TXT! Return this instance"""

        deprecated_method('')
        return self.getStorageObject()

    def getStorageObject(self):
        """!TXT! Return this instance"""

        return self

    def get_storage_id(self):
        """!TXT! Return this instance's id"""

        deprecated_method('')
        return self.getStorageId()

    def getStorageId(self):
        """!TXT! Return this instance's id"""

        return self.getId()

    def get_storage_url(self):
        """!TXT! Return this instance's id"""

        deprecated_method('')
        return self.getStorageURL()

    def getStorageURL(self):
        """!TXT! Return this instance's absolute url"""

        return self.absolute_url()

    # ------------------------------------------------------------------------
    # Storage Configuration

    def get_storage_options(self):
        """Return a list of the Storage's configuration parameters"""

        deprecated_method('')
        return sef.storage_getOptions()

    def storage_getOptions(self):
        """Return a list of the Storage's configuration parameters"""

        raise NotImplementedError

    # ------------------------------------------------------------------------
    # Storage Ordering

    def get_storage_position(self):
        """!TXT! Return the position of this Storage"""

        deprecated_method('')
        return sef.getStoragePosition()

    def getStoragePosition(self):
        """!TXT! Return the position of this Storage"""

        return self.aq_parent.getObjectPosition(self.getId())

    position = ComputedAttribute(lambda self: self.getStoragePosition)

    # ------------------------------------------------------------------------
    # Storage ZMI

    manage_configureStorageForm = DTMLFile('dtml/storagesConfigure', globals())

    def manage_configureStorage(self, REQUEST=None):
        """!TXT! Change Storage's configuration parameters"""

        self.title = REQUEST.get('title', '')

        if REQUEST is not None:
            REQUEST.RESPONSE.redirect(self.get_MetaPublisher2_url() + '/manage_storagesBrowserForm?manage_tabs_message=Changes+saved')

    # ------------------------------------------------------------------------
    # Storage's Field Options

    # ------------------------------------------------------------------------
    # Storage's Field Retrieval

    def count_fields(self):
        """!TXT! Return the number of Fields in the Storage"""

        deprecated_method('')
        return sef.storage_countFields()

    def storage_countFields(self):
        """!TXT! Return the number of Fields in the Storage"""

        # OPTIONAL: overwrite this method for performance
        return len(self.storage_fieldIds())

    def get_field(self, fieldId):
        """!TXT! Return the specified Field of the Storage"""

        deprecated_method('')
        return sef.storage_getField()

    def storage_getField(self, fieldId):
        """!TXT! Return the specified Field of the Storage"""

        # REQUIRED: This method must be overwritten
        raise NotImplementedError

    def get_field_default(self, fieldId):
        """!TXT! Return the specified Field's default value of the Storage"""

        deprecated_method('')
        return sef.storage_getFieldDefault()

    def storage_getFieldDefault(self, fieldId):
        """!TXT! Return the specified Field's default value of the Storage"""

        # REQUIRED: This method must be overwritten
        raise NotImplementedError

    def has_field(self, fieldId):
        """!TXT! Return the specified Field's default value of the Storage"""

        deprecated_method('')

    def has_fields(self):
        """!TXT! Return True if any Fields exist in the Storage"""

        deprecated_method('')

    def storage_hasFields(self):
        """!TXT! Return True if any Fields exist in the Storage"""

        # OPTIONAL: overwrite this method for performance
        return len(self.storage_fieldIds()) and true or false

    def field_ids(self):
        """!TXT! Return ids of Fields of the specified Storage"""

        deprecated_method('')

    def storage_fieldIds(self):
        """!TXT! Return ids of Fields of the specified Storage"""

        # REQUIRED: Either overwrite this method or storage_fieldItems
        return map(lambda item: item[0], self.storage_fieldItems())

    def field_items(self):
        """!TXT! Return tuples of id, value of Fields of the specified Storage"""

        deprecated_method('')

    def storage_fieldItems(self):
        """!TXT! Return tuples of id, value of Fields of the specified Storage"""

        # REQUIRED: Either overwrite this method or storage_fieldItems
        get_field = self.storage_getField
        return map(lambda id: (id, get_field(id)), self.storage_fieldIds())

    def field_values(self):
        """!TXT! Return values of Fields of the specified Storage"""

        deprecated_method('')

    def storage_fieldValues(self):
        """!TXT! Return values of Fields of the specified Storage"""

        # OPTIONAL: overwrite this method for performance
        get_field = self.storage_getField
        return map(lambda id: get_field(id), self.storage_fieldIds())

    # ------------------------------------------------------------------------
    # Storage's Field Mutation

    def storage_delField(self, fieldId):
        """!TXT! Delete the specified Field from the Storage"""

        raise NotImplementedError

    def storage_delFields(self, fieldId=[]):
        """!TXT! Delete the specified Fields from the Storage"""

        raise NotImplementedError

    def storage_renameField(self, fieldId, newId):
        """!TXT! Rename a Field"""

        raise NotImplementedError

    # ------------------------------------------------------------------------
    # Storage's Field Ordering

    def storage_moveField(self, fieldId, position):
        """!TXT! Move a Field"""

        raise NotImplementedError

    def storage_moveFieldTop(self, fieldId):
        """!TXT! Move a Field to the top"""

        raise NotImplementedError

    def storage_moveFieldUp(self, fieldId):
        """!TXT! Move a Field up one position"""

        raise NotImplementedError

    def storage_moveFieldDown(self, fieldId):
        """!TXT! Move a Field down one position"""

        raise NotImplementedError

    def storage_moveFieldBottom(self, fieldId):
        """!TXT! Move a Field to the bottom"""

        raise NotImplementedError

    # ------------------------------------------------------------------------
    # Storage's Entry Retrieval

    def storage_countEntries(self):
        """!TXT! Return the number of Entries of the specified Storage"""

        # OPTIONAL: overwrite this method for performance
        return len(self.storage_entryIds())

    def storage_getEntry(self, entryId):
        """!TXT! Return the specified Entry as a mapping object"""

        # REQUIRED: This method must be overwritten
        raise NotImplementedError

    def storage_hasEntry(self, entryId):
        """!TXT!"""

        # OPTIONAL: overwrite this method for performance
        return entryId in self.storage_entryIds() and true or false

    def storage_hasEntries(self):
        """!TXT!"""

        # OPTIONAL: overwrite this method for performance
        return self.storage_entryIds() and true or false

    def storage_entryIds(self):
        """!TXT! Return ids of Entries of the specified Storage"""

        # REQUIRED: Either overwrite this method or storage_entryItems
        return map(lambda item: item[0], self.storage_entryItems())

    def storage_entryItems(self):
        """!TXT! Return tuples of id, value of Entries of the specified Storage"""

        # REQUIRED: Either overwrite this method or storage_entryIds
        get_entry = self.storage_getEntry
        return map(lambda id: (id, get_entry(id)), self.storage_entryIds())

    def storage_entryValues(self):
        """!TXT! Return values of Entries of the specified Storage"""

        # OPTIONAL: overwrite this method for performance
        get_entry = self.storage_getEntry
        return map(lambda id: get_entry(id), self.storage_entryIds())

    # ------------------------------------------------------------------------
    # Storage's Entry Mutation

    def storage_addEntry(self, entryId, data):
        """!TXT! Add a new Entry in the specified Storage"""

        raise NotImplementedError

    def storage_delEntry(self, entryId):
        """!TXT! Delete an Entry from the specified Storage"""

        raise NotImplementedError

    def storage_delEntries(self, entryids=[]):
        """!TXT! Delete Entries from the specified Storage"""

        raise NotImplementedError

    def storage_duplicateEntry(self, entryId, newId):
        """!TXT! Duplicate an Entry"""

        raise NotImplementedError

    def storage_duplicateEntries(self, entryIds, newIds):
        """!TXT! Duplicate an Entry"""

        raise NotImplementedError

    def storage_editEntry(self, entryId, data):
        """!TXT! Edit an Entry of the specified Storage"""

        raise NotImplementedError

    def storage_renameEntry(self, entryId, newId):
        """!TXT! Rename an Entry"""

        raise NotImplementedError

    def storage_renameEntries(self, entryIds, newIds):
        """!TXT! Rename an Entry"""

        raise NotImplementedError

    def storage_resetEntry(self, entryId):
        """!TXT! Reset an Entry"""

        raise NotImplementedError

    def storage_resetEntries(self, entryIds):
        """!TXT! Reset an Entry"""

        raise NotImplementedError

    # ------------------------------------------------------------------------
    # Storage's Entry Ordering

    def storage_getEntryPosition(self, entry_id):
        """!TXT! Return the position of an Entry"""

        raise NotImplementedError

    def storage_moveEntryToPosition(self, entry_id, position):
        """!TXT! Move an Entry to the specified position"""

        raise NotImplementedError

    def storage_moveEntryTop(self, entry_id):
        """!TXT! Move an Entry to the top"""

        raise NotImplementedError

    def storage_moveEntryUp(self, entry_id):
        """!TXT! Move an Entry up one position"""

        raise NotImplementedError

    def storage_moveEntryDown(self, entry_id):
        """!TXT! Move an Entry down one position"""

        raise NotImplementedError

    def storage_moveEntryBottom(self, entry_id):
        """!TXT! Move an Entry to the bottom"""

        raise NotImplementedError

    # ------------------------------------------------------------------------
    # Storage's EntryField Retrieval

    def storage_getEntryField(self, entry_id, field_id, default=None):
        """!TXT! Return the specified Entry's Field's value"""

        # REQUIRED: This method must be overwritten
        raise NotImplementedError

    def storage_getEntryFields(self, entry_ids, field_id, default=None):
        """!TXT! Return the specified Entries' Field values"""

        # OPTIONAL: overwrite this method for performance
        get_entryfield = self.storage_getEntryField
        return map(lambda id: (id, get_entryfield(id, field_id, default)), entryIds)

    def storage_getEntryFieldsMapping(self, entry_ids, field_id, default=None):
        """!TXT! Return the specified Entries' Field values as a mapping"""

        # OPTIONAL: overwrite this method for performance
        return dict(self.storage_getEntryFields(entryIds, field_id, default))

    def storage_countEntryFields(self, entry_ids, field_id, value):
        """!TXT! Return the number of occurances of a Field's value"""

        # OPTIONAL: overwrite this method for performance
        return self.storage_countUniqueEntryFields(entry_ids, field_id)[value]

    def storage_countUniqueEntryFields(self, entry_ids, field_id, default=None):
        """!TXT! Return the specified Entries' Field's unique values' number of occurances"""

        # OPTIONAL: overwrite this method for performance
        return dict(Counter(self.storage_countEntryFields(entry_ids, field_id, default)))

    def storage_getUniqueEntryFields(self, entry_ids, field_id, default=None):
        """!TXT! Return the specified Entries' Field's unique values"""

        # OPTIONAL: overwrite this method for performance
        return list(Counter(self.storage_getEntryFields(entry_ids, field_id, default)))

    def storage_hasEntryField(self, entry_ids, field_id, value):
        """!TXT! Return True if the specified Field's value exists"""

        # OPTIONAL: overwrite this method for performance
        return self.storage_countUniqueEntryFields(entry_ids, field_id)[value] and true or false

    # ------------------------------------------------------------------------
    # Storage's EntryField Mutation

    def storage_resetEntryField(self, entry_id, field_id):
        """!TXT! Set the specified Entry's Field's value"""

        # OPTIONAL: overwrite this method for performance
        self.storage_setEntryField(entry_id, field_id, self.storage_getFieldDefault(field_id))

    def storage_resetEntryFields(self, entry_ids, field_id):
        """!TXT! Set the specified Entry's Field's value"""

        # OPTIONAL: overwrite this method for performance
        self.storage_setEntryFields(entry_ids, field_id, self.self.storage_getFieldDefault(field_id))

    def storage_setEntryField(self, entry_id, field_id, value):
        """!TXT! Set the specified Entry's Field's value"""

        # REQUIRED: This method must be overwritten
        raise NotImplementedError

    def storage_setEntryFields(self, entry_ids, field_id, value):
        """!TXT! Set the specified Entry's Field's value"""

        set_entryfield = self.storage_setEntryField
        for id in entry_ids:
            set_entryfield(id, field_id, value)

# ----------------------------------------------------------------------------
# initialize class security

InitializeClass(LegacyStoragePlugin)

# !!! bases/storage/legacystorage.py - revise and update legacy api
