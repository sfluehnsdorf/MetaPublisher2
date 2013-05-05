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

__doc__ = """Storages Component

API and ZMI services for managing Storages. Storages contain the definition for
the data source, the Fields defining the data elements that make up a single
data entry, and provide access to the Entries and EntryFields stored within the
Storage. A single Storage is a homogenous list of data, such as list of
addresses, news items or the slides of a slideshow. Storages can be added,
edited, renamed and deleted as well as retrieved, listed and tested for
existence.

$Id: configuration/storages/storages.py 19 2013-05-05 18:04:32Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.interfaces import IEntrySet, IStoragePluginBase
from Products.MetaPublisher2.library import ClassSecurityInfo, DTMLFile, InitializeClass, permission_access_configuration, permission_change_configuration, permission_manage, true, false


# ============================================================================
# Module Exports

__all__ = [
    'Storages',
]


# ============================================================================
class Storages:
    """Storages Mix-In Class"""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # Storage ZMI Forms

    security.declareProtected(permission_access_configuration, 'storages_form')

    storages_form = DTMLFile('storages', globals())

    security.declareProtected(permission_change_configuration, 'add_storage_form')

    add_storage_form = DTMLFile('add_storage', globals())

    security.declareProtected(permission_change_configuration, 'duplicate_storages_form')

    duplicate_storages_form = DTMLFile('duplicate_storages', globals())

    security.declareProtected(permission_change_configuration, 'delete_storages_form')

    delete_storages_form = DTMLFile('delete_storages', globals())

    security.declareProtected(permission_change_configuration, 'change_storage_type_form')

    change_storage_type_form = DTMLFile('change_storage_type', globals())

    security.declareProtected(permission_change_configuration, 'edit_storage_form')

    edit_storage_form = DTMLFile('edit_storage', globals())

    security.declareProtected(permission_change_configuration, 'rename_storages_form')

    rename_storages_form = DTMLFile('rename_storages', globals())

    # ------------------------------------------------------------------------
    # Storage Plugins

    security.declareProtected(permission_manage, 'has_storageplugins')

    def has_storageplugins(self):
        """Return the specified MetaPublisher2 Storage plugin"""

        return self.has_plugins(IStoragePluginBase)

    security.declareProtected(permission_manage, 'get_storageplugin')

    def get_storageplugin(self, storageplugin_id):
        """Return the specified MetaPublisher2 Storage plugin"""

        return self.get_plugin(storageplugin_id, IStoragePluginBase)

    security.declareProtected(permission_manage, 'storageplugin_ids')

    def storageplugin_ids(self):
        """Return ids of installed MetaPublisher2 Storage plugins"""

        return self.plugin_ids(IStoragePluginBase)

    security.declareProtected(permission_manage, 'storageplugin_items')

    def storageplugin_items(self):
        """Return tuples of id, value of installed MetaPublisher2 Storage plugins"""

        return self.plugin_items(IStoragePluginBase)

    security.declareProtected(permission_manage, 'storageplugin_values')

    def storageplugin_values(self):
        """Return tuples of id, value of installed MetaPublisher2 Storage plugins"""

        return self.plugin_values(IStoragePluginBases)

    # ------------------------------------------------------------------------
    # Storage Flag Retrieval

    security.declareProtected(permission_manage, 'get_storageflags')

    def get_storageflags(self, storage_id):
        """Return tuples of id, boolean states of all Plugin flags"""

        storage = get_storage(self, storage_id)
        return storage.get_pluginflag()

    security.declareProtected(permission_manage, 'get_storageflag_ids')

    def get_storageflag_ids(self, storage_id):
        """Return the ids of all Plugin flags"""

        storage = get_storage(self, storage_id)
        return storage.get_pluginflag_ids()

    security.declareProtected(permission_manage, 'get_storageflag')

    def get_storageflag(self, storage_id, pluginflag_id):
        """Return the boolean state of the specified Storage flag if it exists, raises KeyError otherwise"""

        storage = get_storage(self, storage_id)
        return storage.get_pluginflag(pluginflag_id)

    security.declareProtected(permission_manage, 'has_storageflag')

    def has_storageflag(self, storage_id, pluginflag_id):
        """Return True if the Storage flag exists, False otherwise"""

        storage = get_storage(self, storage_id)
        return storage.has_pluginflag(pluginflag_id)

    # ------------------------------------------------------------------------
    # Storage Retrieval API

    security.declareProtected(permission_access_configuration, 'count_storages')

    def count_storages(self):
        """Return the number of Storages."""

        return len(self.storage_ids())

    security.declareProtected(permission_access_configuration, 'get_storage')

    def get_storage(self, source):
        """Return the specified Storage. Source is either a Storage's id, a Storage or an EntrySet. Raises KeyError if no Storage can be returned."""

        if IStoragePluginBase.providedBy(source) or IEntrySet.providedBy(source):
            return source
        return self.get_storage_by_id(source)

    security.declareProtected(permission_access_configuration, 'get_storage_by_id')

    def get_storage_by_id(self, storage_id):
        """Return the specified Storage, raise KeyError otherwise."""

        storage = self._getOb(storage_id)
        if IStoragePluginBase.providedBy(storage):
            return storage
        raise KeyError('Storage "%s" not found.' % storage_id)

    security.declareProtected(permission_access_configuration, 'has_storage')

    def has_storage(self, storage_id):
        """Return True if the specified Storage exists."""

        return storage_id in self.storage_ids()

    security.declareProtected(permission_access_configuration, 'has_storages')

    def has_storages(self):
        """Return True if any Storages exist."""

        return self.storage_ids() and true or false

    security.declareProtected(permission_access_configuration, 'has_all_storages')

    def has_all_storages(self, storage_ids=None, storage_types=None):
        """Return True if all of the specified Storages exist, limited to Storage Types if specified. If no Storages are specified, checks if all Storages are of the specified Storage Types."""

        if storage_types is None:

            # check if any storages exist
            if storage_ids is None:
                return self.storage_ids() and true or false

            # check if all of the storages exist
            else:
                has_storage = self.has_storage
                for storage_id in storage_ids:
                    if not has_storage(storage_id):
                        return false
                return true

        else:

            # check if all of the storages are of the specified types
            if storage_ids is None:
                for storage in self.storage_values():
                    if not storage.meta_type in storage_types:
                        return false
                return true

            # check if all of the storages exist, limited to the specified types
            else:
                has_storage = self.has_storage
                get_storage = self.get_storage
                for storage_id in storage_ids:
                    if not(has_storage(storage_id) and get_storage(storage_id).meta_type in storage_types):
                        return false
                return true

        return false

    security.declareProtected(permission_access_configuration, 'has_any_storages')

    def has_any_storages(self, storage_ids=None, storage_types=None):
        """Return True if any of the specified Storages exist, limited to Storage Types if specified. If no Storages are specified, checks if any Storages are of the specified Storage Types."""

        if storage_types is None:

            # check if any storages exist
            if storage_ids is None:
                return self.storage_ids() and true or false

            # check if any of the storages exist
            else:
                has_storage = self.has_storage
                for storage_id in storage_ids:
                    if has_storage(storage_id):
                        return true

        else:

            # check if any of the storages are of the specified types
            if storage_ids is None:
                for storage in self.storage_values():
                    if storage.meta_type in storage_types:
                        return true

            # check if any of the storages exist, limited to the specified types
            else:
                has_storage = self.has_storage
                get_storage = self.get_storage
                for storage_id in storage_ids:
                    if has_storage(storage_id) and get_storage(storage_id).meta_type in storage_types:
                        return true

        return false

    security.declareProtected(permission_access_configuration, 'storage_ids')

    def storage_ids(self):
        """Return ids of Storages"""

        return map(lambda item: item[0], self.storage_items())

    security.declareProtected(permission_access_configuration, 'storage_items')

    def storage_items(self):
        """Return tuples of id, value of Storages"""

        result = []
        for id, object in self.objectItems():
            if IStoragePluginBase.providedBy(object):
                result.append((id, object))
        return result

    security.declareProtected(permission_access_configuration, 'storage_values')

    def storage_values(self):
        """Return values of Storages"""

        return map(lambda item: item[1], self.storage_items())

    # ------------------------------------------------------------------------
    # Storage Mutation API

    security.declareProtected(permission_change_configuration, 'add_storage_type')

    def add_storage_type(self, storage_type, REQUEST=None):
        """!TXT! add_storage_type"""

        try:
            storageplugin = self.get_plugin(storage_type)
            REQUEST.RESPONSE.redirect('%s/%s' % (
                self.get_MetaPublisher2_url(),
                storageplugin['action']
            ))
        except:
            self.redirect(REQUEST, 'storages_form', 'Storage type "%s" is invalid.' % REQUEST.get('storageType', None))

    security.declareProtected(permission_change_configuration, 'add_storage')

    def add_storage(self, storage_id, storage_type_id, options={}, REQUEST=None, **args):
        """Add a new Storage with specified id and configuration."""

        options.update(args)
        if REQUEST:
            options.update(REQUEST.form)

        plugin = self.get_plugin(storage_type_id)
        plugin_instance = plugin['instance']
        storage = plugin_instance(storage_id)
        self._setObject(storage_id, storage)

        storage = self._getOb(storage_id)
        storage.add_storage(options)

        self.redirect(REQUEST, 'storages_form', 'Storage "%s" added.' % storage_id)

    security.declareProtected(permission_change_configuration, 'delete_storage')

    def delete_storage(self, storage_id, REQUEST=None):
        """Delete the specified Storage."""

        storage = self.get_storage(storage_id)
        storage.before_delete()

        self.manage_delObjects([storage_id, ])

        self.redirect(REQUEST, 'storages_form', 'Storage "%s" deleted.' % storage_id)

    security.declareProtected(permission_change_configuration, 'delete_storages')

    def delete_storages(self, storage_ids=[], REQUEST=None):
        """Delete the specified Storages."""

        for storage_id in storage_ids:
            storage = self.get_storage(storage_id)
            storage.before_delete()

        for storage_id in storage_ids:
            self.manage_delObjects(storage_id)

        self.redirect(REQUEST, 'storages_form', '%d Storages deleted.' % len(ids))

    security.declareProtected(permission_change_configuration, 'duplicate_storage')

    def duplicate_storage(self, storage_id, new_id, REQUEST=None):
        """Duplicate the specified Storage."""

        storage = self.get_storage(storage_id)
        storage.before_duplicate(new_id)

        self.manage_duplicate(self._getOb(storage_id), new_id)

        storage = self.get_storage(new_id)
        storage.after_duplicate(storage_id)

        self.redirect(REQUEST, 'storages_form', 'Storage "%s" duplicated as "%s".' % (storage_id, new_id))

    security.declareProtected(permission_change_configuration, 'duplicate_storages')

    def duplicate_storages(self, storage_ids, new_ids, REQUEST=None):
        """Duplicate the specified Storages. Both id lists must have the same length or ValueError is raised."""

        if len(storage_ids) != len(new_ids):
            raise ValueError("Unmatched ids and new ids lists")

        for index in len(range(storage_ids)):
            storage = self.get_storage(new_ids[index])
            storage.before_duplicate(storage_ids[index], new_ids[index])

        for index in len(range(storage_ids)):
            self.manage_duplicate(self._getOb(storage_ids[index]), new_ids[index])

        for index in len(range(new_ids)):
            storage = self.get_storage(new_ids[index])
            storage.after_duplicate(storage_ids[index], new_ids[index])

        self.redirect(REQUEST, 'storages_form', '%d Storages duplicated.' % len(ids))

    security.declareProtected(permission_change_configuration, 'edit_storage')

    def edit_storage(self, storage_id, options={}, REQUEST=None, **args):
        """Change the specified Storage's configuration."""

        options.update(args)
        if REQUEST:
            options.update(REQUEST.form)
        storage = self.get_storage(storage_id)
        storage.edit_storage(options)

        self.redirect(REQUEST, 'storages_form', 'Storage "%s" edited.' % storage_id)

    security.declareProtected(permission_change_configuration, 'rename_storage')

    def rename_storage(self, storage_id, new_id, REQUEST=None):
        """Rename the specified Storage."""

        storage = self.get_storage(storage_id)
        storage.before_rename(storage_id, new_id)

        self.manage_renameObject(storage_id, new_id)

        storage = self.get_storage(new_id)
        storage.after_rename(storage_id, new_id)

        self.redirect(REQUEST, 'storages_form', 'Storage "%s" renamed to "%s".' % (storage_id, new_id))

    security.declareProtected(permission_change_configuration, 'rename_storages')

    def rename_storages(self, storage_ids, new_ids, REQUEST=None):
        """Rename the specified Storages. Both id lists must have the same length or ValueError is raised."""

        if len(storage_ids) != len(new_ids):
            raise ValueError("Unmatched ids and new ids lists")

        for index in len(range(storage_ids)):
            storage = self.get_storage(new_ids[index])
            storage.before_rename(new_ids[index])

        for index in len(range(storage_ids)):
            self.manage_renameObject(storage_ids[index], new_ids[index])

        for index in len(range(new_ids)):
            storage = self.get_storage(new_ids[index])
            storage.after_rename(storage_ids[index])

        self.redirect(REQUEST, 'storages_form', '%d Storages renamed.' % len(ids))

    # ------------------------------------------------------------------------
    # Storage Ordering API

    security.declareProtected(permission_access_configuration, 'get_storage_position')

    def get_storage_position(self, storage_id):
        """!TXT! Return the position of the specified Storage"""

        ids = self.storage_ids()
        return ids.index(storage_id)

    security.declareProtected(permission_change_configuration, 'move_storage')

    def move_storage(self, storage_id, position, REQUEST=None):
        """!TXT! Move the specified Storage to the specified position"""

        position = int(position)
        object_position = self.objectIds().index(self.storage_ids()[position])
        self.moveObjectToPosition(storage_id, object_position)
        self.redirect(
            REQUEST,
            'storages_form',
            message='Storage "%s" moved to position %d' % (storage_id, position + 1),
            update_menu=True,
        )

    security.declareProtected(permission_change_configuration, 'move_storage_to_top')

    def move_storage_to_top(self, storage_id, REQUEST=None):
        """!TXT! Move the specified Storage to the top"""

        self.move_storage(storage_id, 0)
        self.redirect(
            REQUEST,
            'storages_form',
            message='Storage "%s" moved to the top' % storage_id,
            update_menu=True,
        )

    security.declareProtected(permission_change_configuration, 'move_storage_up')

    def move_storage_up(self, storage_id, REQUEST=None):
        """!TXT! Move the specified Storage up one position"""

        self.move_storage(storage_id, self.get_storage_position(storage_id) - 1)
        self.redirect(
            REQUEST,
            'storages_form',
            message='Storage "%s" moved up' % storage_id,
            update_menu=True,
        )

    security.declareProtected(permission_change_configuration, 'move_storage_down')

    def move_storage_down(self, storage_id, REQUEST=None):
        """!TXT! Move the specified Storage down one position"""

        self.move_storage(storage_id, self.get_storage_position(storage_id) + 1)
        self.redirect(
            REQUEST,
            'storages_form',
            message='Storage "%s" moved down' % storage_id,
            update_menu=True,
        )

    security.declareProtected(permission_change_configuration, 'move_storage_to_bottom')

    def move_storage_to_bottom(self, storage_id, REQUEST=None):
        """!TXT! Move the specified Storage to the bottom"""

        self.move_storage(storage_id, len(self.objectIds()) - 1)
        self.redirect(
            REQUEST,
            'storages_form',
            message='Storage "%s" moved to the bottom' % storage_id,
            update_menu=True,
        )

    # !!! storages.py - implement move_storages_* methods

# ----------------------------------------------------------------------------
# Class Security

InitializeClass(Storages)

# !!! storages.py - form/formlet handler for add_storage
# !!! storages.py - form/formlet handler for edit_storage
# TODO storages.py - support other storage types: sequential, tree, unordered
# TODO storages.py - change_storage_type method
