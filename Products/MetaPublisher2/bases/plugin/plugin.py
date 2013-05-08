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

__doc__ = """Plugin Base

The Plugin base class defines basic identity attributes and a generic API for
describing the Plugin's specififc capabilities, called the plugin details. All
plugin types for the MetaPublisher2 must be based on this class.

$Id: bases/plugin/plugin.py 14 2013-05-08 19:47:13Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from zope.interface import implements

from Products.MetaPublisher2.interfaces import IPluginBase
from Products.MetaPublisher2.library.common import ClassSecurityInfo, InitializeClass, PropertyManager, false


# ==============================================================================
# Module Exports

__all__ = [
    'PluginBase',
]


# ============================================================================
# Plugin Base Class

class PluginBase(PropertyManager):
    """!TXT! Plugin Base Class"""

    security = ClassSecurityInfo()

    implements(IPluginBase)

    # ------------------------------------------------------------------------
    # Plugin ZMI Attributes

    # Default plugin icon, which should never be seen as the specialised
    # plugin base classes provide their own default icons.

    icon = 'misc_/MetaPublisher2/Plugin.gif'

    # The meta type is unique to each plugin and therefore must be
    # overwritten.

    meta_type = 'MetaPublisher2 Plugin'

    # The specified Properties provide read-only access to the plugin
    # information and flags attributes.

    _properties = PropertyManager._properties + (
        {'id': 'plugin_type', 'type': 'string', 'mode': ''},
        {'id': 'plugin_name', 'type': 'string', 'mode': ''},
        {'id': 'plugin_info', 'type': 'string', 'mode': ''},
        {'id': 'plugin_version', 'type': 'string', 'mode': ''},
        {'id': 'plugin_vendor', 'type': 'string', 'mode': ''},
        {'id': 'plugin_author', 'type': 'string', 'mode': ''},
        {'id': 'plugin_homepage', 'type': 'string', 'mode': ''},
        {'id': 'plugin_flags', 'type': 'lines', 'mode': ''},
    )

    # ------------------------------------------------------------------------
    # Plugin Description

    # !TXT!

    plugin_type = ''

    # The plugin name is a short identifier of about 20 characters or less.

    plugin_name = 'Unnamed Plugin'

    # The plugin info should describe the plugin's functionality and capability
    # and may be as long as needed.

    plugin_info = 'No description available.'

    # The version, vendor, author and homepage attributes provide information
    # about the plugin and have no predefined format. These should be empty
    # strings if left undefined.

    plugin_version = ''
    plugin_vendor = ''
    plugin_author = ''
    plugin_homepage = ''

    # ------------------------------------------------------------------------
    # Plugin Flags

    # The list of active plugin flags

    plugin_flags = []

    # ------------------------------------------------------------------------
    # Plugin Flag Retrieval

    def get_immutable_pluginflag_ids(self):
        """!TXT! Return list of Plugin flag ids, which are either constants or set by an external source and may not be altered by MetaPublisher2 or its users"""

        raise NotImplementedError

    def get_immutable_pluginflags(self):
        """!TXT! Return tuples of id, boolean states of all immutable plugin flags"""

        result = []
        result_append = result.append
        pluginflag_ids = self.plugin_flags
        for pluginflag_id in self.get_immutable_pluginflag_ids():
            if pluginflag_id in pluginflag_ids:
                result_append(pluginflag_id)
        return result

    def get_mutable_pluginflag_ids(self):
        """!TXT! Return list of Plugin flag ids, which may be altered by MetaPublisher2 and its users"""

        raise NotImplementedError

    def get_mutable_pluginflags(self):
        """!TXT! Return tuples of id, boolean states of all mutable plugin flags"""

        result = []
        result_append = result.append
        pluginflag_ids = self.plugin_flags
        for pluginflag_id in self.get_mutable_pluginflag_ids():
            if pluginflag_id in pluginflag_ids:
                result_append(pluginflag_id)
        return result

    def get_pluginflag(self, pluginflag_id, failsafe=false):
        """!TXT! Return the boolean state of the specified Plugin flag if it exists, raises KeyError otherwise"""

        if pluginflag_id in self.get_pluginflag_ids():
            return pluginflag_id in self.plugin_flags
        elif failsafe:
            return false
        else:
            raise KeyError(detail_id)

    def get_pluginflags(self):
        """!TXT! Return tuples of id, boolean states of all Plugin flags"""

        return map(lambda id: (id, get_pluginflag(id)), self.get_pluginflag_ids())

    def get_pluginflag_ids(self):
        """!TXT! Return the ids of all Plugin flags"""

        return self.get_immutable_pluginflag_ids() + self.get_mutable_pluginflag_ids()

    def has_pluginflag(self, pluginflag_id):
        """!TXT! Return True if the Plugin flag exists, False otherwise"""

        return pluginflag_id in self.get_pluginflag_ids()

    # ------------------------------------------------------------------------
    # Plugin Flag Mutation

    def define_pluginflags(self, pluginflag_ids=[]):
        """!TXT! Replaces all mutable Plugin flags with the specified flags, raises ImmutableError if the Plugin detail is not mutable or raises KeyError if the Plugin detail is undefined"""

        immutable_pluginflags = self.get_immutable_pluginflag_ids()
        mutable_pluginflags = self.get_mutable_pluginflag_ids()
        result = immutable_pluginflags

        for pluginflag_id in pluginflag_ids:
            if pluginflag_id in mutable_pluginflags:
                result.append(pluginflag_id)
            elif pluginflag_id in immutable_pluginflag:
                raise ImmutableError(pluginflag_id)
            else:
                raise KeyError(pluginflag_id)

        result.sort()
        self.plugin_flags = result

    def set_pluginflag(self, pluginflag_id):
        """!TXT! Set the specified Plugin flag if it is mutable, raises ImmutableError if the Plugin flag is not mutable or raises KeyError if the Plugin flag is not undefined"""

        if pluginflag_id in self.get_immutable_pluginflags():
            raise ImmutableError(pluginflag_id)

        if pluginflag_id in self.get_mutable_pluginflags():
            result = self.plugin_flags
            if not pluginflag_id in result:
                result.append(pluginflag_id)
                result.sort()
                self.plugin_flags = result
        elif pluginflag_id in self.get_immutable_pluginflags():
            raise ImmutableError(pluginflag_id)
        else:
            raise KeyError(pluginflag_id)

    def set_pluginflags(self, pluginflag_ids):
        """!TXT! Set the specified mutable Plugin flags, raises ImmutableError if a Plugin flag is not mutable or raises KeyError if a Plugin flag is not undefined"""

        immutable_pluginflags = self.get_immutable_pluginflags()
        mutable_pluginflags = self.get_mutable_pluginflags()
        result = self.plugin_flags

        for pluginflag_id in pluginflag_ids:
            if pluginflag_id in mutable_pluginflags:
                if not pluginflag_id in result:
                    result.append(pluginflag_id)
            elif pluginflag_id in immutable_pluginflags:
                raise ImmutableError(pluginflag_id)
            else:
                raise KeyError(pluginflag_id)

        result.sort()
        self.plugin_flags = result

    def unset_pluginflag(self, pluginflag_id):
        """!TXT! Set the specified Plugin flag if it is mutable, raises ImmutableError if the Plugin flag is not mutable or raises KeyError if the Plugin flag is not undefined"""

        if pluginflag_id in self.get_immutable_pluginflags():
            raise ImmutableError(pluginflag_id)

        if pluginflag_id in self.get_mutable_pluginflags():
            result = self.plugin_flags
            if pluginflag_id in result:
                result.remove(pluginflag_id)
                result.sort()
                self.plugin_flags = result
        elif pluginflag_id in self.get_immutable_pluginflags():
            raise ImmutableError(pluginflag_id)
        else:
            raise KeyError(pluginflag_id)

    def unset_pluginflags(self, pluginflag_ids):
        """!TXT! Unset the specified mutable Plugin flags, raises ImmutableError if a Plugin flag is not mutable or raises KeyError if a Plugin flag is not undefined"""

        immutable_pluginflags = self.get_immutable_pluginflags()
        mutable_pluginflags = self.get_mutable_pluginflags()
        result = self.plugin_flags

        for pluginflag_id in pluginflag_ids:
            if pluginflag_id in mutable_pluginflags:
                if pluginflag_id in result:
                    result.remove(pluginflag_id)
            elif pluginflag_id in immutable_pluginflags:
                raise ImmutableError(pluginflag_id)
            else:
                raise KeyError(pluginflag_id)

        result.sort()
        self.plugin_flags = result

    # ------------------------------------------------------------------------
    # Plugin Specification API

    def get_plugin_specification(self):
        """!TXT! Return a dictionary describing this Plugin"""

        result = {
            'plugin_type': self.plugin_type,
            'plugin_name': self.plugin_name,
            'plugin_info': self.plugin_info,
            'plugin_version': self.plugin_version,
            'plugin_vendor': self.plugin_vendor,
            'plugin_author': self.plugin_author,
            'plugin_homepage': self.plugin_homepage,
            'plugin_flags': self.plugin_flags,
        }

        get_pluginflag = self.get_pluginflag
        for pluginflag_id in self.get_pluginflag_ids():
            result[pluginflag_id] = get_pluginflag(pluginflag_id)

        return result

    def get_plugin_infos(self):
        """!TXT! Return a string describing the Plugin's configuration"""

        items = self.get_plugin_specification()
        items.sort()
        return ', '.join(map(lambda item: '%s: %s' % item, items))

    # ------------------------------------------------------------------------
    # Plugin Identity API

    def get_plugin_instance(self):
        """!TXT! Return this instance"""

        return self

    def get_plugin_id(self):
        """!TXT! Return this instance's id"""

        return self.getId()

    def get_plugin_url(self):
        """!TXT! Return this instance's absolute url"""

        return self.absolute_url()

# ------------------------------------------------------------------------------
# initialize class security

InitializeClass(PluginBase)
