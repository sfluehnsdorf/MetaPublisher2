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

__doc__ = """Identifier Plugin Base

!TXT! module info

$Id: bases/identifier/identifier.py 4 2013-05-08 22:53:37Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.bases.plugin import PluginBase
from Products.MetaPublisher2.interfaces import IIdentifierPluginBase
from Products.MetaPublisher2.library.common import ClassSecurityInfo, DTMLFile, implements, InitializeClass, true, false


# ============================================================================
# Module Exports

__all__ = [
    'IdentifierPluginBase',
]


# ============================================================================
# Identifier Plugin Base Class

class IdentifierPluginBase(PluginBase):
    """!TXT! Identifier Plugin Base Class"""

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
        """!TXT! Generate a new Entry id for the specified Storage"""

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
        """!TXT!"""

        if entryIdPatternType != 'custom':
            if entryIdPatternType == 'sequence':
                entryIdPattern = '%(storageId)s_%(sequence)04d'
            elif entryIdPatternType == 'random':
                entryIdPattern = '%(storageId)s_%(random)04d'
            elif entryIdPatternType == 'uid':
                entryIdPattern = '%(storageId)s_%(uid)s'
            else:
                errors['entryIdPattern'] = u'!TXT! The specified Entry Id pattern type is unknown!'
        if not 'entryId' in errors:
            entryIdPattern = str(entryIdPattern)
            try:
                test_id = entryIdPattern % {'mp2Id': 'test', 'storageId': 'test', 'sequence': 1, 'random': 1, 'uid': 'abcdef'}
            except Exception, e:
                errors['entryIdPattern'] = u'!TXT! The specified Entry Id pattern has errors (%s)!' % e

        return errors, entryIdPattern

# ----------------------------------------------------------------------------
# initialize class security

InitializeClass(IdentifierPluginBase)

# !!! bases/identifier/identifier.py - define api
# !!! bases/identifier/identifier.py - implement backdrop/failsafe code
# !!! bases/identifier/identifier.py - handle identifier detached from storages (i.e. on storage level, with "redirect" in storage)
