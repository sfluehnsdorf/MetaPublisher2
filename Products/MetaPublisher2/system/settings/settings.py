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

__doc__ = """Settings Component

!TXT! module info

$Id: system/settings/settings.py 3 2012-08-09 19:48:00Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.library import ClassSecurityInfo, DTMLFile, InitializeClass, permission_manage, settings


# ============================================================================
# Module Exports

__all__ = [
    'Settings',
]


# ============================================================================
# Settings Mix-In Class

class Settings:
    """Settings Mix-In Class"""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # Settings ZMI Forms

    security.declareProtected(permission_manage, 'settings_form')

    settings_form = DTMLFile('settings', globals())

    # ------------------------------------------------------------------------
    # Settings Retrieval

    security.declareProtected(permission_manage, 'list_settings')

    def list_settings(self):
        """!TXT! List all settings"""

        result = settings.items()
        result.sort()
        return settings.items()

    security.declareProtected(permission_manage, 'get_setting')

    def get_setting(self, key):
        """!TXT! Return the value for the specified setting"""

        return settings[key]

# ----------------------------------------------------------------------------
# Class Security

InitializeClass(Settings)
