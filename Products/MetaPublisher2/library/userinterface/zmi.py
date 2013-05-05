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

__doc__ = """UserInterface ZMI

!TXT! module info

$Id: library/userinterface/zmi.py 2 2012-08-09 19:48:00Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.library.application import permission_zmi
from Products.MetaPublisher2.library.common import ClassSecurityInfo, DTMLFile, InitializeClass


# ============================================================================
# Module Exports

__all__ = [
    'ZMI',
]


# ============================================================================
# ZMI Mix-In Class

class ZMI:
    """ZMI Mix-In Class"""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # Custom ZMI

    security.declareProtected(permission_zmi, 'manage_MetaPublisher2_header')

    manage_MetaPublisher2_header = DTMLFile('zmi_header', globals())

    security.declareProtected(permission_zmi, 'manage_MetaPublisher2_footer')

    manage_MetaPublisher2_footer = DTMLFile('zmi_footer', globals())

    security.declareProtected(permission_zmi, 'manage_MetaPublisher2_css')

    manage_MetaPublisher2_css = DTMLFile('zmi_css', globals())

    security.declareProtected(permission_zmi, 'manage_MetaPublisher2_js')

    manage_MetaPublisher2_js = DTMLFile('zmi_js', globals())

# ----------------------------------------------------------------------------
# Class Security

InitializeClass(ZMI)