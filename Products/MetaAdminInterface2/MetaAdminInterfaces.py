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
from Products.MetaPublisher2.Library import InterfacePlugin

from MetaAdminInterface import MetaAdminInterface


# =============================================================================


class MetaAdminInterfaces(InterfacePlugin):
    """MetaAdminInterfaces Base Class"""

    meta_type = 'MetaAdminInterfaces'

    # -------------------------------------------------------------------------

    pluginName = 'MetaAdminInterfaces'
    pluginAuthor = 'Sebastian Luehnsdorf - Web-Solutions GbR.'
    pluginVersion = '1.0.1'
    pluginInfo = 'Unified Admin Interface.'

    # -------------------------------------------------------------------------

    _properties = InterfacePlugin._properties

    # -------------------------------------------------------------------------

    def manage_afterAdd(self, item, container):
        if item is self:
            for storageId in self.storageIds():
                storageInterface = MetaAdminInterface(storageId)
                storageInterface.title = storageId
                storageInterface.configure({
                    'listFormBatch': 1,
                    'listFormSession': 1,
                    'listFormBatch': 1,
                    'createFolder': 1,
                    'createFolderId': storageId,
                    'storageId': storageId,
                })
                storageInterface.manage_addOrderedFolder('List')
                storageInterface.manage_addOrderedFolder('Add')
                storageInterface.manage_addOrderedFolder('Edit')
                storageInterface.manage_addOrderedFolder('View')

                self._setObject(storageId, storageInterface)
                storageInterface = self._getOb(storageId)

                for fieldId, field in self.fieldItems(storageId):

                    widgets = self.getWidgetsForField(
                        'List', field.fieldTypeId)
                    widgetData = widgets[0][1]['instance']().getWidgetData(
                        'List')
                    plugin = storageInterface.getPlugin(
                        widgetData['pluginId__'])
                    getattr(
                        storageInterface.List.manage_addProduct[
                            plugin['product']],
                        plugin['action'].split('/')[-1])(
                            fieldId, 'List', widgetData)

                    widgetData = storageInterface.getDefaultWidget(
                        'Add', fieldId, field)
                    plugin = storageInterface.getPlugin(
                        widgetData['pluginId__'])
                    getattr(
                        storageInterface.Add.manage_addProduct[
                            plugin['product']],
                        plugin['action'].split('/')[-1])(
                            fieldId, 'Add', widgetData)

                    widgetData = storageInterface.getDefaultWidget(
                        'Edit', fieldId, field)
                    plugin = storageInterface.getPlugin(
                        widgetData['pluginId__'])
                    getattr(
                        storageInterface.Edit.manage_addProduct[
                            plugin['product']],
                        plugin['action'].split('/')[-1])(
                            fieldId, 'Edit', widgetData)

                    widgetData = storageInterface.getDefaultWidget(
                        'View', fieldId, field)
                    plugin = storageInterface.getPlugin(
                        widgetData['pluginId__'])
                    getattr(
                        storageInterface.View.manage_addProduct[
                            plugin['product']],
                        plugin['action'].split('/')[-1])(
                            fieldId, 'View', widgetData)

    def configure(self, data):
        """Configure the Interface"""
        self.title = data.get('title', self.title)

    # -------------------------------------------------------------------------

    def renderingIds(self):
        """Return list ids for objects created on rendering"""
        return ['admin']

    def renderInterface(self, destination, **options):
        """Render the Interface"""
        ids = self.objectIds()
        for id in ids:
            self._getOb(id).renderInterface(destination)
        menu = '<h3>Storages</h3><ul>'
        for id in ids:
            menu = menu + '<li><a href="%s/%s">%s</a>' % (
                destination.absolute_url(), id, id)
        menu = menu + '</ul>'
        destination.manage_addDTMLMethod(
            'standard_html_header', '', '<html><body>' + menu)
        destination.manage_addDTMLMethod(
            'standard_html_footer', '', '</body></html>')

    # -------------------------------------------------------------------------

    def getInterfacePath(self):
        """Return the path of the Interface"""
        return self.absolute_url()[len(self.zmp2URL()) + 1:]

    # -------------------------------------------------------------------------

    manage_editInterfaceForm = DTMLFile(
        'dtml/editMetaAdminInterfaces', globals())

    def manage_editInterface(self, REQUEST=None):
        """Change the storage this Interface is associated with"""
        self.configure(REQUEST.form)
        if REQUEST is not None:
            REQUEST.RESPONSE.redirect(
                self.zmp2URL() +
                '/manage_interfacesBrowserForm?message=Interface+changed')


# =============================================================================


manage_addMetaAdminInterfacesForm = DTMLFile(
    'dtml/addMetaAdminInterfaces', globals())


def manage_addMetaAdminInterfaces(self, id, title='', REQUEST=None):
    """ZMI constructor for MetaAdminInterfaces"""
    instance = MetaAdminInterfaces(id)
    instance.title = title
    id = self._setObject(id, instance)
    if REQUEST is not None:
        REQUEST.RESPONSE.redirect(
            self.DestinationURL() + '/' + id + '/manage_editInterfaceForm')
