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

__doc__ = """Field Base

$Id: bases/field/field.py 5 2012-02-17 15:45:00Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.bases.plugin import PluginBase
from Products.MetaPublisher2.interfaces import IFieldPluginBase
from Products.MetaPublisher2.library.application import permission_access_configuration, permission_change_configuration
from Products.MetaPublisher2.library.common import ClassSecurityInfo, DTMLFile, false, implements, InitializeClass, OrderedFolder


# ============================================================================
# Module Exports

__all__ = [
    'FieldPluginBase',
]


# ============================================================================
# Field Plugin Base

class FieldPluginBase(PluginBase, OrderedFolder):
    """Field Plugin Base"""

    security = ClassSecurityInfo()

    implements(IFieldPluginBase)

    # ------------------------------------------------------------------------
    # Field Attributes

    icon = 'misc_/MetaPublisher2/field.png'

    _properties = PluginBase._properties + (
        {'id': 'field_type', 'type': 'string', 'mode': ''},
        {'id': 'primary_field', 'type': 'boolean', 'mode': 'w'},
    )

    # ------------------------------------------------------------------------
    # Field Plugin Description

    plugin_type = 'Field'

    field_type = None

    primary_field = false

    # ------------------------------------------------------------------------
    # Field Specification

    security.declareProtected(permission_access_configuration, 'get_plugin_specification')

    def get_plugin_specification(self):
        """Return a dictionary describing this Field"""

        options = PluginBase.get_plugin_specification(self)
        options.update({
            'field_type': self.field_type,
            'primary_field': self.primary_field,
        })
        return options

    # ------------------------------------------------------------------------
    # Field Identity API

    security.declareProtected(permission_access_configuration, 'get_field_instance')

    get_field_instance = PluginBase.get_plugin_instance

    security.declareProtected(permission_access_configuration, 'get_field_id')

    get_field_id = PluginBase.get_plugin_id

    security.declareProtected(permission_access_configuration, 'get_field_url')

    get_field_url = PluginBase.get_plugin_url

    # ------------------------------------------------------------------------
    # Field ZMI

    security.declareProtected(permission_change_configuration, 'add_field_formlet')

    add_field_formlet = DTMLFile('fieldplugin_add', globals())

    security.declareProtected(permission_change_configuration, 'edit_field_formlet')

    edit_field_formlet = DTMLFile('fieldplugin_edit', globals())

    # ------------------------------------------------------------------------
    # !TXT!

    # !!! bases/field/field.py - check api requirements for get_field_info, is_field_gettable, is_field_settable, is_field_nullable, is_field_defaultable, is_field_requirable

    def is_field_requirable(self):
        """!TXT!"""

        return self.requirable

    def is_field_required(self):
        """!TXT!"""

        return self.required

    # ------------------------------------------------------------------------
    # !TXT!

    def setDefault(self, entryId):
        """!TXT! Set the default value for this Field in the Entry"""

        raise NotImplementedError

    def setData(self, entryId, data):
        """!TXT! Set the value inside data for this Field in the Entry"""

        raise NotImplementedError

    # ------------------------------------------------------------------------
    # !TXT!

    def _getValue(self, entryId, default):
        """!TXT! Retrieve a value from an entry"""

        raise NotImplementedError

    def getValue(self, entryId, default=None):
        """!TXT! Wrapper for retrieving a value from an entry"""

        return self._getValue(entryId, default)

    # ------------------------------------------------------------------------
    # !TXT!

    def _setValue(self, entryId, value):
        """!TXT! Store a value in an entry"""

        raise NotImplementedError

    def setValue(self, entryId, value):
        """!TXT! Wrapper for storing a value in an entry"""

        try:
            result = self.testValue(value)
            self._setValue(entryId, result)
        except TestError, error:
            raise error.errorType, error.errorValue

    # ------------------------------------------------------------------------
    # !TXT!

    def _hasValue(self, entryId):
        """!TXT! Return 1 if the Entry has a value stored for this Field, 0 otherwise"""

        raise NotImplementedError

    def hasValue(self, entryId):
        """!TXT! Wrapper for testing existence of a value in an Entry"""

        return self._hasValue(entryId)

    # ------------------------------------------------------------------------
    # !TXT!

    def _testValue(self, value, options={}):
        """!TXT! Test a value for validity"""

        raise NotImplementedError

    def testValue(self, value, **options):
        """!TXT! Wrapper for testing a value's validity"""

        try:
            return self._testValue(value, options)
        except Exception, exception:
            raise TestError(errorType=exception.exc_type, errorValue=exception.exc_value)

    # ------------------------------------------------------------------------
    # !TXT!

    render_modes = {}

    def render_field(self, mode_id, entry_id=None):
        """!TXT! default render method (for management forms)"""

        raise NotImplementedError

    def renderAdd(self):
        """!TXT! Return a html code for adding an Entry with this Field"""

        raise NotImplementedError

    def renderEdit(self, entryId):
        """!TXT! Return a html code for editing an Entry with this Field"""

        raise NotImplementedError

    def renderView(self, entryId):
        """!TXT! Return a html code for viewing an Entry with this Field"""

        raise NotImplementedError

# ----------------------------------------------------------------------------
# initialize class security

InitializeClass(FieldPluginBase)

# !!! bases/field/field.py - define api, including before_ and after_ handlers (see legacystorage.py for default implementations)
# !!! bases/field/field.py - define zmi (with developer notes regarding choice of form and formlet)
# !!! bases/field/field.py - check if TestError is needed
# !!! bases/field/field.py - define conditions system (needed for search and expressions)
# !!! bases/field/field.py - check_field_id method
