"""==================================================================

                  M e t a   Z o p e   S t o r a g e
  -----------------------------------------------------------------

    Copyright (c) 2005, Sebastian Luehnsdorf - Web-Solutions GbR.
    http://zopemeta.com - http://luehnsdorf.de

    This software is subject to the provisions of the
    Zope Public License, Version 2.0 (ZPL).

    A copy of the ZPL should accompany this distribution.

    THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR
    IMPLIED WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED
    TO, THE IMPLIED WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST
    INFRINGEMENT, AND FITNESS FOR A PARTICULAR PURPOSE.

=================================================================="""

from Globals import DTMLFile
import Products

from Products.MetaPublisher2.Library import Folder, StoragePlugin


# =============================================================================


class MetaEntry(Folder):
    "Entry object, storing data using properties and objects"

    meta_type = 'MetaEntry'

    icon = 'misc_/MetaPublisher2/Entry.gif'


# =============================================================================

class MetaEntries(Folder):
    "Container for MetaEntries"

    meta_type = 'MetaEntries'

    icon = 'misc_/MetaPublisher2/Entries.gif'

    meta_types = ()

    # ---------------------------------------------------------------

    meta_types = ({
        'name': 'MetaEntry',
        'action': 'manage_addMetaEntryForm',
        'permission': 'Add MetaEntry'
    },)

    def all_meta_types(self):
        return self.meta_types


# =============================================================================


class MetaZopeStorage(StoragePlugin):
    """MetaZopeStorage Base Class"""

    meta_type = 'MetaZopeStorage'

    manage_options = tuple(Folder.manage_options[:1] + (
        {'label': 'Entries', 'action': 'entries/manage_main'},
    ) + Folder.manage_options[1:])

    # -------------------------------------------------------------------------

    def all_meta_types(self):
        result = []
        for product in Products.meta_types:
            if product.get('visibility', None) == self.meta_type:
                result.append(product)
        return result

    # -------------------------------------------------------------------------

    pluginName = 'MetaZopeStorage'
    pluginAuthor = 'Sebastian Luehnsdorf - Web-Solutions GbR.'
    pluginVersion = '1.0.13'
    pluginInfo = (
        'This is a Zope based Storage, simple but very powerful. The Entries '
        'of this Storage are based on the Folder object. Data is stored in '
        'form of Properties where possible or as objects inside an Entry.')

    # -------------------------------------------------------------------------

    def __init__(self, id, title=''):
        self.id = id
        self.title = title
        self.entries = MetaEntries('entries')

    # -------------------------------------------------------------------------

    manage_configureStorageForm = DTMLFile('dtml/editMetaZopeStorage',
                                           globals())

    def manage_configureStorage(self, REQUEST=None):
        """Change Storage's configuration options"""

        self.title = REQUEST.get('title', '')

        if REQUEST is not None:
            REQUEST.RESPONSE.redirect(
                self.zmp2URL() + '/manage_storagesBrowserForm?' +
                'message=Changes+saved')

    def storage_getOptions(self):
        """Return a list of the Storage's configuration parameters"""

        options = ['uniqueIds', 'linear']
        if getattr(self, 'has_order_support', None):
            options.append('fieldsSortable')
        if getattr(self.entries, 'has_order_support', None):
            options.append('entriesSortable')
        return options

    # -------------------------------------------------------------------------

    def storage_getEntryObject(self, entryId):
        """Return the specified Entry object"""

        return self.entries._getOb(entryId)

    # -------------------------------------------------------------------------

    def storage_getField(self, fieldId):
        """Return the specified Field of the Storage"""

        return self._getOb(fieldId)

    def storage_fieldIds(self):
        """Return ids of Fields of the specified Storage"""

        return self.objectIds()

    def storage_fieldItems(self):
        """Return tuples of id, value of Fields of the specified Storage"""

        return self.objectItems()

    def storage_fieldValues(self):
        """Return values of Fields of the specified Storage"""

        return self.objectValues()

    # -------------------------------------------------------------------------

    def storage_delField(self, fieldId):
        """Delete the specified Field from the Storage"""

        self.manage_delObject(fieldId)

    def storage_delFields(self, fieldIds=[]):
        """Delete the specified Fields from the Storage"""

        self.manage_delObjects(fieldIds)

    def storage_renameField(self, fieldId, newId):
        """Rename a Field"""

        self.manage_renameObject(fieldId, newId)

    # -------------------------------------------------------------------------

    def storage_moveField(self, fieldId, position):
        """Move a Field to the top"""

        self.moveObjectToPosition([fieldId])

    def storage_moveFieldTop(self, fieldId):
        """Move a Field to the top"""

        self.moveObjectsToTop([fieldId])

    def storage_moveFieldUp(self, fieldId):
        """Move a Field up one position"""

        self.moveObjectsUp([fieldId])

    def storage_moveFieldDown(self, fieldId):
        """Move a Field down one position"""

        self.moveObjectsDown([fieldId])

    def storage_moveFieldBottom(self, fieldId):
        """Move a Field to the bottom"""

        self.moveObjectsToBottom([fieldId])

    # -------------------------------------------------------------------------

    def storage_entryIds(self, order_by=None, reverse=False, filters=None,
                         start=0, end=None, limit=None):
        """Return ids of Entries of this Storage"""

        return self.entries.objectIds()

    def storage_entryItems(self, order_by=None, reverse=False, filters=None,
                           start=0, end=None, limit=None):
        """Return tuples of id, value of Entries of this Storage"""

        result = []
        getEntry = self.storage_getEntry
        for id in self.storage_entryIds():
            result.append((id, getEntry(id)))
        return result

    def storage_entryValues(self, order_by=None, reverse=False, filters=None,
                            start=0, end=None, limit=None):
        """Return values of Entries of this Storage"""

        result = []
        getEntry = self.storage_getEntry
        for id in self.storage_entryIds():
            result.append(getEntry(id))
        return result

    def storage_getEntry(self, entryId):
        """Return the specified Entry as a mapping object"""

        result = {}
        for key, field in self.storage_fieldItems():
            value = field.getValue(entryId, None)
            result[key] = value

        result.update({
            'id': entryId,
            'entryId__': entryId,
            'storageId__': self.getId(),
            'entryPosition__': self.storage_getEntryPosition(entryId)
        })

        return result

    def storage_getEntryField(self, entryId, fieldId, default=None):
        """Return the specified Entry's Field's value"""

        field = self.storage_getField(fieldId)
        return field.getValue(entryId, default)

    # -------------------------------------------------------------------------

    def storage_addEntry(self, entryId, entryData):
        """Add a new Entry in this Storage"""

        instance = MetaEntry(entryId)
        self.entries._setObject(entryId, instance)
        for field in self.storage_fieldValues():
            field.setDefault(entryId)
            field.setData(entryId, entryData)

    def storage_delEntry(self, entryId):
        """Delete an Entry from this Storage"""

        self.entries.manage_delObject(entryId)

    def storage_delEntries(self, entryIds=[]):
        """Delete Entries from this Storage"""

        self.entries.manage_delObjects(entryIds)

    def storage_editEntry(self, entryId, entryData):
        """Edit an Entry of this Storage"""

        for field in self.storage_fieldValues():
            field.setData(entryId, entryData)

    def storage_renameEntry(self, entryId, newId):
        """Rename an Entry"""

        self.entries.manage_renameObject(entryId, newId)

    def storage_setEntryField(self, entryId, fieldId, value):
        """Set the specified Entry's Field's value"""

        field = self.storage_getField(fieldId)
        return field.setValue(entryId, value)

    # -------------------------------------------------------------------------

    def storage_getEntryPosition(self, entryId):
        """Return the position of an Entry"""

        return self.entries.getObjectPosition(entryId) + 1

    def storage_moveEntryToPosition(self, entryId, position):
        """Move an Entry to the specified position"""

        self.entries.moveObjectToPosition(entryId, position - 1)

    def storage_moveEntryTop(self, entryId):
        """Move an Entry to the top"""

        self.entries.moveObjectsToTop([entryId])

    def storage_moveEntryUp(self, entryId):
        """Move an Entry up one position"""

        self.entries.moveObjectsUp([entryId])

    def storage_moveEntryDown(self, entryId):
        """Move an Entry down one position"""

        self.entries.moveObjectsDown([entryId])

    def storage_moveEntryBottom(self, entryId):
        """Move an Entry to the bottom"""

        self.entries.moveObjectsToBottom([entryId])

    # -------------------------------------------------------------------------

    def storage_countEntryFields(self, fieldId):
        """!TXT!"""

        return dict(map(
            lambda item: (item[0], len(item[1])),
            self.storage_entryFieldMap(self, fieldId).items()))

    def storage_distinctEntryFields(self, fieldId):
        """!TXT!"""

        return list(set(map(
            lambda entry: entry[fieldId],
            self.storage_entryValues())))

    def storage_entryFieldMap(self, fieldId):
        """!TXT!"""

        result = {}
        for entryId, entry in self.storage_entryItems():
            value = entry[fieldId]
            result[value] = result.get(fieldId, []) + [entryId]
        return result


# =============================================================================


manage_addMetaZopeStorageForm = DTMLFile('dtml/addMetaZopeStorage', globals())


def manage_addMetaZopeStorage(self, id, title='', REQUEST=None):
    """ZMI constructor for MetaZopeStorage"""

    instance = MetaZopeStorage(id)
    instance.title = title
    id = self._setObject(id, instance)

    if REQUEST is not None:
        REQUEST.RESPONSE.redirect(self.zmp2URL() +
                                  '/manage_storagesBrowserForm')
