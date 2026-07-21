"""MetaPublisher2 - Entry Stats Component."""


from Products.MetaPublisher2.library.common import (
    ClassSecurityInfo, InitializeClass)


# ============================================================================
# Module Exports

__all__ = [
    'EntryStats',
]


# ============================================================================
# Entry Stats Component Mix-In Class

class EntryStats:
    """Entry Stats Component Mix-In Class."""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # Entry Stats Retrieval

    def stat_entry(self, source, entry_id):
        """TODO: Docstring for stat_entry."""
        raise NotImplementedError

    def stat_entries(self, source, entry_ids=None, conditions=None):
        """TODO: Docstring for stat_entries."""
        raise NotImplementedError

    def get_entry_stat_size(self, source, entry_id):
        """TODO: Docstring for get_entry_stat_size."""
        raise NotImplementedError

    def get_entry_stat_ctime(self, source, entry_id):
        """TODO: Docstring for get_entry_stat_ctime."""
        raise NotImplementedError

    def get_entry_stat_cuser(self, source, entry_id):
        """TODO: Docstring for get_entry_stat_cuser."""
        raise NotImplementedError

    def get_entry_stat_mtime(self, source, entry_id):
        """TODO: Docstring for get_entry_stat_mtime."""
        raise NotImplementedError

    def get_entry_stat_muser(self, source, entry_id):
        """TODO: Docstring for get_entry_stat_muser."""
        raise NotImplementedError

    def get_entry_stat_atime(self, source, entry_id):
        """TODO: Docstring for get_entry_stat_atime."""
        raise NotImplementedError

    def get_entry_stat_auser(self, source, entry_id):
        """TODO: Docstring for get_entry_stat_auser."""
        raise NotImplementedError

    # ------------------------------------------------------------------------
    # Entry Stats Retrieval

    def touch_entry(self, source, entry_id):
        """TODO: Docstring for touch_entry."""
        raise NotImplementedError

    def touch_entries(self, source, entry_ids=None, conditions=None):
        """TODO: Docstring for touch_entries."""
        raise NotImplementedError

    def access_entry(self, source, entry_id):
        """TODO: Docstring for access_entry."""
        raise NotImplementedError

    def access_entries(self, source, entry_ids=None, conditions=None):
        """TODO: Docstring for access_entries."""
        raise NotImplementedError


# ----------------------------------------------------------------------------
# Class Security

InitializeClass(EntryStats)

# !!! entrystats.py - implement
