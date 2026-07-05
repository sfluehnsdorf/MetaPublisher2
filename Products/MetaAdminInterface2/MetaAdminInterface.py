"""==================================================================

               M e t a   A d m i n   I n t e r f a c e
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
from Products.MetaPublisher2.Library import (
    InterfacePlugin, standard_form_header, standard_form_footer)
from Products.PythonScripts.PythonScript import manage_addPythonScript


# =============================================================================

class MetaAdminInterface(InterfacePlugin):
    """MetaAdminInterface Base Class"""

    meta_type = 'MetaAdminInterface'

    # -------------------------------------------------------------------------

    pluginName = 'MetaAdminInterface'
    pluginAuthor = 'Sebastian Luehnsdorf - Web-Solutions GbR.'
    pluginVersion = '1.0.15'
    pluginInfo = (
        'Basic Web Interface that allows users to manage Entries. It creates '
        'forms and scripts for a list of entries, an add entry form, an edit '
        'entry form and a view entry form.')

    # -------------------------------------------------------------------------

    formTypes = ['DTMLDocument', 'DTMLMethod']

    # -------------------------------------------------------------------------

    storageId = ''
    formHeader = standard_form_header
    formFooter = standard_form_footer
    varPrefix = ''
    idPrefix = ''
    createFolder = 0
    createFolderId = ''

    listFormId = 'index_html'
    listFormTitle = 'List Entries'
    listFormType = 'DTMLMethod'
    listFormInfo = ''
    listFormAddButtonLabel = 'Add New Entry...'
    listFormEditLinkLabel = 'Edit'
    listFormViewLinkLabel = 'View'
    listFormDelButtonLabel = 'Delete'

    listFormOrder = 0
    listFormSort = 0
    listFormSortFields = []
    listFormSortVar = 'sortKey'
    listFormBatch = 0
    listFormBatchSizeVar = 'batchSize'
    listFormBatchStartVar = 'batchStart'
    listFormSession = 0
    deleteMethodId = 'delete'
    moveMethodId = 'move'

    addFormId = 'add.html'
    addFormTitle = 'Add Entry Form'
    addFormType = 'DTMLDocument'
    addFormInfo = ''
    addSubmitLabel = 'Add Entry'
    addCancelLabel = 'Cancel'
    addMethodId = 'add'

    editFormId = 'edit.html'
    editFormTitle = 'Edit Entry Form'
    editFormType = 'DTMLDocument'
    editFormInfo = ''
    editSubmitLabel = 'Save Changes'
    editCancelLabel = 'Cancel'
    editMethodId = 'edit'

    viewFormId = 'view.html'
    viewFormTitle = 'View Entry Form'
    viewFormType = 'DTMLDocument'
    viewFormInfo = ''
    viewBackLabel = 'Back'

    # -------------------------------------------------------------------------

    _properties = InterfacePlugin._properties + (

        {
            'id': 'storageId', 'type': 'selection', 'mode': 'w',
            'select_variable': 'getStorageIds'},
        {'id': 'formHeader', 'type': 'text', 'mode': 'w'},
        {'id': 'formFooter', 'type': 'text', 'mode': 'w'},
        {'id': 'varPrefix', 'type': 'string', 'mode': 'w'},
        {'id': 'idPrefix', 'type': 'string', 'mode': 'w'},
        {'id': 'createFolder', 'type': 'boolean', 'mode': 'w'},
        {'id': 'createFolderId', 'type': 'string', 'mode': 'w'},

        {'id': 'listFormId', 'type': 'string', 'mode': 'w'},
        {'id': 'listFormTitle', 'type': 'string', 'mode': 'w'},
        {
            'id': 'listFormType', 'type': 'selection', 'mode': 'w',
            'select_variable': 'formTypes'},
        {'id': 'listFormInfo', 'type': 'text', 'mode': 'w'},
        {'id': 'listFormOrder', 'type': 'boolean', 'mode': 'w'},
        {'id': 'listFormSort', 'type': 'boolean', 'mode': 'w'},
        {'id': 'listFormSortFields', 'type': 'lines', 'mode': 'w'},
        {'id': 'listFormSortVar', 'type': 'string', 'mode': 'w'},
        {'id': 'listFormBatch', 'type': 'boolean', 'mode': 'w'},
        {'id': 'listFormBatchSizeVar', 'type': 'string', 'mode': 'w'},
        {'id': 'listFormBatchStartVar', 'type': 'string', 'mode': 'w'},
        {'id': 'listFormAddButtonLabel', 'type': 'string', 'mode': 'w'},
        {'id': 'listFormEditLinkLabel', 'type': 'string', 'mode': 'w'},
        {'id': 'listFormViewLinkLabel', 'type': 'string', 'mode': 'w'},
        {'id': 'listFormDelButtonLabel', 'type': 'string', 'mode': 'w'},
        {'id': 'listFormSession', 'type': 'boolean', 'mode': 'w'},
        {'id': 'deleteMethodId', 'type': 'string', 'mode': 'w'},
        {'id': 'moveMethodId', 'type': 'string', 'mode': 'w'},

        {'id': 'addFormId', 'type': 'string', 'mode': 'w'},
        {'id': 'addFormTitle', 'type': 'string', 'mode': 'w'},
        {
            'id': 'addFormType', 'type': 'selection', 'mode': 'w',
            'select_variable': 'formTypes'},
        {'id': 'addFormInfo', 'type': 'text', 'mode': 'w'},
        {'id': 'addSubmitLabel', 'type': 'string', 'mode': 'w'},
        {'id': 'addCancelLabel', 'type': 'string', 'mode': 'w'},
        {'id': 'addMethodId', 'type': 'string', 'mode': 'w'},

        {'id': 'editFormId', 'type': 'string', 'mode': 'w'},
        {'id': 'editFormTitle', 'type': 'string', 'mode': 'w'},
        {
            'id': 'editFormType', 'type': 'selection', 'mode': 'w',
            'select_variable': 'formTypes'},
        {'id': 'editFormInfo', 'type': 'text', 'mode': 'w'},
        {'id': 'editSubmitLabel', 'type': 'string', 'mode': 'w'},
        {'id': 'editCancelLabel', 'type': 'string', 'mode': 'w'},
        {'id': 'editMethodId', 'type': 'string', 'mode': 'w'},

        {'id': 'viewFormId', 'type': 'string', 'mode': 'w'},
        {'id': 'viewFormTitle', 'type': 'string', 'mode': 'w'},
        {
            'id': 'viewFormType', 'type': 'selection', 'mode': 'w',
            'select_variable': 'formTypes'},
        {'id': 'viewFormInfo', 'type': 'text', 'mode': 'w'},
        {'id': 'viewBackLabel', 'type': 'string', 'mode': 'w'},

    )

    # -------------------------------------------------------------------------

    def configure(self, data):
        """Configure the Interface"""

        self.title = data.get('title', self.title)

        self.storageId = data.get('storageId', self.storageId)
        self.formHeader = data.get('formHeader', self.formHeader)
        self.formFooter = data.get('formFooter', self.formFooter)
        self.varPrefix = data.get('varPrefix', self.varPrefix)
        self.idPrefix = data.get('idPrefix', self.idPrefix)
        self.createFolder = int(data.get('createFolder', 0))
        self.createFolderId = data.get('createFolderId', self.createFolderId)

        self.listFormId = data.get('listFormId', self.listFormId)
        self.listFormTitle = data.get('listFormTitle', self.listFormTitle)
        self.listFormType = data.get('listFormType', self.listFormType)
        self.listFormInfo = data.get('listFormInfo', self.listFormInfo)
        self.listFormOrder = int(data.get('listFormOrder', 0))
        self.listFormSort = int(data.get('listFormSort', 0))
        self.listFormSortFields = data.get(
            'listFormSortFields', self.listFormSortFields)
        self.listFormSortVar = data.get(
            'listFormSortVar', self.listFormSortVar)
        self.listFormBatch = int(data.get('listFormBatch', 0))
        self.listFormBatchSizeVar = data.get(
            'listFormBatchSizeVar', self.listFormBatchSizeVar)
        self.listFormBatchStartVar = data.get(
            'listFormBatchStartVar', self.listFormBatchStartVar)
        self.listFormAddButtonLabel = data.get(
            'listFormAddButtonLabel', self.listFormAddButtonLabel)
        self.listFormEditLinkLabel = data.get(
            'listFormEditLinkLabel', self.listFormEditLinkLabel)
        self.listFormViewLinkLabel = data.get(
            'listFormViewLinkLabel', self.listFormViewLinkLabel)
        self.listFormDelButtonLabel = data.get(
            'listFormDelButtonLabel', self.listFormDelButtonLabel)
        self.listFormSession = int(data.get('listFormSession', 0))
        self.deleteMethodId = data.get('deleteMethodId', self.deleteMethodId)
        self.moveMethodId = data.get('moveMethodId', self.moveMethodId)

        self.addFormId = data.get('addFormId', self.addFormId)
        self.addFormTitle = data.get('addFormTitle', self.addFormTitle)
        self.addFormType = data.get('addFormType', self.addFormType)
        self.addFormInfo = data.get('addFormInfo', self.addFormInfo)
        self.addSubmitLabel = data.get('addSubmitLabel', self.addSubmitLabel)
        self.addCancelLabel = data.get('addCancelLabel', self.addCancelLabel)
        self.addMethodId = data.get('addMethodId', self.addMethodId)

        self.editFormId = data.get('editFormId', self.editFormId)
        self.editFormTitle = data.get('editFormTitle', self.editFormTitle)
        self.editFormType = data.get('editFormType', self.editFormType)
        self.editFormInfo = data.get('editFormInfo', self.editFormInfo)
        self.editSubmitLabel = data.get(
            'editSubmitLabel', self.editSubmitLabel)
        self.editCancelLabel = data.get(
            'editCancelLabel', self.editCancelLabel)
        self.editMethodId = data.get('editMethodId', self.editMethodId)

        self.viewFormId = data.get('viewFormId', self.viewFormId)
        self.viewFormTitle = data.get('viewFormTitle', self.viewFormTitle)
        self.viewFormType = data.get('viewFormType', self.viewFormType)
        self.viewFormInfo = data.get('viewFormInfo', self.viewFormInfo)
        self.viewBackLabel = data.get('viewBackLabel', self.viewBackLabel)

    # -------------------------------------------------------------------------

    def getStorageIds(self):
        """Return ids of all Storages"""
        return self.storageIds()

    def getInterfacePath(self):
        """Return the path of the Interface"""
        return self.absolute_url()[len(self.zmp2URL()) + 1:]

    # -------------------------------------------------------------------------

    def renderingIds(self):
        """Return list ids for objects created on rendering"""
        idPrefix = self.idPrefix
        if self.createFolder:
            idPrefix = self.createFolderId + '/' + idPrefix
        return [
            idPrefix + self.listFormId,
            idPrefix + self.deleteMethodId,
            idPrefix + self.moveMethodId,
            idPrefix + self.addFormId,
            idPrefix + self.addMethodId,
            idPrefix + self.editFormId,
            idPrefix + self.editMethodId,
            idPrefix + self.viewFormId
        ]

    def renderInterface(self, destination, **options):
        """Render the Interface"""
        data = {

            'storageId': self.storageId,
            'formHeader': self.formHeader,
            'formFooter': self.formFooter,
            'idPrefix': self.idPrefix,
            'varPrefix': self.varPrefix,
            'createFolder': self.createFolder,
            'createFolderId': self.createFolderId,

            'listFormId': self.listFormId,
            'listFormTitle': self.listFormTitle,
            'listFormType': self.listFormType,
            'listFormInfo': self.listFormInfo,
            'listFormOrder': self.listFormOrder,
            'listFormSort': self.listFormSort,
            'listFormSortFields': self.listFormSortFields,
            'listFormSortVar': self.varPrefix + self.listFormSortVar,
            'listFormBatch': self.listFormBatch,
            'listFormBatchSizeVar': self.varPrefix + self.listFormBatchSizeVar,
            'listFormBatchStartVar': (
                self.varPrefix + self.listFormBatchStartVar),
            'listFormAddButtonLabel': self.listFormAddButtonLabel,
            'listFormEditLinkLabel': self.listFormEditLinkLabel,
            'listFormViewLinkLabel': self.listFormViewLinkLabel,
            'listFormDelButtonLabel': self.listFormDelButtonLabel,
            'listFormSession': self.listFormSession,
            'deleteMethodId': self.deleteMethodId,
            'moveMethodId': self.moveMethodId,

            'addFormId': self.addFormId,
            'addFormTitle': self.addFormTitle,
            'addFormType': self.addFormType,
            'addFormInfo': self.addFormInfo,
            'addSubmitLabel': self.addSubmitLabel,
            'addCancelLabel': self.addCancelLabel,
            'addMethodId': self.addMethodId,

            'editFormId': self.editFormId,
            'editFormTitle': self.editFormTitle,
            'editFormType': self.editFormType,
            'editFormInfo': self.editFormInfo,
            'editSubmitLabel': self.editSubmitLabel,
            'editCancelLabel': self.editCancelLabel,
            'editMethodId': self.editMethodId,

            'viewFormId': self.viewFormId,
            'viewFormTitle': self.viewFormTitle,
            'viewFormType': self.viewFormType,
            'viewFormInfo': self.viewFormInfo,
            'viewBackLabel': self.viewBackLabel
        }

        # - - - - - - - - - - - - - - - - - - - - - - - - -
        # create destination Folder

        if data['createFolder']:
            destination.manage_addFolder(data['createFolderId'])
            destination = destination._getOb(data['createFolderId'])
            destination.title = data['listFormTitle']

        # - - - - - - - - - - - - - - - - - - - - - - - - -
        # create List Form

        source = '%(formHeader)s\n'
        if data['listFormInfo']:
            source = source + '<p class="info">%(listFormInfo)s</p>\n'
        source = source + (
            '<dtml-let zmp2=getZMP2 entryTuples="zmp2.entryItems('
            """%(storageId)s')" entryTuplesLen="len(entryTuples)">""")
        if data['listFormBatch']:
            if data['listFormSession']:
                source = source + (
                    '<dtml-if %(listFormBatchSizeVar)s>'
                    """<dtml-call "REQUEST.set('%(listFormBatchSizeVar)s',"""
                    """ int( %(listFormBatchSizeVar)s ) )">"""
                    """<dtml-call "REQUEST.SESSION.set("""
                    """'%(listFormBatchSizeVar)s',"""
                    """ int( %(listFormBatchSizeVar)s ) )">"""
                    '<dtml-else>'
                    """<dtml-call "REQUEST.set( '%(listFormBatchSizeVar)s', """
                    """REQUEST.SESSION.get('%(listFormBatchSizeVar)s',10))">"""
                    '</dtml-if>'

                    '<dtml-if %(listFormBatchStartVar)s>'
                    """<dtml-call "REQUEST.set('%(listFormBatchStartVar)s',"""
                    """ int( %(listFormBatchStartVar)s ) )">"""
                    """<dtml-call "REQUEST.SESSION.set("""
                    """'%(listFormBatchStartVar)s',"""
                    """ int(%(listFormBatchStartVar)s))">"""
                    '<dtml-else>'
                    """<dtml-call "REQUEST.set('%(listFormBatchStartVar)s', """
                    """REQUEST.SESSION.get('%(listFormBatchStartVar)s',1))">"""
                    '</dtml-if>'

                    '<dtml-in entryTuples start=%(listFormBatchStartVar)s'
                    ' size=%(listFormBatchSizeVar)s prefix=entry>'
                    '<dtml-if entry_end>'
                    """<dtml-call "REQUEST.set('batchEnd', entry_number)">"""
                    """<dtml-call "REQUEST.set('url', absolute_url() +"""
                    """ _['sequence-query'])">"""
                    '</dtml-if>'
                    '</dtml-in>'

                )
            else:
                source = source + (
                    '<dtml-if %(listFormBatchSizeVar)s>\n'
                    """<dtml-call "REQUEST.set('%(listFormBatchSizeVar)s',"""
                    """ int(%(listFormBatchSizeVar)s))">\n"""
                    '<dtml-else>\n'
                    """<dtml-call "REQUEST.set('%(listFormBatchSizeVar)s',"""
                    """ 10)">\n"""
                    '</dtml-if>\n'
                    '<dtml-if %(listFormBatchStartVar)s>\n'
                    """<dtml-call "REQUEST.set('%(listFormBatchStartVar)s',"""
                    """ int(%(listFormBatchStartVar)s))">\n"""
                    '<dtml-else>\n'
                    """<dtml-call "REQUEST.set('%(listFormBatchStartVar)s',"""
                    """ 1)">\n"""
                    '</dtml-if>\n'
                    '<dtml-in entryTuples start=%(listFormBatchStartVar)s'
                    ' size=%(listFormBatchSizeVar)s prefix=entry>\n'
                    '<dtml-if entry_end>\n'
                    """<dtml-call "REQUEST.set('batchEnd', entry_number)">\n"""
                    """<dtml-call "REQUEST.set('url', absolute_url() +"""
                    """ _['sequence-query'])">\n"""
                    '</dtml-if>\n'
                    '</dtml-in>\n'
                )
        source = source + (
            '<form action="&dtml-URL1;" method="post"'
            ' enctype="multipart/form-data">\n'
            '<dtml-if entryTuples>\n'
        )
        if data['listFormBatch']:
            source = source + (
                '<p><table cellspacing="0" cellpadding="0" border="0">\n'
                '<tr>\n'
                '<td nowrap align="left">\n'
                '  <p><input type="submit" name="%(idPrefix)s%(addFormId)s'
                ':method" value="%(listFormAddButtonLabel)s"></p>\n'
                '</td>\n'
                '<td nowrap align="center" width="100%%">\n'
                '  <p>\n'
                '<dtml-if "%(listFormBatchStartVar)s > 1">\n'
                '    [<a href="<dtml-var url>%(listFormBatchStartVar)s=1">'
                'First</a>]\n'
                '<dtml-else>\n'
                '    [First]\n'
                '</dtml-if>\n'
                '<dtml-in entryTuples start=%(listFormBatchStartVar)s'
                ' size=%(listFormBatchSizeVar)s prefix=entry previous>\n'
                '    [<a href="<dtml-var url>%(listFormBatchStartVar)s='
                '<dtml-var previous-sequence-start-number>">Back</a>]\n'
                '<dtml-else>\n'
                '    [Back]\n'
                '</dtml-in>\n'
                '    <b>Entries <dtml-var %(listFormBatchStartVar)s> -'
                ' <dtml-var batchEnd> of <dtml-var entryTuplesLen></b>\n'
                '<dtml-in entryTuples start=%(listFormBatchStartVar)s'
                ' size=%(listFormBatchSizeVar)s prefix=entry next>\n'
                '    [<a href="<dtml-var url>%(listFormBatchStartVar)s='
                '<dtml-var next-sequence-start-number>">Next</a>]\n'
                '<dtml-else>\n'
                '    [Next]\n'
                '</dtml-in>\n'
                '<dtml-if "batchEnd < entryTuplesLen">\n'
                '    [<a href="<dtml-var url>%(listFormBatchStartVar)s='
                '<dtml-var "int(math.ceil((entryTuplesLen - 1) /'
                ' %(listFormBatchSizeVar)s) * %(listFormBatchSizeVar)s)'
                ' + 1">">Last</a>]\n'
                '<dtml-else>\n'
                '    [Last]\n'
                '</dtml-if>\n'
                '  </p>\n'
                '</td>\n'
                '<td nowrap align="right">\n'
                '  <p>\n'
                '    per Page:\n'
                '    <select name="%(listFormBatchSizeVar)s" onChange="'
                """location.href='<dtml-var absolute_url>?batchSize=' +"""
                ' this.options[this.selectedIndex ].value">\n'
                '<dtml-in "range(5, max(5, min(251, entryTuplesLen)), 5)"'
                ' prefix=size>\n'
                '    <option value="&dtml-size_item;"<dtml-if "size_item =='
                ' %(listFormBatchSizeVar)s"> selected</dtml-if>>'
                '&dtml-size_item;</option>\n'
                '</dtml-in>\n'
                '    </select>\n'
                '  </p>\n'
                '</td>\n'
                '</tr>\n'
                '</table></p>\n'
            )
        else:
            source = source + (
                '<p><input type="submit"'
                ' name="%(idPrefix)s%(addFormId)s:method"'
                ' value="%(listFormAddButtonLabel)s"></p>\n')
        source = source + (
            '<table cellspacing="1" cellpadding="4" border="0">\n'
            '<tr>\n'
            '<th nowrap align="right" colspan="2">#</th>\n'
        )
        for id, object in self.List.objectItems():
            widgetCode = object.renderWidget(
                'Header', self.getField(self.storageId, id))
            if widgetCode.has_key('field'):
                source = source + (
                    '<th nowrap align="%(align)s" valign="top">%(title)s'
                    '</th>\n' % widgetCode)
        source = source + (
            '<th nowrap align="left" colspan="2">Actions</th>\n'
            '</tr>\n'
        )
        if data['listFormBatch']:
            source = source + (
                '<dtml-in entryTuples start=%(listFormBatchStartVar)s'
                ' size=%(listFormBatchSizeVar)s prefix=entry>')
        else:
            source = source + '<dtml-in entryTuples prefix=entry>'
        source = source + (
            '<tr class="<dtml-if entry_odd>odd<dtml-else>even</dtml-if>">\n'
            '<td align="left" valign="right"><input type="checkbox"'
            ' name="ids:list" value="&dtml-entry_key;"></td>\n'
            '<td align="right" valign="right"><dtml-var entry_number></td>\n'
        )
        for id, object in self.List.objectItems():
            widgetCode = object.renderWidget(
                'List', self.getField(self.storageId, id), 'entry_item')
            if widgetCode.has_key('field'):
                source = source + (
                    '<td align="%(align)s" valign="%(valign)s">%(field)s'
                    '</td>\n' % widgetCode)
        source = source + (
            '<td align="left" valign="right"><a href="%(viewFormId)s'
            '?entryId__=&dtml-entry_key;">%(listFormViewLinkLabel)s</a></td>\n'
            '<td align="left" valign="right"><a href="%(editFormId)s'
            '?entryId__=&dtml-entry_key;">%(listFormEditLinkLabel)s</a></td>\n'
            '</tr>\n'
            '</dtml-in>\n'
            '</table>\n'
        )
        source = source + (
            '<p><input type="submit" name="%(idPrefix)s%(deleteMethodId)s'
            ':method" value="%(listFormDelButtonLabel)s"></p>\n'
            '<dtml-else>\n'
            '<p><input type="submit" name="%(idPrefix)s%(addFormId)s:method"'
            ' value="%(listFormAddButtonLabel)s"></p>\n'
            '<p><em>No entries added yet...</em></p>\n'
            '</dtml-if>\n'
            '</form>\n'
            '</dtml-let>\n'
            '%(formFooter)s\n'
        )
        if data['listFormType'] == 'DTMLMethod':
            destination.manage_addDTMLMethod(
                data['idPrefix'] + data['listFormId'], data['listFormTitle'],
                source % data)
        else:
            destination.manage_addDTMLDocument(
                data['idPrefix'] + data['listFormId'], data['listFormTitle'],
                source % data)

        # - - - - - - - - - - - - - - - - - - - - - - - - -
        # create Add Form

        source = '%(formHeader)s\n'
        if data['addFormInfo']:
            source = source + '<p class="info">%(addFormInfo)s</p>\n'
        source = source + (
            '<form action="&dtml-URL1;" method="post"'
            ' enctype="multipart/form-data">\n')
        for id, object in self.Add.objectItems():
            widgetCode = object.renderWidget(
                'Add', self.getField(self.storageId, id))
            if widgetCode.has_key('hidden'):
                source = source + '''%s\n''' % widgetCode['hidden']
        source = source + (
            '<table cellspacing="1" cellpadding="4" border="0">\n')
        for id, object in self.Add.objectItems():
            widgetCode = object.renderWidget(
                'Add', self.getField(self.storageId, id))
            if widgetCode.has_key('field'):
                source = source + (
                    '<tr>\n'
                    '<th align="left" valign="top" nowrap>%(title)s</th>\n'
                    '<td align="%(align)s" valign="%(valign)s">%(field)s'
                    '</td>\n'
                    '</tr>\n'
                ) % widgetCode
        source = source + (
            '</table>\n'
            '<p>\n'
            '<input type="submit" name="%(idPrefix)s%(addMethodId)s:method"'
            ' value="%(addSubmitLabel)s">\n'
            '<input type="submit" name="%(idPrefix)s%(listFormId)s:method"'
            ' value="%(addCancelLabel)s">\n'
            '</p>\n'
            '</form>\n'
            '%(formFooter)s\n'
        )
        if data['addFormType'] == 'DTMLMethod':
            destination.manage_addDTMLMethod(
                data['idPrefix'] + data['addFormId'], data['addFormTitle'],
                source % data)
        else:
            destination.manage_addDTMLDocument(
                data['idPrefix'] + data['addFormId'], data['addFormTitle'],
                source % data)

        # - - - - - - - - - - - - - - - - - - - - - - - - -
        # create Add Method

        params = 'REQUEST = None'
        source = (
            "zmp2 = container.getZMP2()\n"
            "newId = zmp2.newEntryId('%(storageId)s')\n"
            "zmp2.addEntry('%(storageId)s', newId, REQUEST.form)\n"
            "REQUEST.RESPONSE.redirect(REQUEST['URL1'] +"
            " '/%(idPrefix)s%(listFormId)s')\n"
        )

        manage_addPythonScript(
            destination, data['idPrefix'] + data['addMethodId'])
        destination._getOb(
            data['idPrefix'] + data['addMethodId']
        ).ZPythonScript_edit(params, source % data)

        # - - - - - - - - - - - - - - - - - - - - - - - - -
        # create Edit Form

        source = (
            '%(formHeader)s\n'
            '<dtml-let zmp2=getZMP2 entry="zmp2.getEntry('
            """'%(storageId)s', entryId__ )">\n"""
        )
        if data['editFormInfo']:
            source = source + '''<p class="info">%(editFormInfo)s</p>\n'''
        source = source + (
            '<form action="&dtml-URL1;" method="post"'
            ' enctype="multipart/form-data">\n'
            '<input type="hidden" name="entryId__"'
            ' value="<dtml-var entryId__>">\n'
        )
        for id, object in self.Edit.objectItems():
            widgetCode = object.renderWidget(
                'Edit', self.getField(self.storageId, id), 'entry')
            if widgetCode.has_key('hidden'):
                source = source + '''%s\n''' % widgetCode['hidden']
        source = source + (
            '<table cellspacing="1" cellpadding="4" border="0">\n')
        for id, object in self.Edit.objectItems():
            widgetCode = object.renderWidget(
                'Add', self.getField(self.storageId, id), 'entry')
            if widgetCode.has_key('field'):
                source = source + (
                    '<tr>\n'
                    '<th align="left" valign="top" nowrap>%(title)s</th>\n'
                    '<td align="%(align)s" valign="%(valign)s">%(field)s'
                    '</td>\n'
                    '</tr>\n'
                ) % widgetCode
        source = source + (
            '</table>\n'
            '<p>\n'
            '<input type="submit" name="%(idPrefix)s%(editMethodId)s:method"'
            ' value="%(editSubmitLabel)s">\n'
            '<input type="submit" name="%(idPrefix)s%(listFormId)s:method"'
            ' value="%(editCancelLabel)s">\n'
            '</p>\n'
            '</form>\n'
            '</dtml-let>\n'
            '%(formFooter)s\n'
        )
        if data['editFormType'] == 'DTMLMethod':
            destination.manage_addDTMLMethod(
                data['idPrefix'] + data['editFormId'], data['editFormTitle'],
                source % data)
        else:
            destination.manage_addDTMLDocument(
                data['idPrefix'] + data['editFormId'], data['editFormTitle'],
                source % data)

        # - - - - - - - - - - - - - - - - - - - - - - - - -
        # create Edit Method

        params = 'entryId__, REQUEST = None'
        source = (
            "zmp2 = container.getZMP2()\n"
            "zmp2.editEntry('%(storageId)s', entryId__, REQUEST.form)\n"
            "REQUEST.RESPONSE.redirect(REQUEST['URL1'] +"
            " '/%(idPrefix)s%(listFormId)s')\n"
        )
        manage_addPythonScript(
            destination, data['idPrefix'] + data['editMethodId'])
        destination._getOb(
            data['idPrefix'] + data['editMethodId']).ZPythonScript_edit(
                params, source % data)

        # - - - - - - - - - - - - - - - - - - - - - - - - -
        # create View Form

        source = (
            '%(formHeader)s\n'
            '<dtml-let zmp2=getZMP2 entry="zmp2.getEntry('
            """'%(storageId)s', entryId__ )">\n"""
        )
        if data['viewFormInfo']:
            source = source + '<p class="info">%(viewFormInfo)s</p>\n'
        source = source + (
            '<form action="&dtml-URL1;" method="post"'
            ' enctype="multipart/form-data">\n'
            '<table cellspacing="1" cellpadding="4" border="0">\n'
        )
        for id, object in self.View.objectItems():
            widgetCode = object.renderWidget(
                'View', self.getField(self.storageId, id), 'entry')
            if widgetCode.has_key('field'):
                source = source + (
                    '<tr>\n'
                    '<th align="left" valign="top" nowrap>%(title)s</th>\n'
                    '<td align="%(align)s" valign="%(valign)s">%(field)s'
                    '</td>\n'
                    '</tr>\n'
                ) % widgetCode
        source = source + (
            '</table>\n'
            '<p>\n'
            '<input type="submit" name="%(idPrefix)s%(listFormId)s:method"'
            ' value="%(viewBackLabel)s"></p>\n'
            '</form>\n'
            '</dtml-let>\n'
            '%(formFooter)s\n'
        )
        if data['viewFormType'] == 'DTMLMethod':
            destination.manage_addDTMLMethod(
                data['idPrefix'] + data['viewFormId'], data['viewFormTitle'],
                source % data)
        else:
            destination.manage_addDTMLDocument(
                data['idPrefix'] + data['viewFormId'], data['viewFormTitle'],
                source % data)

        # - - - - - - - - - - - - - - - - - - - - - - - - -
        # create Delete Method

        params = 'ids = [], REQUEST = None'
        source = (
            "container.getZMP2().delEntries( '%(storageId)s', ids )\n"
            "REQUEST.RESPONSE.redirect( REQUEST[ 'URL1' ] +"
            " '/%(idPrefix)s%(listFormId)s' )\n"
        )
        manage_addPythonScript(
            destination, data['idPrefix'] + data['deleteMethodId'])
        destination._getOb(
            data['idPrefix'] + data['deleteMethodId']
        ).ZPythonScript_edit(params, source % data)

        # - - - - - - - - - - - - - - - - - - - - - - - - -
        # create Move Method

        params = 'dir, ids = [], REQUEST = None'
        source = (
            "zmp2 = container.getZMP2()\n"
            "if dir == 'top':\n"
            "    method = zmp2.moveEntryTop\n"
            "elif dir == 'up':\n"
            "    method = zmp2.moveEntryUp\n"
            "elif dir == 'down':\n"
            "    method = zmp2.moveEntryDown\n"
            "elif dir == 'bottom':\n"
            "    method = zmp2.moveEntryBottom\n"
            "for id in ids:\n"
            "    method( '%(storageId)s', id )\n"
            "REQUEST.RESPONSE.redirect( REQUEST[ 'URL1' ] +"
            " '/%(idPrefix)s%(listFormId)s' )\n"
        ) % data

        manage_addPythonScript(
            destination, data['idPrefix'] + data['moveMethodId'])
        destination._getOb(
            data['idPrefix'] + data['moveMethodId']
        ).ZPythonScript_edit(params, source % data)

    # -------------------------------------------------------------------------

    def getDefaultWidget(self, formTypeId, fieldId, field):
        """Return the list of defined widgets"""
        if fieldId in self[formTypeId].objectIds():
            return self[formTypeId][fieldId].getWidgetData(formTypeId)
        else:
            widgets = self.getWidgetsForField(formTypeId, field.fieldTypeId)
            if formTypeId == 'List' or not widgets:
                return None
            else:
                instance = widgets[0][1]['instance']()
                return instance.getWidgetData(formTypeId)

    # -------------------------------------------------------------------------

    def getWidget(self, formTypeId, widgetId, fieldId):
        """Return the specified widget"""
        field = self.getField(self.storageId, fieldId)
        for id, widget in (
            self.getWidgetsForField(formTypeId, field.fieldTypeId)
        ):
            if id == widgetId:
                return widget['instance']().getWidgetData(formTypeId)
        return None

    # -------------------------------------------------------------------------

    def getWidgetDataList(self, formTypeId, data):
        """Return list of widget data for Interface wizard"""
        result = []
        tempDict = {}
        for key in data.keys():
            if (
                key[:len(formTypeId.lower() + 'Widgets_')] ==
                formTypeId.lower() + 'Widgets_'
            ):
                keyTuple = key[len(formTypeId.lower() + 'Widgets_'):]
                fieldId = keyTuple.split('_')[0]
                if fieldId in tempDict.keys():
                    tempDict[fieldId].update({
                        keyTuple[len(fieldId) + 1:]: data[key]})
                else:
                    tempDict[fieldId] = {
                        keyTuple[len(fieldId) + 1:]: data[key]}
        tempList = tempDict.items()

        def sortTempList(x, y):
            return cmp(
                int(x[1]['position__']),
                int(y[1]['position__']))

        tempList.sort(sortTempList)
        for item in tempList:
            del item[1]['position__']
            if len(item[1].keys()) == 0 or item[1].get('pluginId__', '') == '':
                item = (item[0], None)
            result.append(item)
        return result

    # -------------------------------------------------------------------------

    manage_editInterfaceForm = DTMLFile(
        'dtml/editMetaAdminInterface', globals())

    def manage_editInterface(self, REQUEST=None):
        """Change the storage this Interface is associated with"""
        self.configure(REQUEST.form)

        # List Interface Widgets
        self.List.manage_delObjects(self.List.objectIds())
        for fieldId, widgetData in (
            self.getWidgetDataList('List', REQUEST.form)
        ):
            if widgetData:
                plugin = self.getPlugin(widgetData['pluginId__'])
                getattr(
                    self.List.manage_addProduct[plugin['product']],
                    plugin['action'].split('/')[-1]
                )(fieldId, 'List', widgetData)

        # Add Interface Widgets
        self.Add.manage_delObjects(self.Add.objectIds())
        for fieldId, widgetData in (
            self.getWidgetDataList('Add', REQUEST.form)
        ):
            if widgetData:
                plugin = self.getPlugin(widgetData['pluginId__'])
                getattr(
                    self.Add.manage_addProduct[plugin['product']],
                    plugin['action'].split('/')[-1]
                )(fieldId, 'Add', widgetData)

        # Edit Interface Widgets
        self.Edit.manage_delObjects(self.Edit.objectIds())
        for fieldId, widgetData in (
            self.getWidgetDataList('Edit', REQUEST.form)
        ):
            if widgetData:
                plugin = self.getPlugin(widgetData['pluginId__'])
                getattr(
                    self.Edit.manage_addProduct[plugin['product']],
                    plugin['action'].split('/')[-1]
                )(fieldId, 'Edit', widgetData)

        # View Interface Widgets
        self.View.manage_delObjects(self.View.objectIds())
        for fieldId, widgetData in (
            self.getWidgetDataList('View', REQUEST.form)
        ):
            if widgetData:
                plugin = self.getPlugin(widgetData['pluginId__'])
                getattr(
                    self.View.manage_addProduct[plugin['product']],
                    plugin['action'].split('/')[-1]
                )(fieldId, 'View', widgetData)

        if REQUEST is not None:
            REQUEST.RESPONSE.redirect(
                self.zmp2URL() +
                '/manage_interfacesBrowserForm?message=Interface+changed')


# =============================================================================


manage_addMetaAdminInterfaceForm = DTMLFile(
    'dtml/addMetaAdminInterface', globals())


def manage_addMetaAdminInterface(self, id, title='', REQUEST=None):
    """ZMI constructor for MetaAdminInterface"""
    instance = MetaAdminInterface(id)
    instance.title = title
    instance.storageId = REQUEST.get('storageId', '')
    instance.configure(REQUEST.form)
    instance.manage_addOrderedFolder('List')
    instance.manage_addOrderedFolder('Add')
    instance.manage_addOrderedFolder('Edit')
    instance.manage_addOrderedFolder('View')
    id = self._setObject(id, instance)
    if REQUEST is not None:
        REQUEST.RESPONSE.redirect(
            self.DestinationURL() + '/' + id + '/manage_editInterfaceForm')
