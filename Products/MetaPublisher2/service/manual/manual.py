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

__doc__ = """Manual Component

Simple service providing access to the Web based manual for both end users and
developers. The ZMI forms simply include the manual's web pages on the
MetaPublisher website at http://metapublisher.org.

$Id: service/manual/manual.py 2 2012-02-17 15:45:00Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.library import ClassSecurityInfo, DTMLFile,\
    InitializeClass, permission_zmi


# ============================================================================
# Module Exports

__all__ = [
    'Manual',
]


# ============================================================================
# Manual Mix-In Class

class Manual:
    """Manual Mix-In Class"""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # Manual ZMI

    security.declareProtected(permission_zmi, 'manual_form')

    manual_form = DTMLFile('manual', globals())

    security.declareProtected(permission_zmi, 'manual_top_form')

    manual_top_form = DTMLFile('manual_top', globals(), target='_parent')

    # ------------------------------------------------------------------------
    # Manual Retrieval API

    security.declareProtected(permission_zmi, 'get_manual_url')

    def get_manual_url(self):
        """Return the URL for the online manual service"""

        return self.get_setting('service_manual_url')

# ----------------------------------------------------------------------------
# initialize class security

InitializeClass(Manual)

# !!! manual.py - implement online manual service
