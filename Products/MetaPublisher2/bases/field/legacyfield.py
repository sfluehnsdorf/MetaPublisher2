"""MetaPublisher2 - Legacy Field Plugin Base."""


import sys
from Products.MetaPublisher2.bases.plugin.legacyplugin import LegacyPluginBase
from Products.MetaPublisher2.library.common import (
    ClassSecurityInfo, DTMLFile, InitializeClass)
from Products.MetaPublisher2.library.compatibility import TestError

from field import FieldPluginBase


# ============================================================================
# Module Exports

__all__ = [
    'LegacyFieldPlugin',
]


# ============================================================================
# Legacy Field Plugin Base Class

class LegacyFieldPlugin(LegacyPluginBase, FieldPluginBase):
    """Legacy Field Base Class."""

    security = ClassSecurityInfo()

    # -------------------------------------------------------------------------
    # Field Attributes

    isZMP2FieldPlugin = 1

    # -------------------------------------------------------------------------
    # Field Identity API

    getFieldObject = FieldPluginBase.get_plugin_instance

    getFieldId = FieldPluginBase.get_plugin_id

    getFieldURL = FieldPluginBase.get_plugin_url

    # -------------------------------------------------------------------------

    def get_immutable_pluginflag_ids(self):
        """Return list of Plugin flag ids.

        Return list of Plugin flag ids, which are either constants or set by an
        external source and may not be altered by MetaPublisher2 or its users.
        """
        # !!! bases/field/legacyfield.py - get_immutable_pluginflag_ids
        return []

    def get_mutable_pluginflag_ids(self):
        """Return list of Plugin flag ids.

        Return list of Plugin flag ids, which may be altered by MetaPublisher2
        and its users.
        """
        # !!! bases/field/legacyfield.py - get_mutable_pluginflag_ids
        return []

    # -------------------------------------------------------------------------
    # Field Specification

    def getFieldInfo(self):
        """Return information about this Field if available."""
        raise NotImplementedError

    def get_plugin_infos(self):
        """Return information about this Field if available."""
        return self.getFieldInfo()

    # -------------------------------------------------------------------------
    # Field ZMI

    manage_configureFieldForm = DTMLFile('fieldplugin_edit', globals())

    def manage_configureField(self, REQUEST=None):
        """Change Field's configuration parameters."""
        self.title = REQUEST.get('title', '')

        self.redirect(
            REQUEST,
            'fields_form',
            message='!TXT! Changes saved',
            storage_id=self.getStorageId()
        )

    def renderAdd(self):
        """Return a html code for adding an Entry with this Field."""
        raise NotImplementedError

    def renderEdit(self, entry_id):
        """Return a html code for editing an Entry with this Field."""
        raise NotImplementedError

    def renderView(self, entry_id):
        """Return a html code for viewing an Entry with this Field."""
        raise NotImplementedError

    # -------------------------------------------------------------------------
    # Field Retrieval API

    def _getValue(self, entryId, default):
        """Retrieve a value from an entry."""
        raise NotImplementedError

    def getValue(self, entryId, default=None):
        """Wapper for retrieving a value from an entry."""
        return self._getValue(entryId, default)

    def _hasValue(self, entry_id):
        """Return 1 if the Entry has a value stored in this Field, 0 if not."""
        raise NotImplementedError

    def hasValue(self, entry_id):
        """Test existence of a value in an Entry."""
        return self._hasValue(entry_id)

    def _testValue(self, value, options={}):
        """Test a value for validity."""
        raise NotImplementedError

    def testValue(self, value, **options):
        """Wrapper for testing a value's validity."""
        try:
            return self._testValue(value, options)
        except Exception:
            raise TestError(errorType=sys.exc_type, errorValue=sys.exc_value)

    # -------------------------------------------------------------------------
    # Field Mutation API

    def _setValue(self, entry_id, value):
        """Store a value in an entry."""
        raise NotImplementedError

    def setData(self, entry_id, data):
        """Set the value inside data for this Field in the Entry."""
        raise NotImplementedError

    def setDefault(self, entry_id):
        """Set the default value for this Field in the Entry."""
        raise NotImplementedError

    def setValue(self, entry_id, value):
        """Wapper for storing a value in an entry."""
        result = self.testValue(value)
        self._setValue(entry_id, result)


# ------------------------------------------------------------------------------
# initialize class security


InitializeClass(LegacyFieldPlugin)


# !!! bases/field/legacyfield.py - revise and update legacy api
