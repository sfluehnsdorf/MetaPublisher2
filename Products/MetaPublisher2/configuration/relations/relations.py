# -*- coding: iso-8859-15 -*-
# ==============================================================================
#
#                         M e t a  P u b l i s h e r  2
#
# ------------------------------------------------------------------------------
# Copyright (c) 2002-2011, Sebastian Lühnsdorf - Web-Solutions and contributors
# For more information see the README.txt file or visit www.metapulisher.org
# ------------------------------------------------------------------------------
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
# ==============================================================================

__doc__ = """Relations Component

!TXT! module info

$Id: configuration/relations/relations.py 2 2012-08-09 19:48:00Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ==============================================================================
# Module Imports

from Products.MetaPublisher2.library import ClassSecurityInfo, DTMLFile, InitializeClass, permission_access_configuration, permission_change_configuration, show_future


# ============================================================================
# Module Exports

__all__ = [
    'Relations',
]


# ==============================================================================
# Relations Mix-In Class

class Relations:
    """Relations Mix-In Class"""

    security = ClassSecurityInfo()

    # --------------------------------------------------------------------------
    # !TXT!

    if show_future:

        security.declareProtected(permission_access_configuration, 'relations_form')

        relations_form = DTMLFile('relations', globals())

        security.declareProtected(permission_change_configuration, 'add_relation_form')

        add_relation_form = DTMLFile('add_relation', globals())

        security.declareProtected(permission_change_configuration, 'delete_relations_form')

        delete_relations_form = DTMLFile('delete_relations', globals())

        security.declareProtected(permission_change_configuration, 'duplicate_relations_form')

        duplicate_relations_form = DTMLFile('duplicate_relations', globals())

        security.declareProtected(permission_change_configuration, 'edit_relation_form')

        edit_relation_form = DTMLFile('edit_relation', globals())

        security.declareProtected(permission_change_configuration, 'rename_relations_form')

        rename_relations_form = DTMLFile('rename_relations', globals())

# ------------------------------------------------------------------------------
# Class Security

InitializeClass(Relations)

# TODO: Relations Component

# TODO: relation types (move to base?): unidirectional, bidirectional, weighted, conditional, 1:1, 1:m, m:1, m:n
#     The heart of the database consists of these primary components: Items, Relations
#     An Item consists of:
#     - A unique ID
#     - A block of data, which can be any content-type, such as text/plain, text/html, image/gif.
#     - A parent ID if it is a derivative of a previous Item
#     - Date of creation
#     - The number of times it has been accessed
#     - The times at which these accesses occured
#     A Relation consists of:
#     - A unique ID
#     - An item ID
#     - An second item ID that the first item ID is related to
#     - Date of relation creation
#     - The number of times it has been accessed
#     - The times at which these accesses occured
