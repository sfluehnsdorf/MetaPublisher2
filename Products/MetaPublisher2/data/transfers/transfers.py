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

__doc__ = """Transfers Component

!TXT! module info

$Id: data/transfer/transfer.py 2 2013-05-05 18:01:53Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.library import ClassSecurityInfo, DTMLFile, InitializeClass, permission_access_entries, show_future


# ============================================================================
# Module Exports

__all__ = [
    'Transfers',
]


# ============================================================================
# Transfers Mix-In Class

class Transfers:
    """Transfer Mix-In Class"""

    security = ClassSecurityInfo()

    # -----------------------------------------------------------------------
    # !TXT!

    if show_future:

        security.declareProtected(permission_access_entries, 'transfers_form')

        transfers_form = DTMLFile('transfers', globals())

# ----------------------------------------------------------------------------
# Class Security

InitializeClass(Transfers)

# TODO: Transfers Component
