"""MetaPublisher2 - Historical Compatability.

To ensure to continued operation of deprecated resources, this module provides
wrappers and handlers for these outdated resources. It also provides an API for
logging calls to deprecated resources.
"""


from Products.MetaPublisher2.library.application import (
    permission_access_configuration, permission_access_entries,
    permission_change_configuration, permission_change_entries,
    permission_create_entries, permission_manage, permission_manage_designs,
    permission_manage_frontends, permission_manage_presets,
    permission_publish_frontends, permission_save_presets, permission_zmi)
from Products.MetaPublisher2.library.common import (
    ClassSecurityInfo, InitializeClass, Folder, OrderedFolder, true, false)
from Products.MetaPublisher2.library.compatibility.deprecation import (
    deprecated_form, deprecated_method)


# ============================================================================
# Module Exports

__all__ = [
    'HistoricalCompatibility',
    'InterfacesFolder',
    'OrderedFolder',
    'TestError',
    'false',
    'standard_form_footer',
    'standard_form_header',
    'true',
]


# ============================================================================
# Legacy Plugin Identifiers

all_plugintypes = [
    'ZMP2StoragePlugin', 'ZMP2FieldPlugin', 'ZMP2InterfacePlugin',
    'ZMP2WidgetPlugin']


# ============================================================================
# Legacy Field Value Test Exception

class TestError(Exception):
    """Legacy Field Value Test Error."""

    def __init__(self, **args):
        """Initialize instance."""
        for key in args.keys():
            setattr(self, key, args[key])


# ============================================================================
# Interface Default Layout

standard_form_header = '''\
<dtml-var standard_html_header>
<h2><dtml-var title_or_id></h2>
'''

standard_form_footer = '''\
<p align="center">
  <a target="_blank" href="http://metapublisher.org">
    <img src="<dtml-var BASEPATH1>/misc_/MetaPublisher2/MP2Powered.gif"\
 border="0" alt="Powered by MetaPublisher2">
  </a>
</p>
<dtml-var standard_html_footer>
'''


# ============================================================================
# InterfacesFolder Base Class

class InterfacesFolder(Folder):
    """InterfacesFolder Base Class."""

    meta_type = 'InterfacesFolder'


# ----------------------------------------------------------------------------
# Class Security


InitializeClass(InterfacesFolder)


# ============================================================================
# Historical Compatibility Mix-In Class

class HistoricalCompatibility:
    """Historical Compatibility Mix-In Class."""

    security = ClassSecurityInfo()

    # -------------------------------------------------------------------------
    # MetaPublisher2

    security.declarePublic('zmp2')

    def zmp2(self):
        """Return this instance of MetaPublisher2 (DEPRECATED)."""
        deprecated_method('zmp2')
        return self.get_MetaPublisher2()

    security.declarePublic('get_MetaPublisher2_url')

    def get_MetaPublisher2_url(self):
        """Return this instance's absolute url (DEPRECATED)."""
        deprecated_method('get_MetaPublisher2_url')
        return self.get_MetaPublisher2_url()

    # -------------------------------------------------------------------------
    # UserInterface

    security.declarePublic('manage_zmp2_css')

    def manage_zmp2_css(self, REQUEST=None):
        """Return MetaPublisher2 CSS (DEPRECATED)."""
        deprecated_form('manage_zmp2_css')
        return self.manage_MetaPublisher2_css(self, REQUEST)

    security.declarePublic('sp')

    def sp(self, w=1, h=1, **kw):
        """Return tag for spacer image (DEPRECATED)."""
        deprecated_method('sp')
        params = ''
        for key in kw.keys():
            params = params + ' %s="%s"' % (key, kw[key])
        tag = '<img src="p_/sp" width="%s" height="%s" border="0" alt=""%s/>'
        return tag % (self.REQUEST.BASEPATH1, w, h, params)

    # -------------------------------------------------------------------------
    # Configuration Constraints

    # -------------------------------------------------------------------------
    # Configuration Fields

    security.declareProtected(
        permission_access_configuration, 'manage_fieldsBrowserForm')

    def manage_fieldsBrowserForm(self, REQUEST=None):
        """Return form fields_form (DEPRECATED)."""
        deprecated_form('manage_fieldsBrowserForm')
        return self.fields_form(self, REQUEST)

    security.declareProtected(
        permission_change_configuration, 'manage_fieldsNewForm')

    def manage_fieldsNewForm(self, REQUEST=None):
        """Return form add_field_form (DEPRECATED)."""
        deprecated_form('manage_fieldsNewForm')
        return self.add_field_form(self, REQUEST)

    security.declareProtected(permission_access_configuration, 'getField')

    def getField(self, storageId, fieldId):
        """Return method get_field (DEPRECATED)."""
        deprecated_method('getField')
        return self.get_field(self, storageId, fieldId)

    security.declareProtected(permission_access_configuration, 'fieldIds')

    def fieldIds(self, storageId):
        """Return method field_ids (DEPRECATED)."""
        deprecated_method('fieldIds')
        return self.field_ids(storageId)

    security.declareProtected(permission_access_configuration, 'fieldItems')

    def fieldItems(self, storageId):
        """Return method field_items (DEPRECATED)."""
        deprecated_method('fieldItems')
        return self.field_items(storageId)

    security.declareProtected(permission_access_configuration, 'fieldValues')

    def fieldValues(self, storageId):
        """Return method field_values (DEPRECATED)."""
        deprecated_method('fieldValues')
        return self.field_values(storageId)

    security.declareProtected(
        permission_change_configuration, 'manage_fieldsNew')

    def manage_fieldsNew(self, storageId, fieldType, REQUEST=None):
        """Return method add_field (DEPRECATED)."""
        deprecated_method('manage_fieldsNew')
        return self.add_field(storageId, fieldType, REQUEST)

    security.declareProtected(permission_change_configuration, 'delField')

    def delField(self, storageId, fieldId):
        """Return method delete_field (DEPRECATED)."""
        deprecated_method('delField')
        return self.delete_field(storageId, fieldId)

    security.declareProtected(
        permission_change_configuration, 'manage_fieldsDelete')

    def manage_fieldsDelete(self, storageId, ids=[], REQUEST=None):
        """Return method delete_fields (DEPRECATED)."""
        deprecated_method('manage_fieldsDelete')
        return self.delete_fields(storageId, ids, REQUEST)

    security.declareProtected(permission_change_configuration, 'delFields')

    def delFields(self, storageId, fieldIds=[]):
        """Return method delete_fields (DEPRECATED)."""
        deprecated_method('delFields')
        return self.delete_fields(storageId, fieldIds)

    security.declareProtected(permission_change_configuration, 'renameField')

    def renameField(self, storageId, fieldId, newId):
        """Return method rename_field (DEPRECATED)."""
        deprecated_method('renameField')
        return self.rename_field(storageId, fieldId, newId)

    security.declareProtected(
        permission_access_configuration, 'fieldsSortable')

    def fieldsSortable(self, storageId):
        """Return method are_fields_sortable (DEPRECATED)."""
        deprecated_method('fieldsSortable')
        return self.are_fields_sortable(storageId)

    security.declareProtected(
        permission_change_configuration, 'manage_fieldsMoveTop')

    def manage_fieldsMoveTop(self, storageId, fieldId, REQUEST=None):
        """Return method move_fields_to_top (DEPRECATED)."""
        deprecated_method('manage_fieldMoveTop')
        return self.move_fields_to_top(storageId, fieldId, REQUEST)

    security.declareProtected(permission_change_configuration, 'moveFieldTop')

    def moveFieldTop(self, storageId, fieldId):
        """Return method move_fields_to_top (DEPRECATED)."""
        deprecated_method('moveFieldTop')
        return self.move_fields_to_top(storageId, fieldId)

    security.declareProtected(
        permission_change_configuration, 'manage_fieldsMoveUp')

    def manage_fieldsMoveUp(self, storageId, fieldId, REQUEST=None):
        """Return method move_fields_up (DEPRECATED)."""
        deprecated_method('manage_fieldMoveUp')
        return self.move_fields_up(storageId, fieldId, REQUEST)

    security.declareProtected(permission_change_configuration, 'moveFieldUp')

    def moveFieldUp(self, storageId, fieldId):
        """Return method move_fields_up (DEPRECATED)."""
        deprecated_method('moveFieldUp')
        return self.move_fields_up(storageId, fieldId)

    security.declareProtected(
        permission_change_configuration, 'manage_fieldsMoveDown')

    def manage_fieldsMoveDown(self, storageId, fieldId, REQUEST=None):
        """Return method move_fields_down (DEPRECATED)."""
        deprecated_method('manage_fieldMoveDown')
        return self.move_fields_down(storageId, fieldId, REQUEST)

    security.declareProtected(permission_change_configuration, 'moveFieldDown')

    def moveFieldDown(self, storageId, fieldId):
        """Return method move_fields_down (DEPRECATED)."""
        deprecated_method('moveFieldDown')
        return self.move_fields_down(storageId, fieldId)

    security.declareProtected(
        permission_change_configuration, 'manage_fieldsMoveBottom')

    def manage_fieldsMoveBottom(self, storageId, fieldId, REQUEST=None):
        """Return method move_fields_to_bottom (DEPRECATED)."""
        deprecated_method('manage_fieldMoveBottom')
        return self.move_fields_to_bottom(storageId, fieldId, REQUEST)

    security.declareProtected(
        permission_change_configuration, 'moveFieldBottom')

    def moveFieldBottom(self, storageId, fieldId):
        """Return method move_fields_to_bottom (DEPRECATED)."""
        deprecated_method('moveFieldBottom')
        return self.move_fields_to_bottom(storageId, fieldId)

    # -------------------------------------------------------------------------
    # Configuration Identifiers

    security.declareProtected(permission_access_configuration, 'newEntryId')

    def newEntryId(self, storageId):
        """Return method new_entry_id (DEPRECATED)."""
        deprecated_method('newEntryId')
        return self.new_entry_id(storageId)

    # -------------------------------------------------------------------------
    # Configuration Indexing

    security.declareProtected(
        permission_access_configuration, 'manage_storagesIndexForm')

    def manage_storagesIndexForm(self, REQUEST=None):
        """Return from indexing_form (DEPRECATED)."""
        deprecated_form('manage_storagesIndexForm')
        return self.indexing_form(self, REQUEST)

    # -------------------------------------------------------------------------
    # Configuration Inheritance

    # -------------------------------------------------------------------------
    # Configuration Relations

    # -------------------------------------------------------------------------
    # Configuration Storages

    security.declareProtected(
        permission_change_configuration, 'manage_storagesBrowserForm')

    def manage_storagesBrowserForm(self, REQUEST=None):
        """Return Storages Form (DEPRECATED)."""
        deprecated_form('manage_storagesBrowserForm')
        return self.storages_form(self, REQUEST)

    security.declareProtected(
        permission_change_configuration, 'manage_storagesNewForm')

    def manage_storagesNewForm(self, REQUEST=None):
        """Return new Storage Form (DEPRECATED)."""
        deprecated_form('manage_storagesNewForm')
        return self.add_storage_form(self, REQUEST)

    security.declareProtected(permission_access_configuration, 'getStorage')

    def getStorage(self, storageId):
        """Return method get_storage (DEPRECATED)."""
        deprecated_method('getStorage')
        return self.get_storage(storageId)

    security.declareProtected(permission_access_configuration, 'storageIds')

    def storageIds(self):
        """Return method storage_ids (DEPRECATED)."""
        deprecated_method('storageIds')
        return self.storage_ids()

    security.declareProtected(permission_access_configuration, 'storageItems')

    def storageItems(self):
        """Return method storage_items (DEPRECATED)."""
        deprecated_method('storageItems')
        return self.storage_items()

    security.declareProtected(permission_access_configuration, 'storageValues')

    def storageValues(self):
        """Return method storage_values (DEPRECATED)."""
        deprecated_method('storageValues')
        return self.storage_values()

    security.declareProtected(
        permission_change_configuration, 'manage_storagesNew')

    def manage_storagesNew(self, REQUEST=None):
        """Return method add_storage (DEPRECATED)."""
        deprecated_method('manage_storagesNew')
        return self.add_storage(REQUEST)

    security.declareProtected(
        permission_change_configuration, 'manage_storagesDelete')

    def manage_storagesDelete(self, ids=[], REQUEST=None):
        """Return method delete_storages (DEPRECATED)."""
        deprecated_method('manage_storagesDelete')
        return self.delete_storages(ids, REQUEST)

    # -------------------------------------------------------------------------
    # Configuration Triggers

    # -------------------------------------------------------------------------
    # Data Entries

    security.declareProtected(
        permission_access_entries, 'manage_entriesBrowserForm')

    def manage_entriesBrowserForm(self, REQUEST=None):
        """Return management form for entries (DEPRECATED)."""
        deprecated_form('manage_entriesBrowserForm')
        return self.entries_form(self, REQUEST)

    security.declareProtected(
        permission_create_entries, 'manage_entriesNewForm')

    def manage_entriesNewForm(self, REQUEST=None):
        """Return management form for adding entries (DEPRECATED)."""
        deprecated_form('manage_entriesNewForm')
        return self.entries_form(self, REQUEST)

    security.declareProtected(permission_create_entries, 'manage_entriesNew')

    def manage_entriesNew(self, REQUEST=None):
        """Add entry to storage (DEPRECATED)."""
        deprecated_method('manage_entriesNew')
        source = REQUEST.get('storage_id', REQUEST.get(
            'storageId', self.get_profile_variable(REQUEST, 'storage_id')))
        entry_id = REQUEST.get('entry_id', REQUEST.get('entryId', None))
        entry_id = self.add_entry(source, entry_id, REQUEST.form)
        self.redirect(
            REQUEST,
            'entries_form',
            message='!TXT! Entry "%s" in Storage "%s" added.' % (
                entry_id, source)
        )

    security.declareProtected(
        permission_create_entries, 'manage_entriesNewMore')

    def manage_entriesNewMore(self, REQUEST=None):
        """Add entry to storage (DEPRECATED)."""
        deprecated_method('manage_entriesNewMore')
        source = REQUEST.get('storage_id', REQUEST.get(
            'storageId', self.get_profile_variable(REQUEST, 'storage_id')))
        entry_id = REQUEST.get('entry_id', REQUEST.get('entryId', None))
        entry_id = self.add_entry(source, entry_id, REQUEST.form)
        self.redirect(
            REQUEST,
            'add_entry_form',
            message='!TXT! Entry "%s" in Storage "%s" added.' % (
                entry_id, source)
        )

    security.declareProtected(permission_change_entries, 'manage_entriesEdit')

    def manage_entriesEdit(self, REQUEST=None):
        """Edit entry in storage (DEPRECATED)."""
        source = REQUEST.get('storage_id', REQUEST.get(
            'storageId', self.get_profile_variable(REQUEST, 'storage_id')))
        entry_id = REQUEST.get('entry_id', REQUEST['entryId'])
        self.edit_entry(source, entry_id, REQUEST.form, REQUEST)

    security.declareProtected(
        permission_change_entries, 'manage_entriesDelete')

    def manage_entriesDelete(self, storageId, ids=[], REQUEST=None):
        """Delete entries from storage (DEPRECATED)."""
        deprecated_method('manage_entriesDelete')
        return self.delete_entries(storageId, ids, REQUEST)

    security.declareProtected(permission_access_entries, 'entryIds')

    def entryIds(self, storageId):
        """Retrieve list of ids of entries in storage (DEPRECATED)."""
        deprecated_method('entryIds')
        return self.entry_ids(storageId)

    security.declareProtected(permission_access_entries, 'entryItems')

    def entryItems(self, storageId):
        """Retrieve list of tuples of entries in storage (DEPRECATED)."""
        deprecated_method('entryItems')
        return self.entry_items(storageId)

    security.declareProtected(permission_access_entries, 'entryValues')

    def entryValues(self, storageId):
        """Retrieve list of values of entries in storage (DEPRECATED)."""
        deprecated_method('entryValues')
        return self.entry_values(storageId)

    security.declareProtected(permission_access_entries, 'getEntry')

    def getEntry(self, storageId, entryId):
        """Retrieve entry from storage (DEPRECATED)."""
        deprecated_method('getEntry')
        return self.get_entry(self, storageId, entryId)

    security.declareProtected(permission_create_entries, 'addEntry')

    def addEntry(self, storageId, entryId, entryData={}, **args):
        """Add entry to storage (DEPRECATED)."""
        deprecated_method('addEntry')
        entryData.update(args)
        return self.add_entry(self, storageId, entryId, entryData)

    security.declareProtected(permission_change_entries, 'delEntries')

    def delEntries(self, storageId, entryIds=[]):
        """Delete entries from storage (DEPRECATED)."""
        deprecated_method('delEntries')
        return self.delete_entries(storageId, entryIds)

    security.declareProtected(permission_change_entries, 'delEntry')

    def delEntry(self, storageId, entryId):
        """Delete entry from storage (DEPRECATED)."""
        deprecated_method('delEntry')
        return self.del_entry(storageId, entryId)

    security.declareProtected(permission_change_entries, 'editEntry')

    def editEntry(self, storageId, entryId, entryData={}, **args):
        """Edit entry in storage (DEPRECATED)."""
        deprecated_method('editEntry')
        entryData.update(args)
        return self.edit_entry(storageId, entryId, entryData)

    security.declareProtected(permission_change_entries, 'renameEntry')

    def renameEntry(self, entryId, newId):
        """Rename entry in storage (DEPRECATED)."""
        deprecated_method('renameEntry')
        return self.rename_entry(entryId, newId)

    security.declareProtected(
        permission_change_entries, 'manage_entriesMoveBottom')

    def manage_entriesMoveBottom(self, storageId, entryId, REQUEST=None):
        """Move entry to bottom (DEPRECATED)."""
        deprecated_method('manage_entriesMoveBottom')
        return self.move_entry_to_bottom(storageId, entryId, REQUEST)

    security.declareProtected(
        permission_change_entries, 'manage_entriesMoveDown')

    def manage_entriesMoveDown(self, storageId, entryId, REQUEST=None):
        """Move entry down (DEPRECATED)."""
        deprecated_method('manage_entriesMoveDown')
        return self.move_entry_down(storageId, entryId, REQUEST)

    security.declareProtected(
        permission_change_entries, 'manage_entriesMoveTop')

    def manage_entriesMoveTop(self, storageId, entryId, REQUEST=None):
        """Move entry to top (DEPRECATED)."""
        deprecated_method('manage_entriesMoveTop')
        return self.move_entry_to_top(storageId, entryId, REQUEST)

    security.declareProtected(
        permission_change_entries, 'manage_entriesMoveToPosition')

    def manage_entriesMoveToPosition(
        self, storageId, entryId, position, REQUEST=None
    ):
        """Move entry to position (DEPRECATED)."""
        deprecated_method('manage_entriesMoveToPosition')
        return self.move_entry(storageId, entryId, position, REQUEST)

    security.declareProtected(
        permission_change_entries, 'manage_entriesMoveUp')

    def manage_entriesMoveUp(self, storageId, entryId, REQUEST=None):
        """Move entry up (DEPRECATED)."""
        deprecated_method('manage_entriesMoveUp')
        return self.move_entry_up(storageId, entryId, REQUEST)

    security.declareProtected(permission_change_entries, 'moveEntryBottom')

    def moveEntryBottom(self, storageId, entryId):
        """Move entry to bottom (DEPRECATED)."""
        deprecated_method('moveEntryBottom')
        return self.move_entry_to_bottom(storageId, entryId)

    security.declareProtected(permission_change_entries, 'moveEntryDown')

    def moveEntryDown(self, storageId, entryId):
        """Move entry down (DEPRECATED)."""
        deprecated_method('moveEntryDown')
        return self.move_entry_down(storageId, entryId)

    security.declareProtected(permission_change_entries, 'moveEntryTop')

    def moveEntryTop(self, storageId, entryId):
        """Move entry to top (DEPRECATED)."""
        deprecated_method('moveEntryTop')
        return self.move_entry_to_top(storageId, entryId)

    security.declareProtected(permission_change_entries, 'moveEntryToPosition')

    def moveEntryToPosition(self, storageId, entryId, position):
        """Move entry to position (DEPRECATED)."""
        deprecated_method('moveEntryToPosition')
        return self.move_entry(storageId, entryId, position)

    security.declareProtected(permission_change_entries, 'moveEntryUp')

    def moveEntryUp(self, storageId, entryId):
        """Move entry up (DEPRECATED)."""
        deprecated_method('moveEntryUp')
        return self.move_entry_up(storageId, entryId)

    security.declareProtected(permission_access_entries, 'getEntryPosition')

    def getEntryPosition(self, storageId, entryId):
        """Retrieve position of entry (DEPRECATED)."""
        deprecated_method('getEntryPosition')
        return self.get_entry_position(storageId, entryId)

    security.declareProtected(permission_access_entries, 'getEntryField')

    def getEntryField(self, storageId, entryId, fieldId, default=None):
        """DEPRECTAED: !TXT! Get the value of an Entry's Field."""
        deprecated_method('getEntryField')
        self.get_entry_field(storageId, entryId, fieldId, default)

    security.declareProtected(permission_change_entries, 'setEntryField')

    def setEntryField(self, storageId, entryId, fieldId, value):
        """DEPRECTAED: !TXT! Set the value of an Entry's Field."""
        deprecated_method('setEntryField')
        self.set_entry_field(storageId, entryId, fieldId, value)

    # -------------------------------------------------------------------------
    # Data Exports

    # -------------------------------------------------------------------------
    # Data Expressions

    # -------------------------------------------------------------------------
    # Data Imports

    # -------------------------------------------------------------------------
    # Data Queries

    security.declareProtected(
        permission_access_entries, 'manage_entriesQueriesForm')

    def manage_entriesQueriesForm(self, REQUEST=None):
        """Return form queries_form (DEPRECATED)."""
        return self.queries_form(self, REQUEST)

    # -------------------------------------------------------------------------
    # Data Reports

    # -------------------------------------------------------------------------
    # Data Search

    # -------------------------------------------------------------------------
    # Data Transfer

    # -------------------------------------------------------------------------
    # Publisher Audit

    # -------------------------------------------------------------------------
    # Publisher Caching

    security.declareProtected(
        permission_manage_designs, 'manage_storagesCacheForm')

    def manage_storagesCacheForm(self, REQUEST=None):
        """Return method caching_form (DEPRECATED)."""
        deprecated_form('manage_storagesCacheForm')
        return self.caching_form(self, REQUEST)

    # -------------------------------------------------------------------------
    # Publisher Designs

    security.declareProtected(
        permission_manage_designs, 'manage_interfacesStylesForm')

    def manage_interfacesStylesForm(self, REQUEST=None):
        """Return method designs_form (DEPRECATED)."""
        deprecated_form('manage_interfacesStylesForm')
        return self.designs_form(self, REQUEST)

    # -------------------------------------------------------------------------
    # Publisher Frontends

    security.declareProtected(
        permission_manage_frontends, 'manage_interfacesDelete')

    def manage_interfacesDelete(self, ids=[], REQUEST=None):
        """Delete specified Frontends (DEPRECATED)."""
        deprecated_method('manage_interfacesDelete')
        return self.del_frontends(ids, REQUEST)

    security.declareProtected(permission_manage_frontends, 'interfaceValues')

    def interfaceValues(self):
        """Return values of Frontends (DEPRECATED)."""
        deprecated_method('interfaceValues')
        return self.frontend_values()

    security.declareProtected(permission_manage_frontends, 'interfaceItems')

    def interfaceItems(self):
        """Return tuples of id, value of Frontends (DEPRECATED)."""
        deprecated_method('interfaceItems')
        return self.frontend_items()

    security.declareProtected(permission_manage_frontends, 'interfaceIds')

    def interfaceIds(self):
        """Return ids of Frontends (DEPRECATED)."""
        deprecated_method('interfaceIds')
        return self.frontend_paths()

    security.declareProtected(permission_manage_frontends, 'getInterface')

    def getInterface(self, interfaceId):
        """Return the specified Frontend (DEPRECATED)."""
        deprecated_method('getInterface')
        return self.get_frontend(interfaceId)

    security.declareProtected(permission_manage_frontends, 'getInterfacePaths')

    def getInterfacePaths(self):
        """Return all Frontend object paths recursively (DEPRECATED)."""
        deprecated_method('getInterfacePaths')
        return self.get_frontend_parents()

    security.declareProtected(
        permission_manage_frontends, 'manage_interfacesBrowserForm')

    def manage_interfacesBrowserForm(self, REQUEST=None):
        """Frontends Form (DEPRECATED)."""
        deprecated_form('manage_interfacesStylesForm')
        return self.frontends_form(self, REQUEST)

    security.declareProtected(
        permission_manage_frontends, 'manage_interfacesNewForm')

    def manage_interfacesNewForm(self, REQUEST=None):
        """Add Frontend Form (DEPRECATED)."""
        deprecated_form('manage_interfacesNewForm')
        return self.add_frontend_form(self, REQUEST)

    security.declareProtected(
        permission_manage_frontends, 'manage_interfacesNew')

    def manage_interfacesNew(self, REQUEST=None):
        """Call specified Frontend's factory (DEPRECATED)."""
        deprecated_method('manage_interfacesNew')
        return self.add_frontend_type(REQUEST)

    # -------------------------------------------------------------------------
    # Publisher Languages

    # -------------------------------------------------------------------------
    # Publisher Renderer

    security.declareProtected(
        permission_publish_frontends, 'manage_interfacesRender')

    def manage_interfacesRender(self, ids=[], REQUEST=None):
        """Return method (DEPRECATED)."""
        deprecated_method('manage_interfacesRender')
        self.render_frontends(ids)

    security.declareProtected(
        permission_publish_frontends, 'manage_interfacesRenderForm')

    def manage_interfacesRenderForm(self, REQUEST=None):
        """Render Frontends Form (DEPRECATED)."""
        deprecated_form('manage_interfacesRenderForm')
        return self.renderer_form(self, REQUEST)

    # -------------------------------------------------------------------------
    # Publisher Widgets

    security.declareProtected(
        permission_manage_frontends, 'getWidgetsForField')

    def getWidgetsForField(self, formTypeId, fieldTypeId):
        """Return method (DEPRECATED)."""
        deprecated_method('getWidgetsForField')
        return self.get_widgets_for_field(formTypeId, fieldTypeId)

    # -------------------------------------------------------------------------
    # Service Assistant

    security.declareProtected(permission_manage, 'manage_aboutAssistantForm')

    def manage_aboutAssistantForm(self, REQUEST=None):
        """Assistant Form (DEPRECATED)."""
        deprecated_form('manage_aboutAssistantForm')
        return self.assistant_form(self, REQUEST)

    # -------------------------------------------------------------------------
    # Service Community

    # -------------------------------------------------------------------------
    # Service Feedback

    security.declareProtected(permission_zmi, 'manage_aboutFeedbackForm')

    def manage_aboutFeedbackForm(self, REQUEST=None):
        """Feedback Form (DEPRECATED)."""
        deprecated_form('manage_aboutFeedbackForm')
        return self.feedback_form(self, REQUEST)

    # -------------------------------------------------------------------------
    # Service Help

    # -------------------------------------------------------------------------
    # Service Manual

    security.declareProtected(permission_zmi, 'manage_aboutManualForm')

    def manage_aboutManualForm(self, REQUEST=None):
        """Manual Form (DEPRECATED)."""
        deprecated_form('manage_aboutManualForm')
        return self.manual_form(self, REQUEST)

    # -------------------------------------------------------------------------
    # Service Reference

    # -------------------------------------------------------------------------
    # Service Release

    security.declareProtected(permission_zmi, 'manage_aboutReleaseForm')

    def manage_aboutReleaseForm(self, REQUEST=None):
        """Release Form (DEPRECATED)."""
        deprecated_form('manage_aboutReleaseForm')
        return self.release_form(self, REQUEST)

    security.declareProtected(permission_zmi, 'manage_aboutVersion')

    def manage_aboutVersion(self):
        """Return the contents of the VERSION.txt file (DEPRECATED)."""
        deprecated_method('manage_aboutVersion')
        return self.read_release_version_file()

    security.declareProtected(permission_zmi, 'manage_aboutReadMe')

    def manage_aboutReadMe(self):
        """Return the contents of the README.txt file (DEPRECATED)."""
        deprecated_method('manage_aboutReadMe')
        return self.read_release_readme_file()

    security.declareProtected(permission_zmi, 'manage_aboutLicense')

    def manage_aboutLicense(self):
        """Return the contents of the LICENSE.txt file (DEPRECATED)."""
        deprecated_method('manage_aboutLicense')
        return self.read_release_license_file()

    # -------------------------------------------------------------------------
    # System Events

    # -------------------------------------------------------------------------
    # System Integrity

    security.declareProtected(permission_manage, 'manage_systemIntegrityForm')

    def manage_systemIntegrityForm(self, REQUEST=None):
        """Return form integrity_form (DEPRECATED)."""
        deprecated_form('manage_systemIntegrityForm')
        return self.integrity_form(self, REQUEST)

    # -------------------------------------------------------------------------
    # System Plugins

    security.declareProtected(permission_manage, 'manage_systemPluginsForm')

    def manage_systemPluginsForm(self, REQUEST=None):
        """Return form plugins_form (DEPRECATED)."""
        deprecated_form('manage_systemPluginsForm')
        return self.plugins_form(self, REQUEST)

    security.declareProtected(permission_manage, 'pluginIds')

    def pluginIds(self, pluginTypes=[]):
        """Return ids of plugins (DEPRECATED)."""
        deprecated_method('pluginIds')
        return map(lambda item: item[0], self.pluginItems(pluginTypes))

    security.declareProtected(permission_manage, 'pluginItems')

    def pluginItems(self, pluginTypes=[]):
        """Return tuples of id, value of plugins (DEPRECATED)."""
        deprecated_method('pluginItems')
        result = []
        if isinstance(pluginTypes, str):
            pluginTypes = [pluginTypes, ]
        elif len(pluginTypes) == 0:
            pluginTypes = all_plugintypes  # TODO: was validPluginTypes?
        for plugin_type in pluginTypes:
            for id, plugin in self.plugin_items():
                if plugin.get('visibility', None) in pluginTypes:
                    result.append((id, plugin))
        return result

    security.declareProtected(permission_manage, 'pluginValues')

    def pluginValues(self, pluginTypes=[]):
        """Return values of plugins (DEPRECATED)."""
        deprecated_method('pluginValues')
        return map(lambda item: item[1], self.pluginItems(pluginTypes))

    security.declareProtected(permission_manage, 'getPlugin')

    def getPlugin(self, pluginType):
        """Return the specified plugin (DEPRECATED)."""
        deprecated_method('getPlugin')
        return self.get_plugin(pluginType)

    # -------------------------------------------------------------------------
    # System Presets

    security.declareProtected(
        permission_manage_presets, 'manage_presetsBrowserForm')

    def manage_presetsBrowserForm(self, REQUEST=None):
        """Return form presets_form (DEPRECATED)."""
        deprecated_form('manage_presetsBrowserForm')
        return self.presets_form(self, REQUEST)

    security.declareProtected(permission_save_presets, 'manage_presetsNewForm')

    def manage_presetsNewForm(self, REQUEST=None):
        """Return form save_preset_form (DEPRECATED)."""
        deprecated_form('manage_presetsNewForm')
        return self.save_preset_form(self, REQUEST)

    # -------------------------------------------------------------------------
    # System Profiles

    security.declareProtected(permission_manage, 'manage_systemProfilesForm')

    def manage_systemProfilesForm(self, REQUEST=None):
        """Return form profiles_form (DEPRECATED)."""
        deprecated_form('manage_systemProfilesForm')
        return self.profiles_form(self, REQUEST)

    # -------------------------------------------------------------------------
    # System Settings

    security.declareProtected(permission_manage, 'manage_systemSettingsForm')

    def manage_systemSettingsForm(self, REQUEST=None):
        """Return form settings_form (DEPRECATED)."""
        deprecated_form('manage_systemSettingsForm')
        return self.settings_form(self, REQUEST)

    # -------------------------------------------------------------------------
    # System Tools

    security.declareProtected(permission_manage, 'manage_systemToolsForm')

    def manage_systemToolsForm(self, REQUEST=None):
        """Return form tools_form (DEPRECATED)."""
        deprecated_form('manage_systemToolsForm')
        return self.tools_form(self, REQUEST)


# ----------------------------------------------------------------------------
# Class Security


InitializeClass(HistoricalCompatibility)

# !!! historical.py - handle request vars (entryId instead of entry_id, etc.)
