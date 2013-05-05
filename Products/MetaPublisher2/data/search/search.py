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

__doc__ = """Search Component

Keyword search for Entries in a Storage, allowing to define search conditions
with a variety of conditions, provided by Field plugins.

$Id: data/search/search.py 4 2013-05-05 18:03:58Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.library import ClassSecurityInfo, DTMLFile, InitializeClass, permission_access_entries, show_future


# ============================================================================
# Module Exports

__all__ = [
    'Search',
]


# ============================================================================
# Search Mix-In Class

class Search:
    """Search Mix-In Class"""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # Search ZMI

    if show_future:

        security.declareProtected(permission_access_entries, 'search_form')

        search_form = DTMLFile('search', globals())

# ----------------------------------------------------------------------------
# Class Security

InitializeClass(Search)

# TODO: Search Component
