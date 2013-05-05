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

__doc__ = """Publisher Section

!TXT!Module providing a mix-in class for the MetaPublisher 2's Publisher section.

$Id: publisher/publisher.py 7 2012-08-09 19:48:00Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.library import ClassSecurityInfo, DTMLFile, InitializeClass

from audit import Audit
from caching import Caching
from designs import Designs
from frontends import Frontends
from languages import Languages
from renderer import Renderer
from widgets import Widgets


# ============================================================================
# Module Exports

__all__ = [
    'Publisher',
]


# ============================================================================
# Publisher Mix-In Class

class Publisher(Frontends, Widgets, Designs, Languages, Caching, Audit, Renderer):
    """Publisher Mix-In Class"""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # Publisher ZMI Management Tabs

    manage_options = (
        {'label': 'Frontends', 'action': 'frontends_form'},
        {'label': 'Widgets', 'action': 'widgets_form'},
        {'label': 'Designs', 'action': 'designs_form'},
        {'label': 'Languages', 'action': 'languages_form'},
        {'label': 'Caching', 'action': 'caching_form'},
        {'label': 'Audit', 'action': 'audit_form'},
        {'label': 'Renderer', 'action': 'renderer_form'},
    )

# ----------------------------------------------------------------------------
# Class Security

InitializeClass(Publisher)
