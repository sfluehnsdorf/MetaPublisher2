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

__doc__ = """Design Base

!TXT! module info

$Id: bases/design/design.py 2 2013-05-05 18:01:53Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.interfaces import IDesignPluginBase
from Products.MetaPublisher2.library.common import ClassSecurityInfo, implements, InitializeClass, true, false


# ============================================================================
# Module Exports

__all__ = [
    'DesignPluginBase',
]


# ============================================================================
# Design Plugin Base

class DesignPluginBase:
    """Design Plugin Base"""

    security = ClassSecurityInfo()

    implements(IDesignPluginBase)

# ----------------------------------------------------------------------------
# initialize class security

InitializeClass(DesignPluginBase)

# !!! bases/design/design.py - define api
# !!! bases/design/design.py - implement backdrop/failsafe code
