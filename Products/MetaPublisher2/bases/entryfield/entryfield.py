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

__doc__ = """Entry Field Base

!TXT! module info

$Id: bases/entryfield/entryfield.py 3 2013-05-08 19:53:25Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.interfaces import IEntryField
from Products.MetaPublisher2.library.common import ClassSecurityInfo, implements, InitializeClass, true, false


# ============================================================================
# Module Exports

__all__ = [
    'EntryField',
]


# ============================================================================
# Entry Field Base Class

class EntryField:
    """!TXT! Entry Field Base Class"""

    security = ClassSecurityInfo()

    implements(IEntryField)

# ----------------------------------------------------------------------------
# initialize class security

InitializeClass(EntryField)

# !!! bases/entryfield/entryfield.py - define api
# !!! bases/entryfield/entryfield.py - implement backdrop/failsafe code
