# -*- coding: iso-8859-15 -*-
# ============================================================================
#
#                         M e t a  P u b l i s h e r  2
#
# ----------------------------------------------------------------------------
# Copyright (c) 2002-2013, Sebastian L�hnsdorf - Web-Solutions and others
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

__doc__ = """Identifier Plugin Interface

!TXT! module info

$Id: interfaces/identifier.py 4 2013-05-08 19:36:17Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from zope.interface import Interface


# ============================================================================
# Module Exports

__all__ = [
    'IIdentifierPluginBase',
]


# ============================================================================
# Identifier Plugin Base Interface

class IIdentifierPluginBase(Interface):
    """!TXT! Identifier Plugin Base Interface"""

    pass

# !!! interfaces/identifier.py - define api
