"""Meta Zope Storage."""


from string import letters, digits

from App.special_dtml import DTMLFile

from Products.MetaPublisher2.bases.field.legacyfield import (
    LegacyFieldPlugin as FieldPlugin)


# =============================================================================


_validIdChars = letters + digits + '_-.'


# =============================================================================


class MetaZopeImageField(FieldPlugin):
    """ImageField."""

    pluginName = 'ImageField'
    pluginAuthor = 'Sebastian Luehnsdorf - Web-Solutions GbR.'
    pluginVersion = '1.0.9'
    pluginInfo = (
        'This a Image Field for the MetaZopeStorage. It is used for '
        'a single line of text.')

    storageTypeId = 'MetaZopeStorage'
    fieldTypeId = 'Image'

    # -------------------------------------------------------------------------

    manage_configureFieldForm = DTMLFile(
        'dtml/editMetaZopeImageField', globals())

    def manage_configureField(self, REQUEST=None):
        """Change Field's configuration parameters."""
        self.title = REQUEST.get('title', '')
        if REQUEST is not None:
            REQUEST.RESPONSE.redirect(
                self.zmp2URL() + '/manage_fieldsBrowserForm?storageId=' +
                self.getStorageId() + '&message=Changes+saved')

    # -------------------------------------------------------------------------

    def getFieldInfo(self):
        """Return information about this Field if available."""
        pass

    def getEntryObject(self, entryId):
        """Return the entry object."""
        return self.storage_getEntryObject(entryId)

    # -------------------------------------------------------------------------

    def setDefault(self, entryId):
        """Set the default value for this Field in the Entry."""
        pass

    def setData(self, entryId, data):
        """Set the value inside data for this Field in the Entry."""
        fieldId = self.getId()
        if data.get(fieldId + '_del', None):
            entry = self.getEntryObject(entryId)
            try:
                entry.manage_delObjects([fieldId,])
            except Exception:
                pass
        if data.get(fieldId, None):
            self.setValue(entryId, data[fieldId])

    # -------------------------------------------------------------------------

    def _getValue(self, entryId, default):
        """Retrieve a value from an entry."""
        fieldId = self.getId()
        entry = self.getEntryObject(entryId)
        if fieldId in entry.objectIds():
            folder = entry._getOb(fieldId)
            return folder._getOb(folder.filename)

    def _setValue(self, entryId, value):
        """Store a value in an entry."""
        if value == '':
            return

        fieldId = self.getId()
        entry = self.getEntryObject(entryId)

        if isinstance(value, list):
            data = value[0]
            filename = value[1]
            if filename != '':
                filename = self._normalizeId(filename)
                try:
                    entry.manage_delObjects([fieldId,])
                except Exception:
                    pass
                entry.manage_addFolder(fieldId)
                folder = entry._getOb(fieldId)
                folder._setProperty('filename', filename, 'string')
                folder.manage_addDTMLMethod('index_html', file=(
                    '''<dtml-call "RESPONSE.redirect(URL1 + '/' + '''
                    'filename)">'))
                folder.manage_addImage(filename, data)

        else:
            filename = value.filename.split('\\')[-1].split('/')[-1]
            if filename != '':
                filename = self._normalizeId(filename)
                try:
                    entry.manage_delObjects([fieldId,])
                except Exception:
                    pass
                entry.manage_addFolder(fieldId)
                folder = entry[fieldId]
                folder._setProperty('filename', filename, 'string')
                folder.manage_addDTMLMethod('index_html', file=(
                    '''<dtml-call "RESPONSE.redirect(URL1 + '/' + '''
                    'filename)">'))
                folder.manage_addImage(filename, value)

    def _hasValue(self, entryId):
        """Return 1 if Entry has a value stored for this Field, 0 otherwise."""
        entry = self.getEntryObject(entryId)
        fieldId = self.getId()
        if fieldId in entry.objectIds():
            return 1
        return 0

    def _testValue(self, value, options={}):
        """Test a value for validity."""
        return value

    # -------------------------------------------------------------------------

    def _normalizeId(self, id):
        """Return normalized id."""
        result = ''
        for i in range(len(id)):
            if id[i] in _validIdChars and (i > 0 or id[i] != '_'):
                result = result + id[i]
        return result

    def getThumbnailTag(self, entryId, width=60, height=60):
        """Return HTML code for thumbnail."""
        image = self.getValue(entryId)
        imagewidth = image.width
        imageheight = image.height
        if imagewidth > imageheight:
            if imagewidth > width:
                imageheight = imageheight * width / imagewidth
                imagewidth = width
        else:
            if imageheight > height:
                imagewidth = imagewidth * height / imageheight
                imageheight = height
        return '<a href="%s" target="_blank">%s</a>' % (
            image.absolute_url(), image.tag(
                width=imagewidth, height=imageheight, border=1))

    # -------------------------------------------------------------------------

    def renderAdd(self):
        """Return a html code for adding an Entry with this Field."""
        return u'<input type="file" name="%s" size="40" />' % self.getId()

    def renderEdit(self, entryId):
        """Return a html code for editing an Entry with this Field."""
        result = u'<input type="file" name="%s" size="40" /><br />' % (
            self.getId())
        if self.hasValue(entryId):
            image = self.getValue(entryId)
            result = result + (
                u'<table cellspacing="0" cellpadding="0" border="0">'
                u'<tr>'
                u'<td valign="top">%s</td>'
                u'<td><img src="sp.gif" width="10" height="1" border="0"></td>'
                u'<td valign="top">'
                u'\t<table cellspacing="0" cellpadding="0" border="0">'
                u'\t<tr><td>File Name:</td><td><img src="sp.gif" width="10" '
                u'height="1" border="0"></td><td>%s</td></tr>'
                u'\t<tr><td>Content Type:</td><td></td><td>%s</td></tr>'
                u'\t<tr><td>File Size:</td><td></td><td>%s</td></tr>'
                u'\t<tr><td>Dimensions:</td><td></td><td>%s x %s</td></tr>'
                u'\t</table>'
                u'</td>'
                u'</tr>'
                u'</table>'
            ) % (
                self.getThumbnailTag(entryId), image.getId(),
                image.getContentType(), image.getSize(), image.width,
                image.height
            )
            return result
        else:
            result = result + '<em>No Image uploaded</em>'
        return result

    def renderView(self, entryId):
        """Return a html code for viewing an Entry with this Field."""
        if self.hasValue(entryId):
            return self.getThumbnailTag(entryId)
        return '<em>n/a</em>'


# =============================================================================


manage_addMetaZopeImageFieldForm = DTMLFile(
    'dtml/addMetaZopeImageField', globals())


def manage_addMetaZopeImageField(self, id, title='', default='', REQUEST=None):
    """Add new MetaZopeImageField."""
    instance = MetaZopeImageField(id)
    instance.title = title
    id = self._setObject(id, instance)

    if REQUEST is not None:
        REQUEST.RESPONSE.redirect(
            self.zmp2URL() + '/manage_fieldsBrowserForm?storageId=' +
            self.getStorageId())
