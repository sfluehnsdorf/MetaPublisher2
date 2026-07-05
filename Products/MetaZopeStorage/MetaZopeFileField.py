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

from string import letters, digits

from Globals import DTMLFile

from Products.MetaPublisher2.Library import FieldPlugin


# =============================================================================


_validIdChars = letters + digits + '_-.'


# =============================================================================


class MetaZopeFileField(FieldPlugin):
    """FileField"""

    pluginName = 'FileField'
    pluginAuthor = 'Sebastian Luehnsdorf - Web-Solutions GbR.'
    pluginVersion = '1.0.9'
    pluginInfo = (
        'This a File Field for the MetaZopeStorage. It is used for a single '
        'line of text.')

    storageTypeId = 'MetaZopeStorage'
    fieldTypeId = 'File'

    # -------------------------------------------------------------------------

    manage_configureFieldForm = DTMLFile(
        'dtml/editMetaZopeFileField', globals())

    def manage_configureField(self, REQUEST=None):
        """Change Field's configuration parameters"""
        self.title = REQUEST.get('title', '')

        if REQUEST is not None:
            REQUEST.RESPONSE.redirect(
                self.zmp2URL() + '/manage_fieldsBrowserForm?storageId=' +
                self.getStorageId() + '&message=Changes+saved')

    # -------------------------------------------------------------------------

    def getFieldInfo(self):
        """Return information about this Field if available"""
        pass

    def getEntryObject(self, entryId):
        """Return the entry object"""
        return self.storage_getEntryObject(entryId)

    # -------------------------------------------------------------------------

    def setDefault(self, entryId):
        """Set the default value for this Field in the Entry"""
        pass

    def setData(self, entryId, data):
        """Set the value inside data for this Field in the Entry"""
        fieldId = self.getId()
        if data.get(fieldId + '_del', None):
            entry = self.getEntryObject(entryId)
            try:
                entry.manage_delObjects([fieldId])
            except Exception:
                pass
        if data.get(fieldId, None):
            self.setValue(entryId, data[fieldId])

    # -------------------------------------------------------------------------

    def _getValue(self, entryId, default):
        """Retrieve a value from an entry"""
        fieldId = self.getId()
        entry = self.getEntryObject(entryId)
        if fieldId in entry.objectIds():
            folder = entry._getOb(fieldId)
            return folder._getOb(folder.filename)

    def _setValue(self, entryId, value):
        """Store a value in an entry"""
        if value == '':
            return

        fieldId = self.getId()
        entry = self.getEntryObject(entryId)

        if type([]) == type(value):
            data = value[0]
            filename = value[1]
            if filename != '':
                filename = self._normalizeId(filename)
                try:
                    entry.manage_delObjects([fieldId])
                except Exception:
                    pass
                entry.manage_addFolder(fieldId)
                folder = entry._getOb(fieldId)
                folder._setProperty('filename', filename, 'string')
                folder.manage_addDTMLMethod(
                    'index_html',
                    file=(
                        '''<dtml-call "RESPONSE.redirect(URL1 + '/' + '''
                        'filename)">'))
                folder.manage_addFile(filename, data)

        else:
            filename = value.filename.split('\\')[-1].split('/')[-1]
            if filename != '':
                filename = self._normalizeId(filename)
                try:
                    entry.manage_delObjects([fieldId])
                except Exception:
                    pass
                entry.manage_addFolder(fieldId)
                folder = entry[fieldId]
                folder._setProperty('filename', filename, 'string')
                folder.manage_addDTMLMethod(
                    'index_html', file=(
                        '''<dtml-call "RESPONSE.redirect( URL1 + '/' + '''
                        'filename )">'))
                folder.manage_addFile(filename, value)

    def _hasValue(self, entryId):
        """Return 1 if the Entry has a value stored for this Field, 0
        otherwise"""
        entry = self.getEntryObject(entryId)
        fieldId = self.getId()
        if fieldId in entry.objectIds():
            return 1
        return 0

    def _testValue(self, value, options={}):
        """Test a value for validity"""
        return value

    # -------------------------------------------------------------------------

    def _normalizeId(self, id):
        """!TXT!"""
        result = ''
        for i in range(len(id)):
            if id[i] in _validIdChars and (i > 0 or id[i] != '_'):
                result = result + id[i]
        return result

    # -------------------------------------------------------------------------

    def renderAdd(self):
        """Return a html code for adding an Entry with this Field"""
        return '<input type="file" name="%s" size="40">' % self.getId()

    def renderEdit(self, entryId):
        """Return a html code for editing an Entry with this Field"""
        result = '<input type="file" name="%s" size="40"><br>' % self.getId()
        if self.hasValue(entryId):
            file = self.getValue(entryId)
            result = result + (
                '<a href="%s" target="_blank">Open File</a><br />'
                '<table cellspacing="0" cellpadding="0" border="0">'
                '<tr><td>File Name:</td><td><img src="sp.gif" width="10" '
                'height="1" border="0"></td><td>%s</td></tr>'
                '<tr><td>Content Type:</td><td></td><td>%s</td></tr>'
                '<tr><td>File Size:</td><td></td><td>%s</td></tr>'
                '</table>'
            ) % (
                file.absolute_url(), file.getId(), file.getContentType(),
                file.getSize())
            return result
        else:
            result = result + '<em>No File uploaded</em>'
        return result

    def renderView(self, entryId):
        """Return a html code for viewing an Entry with this Field"""
        if self.hasValue(entryId):
            file = self.getValue(entryId)
            return (
                '<a href="%s" target="_blank">Open File</a>' %
                file.absolute_url())
        return '<em>n/a</em>'


# =============================================================================


manage_addMetaZopeFileFieldForm = DTMLFile(
    'dtml/addMetaZopeFileField', globals())


def manage_addMetaZopeFileField(self, id, title='', default='', REQUEST=None):
    """ZMI constructor for MetaZopeFileField"""
    instance = MetaZopeFileField(id)
    instance.title = title
    id = self._setObject(id, instance)
    if REQUEST is not None:
        REQUEST.RESPONSE.redirect(
            self.zmp2URL() + '/manage_fieldsBrowserForm?storageId=' +
            self.getStorageId())
