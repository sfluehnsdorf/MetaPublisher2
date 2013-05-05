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

__doc__ = """MetaPublisher2 UserInterface

!TXT! module info

$Id: library/userinterface/userinterface.py 4 2013-05-05 18:01:53Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.library.application import permission_zmi
from Products.MetaPublisher2.library.common import ClassSecurityInfo, false, InitializeClass, quote_plus

from dialog import Dialog
from formlet import Formlet
from zmi import ZMI
from resources import Resources


# ============================================================================
# Module Exports

__all__ = [
    'UserInterface',
]


# ============================================================================
# UserInterface Mix-In Class

class UserInterface(Formlet, Dialog, Resources, ZMI):
    """UserInterface Mix-In Class"""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # ZMI Redirect Helper

    def redirect(self, REQUEST, url, message='', update_menu=false, **kw):
        """!TXT! Redirect to the specified URL."""

        if REQUEST:
            if message:
                kw['manage_tabs_message'] = message
            if update_menu:
                kw['update_menu'] = 1
            REQUEST.RESPONSE.redirect('%s/%s%s' % (self.get_MetaPublisher2_url(), url, kw and ('?' + '&'.join(map(lambda item: '%s=%s' % (url_quote(item[0]), url_quote(item[1])), kw.items()))) or ''))

# ----------------------------------------------------------------------------
# Class Security

InitializeClass(UserInterface)

# !!! userinterface.py - add error widget for form error handling
