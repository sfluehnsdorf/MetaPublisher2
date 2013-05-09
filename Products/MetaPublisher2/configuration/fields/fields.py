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

__doc__ = """Fields Component

API and ZMI services for managing Fields. A Field is the configuration for a
single data element, stored in a Storage. A list of Fields make up the full
definition of the data stored in an Entry. Each Field represents a data type,
such as text, numbers, images, files, etc. Fields can be added, edited, renamed,
deleted and ordered as well as retrieved, listed and tested for existence.

$Id: configuration/fields/fields.py 16 2013-05-09 00:05:01Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.interfaces import IFieldPluginBase
from Products.MetaPublisher2.library import ClassSecurityInfo, DTMLFile, InitializeClass, permission_access_configuration, permission_change_configuration, permission_manage


# ============================================================================
# Module Exports

__all__ = [
    'Fields',
]


# ============================================================================
# Fields Component Mix-In Class

class Fields:
    """!TXT! Fields Component Mix-In Class"""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # Field ZMI Forms

    security.declareProtected(permission_access_configuration, 'fields_form')

    fields_form = DTMLFile('fields', globals())

    security.declareProtected(permission_access_configuration, 'add_field_form')

    add_field_form = DTMLFile('fields_add', globals())

    security.declareProtected(permission_access_configuration, 'delete_fields_form')

    delete_fields_form = DTMLFile('delete_fields', globals())

    security.declareProtected(permission_access_configuration, 'duplicate_fields_form')

    duplicate_fields_form = DTMLFile('duplicate_fields', globals())

    security.declareProtected(permission_access_configuration, 'change_field_type_form')

    change_field_type_form = DTMLFile('change_field_type', globals())

    security.declareProtected(permission_access_configuration, 'edit_field_form')

    edit_field_form = DTMLFile('edit_field', globals())

    security.declareProtected(permission_access_configuration, 'rename_fields_form')

    rename_fields_form = DTMLFile('rename_fields', globals())

    # ------------------------------------------------------------------------
    # Field Plugins

    security.declareProtected(permission_manage, 'has_fieldplugins')

    def has_fieldplugins(self):
        """!TXT! Return the specified MetaPublisher2 Field plugin"""

        return self.has_plugins(IFieldPluginBase)

    security.declareProtected(permission_manage, 'get_fieldplugin')

    def get_fieldplugin(self, fieldplugin_id):
        """!TXT! Return the specified MetaPublisher2 Field plugin"""

        return self.get_plugin(fieldplugin_id, IFieldPluginBase)

    security.declareProtected(permission_manage, 'fieldplugin_ids')

    def fieldplugin_ids(self):
        """!TXT! Return ids of installed MetaPublisher2 Field plugins"""

        return self.plugin_ids(IFieldPluginBase)

    security.declareProtected(permission_manage, 'fieldplugin_items')

    def fieldplugin_items(self):
        """!TXT! Return tuples of id, value of installed MetaPublisher2 Field plugins"""

        return self.plugin_items(IFieldPluginBase)

    security.declareProtected(permission_manage, 'fieldplugin_values')

    def fieldplugin_values(self):
        """!TXT! Return tuples of id, value of installed MetaPublisher2 Field plugins"""

        return self.plugin_values(IFieldPluginBase)

    # ------------------------------------------------------------------------
    # Field Flag Retrieval

    security.declareProtected(permission_manage, 'get_fieldflags')

    def get_fieldflags(self, storage_id, field_id):
        """!TXT! Return tuples of id, boolean states of all Plugin flags"""

        field = self.get_field(storage_id, field_id)
        return field.get_pluginflag()

    security.declareProtected(permission_manage, 'get_fieldflag_ids')

    def get_fieldflag_ids(self, storage_id, field_id):
        """!TXT! Return the ids of all Plugin flags"""

        field = self.get_field(storage_id, field_id)
        return field.get_pluginflag_ids()

    security.declareProtected(permission_manage, 'get_fieldflag')

    def get_fieldflag(self, storage_id, field_id, pluginflag_id):
        """!TXT! Return the boolean state of the specified Design flag if it exists, raises KeyError otherwise"""

        field = self.get_field(storage_id, field_id)
        return field.get_pluginflag(pluginflag_id)

    security.declareProtected(permission_manage, 'has_fieldflag')

    def has_fieldflag(self, storage_id, field_id, pluginflag_id):
        """!TXT! Return True if the Design flag exists, False otherwise"""

        field = self.get_field(storage_id, field_id)
        return field.has_pluginflag(pluginflag_id)

    # ------------------------------------------------------------------------
    # Fields Retrieval API

    security.declareProtected(permission_access_configuration, 'count_fields')

    def count_fields(self, storage_id):
        """!TXT! Return the number of Fields of the specified Storage"""

        storage = self.get_storage(storage_id)
        return storage.count_fields()

    security.declareProtected(permission_access_configuration, 'field_ids')

    def field_ids(self, storage_id):
        """!TXT! Return the ids of the specified Storage's Fields."""

        storage = self.get_storage(storage_id)
        return storage.field_ids()

    security.declareProtected(permission_access_configuration, 'field_items')

    def field_items(self, storage_id):
        """!TXT! Return tuples of id, object of the specified Storage's Fields."""

        storage = self.get_storage(storage_id)
        return storage.field_items()

    security.declareProtected(permission_access_configuration, 'field_values')

    def field_values(self, storage_id):
        """!TXT! Return the objects of the specified Storage's Fields."""

        storage = self.get_storage(storage_id)
        return storage.field_values()

    security.declareProtected(permission_access_configuration, 'get_field')

    def get_field(self, storage_id, field_id):
        """!TXT! Return the specified Storage's Field."""

        storage = self.get_storage(storage_id)
        return storage.get_field(field_id)

    security.declareProtected(permission_access_configuration, 'get_field_default')

    def get_field_default(self, storage_id, field_id):
        """!TXT! Return the default value of the specified Storage's Field."""

        storage = self.get_storage(storage_id)
        return storage.get_field_default(field_id)

    security.declareProtected(permission_access_configuration, 'has_all_fields')

    def has_all_fields(self, storage_id, field_ids=None, field_types=None):
        """!TXT! Return True if all of the specified Storage's Fields exist, limited to Field Types if specified. If no Fields are specified, checks if all Fields are of the specified Field Types."""

        storage = self.get_storage(storage_id)
        return storage.has_all_fields(field_ids, field_types)

    security.declareProtected(permission_access_configuration, 'has_any_fields')

    def has_any_fields(self, storage_id, field_ids=None, field_types=None):
        """!TXT! Return True if any of the specified Storage's Fields exist, limited to Field Types if specified. If no Fields are specified, checks if any Fields are of the specified Field Types."""

        storage = self.get_storage(storage_id)
        return storage.has_any_fields(field_ids, field_types)

    security.declareProtected(permission_access_configuration, 'has_field')

    def has_field(self, storage_id, field_id):
        """!TXT! Return True if the specified Storage's Field exists."""

        storage = self.get_storage(storage_id)
        return storage.has_field(field_id)

    # ------------------------------------------------------------------------
    # Fields Mutation API

    security.declareProtected(permission_change_configuration, 'add_field_type')

    def add_field_type(self, storage_id, field_type, REQUEST=None):
        """!TXT!"""

        try:
            fieldplugin = self.get_plugin(field_type)
            REQUEST.RESPONSE.redirect('%s/%s/%s' % (
                self.get_MetaPublisher2_url(),
                storage_id,
                fieldplugin['action']
            ))
        except:
            self.redirect(REQUEST, 'fields_form', '!TXT! Field type "%s" is invalid.' % REQUEST.get('storageType', None))

    security.declareProtected(permission_change_configuration, 'add_field')

    def add_field(self, storage_id, field_id, field_type_id, options={}, REQUEST=None, **args):
        """!TXT! Add a new Field of the specified type in the specified Storage with specified id and configuration."""

        options.update(args)
        if REQUEST:
            options.update(REQUEST.form)

        storage = self.get_storage(storage_id)
        storage.before_add_field(field_id, field_type_id, options)

        plugin = self.get_plugin(field_type_id)
        plugin_instance = plugin['instance']
        field = plugin_instance(field_id)
        storage._setObject(field_id, field)

        field = storage._getOb(field_id)
        field.add_field(options)

        storage.after_add_field(field_id, field_type_id, options)

        self.redirect(REQUEST, 'fields_form', '!TXT! Field "%s" of type "%s" added to Storage "%s".' % (field_id, field_type_id, storage_id))

    security.declareProtected(permission_change_configuration, 'delete_field')

    def delete_field(self, storage_id, field_id, REQUEST=None):
        """!TXT! Delete the specified Storage's Field."""

        storage = self.get_storage(storage_id)
        storage.delete_field(field_id)

        self.redirect(REQUEST, 'fields_form', '!TXT! Field "%s" in Storage "%s" deleted.' % (field_id, storage_id))

    security.declareProtected(permission_change_configuration, 'delete_fields')

    def delete_fields(self, storage_id, field_ids=[], REQUEST=None):
        """!TXT! Delete the specified Storage's Fields."""

        storage = self.get_storage(storage_id)
        storage.delete_fields(field_ids)

        self.redirect(REQUEST, 'fields_form', '!TXT! %d Fields deleted from Storage "%s".' % (len(field_ids), storage_id))

    security.declareProtected(permission_change_configuration, 'duplicate_field')

    def duplicate_field(self, storage_id, field_id, new_id, REQUEST=None):
        """!TXT! Duplicate the specified Storage's Field."""

        storage = self.get_storage(storage_id)
        storage.duplicate_field(field_id, new_id)

        self.redirect(REQUEST, 'fields_form', '!TXT! Field "%s" in Storage "%s" duplicated as "%s".' % (field_id, storage_id, new_id))

    security.declareProtected(permission_change_configuration, 'duplicate_fields')

    def duplicate_fields(self, storage_id, field_ids=[], new_ids=[], REQUEST=None):
        """!TXT! Duplicate the specified Storage's Fields."""

        storage = self.get_storage(storage_id)
        storage.duplicate_fields(field_ids, new_ids)

        self.redirect(REQUEST, 'fields_form', '!TXT! %d Fields in Storage "%s" duplicated .' % (len(field_ids), storage_id))

    security.declareProtected(permission_change_configuration, 'edit_field')

    def edit_field(self, storage_id, field_id, options={}, REQUEST=None, **args):
        """!TXT! Change the specified Storage's Field's configuration."""

        options.update(args)
        if REQUEST:
            options.update(REQUEST.form)

        storage = self.get_storage(storage_id)
        storage.edit_field(field_id, options)

        self.redirect(REQUEST, 'fields_form', '!TXT! Field "%s" in Storage "%s" edited.' % (field_id, storage_id))

    security.declareProtected(permission_change_configuration, 'rename_field')

    def rename_field(self, storage_id, field_id, new_id, REQUEST=None):
        """!TXT! Rename the specified Storage's Field."""

        storage = self.get_storage(storage_id)
        storage.rename_field(field_id, new_id)

        self.redirect(REQUEST, 'fields_form', '!TXT! Field "%s" in Storage "%s" renamed to "%s".' % (field_id, storage_id, new_id))

    security.declareProtected(permission_change_configuration, 'rename_fields')

    def rename_fields(self, storage_id, field_ids, new_ids):
        """!TXT! Rename the specified Storage's Fields."""

        storage = self.get_storage(storage_id)
        storage.rename_fields(field_ids, new_ids)

        self.redirect(REQUEST, 'fields_form', '!TXT! %d Fields in Storage "%s" renamed.' % (len(field_ids), storage_id))

    security.declareProtected(permission_access_configuration, 'set_field_default')

    def set_field_default(self, storage_id, field_id, value):
        """!TXT! Set the default value of the specified Storage's Field."""

        storage = self.get_storage(storage_id)
        storage.set_field_default(field_id, value)

        self.redirect(REQUEST, 'fields_form', '!TXT! Default value of Field "%s" in Storage "%s" changed.' % (field_id, storage_id))

    # ------------------------------------------------------------------------
    # Primary Field API

    security.declareProtected(permission_change_configuration, 'clear_primary_fields')

    def clear_primary_fields(self, storage_id):
        """!TXT! Set all primary Storage's Fields to non-primary."""

        unset_primary_field = self.unset_primary_field
        for field_id in self.primary_field_ids(storage_id):
            unset_primary_field(storage_id, field_id)

    security.declareProtected(permission_access_configuration, 'is_primary_field')

    def is_primary_field(self, storage_id, field_id):
        """!TXT! Return True if the specified Storage's Field is primary, False otherwise."""

        storage = self.get_storage(storage_id)
        return storage.is_primary_field(field_id)

    security.declareProtected(permission_access_configuration, 'primary_field_ids')

    def primary_field_ids(self, storage_id):
        """!TXT! Return the ids of the specified Storage's primary Fields."""

        storage = self.get_storage(storage_id)
        return storage.primary_field_ids()

    security.declareProtected(permission_access_configuration, 'primary_field_items')

    def primary_field_items(self, storage_id):
        """!TXT! Return tuples of id, value of the specified Storage's primary Fields."""

        storage = self.get_storage(storage_id)
        return storage.primary_field_items()

    security.declareProtected(permission_access_configuration, 'primary_field_values')

    def primary_field_values(self, storage_id):
        """!TXT! Return the values of the specified Storage's primary Fields."""

        storage = self.get_storage(storage_id)
        return storage.primary_field_values()

    security.declareProtected(permission_change_configuration, 'set_primary_field')

    def set_primary_field(self, storage_id, field_id):
        """!TXT! Set the specified Storage's Field to primary."""

        storage = self.get_storage(storage_id)
        storage.set_primary_field(field_id)

    security.declareProtected(permission_change_configuration, 'set_primary_fields')

    def set_primary_fields(self, storage_id, field_ids=[]):
        """!TXT! Set all specified Storage's Fields to primary."""

        set_primary_field = self.set_primary_field
        for field_id in field_ids:
            set_primary_field(storage_id, field_id)

    security.declareProtected(permission_change_configuration, 'unset_primary_field')

    def unset_primary_field(self, storage_id, field_id):
        """!TXT! Set the specified Storage's Fields to non-primary."""

        storage = self.get_storage(storage_id)
        storage.unset_primary_field(field_id)

    security.declareProtected(permission_change_configuration, 'unset_primary_fields')

    def unset_primary_fields(self, storage_id, field_ids=[]):
        """!TXT! Set all specified Storage's Fields to non-primary."""

        unset_primary_field = self.unset_primary_field
        for field_id in field_ids:
            unset_primary_field(storage_id, field_id)

    # ------------------------------------------------------------------------
    # Field Ordering API

    # !!! fields.py - implement are_fields_sortable OR use flags

    security.declareProtected(permission_access_configuration, 'get_field_position')

    def get_field_position(self, storage_id, field_id):
        """!TXT! Return the position of an the specified Storage's Field."""

        storage = self.get_storage(storage_id)
        return storage.get_field_position(field_id)

    security.declareProtected(permission_change_configuration, 'move_field_to_position')

    def move_field_to_position(self, storage_id, field_id, position, REQUEST=None):
        """!TXT! Move the specified Storage's Field to the specified position."""

        storage = self.get_storage(storage_id)
        storage.move_field_to_position(field_id, position)

        self.redirect(REQUEST, 'fields_form', '!TXT! Field "%s" in Storage "%s" moved to position %d.' % (field_id, storage_id, position))

    security.declareProtected(permission_change_configuration, 'move_field_to_top')

    def move_field_to_top(self, storage_id, field_id, REQUEST=None):
        """!TXT! Move the specified Storage's Field to the top."""

        storage = self.get_storage(storage_id)
        storage.move_field_to_top(field_id)

        self.redirect(REQUEST, 'fields_form', '!TXT! Field "%s" in Storage "%s" moved to top.' % (field_id, storage_id))

    security.declareProtected(permission_change_configuration, 'move_field_up')

    def move_field_up(self, storage_id, field_id, REQUEST=None):
        """!TXT! Move the specified Storage's Field up one position."""

        storage = self.get_storage(storage_id)
        storage.move_field_up(field_id)

        self.redirect(REQUEST, 'fields_form', '!TXT! Field "%s" in Storage "%s" moved up.' % (field_id, storage_id))

    security.declareProtected(permission_change_configuration, 'move_field_down')

    def move_field_down(self, storage_id, field_id, REQUEST=None):
        """!TXT! Move the specified Storage's Field down one position."""

        storage = self.get_storage(storage_id)
        storage.move_field_down(field_id)

        self.redirect(REQUEST, 'fields_form', '!TXT! Field "%s" in Storage "%s" moved down.' % (field_id, storage_id))

    security.declareProtected(permission_change_configuration, 'move_field_to_bottom')

    def move_field_to_bottom(self, storage_id, field_id, REQUEST=None):
        """!TXT! Move the specified Storage's Field to the bottom."""

        storage = self.get_storage(storage_id)
        storage.move_field_to_bottom(field_id)

        self.redirect(REQUEST, 'fields_form', '!TXT! Field "%s" in Storage "%s" moved to bottom.' % (field_id, storage_id))

    # !!! fields.py - implement move_fields_* methods

# ----------------------------------------------------------------------------
# Class Security

InitializeClass(Fields)

# !!! fields.py - form/formlet handler for add_field
# !!! fields.py - form/formlet handler for edit_field
# TODO fields.py - implement handling of grouped fields (field groups)
# TODO fields.py - implement handling of multi values fields
