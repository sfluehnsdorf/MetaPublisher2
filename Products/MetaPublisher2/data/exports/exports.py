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

__doc__ = """Exports Component

Export service for Entries into various types of files either for the filesystem
or download. Users can choose the Storage and match the Fields in the Storage to
data slots in the file.

$Id: data/exports/exports.py 2 2012-08-09 19:48:00Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.library import ClassSecurityInfo, DTMLFile, InitializeClass, permission_export_entries, show_future


# ============================================================================
# Module Exports

__all__ = [
    'Exports',
]


# ============================================================================
# Exports Mix-In Class

class Exports:
    """Exports Mix-In Class"""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # Exports ZMI

    if show_future:

        security.declareProtected(permission_export_entries, 'exports_form')

        exports_form = DTMLFile('exports', globals())

# ----------------------------------------------------------------------------
# Class Security

InitializeClass(Exports)

# TODO: Exports Component
