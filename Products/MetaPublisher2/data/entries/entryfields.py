"""MetaPublisher2 - Entry Fields Component."""


from Products.MetaPublisher2.library.application import (
    permission_access_entries, permission_change_entries)
from Products.MetaPublisher2.library.common import (
    ClassSecurityInfo, InitializeClass)


# =============================================================================
# Module Exports

__all__ = [
    'EntryFields',
]


# =============================================================================
# Entry Fields Component Mix-In Class

class EntryFields:
    """Entry Fields Component Mix-In Class."""

    security = ClassSecurityInfo()

    # -------------------------------------------------------------------------
    # EntryField Retrieval API

    security.declareProtected(permission_access_entries, 'get_entryfield')

    def get_entryfield(
        self, source, field_id, default=None, parent_entry_id=None,
        entry_id=None, entry_position=None
    ):
        """Return the specified Entry's Field's value."""
        source = self.get_storage(source)
        return source.get_entryfield(
            field_id, default, parent_entry_id, entry_id, entry_position)

    # !!! entryfields.py - implement get_entryfields

    # !!! entryfields.py - implement get_entryfields_mapping

    security.declareProtected(permission_access_entries, 'count_entryfields')

    def count_entryfields(
        self, source, field_id, value, parent_entry_id=None, entry_ids=None,
        entry_positions=None, conditions=None
    ):
        """Count the number of Entries, with a specific Field's value."""
        source = self.get_storage(source)
        return source.count_entryfields(
            field_id, value, parent_entry_id, entry_ids, entry_positions,
            conditions)

    security.declareProtected(
        permission_access_entries, 'count_unique_entryfields')

    def count_unique_entryfields(
        self, source, field_id, parent_entry_id=None, entry_ids=None,
        entry_positions=None, conditions=None
    ):
        """Return a mapping of counts of unique values.

        Return a mapping with the number of Entries for each unique value of a
        specific Field's value.
        """
        source = self.get_storage(source)
        return source.count_unique_entryfields(
            field_id, parent_entry_id, entry_ids, entry_positions, conditions)

    security.declareProtected(permission_access_entries, 'has_any_entryfields')

    def has_any_entryfields(
        self, source, field_id, value, parent_entry_id=None, entry_ids=None,
        entry_positions=None, conditions=None
    ):
        """Return True if any Entries have the value in the specified Field.

        Return True if any of the specified Entries have the specified value in
        the specified Field, limited to the Entries specified and matching
        conditions if defined.
        """
        source = self.get_storage(source)
        return source.has_any_entryfields(
            field_id, value, parent_entry_id, entry_ids, entry_positions,
            conditions)

    security.declareProtected(permission_access_entries, 'has_all_entryfields')

    def has_all_entryfields(
        self, source, field_id, value, parent_entry_id=None, entry_ids=None,
        entry_positions=None, conditions=None
    ):
        """Return True if all Entries have the value in the specified Field.

        Return True if all of the specified Entries have the specified value in
        the specified Field, limited to the Entries specified and matching
        conditions if defined.
        """
        source = self.get_storage(source)
        return source.has_all_entryfields(
            field_id, value, parent_entry_id, entry_ids, entry_positions,
            conditions)

    security.declareProtected(permission_access_entries, 'has_entryfield')

    def has_entryfield(self, source, field_id, entry_id):
        """Return True if the specified EntryField exists."""
        source = self.get_storage(source)
        return source.has_entryfield(field_id, entry_id)

    security.declareProtected(
        permission_access_entries, 'get_unique_entryfields')

    def get_unique_entryfields(
        self, source, field_id, parent_entry_id=None, entry_ids=None,
        entry_positions=None, conditions=None
    ):
        """Return a list of unique values stored in the specified Field.

        Return a list of unique values stored in the specified Field, limited
        to the Entries specified and matching conditions if defined.
        """
        source = self.get_storage(source)
        return source.get_unique_entryfields(
            field_id, parent_entry_id, entry_ids, entry_positions, conditions)

    # -------------------------------------------------------------------------
    # EntryField Mutation API

    security.declareProtected(permission_change_entries, 'reset_entryfield')

    def reset_entryfield(
        self, source, field_id, parent_entry_id=None, entry_id=None,
        entry_position=None
    ):
        """Reset the specified Field to its default value."""
        source = self.get_storage(source)
        source.reset_entryfield(
            field_id, parent_entry_id, entry_id, entry_position)

    security.declareProtected(permission_change_entries, 'reset_entryfields')

    def reset_entryfields(
        self, source, field_id, parent_entry_id=None, entry_ids=None,
        entry_positions=None, conditions=None
    ):
        """Reset the Field of the specified Entries to its default value."""
        source = self.get_storage(source)
        source.reset_entryfields(
            field_id, parent_entry_id, entry_ids, entry_positions, conditions)

    security.declareProtected(permission_change_entries, 'set_entryfield')

    def set_entryfield(
        self, source, field_id, value, parent_entry_id=None, entry_id=None,
        entry_position=None
    ):
        """Set values of specified Field of Entry."""
        source = self.get_storage(source)
        source.set_entryfield(
            field_id, parent_entry_id, entry_id, entry_position)

    security.declareProtected(permission_change_entries, 'set_entryfields')

    def set_entryfields(
        self, source, field_id, value, parent_entry_id=None, entry_ids=None,
        entry_positions=None, conditions=None
    ):
        """Set values of specified Field of Entries, matching conditions."""
        source = self.get_storage(source)
        source.set_entryfields(
            field_id, value, parent_entry_id, entry_ids, entry_positions,
            conditions)


# -----------------------------------------------------------------------------
# Class Security


InitializeClass(EntryFields)


# !!! entryfields.py - max, min, mean, mediate, avg, sum
# !!! entryfields.py - like, startswith, endswith, contains, between
# !!! entryfields.py - is_null, not_null
