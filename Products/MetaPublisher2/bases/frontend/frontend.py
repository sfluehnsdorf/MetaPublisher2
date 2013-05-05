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

__doc__ = """Frontend Base

!TXT! module info

$Id: bases/frontend/frontend.py 4 2013-05-05 18:01:53Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.bases.plugin import PluginBase
from Products.MetaPublisher2.interfaces import IFrontendPluginBase
from Products.MetaPublisher2.library.application import permission_manage_frontends
from Products.MetaPublisher2.library.common import ClassSecurityInfo, DTMLFile, implements, InitializeClass, OrderedFolder


# ============================================================================
# Module Exports

__all__ = [
    'FrontendPluginBase',
]


# ============================================================================
# Frontend Plugin Base

class FrontendPluginBase(PluginBase, OrderedFolder):
    """Frontend Plugin Base"""

    security = ClassSecurityInfo()

    implements(IFrontendPluginBase)

    # ------------------------------------------------------------------------
    # Frontend Attributes

    icon = 'misc_/MetaPublisher2/frontend.png'

    # !!! bases/frontend/frontend.py - _properties
    _properties = PluginBase._properties + (
        {'id': 'frontend_type', 'type': 'string', 'mode': ''},
    )

    # ------------------------------------------------------------------------
    # Frontend Plugin Description

    plugin_type = 'Frontend'

    frontend_type = None

    # ------------------------------------------------------------------------
    # Frontend Specification

    security.declareProtected(permission_manage_frontends, 'get_plugin_specification')

    def get_plugin_specification(self):
        """Return a dictionary describing this Frontend"""

        options = PluginBase.get_plugin_specification(self)
        options.update({
            'frontend_type': self.frontend_type,
        })
        return options

    # ------------------------------------------------------------------------
    # Frontend Identity API

    security.declareProtected(permission_manage_frontends, 'get_frontend_instance')

    get_frontend_instance = PluginBase.get_plugin_instance

    security.declareProtected(permission_manage_frontends, 'get_frontend_id')

    get_frontend_id = PluginBase.get_plugin_id

    security.declareProtected(permission_manage_frontends, 'get_frontend_url')

    get_frontend_url = PluginBase.get_plugin_url

    # ------------------------------------------------------------------------
    # Frontend ZMI

    security.declareProtected(permission_manage_frontends, 'add_frontend_formlet')

    add_frontend_formlet = DTMLFile('frontendplugin_add', globals())

    security.declareProtected(permission_manage_frontends, 'edit_frontend_formlet')

    edit_frontend_formlet = DTMLFile('frontendplugin_edit', globals())

    # ------------------------------------------------------------------------
    # !TXT!

    # !!! bases/frontend/frontend.py - check api requirements for get_rendering_ids, render_frontend, is_renderable, needs_rendering, get_last_rendering_datetime

    # ------------------------------------------------------------------------
    # !TXT!

    # !!! bases/frontend/frontend.py - check api requirements for add_widget_form, add_widget_formlet, add_widget, edit_widget_form, edit_widget_formlet, edit_widget, get_widget, delete_widget, delete_widgets, widget_ids, widget_items, widget_values, move_widget

# ----------------------------------------------------------------------------
# initialize class security

InitializeClass(FrontendPluginBase)

# !!! bases/frontend/frontend.py - changed flag (reset on rendering)
# !!! bases/frontend/frontend.py - flags: addable, editable, deletable, renderable, searchable, binary, unique
# !!! bases/frontend/frontend.py - create widget_frontend.py
# !!! bases/frontend/frontend.py - create designable_frontend.py
