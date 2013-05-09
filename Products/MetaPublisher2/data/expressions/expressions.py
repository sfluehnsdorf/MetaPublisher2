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

__doc__ = """Expressions Component

!TXT! module info

$Id: data/expressions/expressions.py 3 2013-05-08 19:31:45Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.library import ClassSecurityInfo, InitializeClass

from aggregates import Aggregates
from conditions import Conditions
from constants import Constants
from functions import Functions
from groupers import Groupers
from sorters import Sorters


# ============================================================================
# Module Exports

__all__ = [
    'Expressions',
]


# ============================================================================
# Expressions Component Mix-In Class

class Expressions(Aggregates, Conditions, Constants, Functions, Groupers, Sorters):
    """!TXT! Expressions Component Mix-In Class"""

    security = ClassSecurityInfo()

# ----------------------------------------------------------------------------
# Class Security

InitializeClass(Expressions)

# TODO expressions.py - implement
