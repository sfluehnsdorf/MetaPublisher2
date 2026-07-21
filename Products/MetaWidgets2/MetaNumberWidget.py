"""Meta Widgets."""


from App.special_dtml import DTMLFile
from Products.MetaPublisher2.bases.widget.legacywidget import (
    LegacyWidgetPlugin as WidgetPlugin)


# =============================================================================


class MetaNumberWidget(WidgetPlugin):
    """MetaNumberWidget."""

    meta_type = 'MetaNumberWidget'

    # -------------------------------------------------------------------------

    pluginName = 'MetaNumberWidget'
    pluginAuthor = 'Sebastian Luehnsdorf - Web-Solutions GbR.'
    pluginVersion = '1.0.1'
    pluginInfo = 'Basic Web Interface that allows users to add new Entries.'

    formTypeIds = ['Add', 'Edit', 'View', 'List']
    fieldTypeIds = ['Integer', 'Long', 'Float', '', '', '', '', '']

    # -------------------------------------------------------------------------

    displayMode = 'defaultMode'

    align = 'right'
    alignOptions = ['left', 'center', 'right', 'justify']
    valign = 'top'
    valignOptions = ['top', 'middle', 'bottom']

    inputSize = 5
    inputClass = ''
    inputStyle = 'width: 100px; text-align: right;'

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
            self.align = data.get('align', 'right')
            self.valign = data.get('valign', 'top')
            self.inputSize = data.get('inputSize', 60)
            self.inputClass = data.get('inputClass', '')
            self.inputStyle = data.get('inputStyle', '')
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
                    '''<dtml-var "%s['%s']">''' % (entryName, fieldId))
            elif displayMode == 'showDefault':
                result['field'] = (
                    '''<dtml-var "getZMP2().getField('%s', '%s')'''
                    '''.default">''' % (
                        self.storageId, fieldId))
        elif formTypeId == 'View':
            if displayMode == 'defaultMode':
                result['field'] = (
                    '''<dtml-var "%s['%s']">''' % (entryName, fieldId))
            elif displayMode == 'showDefault':
                result['field'] = (
                    '''<dtml-var "getZMP2().getField('%s', '%s')'''
                    '''.default">''' % (self.storageId, fieldId))
        elif formTypeId == 'Add':
            if displayMode == 'defaultMode':
                result['field'] = (
                    '''<input type="text" name="%s"''' % fieldId +
                    addInputOptions(self) +
                    ''' value="<dtml-var "getZMP2().getField('''
                    """'%s', '%s' ).default">">""" % (self.storageId, fieldId))
            elif displayMode == 'inputEmpty':
                result['field'] = (
                    '''<input type="text" name="%s"''' % fieldId +
                    addInputOptions(self) + ''' value="">''')
            elif displayMode == 'showDefault':
                result['field'] = (
                    '''<dtml-var "getZMP2().getField('''
                    """'%s', '%s' ).default">""" % (self.storageId, fieldId))
                result['hidden'] = (
                    '''<input type="hidden" name="%s" value="'''
                    '''<dtml-var "getZMP2().getField('%s', '%s')'''
                    '''.default">">''' % (fieldId, self.storageId, fieldId))
            elif displayMode == 'hiddenDefault':
                result['hidden'] = (
                    '''<input type="hidden" name="%s" value="'''
                    '''<dtml-var "getZMP2().getField('%s', '%s')'''
                    '''.default">">''' % (fieldId, self.storageId, fieldId))
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
                    ''' value="<dtml-var "getZMP2().getField('%s', '%s')'''
                    '''.default">">''' % (self.storageId, fieldId))
            elif displayMode == 'inputEmpty':
                result['field'] = (
                    '''<input type="text" name="%s"''' % fieldId +
                    addInputOptions(self) +
                    ''' value="">''')
            elif displayMode == 'showValue':
                result['field'] = (
                    '''<dtml-var "%s['%s']">''' % (entryName, fieldId))
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
                    '''.default">''' % (
                        self.storageId, fieldId))
                result['hidden'] = (
                    '''<input type="hidden" name="%s" value="'''
                    '''<dtml-var "getZMP2().getField('%s', '%s')'''
                    '''.default">">''' % (
                        fieldId, self.storageId, fieldId))
            elif displayMode == 'hiddenDefault':
                result['hidden'] = (
                    '''<input type="hidden" name="%s" value="'''
                    '''<dtml-var "getZMP2().getField('%s', '%s')'''
                    '''.default">">''' % (fieldId, self.storageId, fieldId))
        return result

    # -------------------------------------------------------------------------

    addFormlet = 'manage_MetaNumberWidget_AddFormlet'
    editFormlet = 'manage_MetaNumberWidget_EditFormlet'
    listFormlet = 'manage_MetaNumberWidget_ListFormlet'
    viewFormlet = 'manage_MetaNumberWidget_ViewFormlet'


# -----------------------------------------------------------------------------


manage_MetaNumberWidget_AddFormlet = DTMLFile(
    'dtml/MetaNumberWidget_AddFormlet', globals())
manage_MetaNumberWidget_EditFormlet = DTMLFile(
    'dtml/MetaNumberWidget_EditFormlet', globals())
manage_MetaNumberWidget_ListFormlet = DTMLFile(
    'dtml/MetaNumberWidget_ListFormlet', globals())
manage_MetaNumberWidget_ViewFormlet = DTMLFile(
    'dtml/MetaNumberWidget_ViewFormlet', globals())


# =============================================================================


def manage_addMetaNumberWidget(self, id, formTypeId, data={}, REQUEST=None):
    """Add new MetaNumberWidget."""
    instance = MetaNumberWidget(id)
    instance.setWidgetData(formTypeId, data)
    id = self._setObject(id, instance)
    if REQUEST is not None:
        REQUEST.RESPONSE.redirect(
            self.zmp2URL() + '/manage_interfacesBrowserForm')
