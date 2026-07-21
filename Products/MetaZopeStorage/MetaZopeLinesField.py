"""Meta Zope Storage."""


from App.special_dtml import DTMLFile
from ZPublisher.Converters import field2lines

from Products.MetaPublisher2.bases.field.legacyfield import (
    LegacyFieldPlugin as FieldPlugin)


# =============================================================================


class MetaZopeLinesField(FieldPlugin):
    """LinesField."""

    pluginName = 'LinesField'
    pluginAuthor = 'Sebastian Luehnsdorf - Web-Solutions GbR.'
    pluginVersion = '1.0.5'
    pluginInfo = (
        'This a Lines Field for the MetaZopeStorage. It is used for multiple '
        'lines of text.')

    storageTypeId = 'MetaZopeStorage'
    fieldTypeId = 'Lines'

    # -------------------------------------------------------------------------

    default = None

    _properties = FieldPlugin._properties + (
        {'id': 'default', 'type': 'lines', 'mode': 'w'},
    )

    # -------------------------------------------------------------------------

    manage_configureFieldForm = DTMLFile(
        'dtml/editMetaZopeLinesField', globals())

    def manage_configureField(self, REQUEST=None):
        """Change Field's configuration parameters."""
        self.title = REQUEST.get('title', '')
        self.default = self._testValue(REQUEST.get('default', ''))

        if REQUEST is not None:
            REQUEST.RESPONSE.redirect(
                self.zmp2URL() + '/manage_fieldsBrowserForm?storageId=' +
                self.getStorageId() + '&message=Changes+saved')

    # -------------------------------------------------------------------------

    def getFieldInfo(self):
        """Return information about this Field if available."""
        if self.default:
            return 'Default Value: "%s"' % ', '.join(
                self.default).replace('<', '&lt;')

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
        else:
            self.setValue(entryId, [])

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
        if value == 1:
            value = []
        if entry.hasProperty(fieldId):
            entry._setPropValue(fieldId, value)
        else:
            entry._setProperty(fieldId, value, 'lines')

    def _hasValue(self, entryId):
        """Return 1 if Entry has a value stored for this Field, 0 otherwise."""
        fieldId = self.getId()
        entry = self.getEntryObject(entryId)
        if entry.hasProperty(fieldId):
            return 1
        return 0

    def _testValue(self, value, options={}):
        """Test a value for validity."""
        if isinstance(value, list):
            value = field2lines(value)
        if len(value) == 0:
            value = 1
        return value

    # -------------------------------------------------------------------------

    def renderAdd(self):
        """Return a html code for adding an Entry with this Field."""
        return (
            u'<textarea name="%s" cols="60" rows="5" class="fw" />%s'
            u'</textarea>' % (self.getId(), '\n'.join(self.default)))

    def renderEdit(self, entryId):
        """Return a html code for editing an Entry with this Field."""
        value = self.getValue(entryId)
        if value is None:
            value = ''
        return (
            u'<textarea name="%s" cols="60" rows="5" class="fw" />%s'
            u'</textarea>' % (self.getId(), '\n'.join(value)))

    def renderView(self, entryId):
        """Return a html code for viewing an Entry with this Field."""
        value = self.getValue(entryId)
        if value is not None:
            result = []
            for line in value:
                result.append(str(line).replace('<', '&lt;'))
            return ', '.join(result)
        return '<em>n/a</em>'

    # -------------------------------------------------------------------------

    def manage_afterAdd(self, item, container):
        """Update old entries."""
        if item is self:
            # update old entries
            for entryId in self.storage_entryIds():
                self.setValue(entryId, self.default)


# =============================================================================


manage_addMetaZopeLinesFieldForm = DTMLFile(
    'dtml/addMetaZopeLinesField', globals())


def manage_addMetaZopeLinesField(self, id, title='', default='', REQUEST=None):
    """Add new MetaZopeLinesField."""
    instance = MetaZopeLinesField(id)
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
