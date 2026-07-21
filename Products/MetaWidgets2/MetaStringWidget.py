"""Meta Widgets."""


from App.special_dtml import DTMLFile
from Products.MetaPublisher2.bases.widget.legacywidget import (
    LegacyWidgetPlugin as WidgetPlugin)


# ===================================================================


class MetaStringWidget(WidgetPlugin):
    """MetaStringWidget."""

    meta_type = 'MetaStringWidget'

    # ---------------------------------------------------------------

    pluginName = 'MetaStringWidget'
    pluginAuthor = 'Sebastian Luehnsdorf - Web-Solutions GbR.'
    pluginVersion = '1.0.1'
    pluginInfo = (
        'Basic Web Interface that allows users to add new Entries.')

    formTypeIds = ['Add', 'Edit', 'View', 'List']
    fieldTypeIds = ['String', 'Text']

    # ---------------------------------------------------------------

    displayMode = 'defaultMode'

    maxChars = 0
    maxCharsCount = 50

    align = 'left'
    alignOptions = ['left', 'center', 'right', 'justify']
    valign = 'top'
    valignOptions = ['top', 'middle', 'bottom']

    case = 'normal'
    caseOptions = ['normal', 'lower', 'upper', 'capitalize']
    quote = 'normal'
    quoteOptions = ['normal', 'html_quote', 'url_quote']

    inputSize = 60
    inputClass = ''
    inputStyle = ''

    # ---------------------------------------------------------------

    _properties = WidgetPlugin._properties + (
        {'id': 'displayMode', 'type': 'string', 'mode': 'w'},
        {'id': 'maxChars', 'type': 'boolean', 'mode': 'w'},
        {'id': 'maxCharsCount', 'type': 'int', 'mode': 'w'},
        {
            'id': 'align', 'type': 'selection', 'mode': 'w',
            'select_variable': 'alignOptions'},
        {
            'id': 'valign', 'type': 'selection', 'mode': 'w',
            'select_variable': 'valignOptions'},
        {
            'id': 'case', 'type': 'selection', 'mode': 'w',
            'select_variable': 'caseOptions'},
        {
            'id': 'quote', 'type': 'selection', 'mode': 'w',
            'select_variable': 'quoteOptions'},
        {'id': 'inputSize', 'type': 'int', 'mode': 'w'},
        {'id': 'inputClass', 'type': 'string', 'mode': 'w'},
        {'id': 'inputStyle', 'type': 'string', 'mode': 'w'},
    )

    # ---------------------------------------------------------------

    def getWidgetId(self):
        """Return Plugin Identifier."""
        return 'MetaWidgets.' + self.meta_type

    # ---------------------------------------------------------------

    def setWidgetData(self, formTypeId, data={}):
        """Configure Widget according to passed data."""
        if data.get('pluginId__', '') == self.getWidgetId():
            self.formTypeId = formTypeId
            self.displayMode = data['displayMode']
            self.maxChars = data.get('maxChars', None)
            self.maxCharsCount = data.get('maxCharsCount', 50)
            self.align = data.get('align', 'left')
            self.valign = data.get('valign', 'top')
            self.case = data.get('case', 'normal')
            self.quote = data.get('quote', 'normal')
            self.inputSize = data.get('inputSize', 60)
            self.inputClass = data.get('inputClass', '')
            self.inputStyle = data.get('inputStyle', '')
        else:
            raise TypeError(
                'Invalid Widget data: "%s" <> "%s"' % (
                    self.getWidgetId(), data.get('pluginId__', '')))

    def getWidgetData(self, formTypeId):
        """Return the data of this Widget."""
        return {
            'pluginId__':  'MetaWidgets.' + self.meta_type,
            'displayMode': self.displayMode,
            'maxChars': self.maxChars and '1' or '0',
            'maxCharsCount': self.maxCharsCount,
            'align': self.align,
            'valign': self.valign,
            'case': self.case,
            'quote': self.quote,
            'inputSize': self.inputSize,
            'inputClass': self.inputClass,
            'inputStyle': self.inputStyle,
        }

    # ---------------------------------------------------------------

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

        def addShowOptions(self):
            options = ''
            if self.maxChars:
                options = options + ' size=%s' % self.maxCharsCount
            if self.case != 'normal':
                options = options + ' ' + self.case
            if self.quote != 'normal':
                options = options + ' ' + self.quote
            return options

        if formTypeId == 'List':
            if displayMode == 'defaultMode':
                result['field'] = (
                    '''<dtml-var "%s['%s']"''' % (
                        entryName, fieldId) + addShowOptions(self) + '>')
            elif displayMode == 'showDefault':
                result['field'] = (
                    '''<dtml-var "getZMP2().getField('%s', '%s')'''
                    '''.default"''' % (
                        self.storageId, fieldId) + addShowOptions(self) + '>')
        elif formTypeId == 'View':
            if displayMode == 'defaultMode':
                result['field'] = (
                    '''<dtml-var "%s['%s']"''' % (
                        entryName, fieldId) + addShowOptions(self) + '>')
            elif displayMode == 'showDefault':
                result['field'] = (
                    '''<dtml-var "getZMP2().getField('%s', '%s')'''
                    '''.default"''' % (
                        self.storageId, fieldId) + addShowOptions(self) + '>')
        elif formTypeId == 'Add':
            if displayMode == 'defaultMode':
                result['field'] = (
                    '''<input type="text" name="%s"''' % fieldId +
                    addInputOptions(self) +
                    ''' value="<dtml-var "getZMP2().getField('''
                    """'%s', '%s').default">">""" % (
                        self.storageId, fieldId))
            elif displayMode == 'inputEmpty':
                result['field'] = (
                    '''<input type="text" name="%s"''' % fieldId +
                    addInputOptions(self) + ''' value="">''')
            elif displayMode == 'showDefault':
                result['field'] = (
                    '''<dtml-var "getZMP2().getField('%s', '%s')'''
                    '''.default"''' % (
                        self.storageId, fieldId) + addShowOptions(self) + '>')
                result['hidden'] = (
                    '''<input type="hidden" name="%s" value="'''
                    '''<dtml-var "getZMP2().getField('%s', '%s')'''
                    '''.default">">''' % (
                        fieldId, self.storageId, fieldId))
            elif displayMode == 'hiddenDefault':
                result['hidden'] = (
                    '''<input type="hidden" name="%s" value="'''
                    '''<dtml-var "getZMP2().getField('%s', '%s')'''
                    '''.default">">''' % (
                        fieldId, self.storageId, fieldId))
        elif formTypeId == 'Edit':
            if displayMode == 'defaultMode':
                result['field'] = (
                    '''<input type="text" name="%s"''' % fieldId +
                    addInputOptions(self) +
                    ''' value="<dtml-var "%s['%s']">">''' % (
                        entryName, fieldId))
            elif displayMode == 'inputDefault':
                result['field'] = (
                    '''<input type="text" name="%s"''' % fieldId +
                    addInputOptions(self) +
                    ''' value="<dtml-var "getZMP2().getField(%s', '%s')'''
                    '''.default">">''' % (
                        self.storageId, fieldId))
            elif displayMode == 'inputEmpty':
                result['field'] = (
                    '''<input type="text" name="%s"''' % fieldId +
                    addInputOptions(self) + ''' value="">''')
            elif displayMode == 'showValue':
                result['field'] = (
                    '''<dtml-var "%s['%s']"''' % (
                        entryName, fieldId) + addShowOptions(self) + '>')
                result['hidden'] = (
                    '''<input type="hidden" name="%s" value="'''
                    '''<dtml-var "%s['%s']">">''' % (
                        fieldId, entryName, fieldId))
            elif displayMode == 'hiddenValue':
                result['hidden'] = (
                    '''<input type="hidden" name="%s" value="'''
                    '''<dtml-var "%s['%s']">">''' % (
                        fieldId, entryName, fieldId))
            elif displayMode == 'showDefault':
                result['field'] = (
                    '''<dtml-var "getZMP2().getField('%s', '%s')'''
                    '''.default"''' % (
                        self.storageId, fieldId) + addShowOptions(self) + '>')
                result['hidden'] = (
                    '''<input type="hidden" name="%s" value="'''
                    '''<dtml-var "getZMP2().getField('%s', '%s')'''
                    '''.default">">''' % (
                        fieldId, self.storageId, fieldId))
            elif displayMode == 'hiddenDefault':
                result['hidden'] = (
                    '''<input type="hidden" name="%s" value="'''
                    '''<dtml-var "getZMP2().getField('%s', '%s')'''
                    '''.default">">''' % (
                        fieldId, self.storageId, fieldId))
        return result

    # ---------------------------------------------------------------

    addFormlet = 'manage_MetaStringWidget_AddFormlet'
    editFormlet = 'manage_MetaStringWidget_EditFormlet'
    listFormlet = 'manage_MetaStringWidget_ListFormlet'
    viewFormlet = 'manage_MetaStringWidget_ViewFormlet'


# -------------------------------------------------------------------


manage_MetaStringWidget_AddFormlet = DTMLFile(
    'dtml/MetaStringWidget_AddFormlet', globals())
manage_MetaStringWidget_EditFormlet = DTMLFile(
    'dtml/MetaStringWidget_EditFormlet', globals())
manage_MetaStringWidget_ListFormlet = DTMLFile(
    'dtml/MetaStringWidget_ListFormlet', globals())
manage_MetaStringWidget_ViewFormlet = DTMLFile(
    'dtml/MetaStringWidget_ViewFormlet', globals())


# ===================================================================


def manage_addMetaStringWidget(
    self, id, formTypeId, data={}, REQUEST=None
):
    """Add new MetaStringWidget."""
    instance = MetaStringWidget(id)
    instance.setWidgetData(formTypeId, data)
    id = self._setObject(id, instance)
    if REQUEST is not None:
        REQUEST.RESPONSE.redirect(
            self.zmp2URL() + '/manage_interfacesBrowserForm')
