# -*- coding: iso-8859-15 -*-
# ==============================================================================
#
#                         M e t a  P u b l i s h e r  2
#
# ------------------------------------------------------------------------------
# Copyright (c) 2002-2011, Sebastian Lühnsdorf - Web-Solutions and contributors
# For more information see the README.txt file or visit www.metapulisher.org
# ------------------------------------------------------------------------------
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
# ==============================================================================

__doc__ = """Identifiers Component

!TXT! module info

$Id: configuration/identifiers/identifiers.py 8 2013-05-10 23:02:56Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ==============================================================================
# Module Imports

from Products.MetaPublisher2.library import ClassSecurityInfo, DTMLFile, InitializeClass, permission_manage, permission_access_configuration, show_future


# ============================================================================
# Module Exports

__all__ = [
    'Identifiers',
]


# ==============================================================================
# Identifiers Component Mix-In Class

class Identifiers:
    """!TXT! Identifiers Component Mix-In Class"""

    security = ClassSecurityInfo()

    # --------------------------------------------------------------------------
    # Identifiers ZMI

    security.declareProtected(permission_access_configuration, 'identifiers_form')

    identifiers_form = DTMLFile('identifiers', globals())

    security.declareProtected(permission_access_configuration, 'add_identifier_form')

    add_identifier_form = DTMLFile('add_identifier', globals())

    security.declareProtected(permission_access_configuration, 'delete_identifiers_form')

    delete_identifiers_form = DTMLFile('delete_identifiers', globals())

    security.declareProtected(permission_access_configuration, 'duplicate_identifiers_form')

    duplicate_identifiers_form = DTMLFile('duplicate_identifiers', globals())

    security.declareProtected(permission_access_configuration, 'edit_identifier_form')

    edit_identifier_form = DTMLFile('edit_identifier', globals())

    security.declareProtected(permission_access_configuration, 'rename_identifiers_form')

    rename_identifiers_form = DTMLFile('rename_identifiers', globals())

    # ------------------------------------------------------------------------
    # Storage Plugins

    security.declareProtected(permission_manage, 'has_identifierplugins')

    def has_identifierplugins(self):
        """!TXT! Return the specified MetaPublisher2 Storage plugin"""

        return self.has_plugins(IStoragePluginBase)

    security.declareProtected(permission_manage, 'get_identifierplugin')

    def get_identifierplugin(self, identifierplugin_id):
        """!TXT! Return the specified MetaPublisher2 Storage plugin"""

        return self.get_plugin(identifierplugin_id, IStoragePluginBase)

    security.declareProtected(permission_manage, 'identifierplugin_ids')

    def identifierplugin_ids(self):
        """!TXT! Return ids of installed MetaPublisher2 Storage plugins"""

        return self.plugin_ids(IStoragePluginBase)

    security.declareProtected(permission_manage, 'identifierplugin_items')

    def identifierplugin_items(self):
        """!TXT! Return tuples of id, value of installed MetaPublisher2 Storage plugins"""

        return self.plugin_items(IStoragePluginBase)

    security.declareProtected(permission_manage, 'identifierplugin_values')

    def identifierplugin_values(self):
        """!TXT! Return tuples of id, value of installed MetaPublisher2 Storage plugins"""

        return self.plugin_values(IStoragePluginBases)

    # --------------------------------------------------------------------------
    # Identifiers Retrieval API

    security.declareProtected(permission_access_configuration, 'last_entry_id')

    def last_entry_id(self, identifier_id):
        """!TXT! Returns the last generated Entry id."""

        identifier = self.get_identifier(identifier_id)
        return identifier.last_entry_id()

    security.declareProtected(permission_access_configuration, 'last_entry_id_of_storage')

    def last_entry_id_of_storage(self, storage_id):
        """!TXT! Returns the last generated Entry id."""

        identifier = self.get_storage(storage_id).get_identifier(identifier_id)
        return identifier.last_entry_id()

    # --------------------------------------------------------------------------
    # Identifiers Mutation API

    security.declareProtected(permission_access_configuration, 'new_entry_id')

    def new_entry_id(self, identifier_id):
        """!TXT! Generate a new Entry id, suitable for the specified Storage."""

        identifier = self.get_identifier(identifier_id)
        return identifier.new_entry_id()

    security.declareProtected(permission_access_configuration, 'new_entry_id_for_storage')

    def new_entry_id_for_storage(self, storage_id):
        """!TXT! Generate a new Entry id, suitable for the specified Storage."""

        identifier = self.get_storage(storage_id).get_identifier(identifier_id)
        return identifier.new_entry_id()

# ------------------------------------------------------------------------------
# Class Security

InitializeClass(Identifiers)

# !!! identifiers.py - implement additional identifiers api (reset)
# !!! identifiers.py - allow identifiers to be seperate from storage (metapublisher2identifiers folder? or in storages folder)
