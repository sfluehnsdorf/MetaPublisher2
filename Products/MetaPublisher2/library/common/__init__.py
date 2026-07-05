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

__doc__ = """Common Library Initialisation

Common Zope Python resources, including constants, definitions and API's. By
providing these resources in a central location, it is easy to adapt this
application to the various implementations of the Zope server and the Python
programming language.

$Id: library/common/__init__.py 4 2013-05-08 20:23:16Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from common import (
    BeforeDeleteException, ClassSecurityInfo, ComputedAttribute, Counter,
    DTMLFile, Folder, ImageFile, Implicit, InitializeClass, ItemBase,
    NamedItem, OrderedFolder, Products, PropertyManager, RoleManager,
    SimpleItem, exists, false, implements, isdir, join, listdir,
    manage_addPythonScript, normpath, quote_plus, sep, split, split_paths,
    splitext, true, uuid4)
from log import log
from typeid import eval_valuestring, identify_type


# ============================================================================
# Module Exports

__all__ = [
    'BeforeDeleteException',
    'ClassSecurityInfo',
    'ComputedAttribute',
    'Counter',
    'DTMLFile',
    'Folder',
    'ImageFile',
    'Implicit',
    'InitializeClass',
    'ItemBase',
    'NamedItem',
    'OrderedFolder',
    'Products',
    'PropertyManager',
    'RoleManager',
    'SimpleItem',
    'eval_valuestring',
    'exists',
    'false',
    'identify_type',
    'implements',
    'isdir',
    'join',
    'listdir',
    'log',
    'manage_addPythonScript',
    'normpath',
    'quote_plus',
    'sep',
    'split',
    'split_paths',
    'splitext',
    'true',
    'uuid4',
]
