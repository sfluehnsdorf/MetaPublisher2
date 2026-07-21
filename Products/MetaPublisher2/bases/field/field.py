"""MetaPublisher2 - Field Plugin Base."""


from Products.MetaPublisher2.bases.plugin import PluginBase
from Products.MetaPublisher2.interfaces import IFieldPluginBase
from Products.MetaPublisher2.library.application import (
    permission_access_configuration, permission_change_configuration)
from Products.MetaPublisher2.library.common import (
    ClassSecurityInfo, DTMLFile, InitializeClass, OrderedFolder, false,
    implements)
from Products.MetaPublisher2.library.compatibility.historical import TestError


# =============================================================================
# Module Exports

__all__ = [
    'FieldPluginBase',
]


# =============================================================================
# Field Plugin Base Class

class FieldPluginBase(PluginBase, OrderedFolder):
    """Field Plugin Base Class."""

    security = ClassSecurityInfo()

    implements(IFieldPluginBase)

    # -------------------------------------------------------------------------
    # Field Attributes

    icon = 'misc_/MetaPublisher2/field.png'

    _properties = PluginBase._properties + (
        {'id': 'field_type', 'type': 'string', 'mode': ''},
        {'id': 'primary_field', 'type': 'boolean', 'mode': 'w'},
    )

    # -------------------------------------------------------------------------
    # Field Plugin Description

    plugin_type = 'Field'

    field_type = None

    primary_field = false

    # -------------------------------------------------------------------------
    # Field Specification

    security.declareProtected(
        permission_access_configuration, 'get_plugin_specification')

    def get_plugin_specification(self):
        """Return a dictionary describing this Field."""
        options = PluginBase.get_plugin_specification(self)
        options.update({
            'field_type': self.field_type,
            'primary_field': self.primary_field,
        })
        return options

    # -------------------------------------------------------------------------
    # Field Identity API

    security.declareProtected(
        permission_access_configuration, 'get_field_instance')

    get_field_instance = PluginBase.get_plugin_instance

    security.declareProtected(permission_access_configuration, 'get_field_id')

    get_field_id = PluginBase.get_plugin_id

    security.declareProtected(permission_access_configuration, 'get_field_url')

    get_field_url = PluginBase.get_plugin_url

    # -------------------------------------------------------------------------
    # Field ZMI

    security.declareProtected(
        permission_change_configuration, 'add_field_formlet')

    add_field_formlet = DTMLFile('fieldplugin_add', globals())

    security.declareProtected(
        permission_change_configuration, 'edit_field_formlet')

    edit_field_formlet = DTMLFile('fieldplugin_edit', globals())

    # -------------------------------------------------------------------------
    # !TXT!

    # !!! bases/field/field.py - check api requirements for get_field_info,
    #     is_field_gettable, is_field_settable, is_field_nullable,
    #     is_field_defaultable, is_field_requirable

    def is_field_requirable(self):
        """TODO: Docstring for is_field_requirable."""
        return self.requirable

    def is_field_required(self):
        """TODO: Docstring for is_field_required."""
        return self.required

    # -------------------------------------------------------------------------
    # !TXT!

    def setDefault(self, entryId):
        """Set the default value for this Field in the Entry."""
        raise NotImplementedError

    def setData(self, entryId, data):
        """Set the value inside data for this Field in the Entry."""
        raise NotImplementedError

    # -------------------------------------------------------------------------
    # !TXT!

    def _getValue(self, entryId, default):
        """Retrieve a value from an entry."""
        raise NotImplementedError

    def getValue(self, entryId, default=None):
        """Retrieve a value from an entry."""
        return self._getValue(entryId, default)

    # -------------------------------------------------------------------------
    # !TXT!

    def _setValue(self, entryId, value):
        """Store a value in an entry."""
        raise NotImplementedError

    def setValue(self, entryId, value):
        """Store a value in an entry."""
        result = self.testValue(value)
        self._setValue(entryId, result)

    # -------------------------------------------------------------------------
    # !TXT!

    def _hasValue(self, entryId):
        """Return 1 if Entry has a value stored for this Field, 0 if not."""
        raise NotImplementedError

    def hasValue(self, entryId):
        """Test existence of a value in an Entry."""
        return self._hasValue(entryId)

    # -------------------------------------------------------------------------
    # !TXT!

    def _testValue(self, value, options={}):
        """Test a value for validity."""
        raise NotImplementedError

    def testValue(self, value, **options):
        """Test a value for validity."""
        try:
            return self._testValue(value, options)
        except Exception as exception:
            raise TestError(
                errorType=exception.exc_type, errorValue=exception.exc_value)

    # -------------------------------------------------------------------------
    # !TXT!

    render_modes = {}

    def render_field(self, mode_id, entry_id=None):
        """Render method (for management forms)."""
        raise NotImplementedError

    def renderAdd(self):
        """Return a html code for adding an Entry with this Field."""
        raise NotImplementedError

    def renderEdit(self, entryId):
        """Return a html code for editing an Entry with this Field."""
        raise NotImplementedError

    def renderView(self, entryId):
        """Return a html code for viewing an Entry with this Field."""
        raise NotImplementedError


# -----------------------------------------------------------------------------
# initialize class security


InitializeClass(FieldPluginBase)


# !!! bases/field/field.py - define api, including before_ and after_ handlers
#     (see legacystorage.py for default implementations)
# !!! bases/field/field.py - define zmi (with developer notes regarding choice
#     of form and formlet)
# !!! bases/field/field.py - check if TestError is needed
# !!! bases/field/field.py - define conditions system (needed for search and
#     expressions)
# !!! bases/field/field.py - check_field_id method
