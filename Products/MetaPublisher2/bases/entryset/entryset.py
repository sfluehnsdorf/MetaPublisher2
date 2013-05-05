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

__doc__ = """EntrySet Base

$Id: bases/entryset/entryset.py 1 2012-02-17 15:45:00Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.bases.entrycontainer import EntryContainer
from Products.MetaPublisher2.interfaces import IEntrySet
from Products.MetaPublisher2.library.common import ClassSecurityInfo, implements, InitializeClass, true, false


# ============================================================================
# Module Exports

__all__ = [
    'EntrySet',
]


# ============================================================================
# Entry Set Base

class EntrySet(EntryContainer):
    """Entry Set Base"""

    security = ClassSecurityInfo()

    implements(IEntrySet)

# ----------------------------------------------------------------------------
# initialize class security

InitializeClass(EntrySet)

# !!! bases/entryset/entryset.py - define api
# !!! bases/entryset/entryset.py - implement source/storage handling
# !!! bases/entryset/entryset.py - implement live linking
# !!! bases/entryset/entryset.py - implement query storage
