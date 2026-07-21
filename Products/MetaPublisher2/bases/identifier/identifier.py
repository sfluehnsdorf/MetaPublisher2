"""MetaPublisher2 - Identifier Plugin Base."""


from Products.MetaPublisher2.bases.plugin import PluginBase
from Products.MetaPublisher2.interfaces import IIdentifierPluginBase
from Products.MetaPublisher2.library.common import (
    ClassSecurityInfo, DTMLFile, implements, InitializeClass)


# ============================================================================
# Module Exports

__all__ = [
    'IdentifierPluginBase',
]


# ============================================================================
# Identifier Plugin Base Class

class IdentifierPluginBase(PluginBase):
    """Identifier Plugin Base Class."""

    security = ClassSecurityInfo()

    implements(IIdentifierPluginBase)

    # ------------------------------------------------------------------------
    # Plugin Attributes

    id_counter = 0

    id_template = '%(storage)s_%04(counter)d'

    # ------------------------------------------------------------------------
    # ZMI Attributes

    isZMP2StoragePlugin = 1

    icon = 'misc_/MetaPublisher2/Storage.gif'

    _properties = PluginBase._properties + (
        {'id': 'id_counter', 'type': 'int', 'mode': 'w'},
        {'id': 'id_template', 'type': 'string', 'mode': 'w'},
    )

    # ------------------------------------------------------------------------
    # Storage's Identifier

    # !!! bases/identifier/identifier.py - StoragePlugin: last_entry_id

    # !!! bases/identifier/identifier.py - StoragePlugin: new_entry_id

    def storage_newEntryId(self):
        """Generate a new Entry id for the specified Storage."""
        storageId = self.getStorageId()
        counter = 0
        entryId = '%s_%04d' % (storageId, counter)
        entryIds = self.storage_entryIds()
        while entryId in entryIds:
            counter = counter + 1
            entryId = '%s_%04d' % (storageId, counter)
        return entryId

    # --------------------------------------------------------------------------
    # EntryIdPattern Formlet

    entryIdPattern_formlet = DTMLFile('formlet_entryIdPattern', globals())

    def entryIdPattern_test(self, errors, entryIdPatternType, entryIdPattern):
        """TODO: Docstring for entryIdPattern_test."""
        if entryIdPatternType != 'custom':
            if entryIdPatternType == 'sequence':
                entryIdPattern = '%(storageId)s_%(sequence)04d'
            elif entryIdPatternType == 'random':
                entryIdPattern = '%(storageId)s_%(random)04d'
            elif entryIdPatternType == 'uid':
                entryIdPattern = '%(storageId)s_%(uid)s'
            else:
                errors['entryIdPattern'] = (
                    u'!TXT! The specified Entry Id pattern type is unknown!')
        if 'entryId' not in errors:
            entryIdPattern = str(entryIdPattern)
            try:
                entryIdPattern % {
                    'mp2Id': 'test',
                    'storageId': 'test',
                    'sequence': 1,
                    'random': 1,
                    'uid': 'abcdef'}
            except Exception as e:
                errors['entryIdPattern'] = (
                    u'!TXT! The specified Entry Id pattern has errors '
                    u'(%s)!' % e)

        return errors, entryIdPattern


# ----------------------------------------------------------------------------
# initialize class security


InitializeClass(IdentifierPluginBase)


# !!! bases/identifier/identifier.py - define api
# !!! bases/identifier/identifier.py - implement backdrop/failsafe code
# !!! bases/identifier/identifier.py - handle identifier detached from storages
#     (i.e. on storage level, with "redirect" in storage)
