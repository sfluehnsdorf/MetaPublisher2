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

__doc__ = """Future Compatibility

!TXT! module info

$Id: library/compatibility/future.py 4 2013-05-07 17:50:03Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.library.common import ClassSecurityInfo, false, InitializeClass, true


# ============================================================================
# Module Exports

__all__ = [
    'Future',
    'show_future',
]


# ============================================================================
# Development Flag

# If the following flag is "true", planned but hidden features will be
# revealed. This may enable unreleased functionalities but more likely will
# only clutter the management interface with empty and inactive forms.

#show_future = false
show_future = true


# ============================================================================
# Future Mix-In Class

class Future:
    """Future Mix-In Class"""

    security = ClassSecurityInfo()

# ----------------------------------------------------------------------------
# Class Security

InitializeClass(Future)
