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

$Id: service/reference/reference.py 7 2013-05-09 00:07:55Z sfluehnsdorf $
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
# Reference Component Mix-In Class

class Reference:
    """!TXT! Reference Component Mix-In Class"""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # Reference ZMI Forms

    if show_future:

        security.declareProtected(permission_zmi, 'reference_form')

        reference_form = DTMLFile('reference', globals())

        security.declareProtected(permission_zmi, 'reference_top_form')

        reference_top_form = DTMLFile('reference_top', globals(), target='_parent')

    # ------------------------------------------------------------------------
    # Manual Retrieval API

    security.declareProtected(permission_zmi, 'get_reference_url')

    def get_reference_url(self):
        """!TXT! Return the URL for the online reference service"""

        return self.get_setting('service_reference_url')

# ----------------------------------------------------------------------------
# Class Security

InitializeClass(Reference)

# TODO reference.py - implement online reference service
