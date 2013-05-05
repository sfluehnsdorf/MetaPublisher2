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

__doc__ = """Configuration Section

!TXT! module info
Module providing a mix-in class for the MetaPublisher 2's Configuration section.

$Id: configuration/configuration.py 7 2013-05-05 18:04:45Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.library import ClassSecurityInfo, DTMLFile, InitializeClass

from constraints import Constraints
from fields import Fields
from identifiers import Identifiers
from indexing import Indexing
from inheritance import Inheritance
from relations import Relations
from storages import Storages
from triggers import Triggers


# ============================================================================
# Module Exports

__all__ = [
    'Configuration',
]


# ============================================================================
# Configuration Section Mix-In Class

class Configuration(Storages, Fields, Identifiers, Constraints, Relations, Triggers, Inheritance, Indexing):
    """Configuration Section Mix-In Class"""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # Configuration ZMI Management Tabs

    manage_options = (
        {'label': 'Storages', 'action': 'storages_form'},
        {'label': 'Fields', 'action': 'fields_form'},
        {'label': 'Identifiers', 'action': 'identifiers_form'},
        {'label': 'Constraints', 'action': 'constraints_form'},
        {'label': 'Relations', 'action': 'relations_form'},
        {'label': 'Triggers', 'action': 'triggers_form'},
        {'label': 'Inheritance', 'action': 'inheritance_form'},
        {'label': 'Indexing', 'action': 'indexing_form'},
    )

# ----------------------------------------------------------------------------
# Class Security

InitializeClass(Configuration)
