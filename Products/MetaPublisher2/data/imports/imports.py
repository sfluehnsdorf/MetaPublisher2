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

__doc__ = """Imports Component

Import service for Entries from various types of files either in the filesystem
or uploaded. Users can choose the destination Storage and match the data in the
file to the Fields in the Storage.

$Id: data/imports/imports.py 3 2012-08-09 19:48:00Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.library import ClassSecurityInfo, DTMLFile, InitializeClass, permission_import_entries, show_future


# ============================================================================
# Module Exports

__all__ = [
    'Imports',
]


# ============================================================================
# Imports Mix-In Class

class Imports:
    """Imports Mix-In Class"""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # Imports ZMI

    if show_future:

        security.declareProtected(permission_import_entries, 'imports_form')

        imports_form = DTMLFile('imports', globals())

    # ------------------------------------------------------------------------
    # Imports API

    security.declareProtected(permission_import_entries, 'import_entries')

    def import_entries(self, file, storage_id, field_map={}, REQUEST=None):
        """Import entries from the specified local file into the specified Storage, mapping the data to the Storage's Field according the specified field map."""

        raise NotImplemented

    security.declareProtected(permission_import_entries, 'upload_entries')

    def upload_entries(self, file, storage_id, field_map={}, REQUEST=None):
        """Upload a data file for entry import to a local file."""

        raise NotImplemented

    def _inspect_entry_import(self, filename):
        """Inspect a data file for importing, returning the file format and available data for mapping it to a Storage's Fields."""

        raise NotImplemented

# ----------------------------------------------------------------------------
# Class Security

InitializeClass(Imports)

# TODO: Imports Component
