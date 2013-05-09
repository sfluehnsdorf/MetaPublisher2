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

__doc__ = """Plugin Base Interface

!TXT! module info

$Id: interfaces/plugin.py 7 2013-05-08 23:34:00Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from zope.interface import Interface
from zope.schema import BytesLine, List, Text, TextLine, Tuple, URI


# ============================================================================
# Module Exports

__all__ = [
    'IPluginBase',
]


# ============================================================================
# Plugin Base Interface

class IPluginBase(Interface):
    """!TXT! Plugin base interface

    This interface provides a common base class for all MetaPublisher2 Plugins.
    """

    # ------------------------------------------------------------------------
    # Plugin Identity

    icon = BytesLine(
        title=u"Icon",
        description=u"!TXT! Name of icon, relative to SOFTWARE_URL",
    )

    meta_type = BytesLine(
        title=u"Meta type",
        description=u"!TXT! The object's Zope2 meta type",
    )

    # ------------------------------------------------------------------------
    # Plugin Description

    plugin_type = BytesLine(
        title=u"Plugin Type",
        description=u"!TXT! Plugin type realised with this PluginBase.",
    )

    plugin_name = TextLine(
        title=u"Plugin Name",
        description=u"!TXT! Name of the Plugin realised with this PluginBase.",
    )

    plugin_info = Text(
        title=u"Plugin Info",
        description=u"!TXT! Description of the Plugin realised with this PluginBase.",
    )

    plugin_version = TextLine(
        title=u"Plugin Version",
        description=u"!TXT! Version of the Plugin realised with this PluginBase.",
    )

    plugin_vendor = TextLine(
        title=u"Plugin Vendor",
        description=u"!TXT! Vendor of the Plugin realised with this PluginBase.",
    )

    plugin_author = TextLine(
        title=u"Plugin Author",
        description=u"!TXT! Author of the Plugin realised with this PluginBase.",
    )

    plugin_homepage = URI(
        title=u"Plugin URL",
        description=u"!TXT! URL of the homepage of the Plugin realised with this PluginBase",
    )

    plugin_flags = List(
        title=u"!TXT! List of active plugin flags",
    )

    _properties = Tuple(
        title=u"!TXT! Properties",
    )

    # ------------------------------------------------------------------------
    # Plugin Detail Retrieval

    def pluginflag_ids(self):
        """!TXT! Return the ids of all Plugin flags"""

    def pluginflag_items(self):
        """!TXT! Return tuples of id, boolean states of all Plugin flags"""

    def pluginflag_values(self):
        """!TXT! Return the boolean states of all Plugin flags"""

    def get_available_immutable_pluginflags(self):
        """!TXT! Return list of Plugin flag ids, which are either constants or set by an external source and may not be altered by MetaPublisher3 or its users"""

    def get_available_mutable_pluginflags(self):
        """!TXT! Return list of Plugin flag ids, which may be altered by MetaPublisher3 and its users"""

    def get_pluginflag(self, pluginflag_id, failsafe=None):
        """!TXT! Return the boolean state of the specified Plugin flag if it exists, raises KeyError otherwise"""

    def get_plugin_specification(self):
        """!TXT! Return a dictionary describing this Plugin"""

    def has_pluginflag(self, pluginflag_id):
        """!TXT! Return True if the Plugin flag exists, False otherwise"""

    # ------------------------------------------------------------------------
    # Plugin Detail Mutation

    def define_pluginflags(self, pluginflag_ids):
        """!TXT! Clear all mutable Plugin flags and set the specified Plugin flags, raises ImmutableError if the Plugin flag is not mutable or raises KeyError if the Plugin flag is not undefined"""

    def set_pluginflag(self, pluginflag_id):
        """!TXT! Set the specified Plugin flag if it is mutable, raises ImmutableError if the Plugin flag is not mutable or raises KeyError if the Plugin flag is not undefined"""

    def set_pluginflags(self, pluginflag_ids):
        """!TXT! Set the specified mutable Plugin flags, raises ImmutableError if a Plugin flag is not mutable or raises KeyError if a Plugin flag is not undefined"""

    def unset_pluginflag(self, pluginflag_id):
        """!TXT! Set the specified Plugin flag if it is mutable, raises ImmutableError if the Plugin flag is not mutable or raises KeyError if the Plugin flag is not undefined"""

    def unset_pluginflags(self, pluginflag_ids):
        """!TXT! Unset the specified mutable Plugin flags, raises ImmutableError if a Plugin flag is not mutable or raises KeyError if a Plugin flag is not undefined"""

# !!! interfaces/plugin.py - review api
