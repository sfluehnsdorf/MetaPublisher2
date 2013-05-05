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

__doc__ = """Community Component

Simple service providing access to the Web based community service. The ZMI
forms simply include the community service's web pages on the MetaPublisher
website at http://metapublisher.org.

$Id: service/community/community.py 4 2013-05-05 18:01:23Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.library import ClassSecurityInfo, DTMLFile,\
    InitializeClass, permission_zmi


# ============================================================================
# Module Exports

__all__ = [
    'Community',
]


# ============================================================================
# Community Mix-In Class

class Community:
    """Community Mix-In Class"""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # Community ZMI

    security.declareProtected(permission_zmi, 'community_form')

    community_form = DTMLFile('community', globals())

    security.declareProtected(permission_zmi, 'community_top_form')

    community_top_form = DTMLFile('community_top', globals(), target='_parent')

    # ------------------------------------------------------------------------
    # Community Retrieval API

    security.declareProtected(permission_zmi, 'get_community_url')

    def get_community_url(self):
        """Return the URL for the online community service"""

        return self.get_setting('service_community_url')

# ----------------------------------------------------------------------------
# initialize class security

InitializeClass(Community)

# !!! community.py - implement online community service
