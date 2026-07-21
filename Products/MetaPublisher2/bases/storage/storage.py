"""MetaPublisher2 - Storage Plugin Base."""


from Products.MetaPublisher2.bases.entrycontainer import EntryContainer
from Products.MetaPublisher2.bases.plugin import PluginBase
from Products.MetaPublisher2.interfaces import IStoragePluginBase
from Products.MetaPublisher2.library.application import (
    permission_access_configuration, permission_change_configuration)
from Products.MetaPublisher2.library.common import (
    ClassSecurityInfo, DTMLFile, InitializeClass, OrderedFolder, implements,
    true)
from Products.MetaPublisher2.library.userinterface import UserInterface


# ==============================================================================
# Module Exports

__all__ = [
    'StoragePluginBase',
]


# =============================================================================
# Storage Plugin Base Class


class StoragePluginBase(
    EntryContainer, UserInterface, PluginBase, OrderedFolder
):
    """Storage Plugin Base Class."""

    security = ClassSecurityInfo()

    implements(IStoragePluginBase)

    # -------------------------------------------------------------------------
    # Storage Attributes

    icon = 'misc_/MetaPublisher2/storage.png'

    _properties = PluginBase._properties + (
        {'id': 'storage_type', 'type': 'string', 'mode': ''},
    )

    # -------------------------------------------------------------------------
    # Storage Plugin Description

    plugin_type = 'Storage'

    storage_type = None

    # -------------------------------------------------------------------------
    # Storage Specification

    security.declareProtected(
        permission_access_configuration, 'get_plugin_specification')

    def get_plugin_specification(self):
        """Return a dictionary describing this Storage."""
        options = PluginBase.get_plugin_specification(self)
        options.update({
            'storage_type': self.storage_type,
        })
        return options

    # -------------------------------------------------------------------------
    # Storage Identity API

    security.declareProtected(
        permission_access_configuration, 'get_storage_instance')

    get_storage_instance = PluginBase.get_plugin_instance

    security.declareProtected(
        permission_access_configuration, 'get_storage_id')

    get_storage_id = PluginBase.get_plugin_id

    security.declareProtected(
        permission_access_configuration, 'get_storage_url')

    get_storage_url = PluginBase.get_plugin_url

    # -------------------------------------------------------------------------
    # Storage ZMI

    security.declareProtected(
        permission_change_configuration, 'add_storage_formlet')

    add_storage_formlet = DTMLFile('storageplugin_add', globals())

    security.declareProtected(
        permission_change_configuration, 'edit_storage_formlet')

    edit_storage_formlet = DTMLFile('storageplugin_edit', globals())

    # -------------------------------------------------------------------------
    # Storage Retrieval API

    def get_status(self):
        """TODO: Docstring for get_status."""
        # TODO: IMPORTANT - get_status !TXT!
        pass

    # -------------------------------------------------------------------------
    # Storage Mutation API

    def add_storage(self, options):
        """TODO: Docstring for add_storage."""
        # TODO: IMPORTANT - add_storage !TXT! maybe auto set properties
        #   as placeholder
        pass

    def edit_storage(self, options):
        """TODO: Docstring for edit_storage."""
        # TODO: IMPORTANT - edit_storage !TXT! maybe auto set properties
        #   as placeholder
        pass

    def before_duplicate(self, new_id):
        """TODO: Docstring for before_duplicate."""
        # TODO: OPTIONAL - before_duplicate !TXT!
        pass

    def after_duplicate(self, old_id):
        """TODO: Docstring for after_duplicate."""
        # TODO: OPTIONAL - after_duplicate !TXT!
        pass

    def before_rename(self, new_id):
        """TODO: Docstring for before_rename."""
        # TODO: OPTIONAL - before_rename !TXT!
        pass

    def after_rename(self, old_id):
        """TODO: Docstring for after_rename."""
        # TODO: OPTIONAL - after_rename !TXT!
        pass

    def before_delete(self):
        """TODO: Docstring for before_delete."""
        # TODO: OPTIONAL - before_delete !TXT!
        pass

    def is_source_storage(self):
        """TODO: Docstring for is_source_storage."""
        return true

    def get_source_storages(self):
        """TODO: Docstring for get_source_storages."""
        return []

    # -------------------------------------------------------------------------
    # Identifiers Retrieval API

    def last_entry_id(self):
        """Read last entry id from property."""
        pass

    def new_entry_id(self):
        """TODO: Docstring for new_entry_id."""
        pass

    # -------------------------------------------------------------------------
    # Fields Retrieval API

    def count_fields(self):
        """Docstring for count_fields."""
        pass

    def field_ids(self):
        """Docstring for field_ids."""
        pass

    def field_items(self):
        """Docstring for field_items."""
        pass

    def field_values(self):
        """Docstring for field_values."""
        pass

    def get_field(self, field_id):
        """Docstring for get_field."""
        pass

    def get_field_default(self, field_id):
        """Docstring for get_field_default."""
        pass

    def has_all_fields(self, field_ids=None, field_types=None):
        """Docstring for has_all_fields."""
        pass

    def has_any_fields(self, field_ids=None, field_types=None):
        """Docstring for has_any_fields."""
        pass

    def has_field(self, field_id):
        """Docstring for has_field."""
        pass

    # -------------------------------------------------------------------------
    # Fields Mutation API

    def before_add_field(self, field_id, field_type_id, options):
        """Docstring for before_add_field."""
        pass

    def after_add_field(self, field_id, field_type_id, options):
        """Docstring for after_add_field."""
        pass

    def delete_field(self, field_id):
        """Docstring for delete_field."""
        pass

    def delete_fields(self, field_ids):
        """Docstring for delete_fields."""
        pass

    def duplicate_field(self, field_id, new_id):
        """Docstring for duplicate_field."""
        pass

    def duplicate_fields(self, field_ids, new_ids):
        """Docstring for duplicate_fields."""
        pass

    def edit_field(self, field_id, options):
        """Docstring for edit_field."""
        pass

    def rename_field(self, field_id, new_id):
        """Docstring for rename_field."""
        pass

    def rename_fields(self, field_ids, new_ids):
        """Docstring for rename_fields."""
        pass

    def set_field_default(self, field_id, value):
        """Docstring for set_field_default."""
        pass

    # -------------------------------------------------------------------------
    # Primary Field API

    def is_primary_field(self, field_id):
        """Docstring for is_primary_field."""
        pass

    def primary_field_ids(self):
        """Docstring for primary_field_ids."""
        pass

    def primary_field_items(self):
        """Docstring for primary_field_items."""
        pass

    def primary_field_values(self):
        """Docstring for primary_field_values."""
        pass

    def set_primary_field(self, field_id):
        """Docstring for set_primary_field."""
        pass

    def unset_primary_field(self, field_id):
        """Docstring for unset_primary_field."""
        pass

    # -------------------------------------------------------------------------
    # Field Ordering API

    def get_field_position(self, field_id):
        """Docstring for get_field_position."""
        pass

    def move_field_to_position(self, field_id, position):
        """Docstring for move_field_to_position."""
        pass

    def move_field_to_top(self, field_id):
        """Docstring for move_field_to_top."""
        pass

    def move_field_up(self, field_id):
        """Docstring for move_field_up."""
        pass

    def move_field_down(self, field_id):
        """Docstring for move_field_down."""
        pass

    def move_field_to_bottom(self, field_id):
        """Docstring for move_field_to_bottom."""
        pass


# ----------------------------------------------------------------------------
# initialize class security


InitializeClass(StoragePluginBase)

# !!! bases/storage/storage.py - define api, including before_ and after_
#     handlers (see legacystorage.py for default implementations)
# !!! bases/storage/storage.py - define zmi (with developer notes regarding
#     choice of form and formlet)
# !!! bases/storage/storage.py - create unreadable_storage.py
# !!! bases/storage/storage.py - create unwriteable_storage.py
# !!! bases/storage/storage.py - create unconfigurable_storage.py
