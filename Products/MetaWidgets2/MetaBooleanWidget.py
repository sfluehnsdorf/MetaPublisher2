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


# =============================================================================


class MetaBooleanWidget(WidgetPlugin):
    """MetaBooleanWidget"""

    meta_type = 'MetaBooleanWidget'

    # -------------------------------------------------------------------------

    pluginName = 'MetaBooleanWidget'
    pluginAuthor = 'Sebastian Luehnsdorf - Web-Solutions GbR.'
    pluginVersion = '1.0.1'
    pluginInfo = 'Basic Web Interface that allows users to add new Entries.'

    formTypeIds = ['Add', 'Edit', 'View', 'List']
    fieldTypeIds = ['Boolean',]

    # -------------------------------------------------------------------------

    displayMode = 'defaultMode'

    labelTrue = ''
    labelFalse = ''

    align = 'left'
    alignOptions = ['left', 'center', 'right', 'justify']
    valign = 'top'
    valignOptions = ['top', 'middle', 'bottom']

    # -------------------------------------------------------------------------

    _properties = WidgetPlugin._properties + (
        {'id': 'displayMode', 'type': 'string', 'mode': 'w'},
        {'id': 'labelTrue', 'type': 'string', 'mode': 'w'},
        {'id': 'labelFalse', 'type': 'string', 'mode': 'w'},
        {
            'id': 'align', 'type': 'selection', 'mode': 'w',
            'select_variable': 'alignOptions'},
        {
            'id': 'valign', 'type': 'selection', 'mode': 'w',
            'select_variable': 'valignOptions'},
    )

    # -------------------------------------------------------------------------

    def getWidgetId(self):
        """Return Plugin Identifier"""
        return 'MetaWidgets.' + self.meta_type

    # -------------------------------------------------------------------------

    def setWidgetData(self, formTypeId, data={}):
        """Configure Widget according to passed data"""
        if data.get('pluginId__', '') == self.getWidgetId():
            self.formTypeId = formTypeId
            self.displayMode = data['displayMode']
            self.labelTrue = data.get('labelTrue', '')
            self.labelFalse = data.get('labelFalse', '')
            self.align = data.get('align', 'left')
            self.valign = data.get('valign', 'top')
        else:
            raise TypeError('Invalid Widget data: "%s" <> "%s"' % (
                self.getWidgetId(), data.get('pluginId__', '')))

    def getWidgetData(self, formTypeId):
        """Return the data of this Widget"""
        return {
            'pluginId__':  'MetaWidgets.' + self.meta_type,
            'displayMode': self.displayMode,
            'labelTrue': self.labelTrue,
            'labelFalse': self.labelFalse,
            'align': self.align,
            'valign': self.valign
        }

    # -------------------------------------------------------------------------

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

        if formTypeId == 'List':
            if displayMode == 'defaultMode':
                result['field'] = (
                    '''<dtml-if "%s['%s']">%s<dtml-else>%s</dtml-if>''' % (
                        entryName, fieldId, self.labelTrue, self.labelFalse))
            elif displayMode == 'showDefault':
                result['field'] = (
                    '''<dtml-if "getZMP2().getField( '%s', '%s' ).default">'''
                    '''%s<dtml-else>%s</dtml-if>''' % (
                        self.storageId, fieldId, self.labelTrue,
                        self.labelFalse))
        elif formTypeId == 'View':
            if displayMode == 'defaultMode':
                result['field'] = (
                    '''<dtml-if "%s['%s']">%s<dtml-else>%s</dtml-if>''' % (
                        entryName, fieldId, self.labelTrue, self.labelFalse))
            elif displayMode == 'showDefault':
                result['field'] = (
                    '''<dtml-if "getZMP2().getField( '%s', '%s' ).default">'''
                    '''%s<dtml-else>%s</dtml-if>''' % (
                        self.storageId, fieldId, self.labelTrue,
                        self.labelFalse))
        elif formTypeId == 'Add':
            if displayMode == 'defaultMode':
                result['field'] = (
                    '''<input type="radio" name="%s" id="%s1" value="1"'''
                    '''<dtml-if "getZMP2().getField( '%s', '%s' ).default">'''
                    ''' checked</dtml-if>> <label for="%s1">%s</label> '''
                    '''<input type="radio" name="%s" id="%s2" value="0"'''
                    '''<dtml-unless "getZMP2().getField( '%s', '%s' )'''
                    '''.default"> checked</dtml-unless>> <label for="%s2">'''
                    '''%s</label>''' % (
                        fieldId, fieldId, self.storageId, fieldId, fieldId,
                        self.labelTrue, fieldId, fieldId, self.storageId,
                        fieldId, fieldId, self.labelFalse))
            elif displayMode == 'inputTrue':
                result['field'] = (
                    '''<input type="radio" name="%s" id="%s1" value="1"'''
                    ''' checked> <label for="%s1">%s</label> '''
                    '''<input type="radio" name="%s" id="%s2" value="0"> '''
                    '''<label for="%s2">%s</label>''' % (
                        fieldId, fieldId, fieldId, self.labelTrue, fieldId,
                        fieldId, fieldId, self.labelFalse))
            elif displayMode == 'inputFalse':
                result['field'] = (
                    '''<input type="radio" name="%s" id="%s1" value="1"> '''
                    '''<label for="%s1">%s</label> <input type="radio" '''
                    '''name="%s" id="%s2" value="0" checked> <label '''
                    '''for="%s2">%s</label>''' % (
                        fieldId, fieldId, fieldId, self.labelTrue, fieldId,
                        fieldId, fieldId, self.labelFalse))
            elif displayMode == 'showDefault':
                result['field'] = (
                    '''<dtml-if "getZMP2().getField( '%s', '%s' ).default">'''
                    '''%s<dtml-else>%s</dtml-if>''' % (
                        self.storageId, fieldId, self.labelTrue,
                        self.labelFalse))
                result['hidden'] = (
                    '''<input type="hidden" name="%s" value="'''
                    '''<dtml-if "getZMP2().getField( '%s', '%s' ).default">1'''
                    '''<dtml-else>0</dtml-if>">''' % (
                        fieldId, self.storageId, fieldId))
            elif displayMode == 'hiddenDefault':
                result['hidden'] = (
                    '''<input type="hidden" name="%s" value="'''
                    '''<dtml-if "getZMP2().getField( '%s', '%s' ).default">1'''
                    '''<dtml-else>0</dtml-if>">''' % (
                        fieldId, self.storageId, fieldId))
            elif displayMode == 'showTrue':
                result['field'] = self.labelTrue
                result['hidden'] = (
                    '<input type="hidden" name="%s" value="1">' % fieldId)
            elif displayMode == 'hiddenTrue':
                result['hidden'] = (
                    '<input type="hidden" name="%s" value="1">' % fieldId)
            elif displayMode == 'showFalse':
                result['field'] = self.labelFalse
                result['hidden'] = (
                    '<input type="hidden" name="%s" value="0">' % fieldId)
            elif displayMode == 'hiddenFalse':
                result['hidden'] = (
                    '<input type="hidden" name="%s" value="0">' % fieldId)
        elif formTypeId == 'Edit':
            if displayMode == 'defaultMode':
                result['field'] = (
                    '''<input type="radio" name="%s" id="%s1" value="1"'''
                    '''<dtml-if "%s['%s']"> checked</dtml-if>> '''
                    '''<label for="%s1">%s</label> <input type="radio"'''
                    ''' name="%s" id="%s2" value="0"<dtml-unless "%s['%s']">'''
                    ''' checked</dtml-unless>> <label for="%s2">%s'''
                    '''</label>''' % (
                        fieldId, fieldId, entryName, fieldId, fieldId,
                        self.labelTrue, fieldId, fieldId, entryName, fieldId,
                        fieldId, self.labelFalse))
            elif displayMode == 'inputDefault':
                result['field'] = (
                    '''<input type="radio" name="%s" id="%s1" value="1"'''
                    '''<dtml-if "getZMP2().getField( '%s', '%s' ).default"> '''
                    '''checked</dtml-if>> <label for="%s1">%s</label> '''
                    '''<input type="radio" name="%s" id="%s2" value="0"'''
                    '''<dtml-unless "getZMP2().getField( '%s', '%s' )'''
                    '''.default"> checked</dtml-unless>> <label for="%s2">'''
                    '''%s</label>''' % (
                        fieldId, fieldId, self.storageId, fieldId, fieldId,
                        self.labelTrue, fieldId, fieldId, self.storageId,
                        fieldId, fieldId, self.labelFalse))
            elif displayMode == 'inputTrue':
                result['field'] = (
                    '''<input type="radio" name="%s" id="%s1" value="1"'''
                    ''' checked> <label for="%s1">%s</label> '''
                    '''<input type="radio" name="%s" id="%s2" value="0"> '''
                    '''<label for="%s2">%s</label>''' % (
                        fieldId, fieldId, fieldId, self.labelTrue, fieldId,
                        fieldId, fieldId, self.labelFalse))
            elif displayMode == 'inputFalse':
                result['field'] = (
                    '''<input type="radio" name="%s" id="%s1" value="1"> '''
                    '''<label for="%s1">%s</label> <input type="radio"'''
                    ''' name="%s" id="%s2" value="0" checked> '''
                    '''<label for="%s2">%s</label>''' % (
                        fieldId, fieldId, fieldId, self.labelTrue, fieldId,
                        fieldId, fieldId, self.labelFalse))
            elif displayMode == 'showValue':
                result['field'] = (
                    '''<dtml-if "%s['%s']">%s<dtml-else>%s</dtml-if>''' % (
                        entryName, fieldId, self.labelTrue, self.labelFalse))
                result['hidden'] = (
                    '''<input type="hidden" name="%s" value="'''
                    '''<dtml-if "%s['%s']">1<dtml-else>0</dtml-if>">''' % (
                        fieldId, entryName, fieldId))
            elif displayMode == 'hiddenValue':
                result['hidden'] = (
                    '''<input type="hidden" name="%s" value="'''
                    '''<dtml-if "%s['%s']">1<dtml-else>0</dtml-if>">''' % (
                        fieldId, entryName, fieldId))
            elif displayMode == 'showDefault':
                result['field'] = (
                    '''<dtml-if "getZMP2().getField( '%s', '%s' ).default">'''
                    '''%s<dtml-else>%s</dtml-if>''' % (
                        self.storageId, fieldId, self.labelTrue,
                        self.labelFalse))
                result['hidden'] = (
                    '''<input type="hidden" name="%s" value="'''
                    '''<dtml-if "getZMP2().getField( '%s', '%s' ).default">1'''
                    '''<dtml-else>0</dtml-if>">''' % (
                        fieldId, self.storageId, fieldId))
            elif displayMode == 'hiddenDefault':
                result['hidden'] = (
                    '''<input type="hidden" name="%s" value="'''
                    '''<dtml-if "getZMP2().getField( '%s', '%s' ).default">1'''
                    '''<dtml-else>0</dtml-if>">''' % (
                        fieldId, self.storageId, fieldId))
            elif displayMode == 'showTrue':
                result['field'] = self.labelTrue
                result['hidden'] = (
                    '<input type="hidden" name="%s" value="1">' % fieldId)
            elif displayMode == 'hiddenTrue':
                result['hidden'] = (
                    '<input type="hidden" name="%s" value="1">' % fieldId)
            elif displayMode == 'showFalse':
                result['field'] = self.labelFalse
                result['hidden'] = (
                    '<input type="hidden" name="%s" value="0">' % fieldId)
            elif displayMode == 'hiddenFalse':
                result['hidden'] = (
                    '<input type="hidden" name="%s" value="0">' % fieldId)
        return result

    # -------------------------------------------------------------------------

    addFormlet = 'manage_MetaBooleanWidget_AddFormlet'
    editFormlet = 'manage_MetaBooleanWidget_EditFormlet'
    listFormlet = 'manage_MetaBooleanWidget_ListFormlet'
    viewFormlet = 'manage_MetaBooleanWidget_ViewFormlet'


# -----------------------------------------------------------------------------


manage_MetaBooleanWidget_AddFormlet = DTMLFile(
    'dtml/MetaBooleanWidget_AddFormlet', globals())
manage_MetaBooleanWidget_EditFormlet = DTMLFile(
    'dtml/MetaBooleanWidget_EditFormlet', globals())
manage_MetaBooleanWidget_ListFormlet = DTMLFile(
    'dtml/MetaBooleanWidget_ListFormlet', globals())
manage_MetaBooleanWidget_ViewFormlet = DTMLFile(
    'dtml/MetaBooleanWidget_ViewFormlet', globals())


# =============================================================================


def manage_addMetaBooleanWidget(self, id, formTypeId, data={}, REQUEST=None):
    """ZMI constructor for MetaBooleanWidget"""
    instance = MetaBooleanWidget(id)
    instance.setWidgetData(formTypeId, data)
    id = self._setObject(id, instance)
    if REQUEST is not None:
        REQUEST.RESPONSE.redirect(
            self.zmp2URL() + '/manage_interfacesBrowserForm')
