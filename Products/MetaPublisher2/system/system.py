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

__doc__ = """System Section

!TXT! module info
Module providing a mix-in class for the MetaPublisher 2's System section.

$Id: system/system.py 10 2013-05-05 18:00:47Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.library import ClassSecurityInfo, InitializeClass

from events import Events
from integrity import Integrity
from plugins import Plugins
from presets import Presets
from profiles import Profiles
from settings import Settings
from tools import Tools


# ============================================================================
# Module Exports

__all__ = [
    'System',
]


# ============================================================================
# System Section Mix-In Class

class System(Tools, Integrity, Presets, Events, Profiles, Settings, Plugins):
    """System Section Mix-In Class"""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # System ZMI Management Tabs

    manage_options = (
        {'label': 'Integrity', 'action': 'integrity_form'},
        {'label': 'Tools', 'action': 'tools_form'},
        {'label': 'Presets', 'action': 'presets_form'},
        {'label': 'Events', 'action': 'events_form'},
        {'label': 'Profiles', 'action': 'profiles_form'},
        {'label': 'Settings', 'action': 'settings_form'},
        {'label': 'Plugins', 'action': 'plugins_form'},
    )

# ----------------------------------------------------------------------------
# Class Security

InitializeClass(System)
