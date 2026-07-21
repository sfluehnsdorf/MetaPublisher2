"""Meta Widgets."""


from App.special_dtml import DTMLFile
from Products.MetaPublisher2.bases.widget.legacywidget import (
    LegacyWidgetPlugin as WidgetPlugin)


# =============================================================================


class MetaFileWidget(WidgetPlugin):
    """MetaFileWidget."""

    meta_type = 'MetaFileWidget'

    # -------------------------------------------------------------------------

    pluginName = 'MetaFileWidget'
    pluginAuthor = 'Sebastian Luehnsdorf - Web-Solutions GbR.'
    pluginVersion = '1.0.1'
    pluginInfo = (
        'Basic Web Interface that allows users to add new Entries.')

    formTypeIds = ['Add', 'Edit', 'View', 'List']
    fieldTypeIds = ['File', 'Image']

    # -------------------------------------------------------------------------

    displayMode = 'defaultMode'

    maxChars = 0
    maxCharsCount = 50

    align = 'left'
    alignOptions = ['left', 'center', 'right', 'justify']
    valign = 'top'
    valignOptions = ['top', 'middle', 'bottom']

    inputSize = 60
    inputClass = ''
    inputStyle = ''

    showFileName = 0
    showFileSize = 0
    showFileType = 0

    # -------------------------------------------------------------------------

    _properties = WidgetPlugin._properties + (
        {'id': 'displayMode', 'type': 'string', 'mode': 'w'},
        {
            'id': 'align', 'type': 'selection', 'mode': 'w',
            'select_variable': 'alignOptions'},
        {
            'id': 'valign', 'type': 'selection', 'mode': 'w',
            'select_variable': 'valignOptions'},
        {'id': 'inputSize', 'type': 'int', 'mode': 'w'},
        {'id': 'inputClass', 'type': 'string', 'mode': 'w'},
        {'id': 'inputStyle', 'type': 'string', 'mode': 'w'},
        {'id': 'showFileName', 'type': 'boolean', 'mode': 'w'},
        {'id': 'showFileSize', 'type': 'boolean', 'mode': 'w'},
        {'id': 'showFileType', 'type': 'boolean', 'mode': 'w'},
    )

    # -------------------------------------------------------------------------

    def getWidgetId(self):
        """Return Plugin Identifier."""
        return 'MetaWidgets.' + self.meta_type

    # -------------------------------------------------------------------------

    def setWidgetData(self, formTypeId, data={}):
        """Configure Widget according to passed data."""
        if data.get('pluginId__', '') == self.getWidgetId():
            self.formTypeId = formTypeId
            self.displayMode = data['displayMode']
            self.align = data.get('align', 'left')
            self.valign = data.get('valign', 'top')
            self.inputSize = data.get('inputSize', 60)
            self.inputClass = data.get('inputClass', '')
            self.inputStyle = data.get('inputStyle', '')
            self.showFileName = data.get('showFileName', 0)
            self.showFileSize = data.get('showFileSize', 0)
            self.showFileType = data.get('showFileType', 0)
        else:
            raise TypeError('Invalid Widget data: "%s" <> "%s"' % (
                self.getWidgetId(), data.get('pluginId__', '')))

    def getWidgetData(self, formTypeId):
        """Return the data of this Widget."""
        return {
            'pluginId__':  'MetaWidgets.' + self.meta_type,
            'displayMode': self.displayMode,
            'align': self.align,
            'valign': self.valign,
            'inputSize': self.inputSize,
            'inputClass': self.inputClass,
            'inputStyle': self.inputStyle
        }

    # -------------------------------------------------------------------------

    def renderWidget(self, elementId, field, entryName=''):
        """Render widget according to configuration."""
        fieldId = field.getId()
        formTypeId = self.formTypeId
        displayMode = self.displayMode
        result = {
            'align': self.align,
            'valign': self.valign,
            'title': field.title or fieldId
        }

        def addInputOptions(self):
            options = ' size="%s"' % self.inputSize
            if self.inputClass:
                options = options + ' class="%s"' % self.inputClass
            if self.inputStyle:
                options = options + ' style="%s"' % self.inputStyle
            return options

        if formTypeId == 'List':
            if displayMode == 'defaultMode':
                result['field'] = (
                    '''<dtml-let file_object="%s[ '%s' ]">'''
                    '<dtml-if file_object><a target="_blank" href="'
                    '<dtml-var "file_object.absolute_url()">">' % (
                        entryName, fieldId))
                if self.showFileName:
                    result['field'] = result['field'] + (
                        '<dtml-var "file_object.getId()">')
                else:
                    result['field'] = result['field'] + 'Download'
                result['field'] = result['field'] + '''</a>'''
                if self.showFileSize:
                    result['field'] = (
                        result['field'] +
                        '''<br /><dtml-var "'%%0.2f' %% ('''
                        '''float(file_object.get_size()) / 1024)">kB''')
                if self.showFileType:
                    result['field'] = result['field'] + (
                        '<br /><dtml-var "file_object.getContentType()">')
                result['field'] = result['field'] + (
                    '<dtml-else><em>n/a</em></dtml-if></dtml-let>')
        elif formTypeId == 'View':
            if displayMode == 'defaultMode':
                result['field'] = (
                    '''<dtml-let file_object="%s[ '%s' ]">'''
                    '''<dtml-if file_object><a target="_blank" href="'''
                    '''<dtml-var "file_object.absolute_url()">">''' % (
                        entryName, fieldId))
                if self.showFileName:
                    result['field'] = result['field'] + (
                        '<dtml-var "file_object.getId()">')
                else:
                    result['field'] = result['field'] + 'Download'
                result['field'] = result['field'] + '</a>'
                if self.showFileSize:
                    result['field'] = result['field'] + (
                        '''<br /><dtml-var "'%%0.2f' %% ('''
                        '''float(file_object.get_size()) / 1024)">kB''')
                if self.showFileType:
                    result['field'] = result['field'] + (
                        '<br /><dtml-var "file_object.getContentType()">')
                result['field'] = result['field'] + (
                    '<dtml-else><em>n/a</em></dtml-if></dtml-let>')
        elif formTypeId == 'Add':
            if displayMode == 'defaultMode':
                result['field'] = (
                    '''<input type="file" name="%s" id="%s" value=""''' % (
                        fieldId, fieldId) +
                    addInputOptions(self) + '>')
        elif formTypeId == 'Edit':
            if displayMode == 'defaultMode':
                result['field'] = (
                    '''<input type="file" name="%s" id="%s" value=""''' % (
                        fieldId, fieldId) +
                    addInputOptions(self) +
                    '''><br /><dtml-let file_object="%s[ '%s' ]">'''
                    '''<dtml-if file_object><a target="_blank" href="'''
                    '''<dtml-var "file_object.absolute_url()">">''' % (
                        entryName, fieldId))
                if self.showFileName:
                    result['field'] = result['field'] + (
                        '<dtml-var "file_object.getId()">')
                else:
                    result['field'] = result['field'] + 'Download'
                result['field'] = result['field'] + '</a>'
                if self.showFileSize:
                    result['field'] = result['field'] + (
                        '''<br /><dtml-var "'%%0.2f' %% ('''
                        '''float(file_object.get_size()) / 1024)">kB''')
                if self.showFileType:
                    result['field'] = result['field'] + (
                        '<br /><dtml-var "file_object.getContentType()">')
                result['field'] = result['field'] + (
                    '''<br /><input type="checkbox" name="%s_del"'''
                    ''' id="%s_del" value="1"> <label for="%s_del">'''
                    '''Delete file</label><dtml-else><em>n/a</em></dtml-if>'''
                    '''</dtml-let>''' % (
                        fieldId, fieldId, fieldId))
        return result

    # -------------------------------------------------------------------------

    addFormlet = 'manage_MetaFileWidget_AddFormlet'
    editFormlet = 'manage_MetaFileWidget_EditFormlet'
    listFormlet = 'manage_MetaFileWidget_ListFormlet'
    viewFormlet = 'manage_MetaFileWidget_ViewFormlet'


# -------------------------------------------------------------------


manage_MetaFileWidget_AddFormlet = DTMLFile(
    'dtml/MetaFileWidget_AddFormlet', globals())
manage_MetaFileWidget_EditFormlet = DTMLFile(
    'dtml/MetaFileWidget_EditFormlet', globals())
manage_MetaFileWidget_ListFormlet = DTMLFile(
    'dtml/MetaFileWidget_ListFormlet', globals())
manage_MetaFileWidget_ViewFormlet = DTMLFile(
    'dtml/MetaFileWidget_ViewFormlet', globals())


# =============================================================================


def manage_addMetaFileWidget(self, id, formTypeId, data={}, REQUEST=None):
    """Add new MetaFileWidget."""
    instance = MetaFileWidget(id)
    instance.setWidgetData(formTypeId, data)
    id = self._setObject(id, instance)
    if REQUEST is not None:
        REQUEST.RESPONSE.redirect(
            self.zmp2URL() + '/manage_interfacesBrowserForm')
