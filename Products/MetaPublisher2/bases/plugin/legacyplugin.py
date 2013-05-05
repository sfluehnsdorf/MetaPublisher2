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

__doc__ = """Legacy Plugin Base

NOTE: This class is provided for backward compatibility and should not be of
interest to you!

It defines a plugin identifier and maps old style plugin detail attributes. It
must preceed the plugin type base class in inheritance order to function
properly.

$Id: bases/plugin/legacyplugin.py 7 2013-05-05 18:04:52Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.library.common import ClassSecurityInfo, ComputedAttribute, InitializeClass


# ==============================================================================
# Module Exports

__all__ = [
    'LegacyPluginBase',
]


# ============================================================================
# Legacy Plugin Identifiers

all_plugintypes = ['ZMP2StoragePlugin', 'ZMP2FieldPlugin', 'ZMP2InterfacePlugin', 'ZMP2WidgetPlugin']


# ============================================================================
# Legacy Plugin Base Class

class LegacyPluginBase:
    """Legacy Plugin Base Mix-In Class"""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # Legacy Plugin Identity Attributes

    isZMP2Plugin = 1

    # ------------------------------------------------------------------------
    # Legacy Plugin Information Attributes

    pluginName = 'Unknown Plugin Type'

    pluginAuthor = 'Unknown Author'

    pluginVersion = 'Unknown Version'

    pluginInfo = 'No description available.'

    # ------------------------------------------------------------------------
    # Plugin Information Attributes Remapping

    plugin_name = ComputedAttribute(lambda self: self.pluginName)

    plugin_author = ComputedAttribute(lambda self: self.pluginAuthor)

    plugin_version = ComputedAttribute(lambda self: self.pluginVersion)

    plugin_info = ComputedAttribute(lambda self: self.pluginInfo)

# ----------------------------------------------------------------------------
# initialize class security

InitializeClass(LegacyPluginBase)
