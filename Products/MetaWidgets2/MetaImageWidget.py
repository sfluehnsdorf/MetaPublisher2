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


class MetaImageWidget(WidgetPlugin):
    """MetaImageWidget"""

    meta_type = 'MetaImageWidget'

    # -------------------------------------------------------------------------

    pluginName = 'MetaImageWidget'
    pluginAuthor = 'Sebastian Luehnsdorf - Web-Solutions GbR.'
    pluginVersion = '1.0.1'
    pluginInfo = 'Basic Web Interface that allows users to add new Entries.'

    formTypeIds = ['Add', 'Edit', 'View', 'List']
    fieldTypeIds = ['Image', 'File']

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

    showImageName = 0
    showImageSize = 0
    showImageType = 0

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
        {'id': 'showImageName', 'type': 'boolean', 'mode': 'w'},
        {'id': 'showImageSize', 'type': 'boolean', 'mode': 'w'},
        {'id': 'showImageType', 'type': 'boolean', 'mode': 'w'},
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
            self.align = data.get('align', 'left')
            self.valign = data.get('valign', 'top')
            self.inputSize = data.get('inputSize', 60)
            self.inputClass = data.get('inputClass', '')
            self.inputStyle = data.get('inputStyle', '')
            self.showImageName = data.get('showImageName', 0)
            self.showImageSize = data.get('showImageSize', 0)
            self.showImageType = data.get('showImageType', 0)
        else:
            raise TypeError('Invalid Widget data: "%s" <> "%s"' % (
                self.getWidgetId(), data.get('pluginId__', '')))

    def getWidgetData(self, formTypeId):
        """Return the data of this Widget"""
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
            options = ' size="%s"' % self.inputSize
            if self.inputClass:
                options = options + ' class="%s"' % self.inputClass
            if self.inputStyle:
                options = options + ' style="%s"' % self.inputStyle
            return options

        if formTypeId == 'List':
            result['field'] = (
                '''<dtml-let image_object="%s['%s']">'''
                '''<dtml-if image_object>''' % (entryName, fieldId))
            if displayMode == 'defaultMode':
                result['field'] = result['field'] + (
                    '''<dtml-var "getZMP2().getField('%s', '%s')'''
                    '''.getThumbnailTag(%s['entryId__'])">''' % (
                        self.storageId, fieldId, entryName))
            elif displayMode == 'showImage':
                result['field'] = result['field'] + (
                    '<dtml-var "image_object.tag()">')
            elif displayMode == 'showInfo':
                result['field'] = result['field'] + (
                    '''<a target="_blank" href="'''
                    '''<dtml-var "image_object.absolute_url()">">'''
                    '''View Image</a>''')
            if self.showImageName:
                result['field'] = result['field'] + (
                    '''<br /><dtml-var "image_object.getId()">''')
            if self.showImageSize:
                result['field'] = result['field'] + (
                    '''<br /><dtml-var "'%%0.2f' %% ('''
                    '''float(image_object.get_size()) / 1024 )">kB''')
            if self.showImageType:
                result['field'] = result['field'] + (
                    '''<br /><dtml-var "image_object.getContentType()">''')
            result['field'] = result['field'] + (
                '''<dtml-else><em>n/a</em></dtml-if></dtml-let>''')
        elif formTypeId == 'View':
            result['field'] = (
                '''<dtml-let image_object="%s['%s']">'''
                '''<dtml-if image_object>''' % (entryName, fieldId))
            if displayMode == 'defaultMode':
                result['field'] = result['field'] + (
                    '''<dtml-var "getZMP2().getField('%s', '%s')'''
                    '''.getThumbnailTag(%s['entryId__'])">''' % (
                        self.storageId, fieldId, entryName))
            elif displayMode == 'showImage':
                result['field'] = result['field'] + (
                    '<dtml-var "image_object.tag()">')
            elif displayMode == 'showInfo':
                result['field'] = result['field'] + (
                    '''<a target="_blank" href="'''
                    '''<dtml-var "image_object.absolute_url()">">'''
                    '''View Image</a>''')
            if self.showImageName:
                result['field'] = result['field'] + (
                    '''<br /><dtml-var "image_object.getId()">''')
            if self.showImageSize:
                result['field'] = result['field'] + (
                    '''<br /><dtml-var "'%%0.2f' %% ('''
                    '''float(image_object.get_size()) / 1024 )">kB''')
            if self.showImageType:
                result['field'] = result['field'] + (
                    '''<br /><dtml-var "image_object.getContentType()">''')
            result['field'] = result['field'] + (
                '''<dtml-else><em>n/a</em></dtml-if></dtml-let>''')
        elif formTypeId == 'Add':
            if displayMode == 'defaultMode':
                result['field'] = (
                    '''<input type="file" name="%s" id="%s" value=""''' % (
                        fieldId, fieldId) +
                    addInputOptions(self) + '>')
        elif formTypeId == 'Edit':
            result['field'] = (
                '''<input type="file" name="%s" id="%s" value=""''' % (
                    fieldId, fieldId) +
                addInputOptions(self) + '''><br />''')
            result['field'] = result['field'] + (
                '''<dtml-let image_object="%s['%s']">'''
                '''<dtml-if image_object>''' % (entryName, fieldId))
            if displayMode == 'defaultMode':
                result['field'] = result['field'] + (
                    '''<dtml-var "getZMP2().getField('%s', '%s')'''
                    '''.getThumbnailTag(%s['entryId__'])">''' % (
                        self.storageId, fieldId, entryName))
            elif displayMode == 'showImage':
                result['field'] = result['field'] + (
                    '<dtml-var "image_object.tag()">')
            elif displayMode == 'showInfo':
                result['field'] = result['field'] + (
                    '''<a target="_blank" href="'''
                    '''<dtml-var "image_object.absolute_url()">">'''
                    '''View Image</a>''')
            if self.showImageName:
                result['field'] = result['field'] + (
                    '''<br /><dtml-var "image_object.getId()">''')
            if self.showImageSize:
                result['field'] = result['field'] + (
                    '''<br /><dtml-var "'%%0.2f' %% ('''
                    '''float(image_object.get_size()) / 1024 )">kB''')
            if self.showImageType:
                result['field'] = result['field'] + (
                    '''<br /><dtml-var "image_object.getContentType()">''')
            result['field'] = result['field'] + (
                '''<br /><input type="checkbox" name="%s_del" id="%s_del"'''
                ''' value="1"> <label for="%s_del">Delete file</label>''' % (
                    fieldId, fieldId, fieldId))
            result['field'] = result['field'] + (
                '''<dtml-else><em>n/a</em></dtml-if></dtml-let>''')
        return result

    # -------------------------------------------------------------------------

    addFormlet = 'manage_MetaImageWidget_AddFormlet'
    editFormlet = 'manage_MetaImageWidget_EditFormlet'
    listFormlet = 'manage_MetaImageWidget_ListFormlet'
    viewFormlet = 'manage_MetaImageWidget_ViewFormlet'


# -----------------------------------------------------------------------------


manage_MetaImageWidget_AddFormlet = DTMLFile(
    'dtml/MetaImageWidget_AddFormlet', globals())
manage_MetaImageWidget_EditFormlet = DTMLFile(
    'dtml/MetaImageWidget_EditFormlet', globals())
manage_MetaImageWidget_ListFormlet = DTMLFile(
    'dtml/MetaImageWidget_ListFormlet', globals())
manage_MetaImageWidget_ViewFormlet = DTMLFile(
    'dtml/MetaImageWidget_ViewFormlet', globals())


# =============================================================================


def manage_addMetaImageWidget(self, id, formTypeId, data={}, REQUEST=None):
    """ZMI constructor for MetaImageWidget"""
    instance = MetaImageWidget(id)
    instance.setWidgetData(formTypeId, data)
    id = self._setObject(id, instance)
    if REQUEST is not None:
        REQUEST.RESPONSE.redirect(
            self.zmp2URL() + '/manage_interfacesBrowserForm')
