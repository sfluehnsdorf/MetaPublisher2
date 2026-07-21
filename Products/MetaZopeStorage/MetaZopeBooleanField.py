"""Meta Zope Storage."""


from App.special_dtml import DTMLFile
from ZPublisher.Converters import field2boolean, field2ustring

from Products.MetaPublisher2.bases.field.legacyfield import (
    LegacyFieldPlugin as FieldPlugin)


# =============================================================================


class MetaZopeBooleanField(FieldPlugin):
    """BooleanField."""

    pluginName = 'BooleanField'
    pluginAuthor = 'Sebastian Luehnsdorf - Web-Solutions GbR.'
    pluginVersion = '1.0.4'
    pluginInfo = 'This a Boolean Field for the MetaZopeStorage.'

    storageTypeId = 'MetaZopeStorage'
    fieldTypeId = 'Boolean'

    # -------------------------------------------------------------------------

    default = None
    labelTrue = None
    labelFalse = None

    _properties = FieldPlugin._properties + (
        {'id': 'default', 'type': 'boolean', 'mode': 'w'},
        {'id': 'labelTrue', 'type': 'ustring', 'mode': 'w'},
        {'id': 'labelFalse', 'type': 'ustring', 'mode': 'w'},
    )

    # -------------------------------------------------------------------------

    manage_configureFieldForm = DTMLFile(
        'dtml/editMetaZopeBooleanField', globals())

    def manage_configureField(self, REQUEST=None):
        """Change Field's configuration parameters."""
        self.title = REQUEST.get('title', '')
        self.default = self._testValue(REQUEST.get('default', None))
        self.labelTrue = field2ustring(REQUEST.get('labelTrue', ''))
        self.labelFalse = field2ustring(REQUEST.get('labelFalse', ''))
        if REQUEST is not None:
            REQUEST.RESPONSE.redirect(
                self.zmp2URL() + '/manage_fieldsBrowserForm?storageId=' +
                self.getStorageId() + '&message=Changes+saved')

    # -------------------------------------------------------------------------

    def getFieldInfo(self):
        """Return information about this Field if available."""
        if self.default:
            return 'Default Value: "%s"' % (
                repr(self.default).replace('<', '&lt;'))

    def getEntryObject(self, entryId):
        """Return the entry object."""
        return self.storage_getEntryObject(entryId)

    # -------------------------------------------------------------------------

    def setDefault(self, entryId):
        """Set the default value for this Field in the Entry."""
        self.setValue(entryId, self.default)

    def setData(self, entryId, data):
        """Set the value inside data for this Field in the Entry."""
        fieldId = self.getId()
        if data.has_key(fieldId):
            self.setValue(entryId, data[fieldId])

    # -------------------------------------------------------------------------

    def _getValue(self, entryId, default):
        """Retrieve a value from an entry."""
        fieldId = self.getId()
        entry = self.getEntryObject(entryId)
        return entry.getProperty(fieldId, default)

    def _setValue(self, entryId, value):
        """Store a value in an entry."""
        fieldId = self.getId()
        entry = self.getEntryObject(entryId)
        if entry.hasProperty(fieldId):
            entry._setPropValue(fieldId, value)
        else:
            entry._setProperty(fieldId, value, 'boolean')

    def _hasValue(self, entryId):
        """Return 1 if Entry has a value stored for this Field, 0 otherwise."""
        fieldId = self.getId()
        entry = self.getEntryObject(entryId)
        if entry.hasProperty(fieldId):
            return 1
        return 0

    def _testValue(self, value, options={}):
        """Test a value for validity."""
        if value == '0':
            value = None
        return field2boolean(value)

    # -------------------------------------------------------------------------

    def renderAdd(self):
        """Return a html code for adding an Entry with this Field."""
        fieldId = self.getId()
        if self.default:
            return (
                '<input type="radio" name="%s" value="1" checked> %s<br>'
                '<input type="radio" name="%s" value="0"> %s' % (
                    fieldId, self.labelTrue, fieldId, self.labelFalse))
        else:
            return (
                '<input type="radio" name="%s" value="1"> %s<br>'
                '<input type="radio" name="%s" value="0" checked> %s' % (
                    fieldId, self.labelTrue, fieldId, self.labelFalse))

    def renderEdit(self, entryId):
        """Return a html code for editing an Entry with this Field."""
        fieldId = self.getId()
        if self.getValue(entryId):
            return (
                '<input type="radio" name="%s" value="1" checked> %s<br>'
                '<input type="radio" name="%s" value="0"> %s' % (
                    fieldId, self.labelTrue, fieldId, self.labelFalse))
        else:
            return (
                '<input type="radio" name="%s" value="1"> %s<br>'
                '<input type="radio" name="%s" value="0" checked> %s' % (
                    fieldId, self.labelTrue, fieldId, self.labelFalse))

    def renderView(self, entryId):
        """Return a html code for viewing an Entry with this Field."""
        if self.getValue(entryId):
            return self.labelTrue
        return self.labelFalse

    # -------------------------------------------------------------------------

    def manage_afterAdd(self, item, container):
        """Update old entries."""
        if item is self:
            # update old entries
            for entryId in self.storage_entryIds():
                self.setValue(entryId, self.default)


# =============================================================================


manage_addMetaZopeBooleanFieldForm = DTMLFile(
    'dtml/addMetaZopeBooleanField', globals())


def manage_addMetaZopeBooleanField(
    self, id, title='', default=None, labelTrue='', labelFalse='', REQUEST=None
):
    """Add new MetaZopeBooleanField."""
    instance = MetaZopeBooleanField(id)
    instance.title = title
    instance.default = instance._testValue(default)
    instance.labelTrue = field2ustring(labelTrue)
    instance.labelFalse = field2ustring(labelFalse)
    id = self._setObject(id, instance)
    if REQUEST is not None:
        REQUEST.RESPONSE.redirect(
            self.zmp2URL() + '/manage_fieldsBrowserForm?storageId=' +
            self.getStorageId())
