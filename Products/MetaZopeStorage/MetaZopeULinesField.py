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
from ZPublisher.Converters import field2ulines

from Products.MetaPublisher2.Library import FieldPlugin


# =============================================================================


class MetaZopeULinesField(FieldPlugin):
    """UnicodeLinesField"""

    pluginName = 'UnicodeLinesField'
    pluginAuthor = 'Sebastian Luehnsdorf - Web-Solutions GbR.'
    pluginVersion = '1.0.5'
    pluginInfo = (
        "This an Unicode Lines Field for the MetaZopeStorage. It is used for "
        "multiple lines of text.")

    storageTypeId = 'MetaZopeStorage'
    fieldTypeId = 'UnicodeLines'

    # -------------------------------------------------------------------------

    default = None

    _properties = FieldPlugin._properties + (
        {'id': 'default', 'type': 'ulines', 'mode': 'w'},
    )

    # -------------------------------------------------------------------------

    manage_configureFieldForm = DTMLFile(
        'dtml/editMetaZopeULinesField', globals())

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
            return 'Default Value: "%s"' % u', '.join(
                self.default).replace('<', '&lt;')

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
        if value == 1:
            value = []
        if entry.hasProperty(fieldId):
            entry._setPropValue(fieldId, value)
        else:
            entry._setProperty(fieldId, value, 'ulines')

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
        if type(value) != type([]):
            value = field2ulines(value)
        if len(value) == 0:
            value = 1
        return value

    # -------------------------------------------------------------------------

    def renderAdd(self):
        """Return a html code for adding an Entry with this Field"""
        value = self.default
        if value is None:
            value = ''
        else:
            for i in range(len(value)):
                if isinstance(value[i], str):
                    value[i] = unicode(value[i], 'latin-1')
            value = u'\n'.join(value).replace('<', '&lt;')
        return (
            u'<textarea name="%s:utf8:ulines" cols="60" rows="5" class="fw">'
            u'%s</textarea>' % (self.getId(), value))

    def renderEdit(self, entryId):
        """Return a html code for editing an Entry with this Field"""
        value = self.getValue(entryId)
        if value is None:
            value = ''
        else:
            value = list(value)
            value = u'\n'.join(value).replace('<', '&lt;')
        return (
            u'<textarea name="%s:utf8:ulines" cols="60" rows="5" class="fw">'
            u'%s</textarea>' % (self.getId(), value))

    def renderView(self, entryId):
        """Return a html code for viewing an Entry with this Field"""
        value = self.getValue(entryId)
        if value is not None:
            result = []
            for line in value:
                result.append(str(line).replace('<', '&lt;'))
            return ', '.join(result)
        return '<em>n/a</em>'

    # -------------------------------------------------------------------------

    def manage_afterAdd(self, item, container):
        if item is self:
            # update old entries
            for entryId in self.storage_entryIds():
                self.setValue(entryId, self.default)


# =============================================================================


manage_addMetaZopeULinesFieldForm = DTMLFile(
    'dtml/addMetaZopeULinesField', globals())


def manage_addMetaZopeULinesField(
    self, id, title='', default='', REQUEST=None
):
    """ZMI constructor for MetaZopeULinesField"""
    instance = MetaZopeULinesField(id)
    instance.title = title
    default = instance._testValue(default)
    if default == 1:
        instance.default = []
    else:
        instance.default = default
    id = self._setObject(id, instance)

    if REQUEST is not None:
        REQUEST.RESPONSE.redirect(
            self.zmp2URL() + '/manage_fieldsBrowserForm?storageId=' +
            self.getStorageId())
