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

__doc__ = """Widget Plugin Base

!TXT! module info

$Id: bases/widget/widget.py 9 2013-05-10 23:39:52Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.bases.plugin import PluginBase
from Products.MetaPublisher2.interfaces import IWidgetPluginBase
from Products.MetaPublisher2.library.application import permission_manage_frontends
from Products.MetaPublisher2.library.common import ClassSecurityInfo, DTMLFile, implements, InitializeClass, OrderedFolder


# ============================================================================
# Module Exports

__all__ = [
    'WidgetPluginBase',
]


# ============================================================================
# Widget Plugin Base Class

class WidgetPluginBase(PluginBase, OrderedFolder):
    """!TXT! Widget Plugin Base Class"""

    security = ClassSecurityInfo()

    implements(IWidgetPluginBase)

    # ------------------------------------------------------------------------
    # Widget Attributes

    icon = 'misc_/MetaPublisher2/widget.png'

    _properties = PluginBase._properties + (
        {'id': 'widget_type', 'type': 'string', 'mode': ''},
        {'id': 'field_types', 'type': 'lines', 'mode': ''},
        {'id': 'frontend_types', 'type': 'lines', 'mode': ''},
        {'id': 'frontend_type', 'type': 'string', 'mode': ''},
    )

    # ------------------------------------------------------------------------
    # Widget Plugin Description

    plugin_type = 'Widget'

    widget_type = None

    field_types = []

    frontend_types = []

    frontend_type = ''

    # ------------------------------------------------------------------------
    # Widget Specification

    security.declareProtected(permission_manage_frontends, 'get_plugin_specification')

    def get_plugin_specification(self):
        """!TXT! Return a dictionary describing this Widget"""

        options = PluginBase.get_plugin_specification(self)
        options.update({
            'widget_type': self.widget_type,
            'field_types': self.field_types,
            'frontend_type': self.frontend_type,
            'frontend_types': self.frontend_types,
        })
        return options

    # ------------------------------------------------------------------------
    # Widget Identity API

    security.declareProtected(permission_manage_frontends, 'get_widget_instance')

    get_widget_instance = PluginBase.get_plugin_instance

    security.declareProtected(permission_manage_frontends, 'get_widget_id')

    get_widget_id = PluginBase.get_plugin_id

    security.declareProtected(permission_manage_frontends, 'get_widget_url')

    get_widget_url = PluginBase.get_plugin_url

    # ------------------------------------------------------------------------
    # Widget ZMI

    security.declareProtected(permission_manage_frontends, 'add_widget_formlet')

    add_widget_formlet = DTMLFile('widgetplugin_add', globals())

    security.declareProtected(permission_manage_frontends, 'edit_widget_formlet')

    edit_widget_formlet = DTMLFile('widgetplugin_edit', globals())

    # ------------------------------------------------------------------------
    # Widget API

    security.declareProtected(permission_manage_frontends, 'render_widget')

    def render_widget(self, frontend_type_id):
        """!TXT!"""

        raise NotImplementedError

# ----------------------------------------------------------------------------
# initialize class security

InitializeClass(WidgetPluginBase)

# TODO bases/widget/widget.py - define api, including before_ and after_ handlers
# TODO bases/widget/widget.py - define zmi (with developer notes regarding choice of form and formlet)
# TODO bases/widget/widget.py - define frontend type and field type bindings
# TODO bases/widget/widget.py - predefine css and style support
# TODO bases/widget/widget.py - predefine rendering api and modes
