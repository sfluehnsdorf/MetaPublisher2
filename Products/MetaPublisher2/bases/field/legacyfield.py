# -*- coding: iso-8859-15 -*-
# ============================================================================
#
#                         M e t a  P u b l i s h e r  2
#
# ----------------------------------------------------------------------------
# Copyright (c) 2002-2013, Sebastian Lühnsdorf - Web-Solutions and others
# For more information see the README.txt file or visit www.metapulisher.org
# ----------------------------------------------------------------------------
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).
#
# A copy of the ZPL should accompany this distribution.
#
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE
#
# ============================================================================

__doc__ = """Legacy Field Base

$Id: bases/field/legacyfield.py 7 2012-02-17 15:45:00Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.bases.plugin.legacyplugin import LegacyPluginBase
from Products.MetaPublisher2.library.common import ClassSecurityInfo, DTMLFile, InitializeClass

from field import FieldPluginBase


# ============================================================================
# Module Exports

__all__ = [
    'LegacyFieldPlugin',
]


# ============================================================================
# Legacy Field Base

class LegacyFieldPlugin(LegacyPluginBase, FieldPluginBase):
    """Legacy Field Base"""

    security = ClassSecurityInfo()

    # --------------------------------------------------------------------------
    # Field Attributes

    isZMP2FieldPlugin = 1

    # --------------------------------------------------------------------------
    # Field Identity API

    getFieldObject = FieldPluginBase.get_plugin_instance

    getFieldId = FieldPluginBase.get_plugin_id

    getFieldURL = FieldPluginBase.get_plugin_url

    # --------------------------------------------------------------------------

    def get_immutable_pluginflag_ids(self):
        """Return list of Plugin flag ids, which are either constants or set by an external source and may not be altered by MetaPublisher2 or its users"""

        # !!! bases/field/legacyfield.py - get_immutable_pluginflag_ids
        return []

    def get_mutable_pluginflag_ids(self):
        """Return list of Plugin flag ids, which may be altered by MetaPublisher2 and its users"""

        # !!! bases/field/legacyfield.py - get_mutable_pluginflag_ids
        return []

    # --------------------------------------------------------------------------
    # Field Specification

    def getFieldInfo(self):
        """Return information about this Field if available"""

        raise NotImplementedError

    def get_plugin_infos(self):
        """Return information about this Field if available"""

        return self.getFieldInfo()

    # --------------------------------------------------------------------------
    # Field ZMI

    manage_configureFieldForm = DTMLFile('fieldplugin_edit', globals())

    def manage_configureField(self, REQUEST=None):
        """Change Field's configuration parameters"""

        self.title = REQUEST.get('title', '')

        self.redirect(REQUEST, 'fields_form', 'Changes saved', storage_id=self.getStorageId())

    def renderAdd(self):
        """Return a html code for adding an Entry with this Field"""

        raise NotImplementedError

    def renderEdit(self, entry_id):
        """Return a html code for editing an Entry with this Field"""

        raise NotImplementedError

    def renderView(self, entry_id):
        """Return a html code for viewing an Entry with this Field"""

        raise NotImplementedError

    # --------------------------------------------------------------------------
    # Field Retrieval API

    def _getValue(self, entryId, default):
        """Retrieve a value from an entry"""

        raise NotImplementedError

    def getValue(self, entryId, default=None):
        """Wapper for retrieving a value from an entry"""

        return self._getValue(entryId, default)

    def _hasValue(self, entry_id):
        """Return 1 if the Entry has a value stored for this Field, 0 otherwise"""

        raise NotImplementedError

    def hasValue(self, entry_id):
        """Wrapper for testing existence of a value in an Entry"""

        return self._hasValue(entry_id)

    def _testValue(self, value, options={}):
        """Test a value for validity"""

        raise NotImplementedError

    def testValue(self, value, **options):
        """Wrapper for testing a value's validity"""

        try:
            return self._testValue(value, options)
        except:
            raise TestError(errorType=sys.exc_type, errorValue=sys.exc_value)

    # --------------------------------------------------------------------------
    # Field Mutation API

    def _setValue(self, entry_id, value):
        """Store a value in an entry"""

        raise NotImplementedError

    def setData(self, entry_id, data):
        """Set the value inside data for this Field in the Entry"""

        raise NotImplementedError

    def setDefault(self, entry_id):
        """Set the default value for this Field in the Entry"""

        raise NotImplementedError

    def setValue(self, entry_id, value):
        """Wapper for storing a value in an entry"""

        try:
            result = self.testValue(value)
            self._setValue(entry_id, result)
        except TestError, error:
            raise error.errorType, error.errorValue

# ------------------------------------------------------------------------------
# initialize class security

InitializeClass(LegacyFieldPlugin)

# !!! bases/field/legacyfield.py - revise and update legacy api
