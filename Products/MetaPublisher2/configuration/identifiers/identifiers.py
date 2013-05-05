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

$Id: configuration/identifiers/identifiers.py 4 2013-05-05 18:01:53Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ==============================================================================
# Module Imports

from Products.MetaPublisher2.library import ClassSecurityInfo, DTMLFile, InitializeClass, permission_access_configuration, show_future


# ============================================================================
# Module Exports

__all__ = [
    'Identifiers',
]


# ==============================================================================
# Identifiers Mix-In Class

class Identifiers:
    """Identifiers Mix-In Class"""

    security = ClassSecurityInfo()

    # --------------------------------------------------------------------------
    # Identifiers ZMI

    if show_future:

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

    # --------------------------------------------------------------------------
    # Identifiers Retrieval API

    security.declareProtected(permission_access_configuration, 'last_entry_id')

    def last_entry_id(self, storage_id):
        """Returns the last generated Entry id."""

        storage = self.get_storage(storage_id)
        return storage.last_entry_id()

    # --------------------------------------------------------------------------
    # Identifiers Mutation API

    security.declareProtected(permission_access_configuration, 'new_entry_id')

    def new_entry_id(self, storage_id):
        """Generate a new Entry id, suitable for the specified Storage."""

        storage = self.get_storage(storage_id)
        return storage.new_entry_id()

# ------------------------------------------------------------------------------
# Class Security

InitializeClass(Identifiers)

# !!! identifiers.py - implement additional identifiers api (reset)
# !!! identifiers.py - allow identifiers to be seperate from storage (metapublisher2identifiers folder? or in storages folder)
