# -*- coding: iso-8859-15 -*-
# ==============================================================================
#
#                         M e t a  P u b l i s h e r  2
#
# ------------------------------------------------------------------------------
# Copyright (c) 2002-2011, Sebastian L�hnsdorf - Web-Solutions and contributors
# For more information see the README.txt file or visit www.metapulisher.org
# ------------------------------------------------------------------------------
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
# ==============================================================================

__doc__ = """Triggers Component

$Id: configuration/triggers/triggers.py 1 2012-08-09 19:48:00Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ==============================================================================
# Module Imports

from Products.MetaPublisher2.library import ClassSecurityInfo, DTMLFile, InitializeClass, permission_access_configuration, show_future


# ============================================================================
# Module Exports

__all__ = [
    'Triggers',
]


# ==============================================================================
# Triggers Mix-In Class

class Triggers:
    """Triggers Mix-In Class"""

    security = ClassSecurityInfo()

    # --------------------------------------------------------------------------
    # Trigger ZMI

    if show_future:

        security.declareProtected(permission_access_configuration, 'triggers_form')

        triggers_form = DTMLFile('triggers', globals())

# ------------------------------------------------------------------------------
# Class Security

InitializeClass(Triggers)

# TODO: Triggers Component
