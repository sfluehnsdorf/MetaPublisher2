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

__doc__ = """Data Section

!TXT! module info
Module providing a mix-in class for the MetaPublisher 2's Data section.

$Id: data/data.py 8 2012-08-09 19:48:00Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.library import ClassSecurityInfo, DTMLFile, InitializeClass

from entries import Entries
from exports import Exports
from expressions import Expressions
from imports import Imports
from queries import Queries
from reports import Reports
from search import Search
from transfers import Transfers


# ============================================================================
# Module Exports

__all__ = [
    'Data',
]


# ============================================================================
# Data Section Mix-In Class

class Data(Entries, Expressions, Reports, Search, Queries, Imports, Exports, Transfers):
    """Data Section Mix-In Class"""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # Data ZMI Management Tabs

    manage_options = (
        {'label': 'Entries', 'action': 'entries_form'},
        {'label': 'Reports', 'action': 'reports_form'},
        {'label': 'Search', 'action': 'search_form'},
        {'label': 'Queries', 'action': 'queries_form'},
        {'label': 'Imports', 'action': 'imports_form'},
        {'label': 'Exports', 'action': 'exports_form'},
        {'label': 'Transfers', 'action': 'transfers_form'},
    )

# ----------------------------------------------------------------------------
# Class Security

InitializeClass(Data)
