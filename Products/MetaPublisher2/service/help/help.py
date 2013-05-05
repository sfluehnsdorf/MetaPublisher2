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

__doc__ = """Help Component

The online help service provides access to contextual documentation of the
MetaPublisher2. As Zope's built-in contextual help system is not always fully
supported beginning with release Zope 2.12, this is a useful alternative
interface to access these help pages.

NOTE: Future releases of MetaPublisher2 will provide a replacement for Zope's
HelpSys module to reintegrate the contextual help into the ZMI, introducing
new features such as structured help pages and automatic API reference
generation.

$Id: service/help/help.py 2 2013-05-05 18:01:12Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.library import ClassSecurityInfo, DTMLFile,\
    InitializeClass, permission_zmi, show_future


# ============================================================================
# Module Exports

__all__ = [
    'Help',
]


# ============================================================================
# Help Mix-In Class

class Help:
    """Help Mix-In Class"""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # Help ZMI

    if show_future:

        security.declareProtected(permission_zmi, 'help_form')

        help_form = DTMLFile('help', globals())

        security.declareProtected(permission_zmi, 'help_main_form')

        help_main_form = DTMLFile('help_main', globals())

        security.declareProtected(permission_zmi, 'help_top_form')

        help_top_form = DTMLFile('help_top', globals(), target='_parent')

# ----------------------------------------------------------------------------
# Class Security

InitializeClass(Help)

# TODO: help.py - implement help browser
