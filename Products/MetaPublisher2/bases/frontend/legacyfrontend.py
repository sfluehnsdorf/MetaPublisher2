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

__doc__ = """Legacy Frontend Base

!TXT! module info

$Id: bases/frontend/legacyfrontend.py 2 2013-05-05 18:01:54Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.bases.plugin.legacyplugin import LegacyPluginBase
from Products.MetaPublisher2.library.common import ClassSecurityInfo, DTMLFile, InitializeClass

from frontend import FrontendPluginBase


# ============================================================================
# Module Exports

__all__ = [
    'LegacyFrontendPlugin',
]


# ============================================================================
# Legacy Frontend Plugin Base

class LegacyFrontendPlugin(LegacyPluginBase, FrontendPluginBase):
    """Legacy Frontend Plugin Base"""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # !TXT!

    isZMP2InterfacePlugin = 1

    icon = 'misc_/MetaPublisher2/Interface.gif'

    # ------------------------------------------------------------------------
    # !TXT!

    getInterfaceObject = FrontendPluginBase.get_plugin_instance

    getInterfaceId = FrontendPluginBase.get_plugin_id

    getInterfaceURL = FrontendPluginBase.get_plugin_url

    # ------------------------------------------------------------------------
    # !TXT!

    def get_immutable_pluginflag_ids(self):
        """Return list of Plugin flag ids, which are either constants or set by an external source and may not be altered by MetaPublisher2 or its users"""

        # !!! bases/frontend/legacyfrontend.py -  get_immutable_pluginflag_ids
        return []

    def get_mutable_pluginflag_ids(self):
        """Return list of Plugin flag ids, which may be altered by MetaPublisher2 and its users"""

        # !!! bases/frontend/legacyfrontend.py -  get_immutable_pluginflag_ids
        return []

    # ------------------------------------------------------------------------
    # !TXT!

    def all_meta_types(self, interfaces=None):

        result = FrontendPluginBase.all_meta_types(interfaces)
        for product in Products.meta_types:
            if product.get('visibility', None) == 'ZMP2WidgetPlugin' and not(product in result):
                result.append(product)
        return result

    # ------------------------------------------------------------------------
    # !TXT!

    def renderingIds(self):
        """Return list ids for objects created on rendering"""

        raise NotImplementedError

    def rendering_ids(self):
        """Return list ids for objects created on rendering"""

        self.renderingIds()

    # ------------------------------------------------------------------------
    # !TXT!

    def renderInterface(self, destination, **options):
        """Render the Interface"""

        raise NotImplementedError

# ----------------------------------------------------------------------------
# initialize class security

InitializeClass(LegacyFrontendPlugin)

# !!! bases/frontend/legacyfrontend.py - revise and update legacy api
