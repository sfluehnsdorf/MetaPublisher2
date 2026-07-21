"""MetaPublisher2 - Storage Plugin Interface."""


from zope.interface import Interface


# ============================================================================
# Module Exports

__all__ = [
    'IStoragePluginBase',
]


# ============================================================================
# Storage Plugin Base Interface

class IStoragePluginBase(Interface):
    """Storage Plugin Base Interface."""

    # ------------------------------------------------------------------------
    # Storage Mutation API

    def add_storage(options):
        """TODO: Docstring for add_storage."""

    def edit_storage(options):
        """TODO: Docstring for edit_storage."""

    def before_duplicate(new_id):
        """TODO: Docstring for before_duplicate."""

    def after_duplicate(old_id):
        """TODO: Docstring for after_duplicate."""

    def before_rename(new_id):
        """TODO: Docstring for before_rename."""

    def after_rename(old_id):
        """TODO: Docstring for after_rename."""

    def before_delete():
        """TODO: Docstring for before_delete."""

    # ------------------------------------------------------------------------
    # Identifiers Retrieval API

    def last_entry_id():
        """TODO: Docstring for last_entry_id."""

    def new_entry_id():
        """TODO: Docstring for new_entry_id."""

    # ------------------------------------------------------------------------
    # Fields Retrieval API

    def count_fields():
        """TODO: Docstring for count_fields."""

    def field_ids():
        """TODO: Docstring for field_ids."""

    def field_items():
        """TODO: Docstring for field_items."""

    def field_values():
        """TODO: Docstring for field_values."""

    def get_field(field_id):
        """TODO: Docstring for get_field."""

    def get_field_default():
        """TODO: Docstring for get_field_default."""

    def has_all_fields(field_ids=None, field_types=None):
        """TODO: Docstring for has_all_fields."""

    def has_any_fields(field_ids=None, field_types=None):
        """TODO: Docstring for has_any_fields."""

    def has_field(field_id):
        """TODO: Docstring for has_field."""

    # ------------------------------------------------------------------------
    # Fields Mutation API

    def before_add_field(field_id, field_type_id, options):
        """TODO: Docstring for before_add_field."""

    def after_add_field(field_id, field_type_id, options):
        """TODO: Docstring for after_add_field."""

    def delete_field(field_id):
        """TODO: Docstring for delete_field."""

    def delete_fields(field_ids):
        """TODO: Docstring for delete_fields."""

    def duplicate_field(field_id, new_id):
        """TODO: Docstring for duplicate_field."""

    def duplicate_fields(field_ids, new_ids):
        """TODO: Docstring for duplicate_fields."""

    def edit_field(field_id, options):
        """TODO: Docstring for edit_field."""

    def rename_field(field_id, new_id):
        """TODO: Docstring for rename_field."""

    def rename_fields(field_ids, new_ids):
        """TODO: Docstring for rename_fields."""

    def set_field_default(field_id, value):
        """TODO: Docstring for set_field_default."""

    # ------------------------------------------------------------------------
    # Primary Field API

    def is_primary_field(field_id):
        """TODO: Docstring for is_primary_field."""

    def primary_field_ids():
        """TODO: Docstring for primary_field_ids."""

    def primary_field_items():
        """TODO: Docstring for primary_field_items."""

    def primary_field_values():
        """TODO: Docstring for primary_field_values."""

    def set_primary_field(field_id):
        """TODO: Docstring for set_primary_field."""

    def unset_primary_field(field_id):
        """TODO: Docstring for unset_primary_field."""

    # ------------------------------------------------------------------------
    # Field Ordering API

    def get_field_position(field_id):
        """TODO: Docstring for get_field_position."""

    def move_field_to_position(field_id, position):
        """TODO: Docstring for move_field_to_position."""

    def move_field_to_top(field_id):
        """TODO: Docstring for move_field_to_top."""

    def move_field_up(field_id):
        """TODO: Docstring for move_field_up."""

    def move_field_down(field_id):
        """TODO: Docstring for move_field_down."""

    def move_field_to_bottom(field_id):
        """TODO: Docstring for move_field_to_bottom."""

# !!! interfaces/storage.py - review api
