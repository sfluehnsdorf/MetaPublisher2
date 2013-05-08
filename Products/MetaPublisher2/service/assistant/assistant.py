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

__doc__ = """Assistant Component

Guidance service that assists in configuring the MetaPublisher2 by leading the
user through the various steps. Users can select one of the three experience
levels "novice", "intermediate" and "expert". This customises the information
and the form of the presentation.

$Id: service/assistant/assistant.py 4 2013-05-08 18:55:47Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.library import ClassSecurityInfo, DTMLFile,\
    InitializeClass, permission_manage, show_future


# ============================================================================
# Module Exports

__all__ = [
    'Assistant',
]


# ============================================================================
# Assistant Component Mix-In Class

class Assistant:
    """!TXT! Assistant Component Mix-In Class"""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # Assistant ZMI Forms

    if show_future:

        security.declareProtected(permission_manage, 'assistant_form')

        assistant_form = DTMLFile('assistant', globals())

# ----------------------------------------------------------------------------
# Class Security

InitializeClass(Assistant)

# TODO: Assistant Component
