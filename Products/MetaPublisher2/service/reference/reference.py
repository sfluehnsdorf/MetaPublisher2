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

__doc__ = """Reference Component

!TXT! module info

$Id: system/reference/reference.py 1 2012-08-09 19:48:00Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.library import ClassSecurityInfo, DTMLFile,\
    InitializeClass, permission_zmi, show_future


# ============================================================================
# Module Exports

__all__ = [
    'Reference',
]


# ============================================================================
# Reference Mix-In Class

class Reference:
    """Reference Mix-In Class"""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # Reference ZMI Forms

    if show_future:

        security.declareProtected(permission_zmi, 'reference_form')

        reference_form = DTMLFile('reference', globals())

# ----------------------------------------------------------------------------
# Class Security

InitializeClass(Reference)

# !!! reference.py - create placeholder forms
# !!! reference.py - implement online reference service
