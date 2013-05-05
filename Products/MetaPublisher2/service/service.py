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

__doc__ = """Service Section

Module providing a mix-in class for the MetaPublisher 2's Service section.

$Id: service/service.py 5 2013-05-05 18:01:43Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.library import ClassSecurityInfo, InitializeClass

from assistant import Assistant
from community import Community
from feedback import Feedback
from help import Help
from manual import Manual
from reference import Reference
from release import Release


# ============================================================================
# Module Exports

__all__ = [
    'Service',
]


# ============================================================================
# Service Section Mix-In Class

class Service(Assistant, Release, Community, Manual, Help, Reference, Feedback):
    """Service Section Mix-In Class"""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # Service ZMI Management Tabs

    manage_options = (
        {'label': 'Assistant', 'action': 'assistant_form'},
        {'label': 'Release', 'action': 'release_form'},
        {'label': 'Community', 'action': 'community_form'},
        {'label': 'Manual', 'action': 'manual_form'},
        {'label': 'Help', 'action': 'help_form'},
        {'label': 'Reference', 'action': 'reference_form'},
        {'label': 'Feedback', 'action': 'feedback_form'},
    )

# ----------------------------------------------------------------------------
# Class Security

InitializeClass(Service)
