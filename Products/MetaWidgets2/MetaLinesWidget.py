"""==================================================================

                       M e t a   W i d g e t s
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
from Products.MetaPublisher2.Library import WidgetPlugin


# ===================================================================


class MetaLinesWidget(WidgetPlugin):
    """MetaLinesWidget"""

    meta_type = 'MetaLinesWidget'

    # ---------------------------------------------------------------

    pluginName = 'MetaLinesWidget'
    pluginAuthor = 'Sebastian Luehnsdorf - Web-Solutions GbR.'
    pluginVersion = '1.0.1'
    pluginInfo = (
        'Basic Web Interface that allows users to add new Entries.')

    formTypeIds = ['Add', 'Edit', 'View', 'List']
    fieldTypeIds = ['Lines']

    # ---------------------------------------------------------------

    displayMode = 'defaultMode'

    maxChars = 0
    maxCharsCount = 20

    align = 'left'
    alignOptions = ['left', 'center', 'right', 'justify']
    valign = 'top'
    valignOptions = ['top', 'middle', 'bottom']

    case = 'normal'
    caseOptions = ['normal', 'lower', 'upper', 'capitalize']
    quote = 'normal'
    quoteOptions = ['normal', 'html_quote', 'url_quote']

    inputCols = 50
    inputRows = 8
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
        {'id': 'inputCols', 'type': 'int', 'mode': 'w'},
        {'id': 'inputRows', 'type': 'int', 'mode': 'w'},
        {'id': 'inputClass', 'type': 'string', 'mode': 'w'},
        {'id': 'inputStyle', 'type': 'string', 'mode': 'w'},
    )

    # ---------------------------------------------------------------

    def getWidgetId(self):
        """Return Plugin Identifier"""
        return 'MetaWidgets.' + self.meta_type

    # ---------------------------------------------------------------

    def setWidgetData(self, formTypeId, data={}):
        """Configure Widget according to passed data"""
        if data.get('pluginId__', '') == self.getWidgetId():
            self.formTypeId = formTypeId
            self.displayMode = data['displayMode']
            self.maxChars = data.get('maxChars', None)
            self.maxCharsCount = data.get('maxCharsCount', 20)
            self.align = data.get('align', 'left')
            self.valign = data.get('valign', 'top')
            self.case = data.get('case', 'normal')
            self.quote = data.get('quote', 'normal')
            self.inputCols = data.get('inputCols', 50)
            self.inputRows = data.get('inputRows', 8)
            self.inputClass = data.get('inputClass', '')
            self.inputStyle = data.get('inputStyle', '')

        else:
            raise TypeError('Invalid Widget data: "%s" <> "%s"' % (
                self.getWidgetId(), data.get('pluginId__', '')))

    def getWidgetData(self, formTypeId):
        """Return the data of this Widget"""
        return {
            'pluginId__': 'MetaWidgets.' + self.meta_type,
            'displayMode': self.displayMode,
            'maxChars': self.maxChars and '1' or '0',
            'maxCharsCount': self.maxCharsCount,
            'align': self.align,
            'valign': self.valign,
            'case': self.case,
            'quote': self.quote,
            'inputCols': self.inputCols,
            'inputRows': self.inputRows,
            'inputClass': self.inputClass,
            'inputStyle': self.inputStyle
        }

    # ---------------------------------------------------------------

    def renderWidget(self, elementId, field, entryName=''):
        """Render widget according to configuration"""
        fieldId = field.getId()
        formTypeId = self.formTypeId
        displayMode = self.displayMode
        result = {
          'align': self.align,
          'valign': self.valign,
          'title': field.title or fieldId
          }

        def addInputOptions(self):
            options = ' cols="%s" rows="%s"' % (self.inputCols, self.inputRows)
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
                    '''<dtml-in "%s['%s']" prefix=line>'''
                    '''<dtml-var line_item''' % (entryName, fieldId) +
                    addShowOptions(self) +
                    '><dtml-unless line_end><br /></dtml-unless></dtml-in>')
            elif displayMode == 'showDefault':
                result['field'] = (
                    '''<dtml-in "getZMP2().getField('%s', '%s').default"'''
                    ''' prefix=line><dtml-var line_item''' % (
                        self.storageId, fieldId) +
                    addShowOptions(self) +
                    '''><dtml-unless line_end><br /></dtml-unless>'''
                    '''</dtml-in>''')
        elif formTypeId == 'View':
            if displayMode == 'defaultMode':
                result['field'] = (
                    '''<dtml-in "%s['%s']" prefix=line>'''
                    '''<dtml-var line_item''' % (entryName, fieldId) +
                    addShowOptions(self) +
                    '''><dtml-unless line_end><br /></dtml-unless>'''
                    '''</dtml-in>''')
            elif displayMode == 'showDefault':
                result['field'] = (
                    '''<dtml-in "getZMP2().getField('%s', '%s').default" '''
                    '''prefix=line><dtml-var line_item''' % (
                        self.storageId, fieldId) +
                    addShowOptions(self) +
                    '''><dtml-unless line_end><br /></dtml-unless>'''
                    '''</dtml-in>''')
        elif formTypeId == 'Add':
            if displayMode == 'defaultMode':
                result['field'] = (
                    '''<textarea name="%s"''' % fieldId +
                    addInputOptions(self) +
                    '''><dtml-in "getZMP2().getField('%s', '%s').default"'''
                    ''' prefix=line><dtml-var line_item>\n</dtml-in>'''
                    '''</textarea>''' % (self.storageId, fieldId))
            elif displayMode == 'inputEmpty':
                result['field'] = (
                    '''<textarea name="%s"''' % fieldId +
                    addInputOptions(self) + '''></textarea>''')
            elif displayMode == 'showDefault':
                result['field'] = (
                    '''<dtml-in "getZMP2().getField('%s', '%s').default"'''
                    ''' prefix=line><dtml-var line_item''' % (
                        self.storageId, fieldId) +
                    addShowOptions(self) +
                    '''><dtml-unless line_end><br /></dtml-unless>'''
                    '''</dtml-in>''')
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
                    '''<textarea name="%s"''' % fieldId +
                    addInputOptions(self) +
                    '''><dtml-in "%s['%s']" prefix=line>'''
                    '''<dtml-var line_item>\n</dtml-in></textarea>''' % (
                        entryName, fieldId))
            elif displayMode == 'inputDefault':
                result['field'] = (
                    '''<textarea name="%s"''' % fieldId +
                    addInputOptions(self) +
                    '''><dtml-in "getZMP2().getField('%s', '%s').default"'''
                    ''' prefix=line><dtml-var line_item>\n</dtml-in>'''
                    '''</textarea>''' % (self.storageId, fieldId))
            elif displayMode == 'inputEmpty':
                result['field'] = (
                    '''<textarea name="%s"''' % fieldId +
                    addInputOptions(self) +
                    '''></textarea>''')
            elif displayMode == 'showValue':
                result['field'] = (
                    '''<dtml-in "%s['%s']" prefix=line>'''
                    '''<dtml-var line_item''' % (entryName, fieldId) +
                    addShowOptions(self) +
                    '''><dtml-unless line_end><br /></dtml-unless>'''
                    '''</dtml-in>''')
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
                    '''<dtml-in "getZMP2().getField('%s', '%s').default"'''
                    ''' prefix=line><dtml-var line_item''' % (
                        self.storageId, fieldId) +
                    addShowOptions(self) +
                    '''><dtml-unless line_end><br /></dtml-unless>'''
                    '''</dtml-in>''')
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

    addFormlet = 'manage_MetaLinesWidget_AddFormlet'
    editFormlet = 'manage_MetaLinesWidget_EditFormlet'
    listFormlet = 'manage_MetaLinesWidget_ListFormlet'
    viewFormlet = 'manage_MetaLinesWidget_ViewFormlet'


# -------------------------------------------------------------------


manage_MetaLinesWidget_AddFormlet = DTMLFile(
    'dtml/MetaLinesWidget_AddFormlet', globals())
manage_MetaLinesWidget_EditFormlet = DTMLFile(
    'dtml/MetaLinesWidget_EditFormlet', globals())
manage_MetaLinesWidget_ListFormlet = DTMLFile(
    'dtml/MetaLinesWidget_ListFormlet', globals())
manage_MetaLinesWidget_ViewFormlet = DTMLFile(
    'dtml/MetaLinesWidget_ViewFormlet', globals())


# =============================================================================


def manage_addMetaLinesWidget(self, id, formTypeId, data={}, REQUEST=None):
    """ZMI constructor for MetaLinesWidget"""
    instance = MetaLinesWidget(id)
    instance.setWidgetData(formTypeId, data)
    id = self._setObject(id, instance)
    if REQUEST is not None:
        REQUEST.RESPONSE.redirect(
            self.zmp2URL() + '/manage_interfacesBrowserForm')
