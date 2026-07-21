"""Meta Zope Storage."""


from App.special_dtml import DTMLFile
from ZPublisher.Converters import field2text

from Products.MetaPublisher2.bases.field.legacyfield import (
    LegacyFieldPlugin as FieldPlugin)


# =============================================================================


class MetaZopeTextField(FieldPlugin):
    """TextField."""

    pluginName = 'TextField'
    pluginAuthor = 'Sebastian Luehnsdorf - Web-Solutions GbR.'
    pluginVersion = '1.0.3'
    pluginInfo = (
        'This a Text Field for the MetaZopeStorage. It is used for multiple '
        'lines of text.')

    storageTypeId = 'MetaZopeStorage'
    fieldTypeId = 'Text'

    # -------------------------------------------------------------------------

    default = None

    _properties = FieldPlugin._properties + (
        {'id': 'default', 'type': 'text', 'mode': 'w'},
    )

    # -------------------------------------------------------------------------

    manage_configureFieldForm = DTMLFile(
        'dtml/editMetaZopeTextField', globals())

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
            return 'Default Value: "%s"' % self.default.replace('<', '&lt;')

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
            entry._setProperty(fieldId, value, 'text')

    def _hasValue(self, entryId):
        """Return 1 if Entry has a value stored for this Field, 0 otherwise."""
        fieldId = self.getId()
        entry = self.getEntryObject(entryId)
        if entry.hasProperty(fieldId):
            return 1
        return 0

    def _testValue(self, value, options={}):
        """Test a value for validity."""
        return field2text(value)

    # -------------------------------------------------------------------------

    def renderAdd(self):
        """Return a html code for adding an Entry with this Field."""
        return (
            u'<textarea name="%s" cols="60" rows="5" class="fw" />%s'
            u'</textarea>' % (self.getId(), self.default))

    def renderEdit(self, entryId):
        """Return a html code for editing an Entry with this Field."""
        value = self.getValue(entryId)
        return (
            u'<textarea name="%s" cols="60" rows="5" class="fw" />%s'
            u'</textarea>\n<pre><code>%s</code></pre>' % (
                self.getId(),
                value and value.replace('&', '&amp;') or '',
                value and value.replace('&', '&amp;') or ''
            )
        )

    def renderView(self, entryId):
        """Return a html code for viewing an Entry with this Field."""
        value = self.getValue(entryId)
        if value is not None:
            return str(value).replace('&', '&amp;').replace(
                '<', '&lt;').replace('\n', '<br>')
        return '<em>n/a</em>'

    # -------------------------------------------------------------------------

    def manage_afterAdd(self, item, container):
        """Update old entries."""
        if item is self:
            # update old entries
            for entryId in self.storage_entryIds():
                self.setValue(entryId, self.default)


# =============================================================================


manage_addMetaZopeTextFieldForm = DTMLFile(
    'dtml/addMetaZopeTextField', globals())


def manage_addMetaZopeTextField(self, id, title='', default='', REQUEST=None):
    """Add new MetaZopeTextField."""
    instance = MetaZopeTextField(id)
    instance.title = title
    instance.default = instance._testValue(default)
    id = self._setObject(id, instance)
    if REQUEST is not None:
        REQUEST.RESPONSE.redirect(
            self.zmp2URL() + '/manage_fieldsBrowserForm?storageId=' +
            self.getStorageId())
