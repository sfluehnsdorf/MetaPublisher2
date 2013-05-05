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

__doc__ = """Legacy Widget Base

$Id: bases/widget/legacywidget.py 4 2012-02-17 15:45:00Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.bases.plugin.legacyplugin import LegacyPluginBase
from Products.MetaPublisher2.library.common import ClassSecurityInfo, ComputedAttribute, InitializeClass

from widget import WidgetPluginBase


# ============================================================================
# Module Exports

__all__ = [
    'LegacyWidgetPlugin',
]


# ============================================================================
# Legacy Widget Plugin Base

class LegacyWidgetPlugin(LegacyPluginBase, WidgetPluginBase):
    """Widget Plugin Base"""

    security = ClassSecurityInfo()

    # --------------------------------------------------------------------------
    # !TXT!

    isZMP2WidgetPlugin = 1

    icon = 'misc_/MetaPublisher2/Widget.gif'

    fieldTypeIds = []

    formTypeIds = []

    formTypeId = ''

    field_types = ComputedAttribute(lambda self: self.fieldTypeIds)

    frontend_types = ComputedAttribute(lambda self: self.formTypeIds)

    frontend_type = ComputedAttribute(lambda self: self.formTypeId)

    # ------------------------------------------------------------------------
    # Plugin Identity API

    getWidgetObject = WidgetPluginBase.get_plugin_instance

    getWidgetId = WidgetPluginBase.get_plugin_id

    getWidgetURL = WidgetPluginBase.get_plugin_url

    # ------------------------------------------------------------------------
    # !TXT!

    def get_immutable_pluginflag_ids(self):
        """Return list of Plugin flag ids, which are either constants or set by an external source and may not be altered by MetaPublisher2 or its users"""

        # !!! bases/widget/legacywidget.py -  get_immutable_pluginflag_ids
        return []

    def get_mutable_pluginflag_ids(self):
        """Return list of Plugin flag ids, which may be altered by MetaPublisher2 and its users"""

        # !!! bases/widget/legacywidget.py -  get_mutable_pluginflag_ids
        return []

    # ------------------------------------------------------------------------
    # !TXT!

    def setWidgetData(self, data={}):
        """Return a dictionary describing this widget"""

        raise NotImplementedError

    def getWidgetData(self, form_type_id):
        """Return a dictionary describing this widget"""

        raise NotImplementedError

# ------------------------------------------------------------------------------
# initialize class security

InitializeClass(LegacyWidgetPlugin)

# !!! bases/widget/legacywidget.py - revise and update legacy api
