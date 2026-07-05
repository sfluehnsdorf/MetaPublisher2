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
from ZPublisher.Converters import field2long

from Products.MetaPublisher2.Library import FieldPlugin


# =============================================================================


class MetaZopeLongField(FieldPlugin):
    """LongField"""

    pluginName = 'LongField'
    pluginAuthor = 'Sebastian Luehnsdorf - Web-Solutions GbR.'
    pluginVersion = '1.0.2'
    pluginInfo = (
        'This a Long Field for the MetaZopeStorage. Longs are whole numbers '
        'of any range, limited only by memory.')

    storageTypeId = 'MetaZopeStorage'
    fieldTypeId = 'Long'

    # -------------------------------------------------------------------------

    default = long(0)

    _properties = FieldPlugin._properties + (
        {'id': 'default', 'type': 'long', 'mode': 'w'},
    )

    # -------------------------------------------------------------------------

    manage_configureFieldForm = DTMLFile(
        'dtml/editMetaZopeLongField', globals())

    def manage_configureField(self, REQUEST=None):
        """Change Field's configuration parameters"""
        self.title = REQUEST.get('title', '')
        self.default = self._testValue(REQUEST.get('default', ''))
        if REQUEST is not None:
            REQUEST.RESPONSE.redirect(
                self.zmp2URL() + '/manage_fieldsBrowserForm?storageId=' +
                self.getStorageId() + '&message=Changes+saved')

    # -------------------------------------------------------------------------

    def getFieldInfo(self):
        """Return information about this Field if available"""
        if self.default:
            return 'Default Value: "%s"' % self.default

    def getEntryObject(self, entryId):
        """Return the entry object"""
        return self.storage_getEntryObject(entryId)

    # -------------------------------------------------------------------------

    def setDefault(self, entryId):
        """Set the default value for this Field in the Entry"""
        self.setValue(entryId, self.default)

    def setData(self, entryId, data):
        """Set the value inside data for this Field in the Entry"""
        fieldId = self.getId()
        if data.has_key(fieldId):
            self.setValue(entryId, data[fieldId])

    # -------------------------------------------------------------------------

    def _getValue(self, entryId, default):
        """Retrieve a value from an entry"""
        fieldId = self.getId()
        entry = self.getEntryObject(entryId)
        return entry.getProperty(fieldId, default)

    def _setValue(self, entryId, value):
        """Store a value in an entry"""
        fieldId = self.getId()
        entry = self.getEntryObject(entryId)
        if entry.hasProperty(fieldId):
            entry._setPropValue(fieldId, value)
        else:
            entry._setProperty(fieldId, value, 'long')

    def _hasValue(self, entryId):
        """Return 1 if the Entry has a value stored for this Field, 0
        otherwise"""
        fieldId = self.getId()
        entry = self.getEntryObject(entryId)
        if entry.hasProperty(fieldId):
            return 1
        return 0

    def _testValue(self, value, options={}):
        """Test a value for validity"""
        return field2long(value)

    # -------------------------------------------------------------------------

    def renderAdd(self):
        """Return a html code for adding an Entry with this Field"""
        return (
            u'<input type="text" name="%s" value="%s" size="10" '
            u'class="num">' % (self.getId(), self.default))

    def renderEdit(self, entryId):
        """Return a html code for editing an Entry with this Field"""
        value = self.getValue(entryId)
        if value is None:
            value = '0'
        return (
            u'<input type="text" name="%s" value="%s" size="10" '
            u'class="num">' % (self.getId(), value))

    def renderView(self, entryId):
        """Return a html code for viewing an Entry with this Field"""
        value = self.getValue(entryId)
        if value is not None:
            return str(value)
        return '<em>n/a</em>'

    # -------------------------------------------------------------------------

    def manage_afterAdd(self, item, container):
        if item is self:
            # update old entries
            for entryId in self.storage_entryIds():
                self.setValue(entryId, self.default)


# =============================================================================


manage_addMetaZopeLongFieldForm = DTMLFile(
    'dtml/addMetaZopeLongField', globals())


def manage_addMetaZopeLongField(self, id, title='', default=0, REQUEST=None):
    """ZMI constructor for MetaZopeLongField"""
    instance = MetaZopeLongField(id)
    instance.title = title
    instance.default = instance._testValue(default)
    id = self._setObject(id, instance)

    if REQUEST is not None:
        REQUEST.RESPONSE.redirect(
            self.zmp2URL() + '/manage_fieldsBrowserForm?storageId=' +
            self.getStorageId())
