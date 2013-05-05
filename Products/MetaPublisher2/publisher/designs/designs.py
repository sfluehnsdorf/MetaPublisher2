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

__doc__ = """Designs Component

$Id: publisher/designs/designs.py 2 2012-08-09 19:48:00Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.interfaces import IDesignPluginBase
from Products.MetaPublisher2.library import ClassSecurityInfo, DTMLFile, InitializeClass, permission_manage, permission_manage_designs, show_future


# ============================================================================
# Module Exports

__all__ = [
    'Designs',
]


# ============================================================================
# Designs Mix-In Class

class Designs:
    """Designs Mix-In Class"""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # Designs ZMI Forms

    if show_future:

        security.declareProtected(permission_manage_designs, 'designs_form')

        designs_form = DTMLFile('designs', globals())

        security.declareProtected(permission_manage_designs, 'setup_design_form')

        setup_design_form = DTMLFile('setup_design', globals())

        security.declareProtected(permission_manage_designs, 'preview_design_form')

        preview_design_form = DTMLFile('preview_design', globals())

        security.declareProtected(permission_manage_designs, 'preview_design_top_form')

        preview_design_top_form = DTMLFile('preview_design_top', globals(), target='_parent')

    # ------------------------------------------------------------------------
    # Design Plugin API

    security.declareProtected(permission_manage, 'has_designplugins')

    def has_designplugins(self):
        """Return the specified MetaPublisher2 Design plugin"""

        return self.has_plugins(IDesignPluginBase)

    security.declareProtected(permission_manage, 'get_designplugin')

    def get_designplugin(self, designplugin_id):
        """Return the specified MetaPublisher2 Design plugin"""

        return self.get_plugin(designplugin_id, IDesignPluginBase)

    security.declareProtected(permission_manage, 'designplugin_ids')

    def designplugin_ids(self):
        """Return ids of installed MetaPublisher2 Design plugins"""

        return self.plugin_ids(IDesignPluginBase)

    security.declareProtected(permission_manage, 'designplugin_items')

    def designplugin_items(self):
        """Return tuples of id, value of installed MetaPublisher2 Design plugins"""

        return self.plugin_items(IDesignPluginBase)

    security.declareProtected(permission_manage, 'designplugin_values')

    def designplugin_values(self):
        """Return tuples of id, value of installed MetaPublisher2 Design plugins"""

        return self.plugin_values(IDesignPluginBase)

    # ------------------------------------------------------------------------
    # Design Flag Retrieval

    security.declareProtected(permission_manage_designs, 'get_designflags')

    def get_designflags(self, design_id):
        """Return tuples of id, boolean states of all Plugin flags"""

        design = get_design(self, design_id)
        return design.get_designflags()

    security.declareProtected(permission_manage_designs, 'get_designflag_ids')

    def get_designflag_ids(self, design_id):
        """Return the ids of all Plugin flags"""

        design = get_design(self, design_id)
        return design.get_designflag_ids()

    security.declareProtected(permission_manage_designs, 'get_designflag')

    def get_designflag(self, design_id, pluginflag_id):
        """Return the boolean state of the specified Design flag if it exists, raises KeyError otherwise"""

        design = get_design(self, design_id)
        return design.get_pluginflag(pluginflag_id)

    security.declareProtected(permission_manage_designs, 'has_designflag')

    def has_designflag(self, design_id, pluginflag_id):
        """Return True if the Design flag exists, False otherwise"""

        design = get_design(self, design_id)
        return design.has_pluginflag(pluginflag_id)

    # ------------------------------------------------------------------------
    # Design Retrieval API

    security.declareProtected(permission_manage_designs, 'design_ids')

    def design_ids(self):
        """Return the ids of Frontends."""

        return self.designs.objectIds()

    security.declareProtected(permission_manage_designs, 'design_items')

    def design_items(self):
        """Return tuples of id, objects of Frontends."""

        return self.designs.objectItems()

    security.declareProtected(permission_manage_designs, 'design_values')

    def design_values(self):
        """Return the objects of Frontends."""

        return self.designs.objectValues()

    security.declareProtected(permission_manage_designs, 'get_design')

    def get_design(self, design_id):
        """Return the specified Frontend."""

        return self.designs._getOb(design_id)

    security.declareProtected(permission_manage_designs, 'preview_design')

    def preview_design(self, design_id, options={}, REQUEST=None, **args):
        """Preview a Design with the specified options."""

        # TODO: preview_design
        raise NotImplemented

    # ------------------------------------------------------------------------
    # Design Mutation API

    security.declareProtected(permission_manage_designs, 'setup_design')

    def setup_design(self, frontend_parent_id, design_id, options={}, REQUEST=None, **args):
        """Add a Design with the specified options to the Frontends."""

        # TODO: setup_design
        raise NotImplemented

# ----------------------------------------------------------------------------
# Class Security

InitializeClass(Designs)

# !!! designs.py - implement
# !!! designs.py - handle default designs and secondary designs
