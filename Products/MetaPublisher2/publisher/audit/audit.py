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

__doc__ = """Audit Component

!TXT! module info

$Id: publisher/audit/audit.py 3 2013-05-08 19:03:47Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.library import ClassSecurityInfo, DTMLFile, InitializeClass, permission_manage_frontends, show_future


# ============================================================================
# Module Exports

__all__ = [
    'Audit',
]


# ============================================================================
# Audit Component Mix-In Class

class Audit:
    """!TXT! Audit Component Mix-In Class"""

    security = ClassSecurityInfo()

    # --------------------------------------------------------------------------
    # Audit ZMI Forms

    if show_future:

        security.declareProtected(permission_manage_frontends, 'audit_form')

        audit_form = DTMLFile('audit', globals())

# ------------------------------------------------------------------------------
# Class Audit

InitializeClass(Audit)

# TODO: Audit Component
#       The Audit displays a summary of Permission settings to help find security problems), security map, permissions, roles, ownership, ...
#       owners, permissions, proxies, roles, users
