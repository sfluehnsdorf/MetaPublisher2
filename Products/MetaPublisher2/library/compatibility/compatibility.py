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

__doc__ = """Compatibility Mix-In

To ensure to continued operation of deprecated resources, this module provides
wrappers and handlers for these outdated resources. It also provides an API for
logging calls to deprecated resources.

$Id: library/compatibility/historical.py 6 2013-05-05 18:03:21Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.library.common import ClassSecurityInfo, InitializeClass

import historical
from deprecation import *
from future import *
from historical import *


# ============================================================================
# Module Exports

__all__ = [
    'Compatibility',
    'show_future',
]


# ============================================================================
# Compatibility Mix-In Class

class Compatibility(Future, Historical):
    """Compatibility Mix-In Class"""

    security = ClassSecurityInfo()

# ----------------------------------------------------------------------------
# Class Security

InitializeClass(Compatibility)
