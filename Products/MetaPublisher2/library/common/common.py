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

__doc__ = """Common Resource Library

Central repository for Python and Zope resources, including imports, constants
and API's. By providing these resources in a central location, it is easy to
adapt calls to these resources to the various implementations of the Zope server
and the Python programming language.

$Id: library/common/common.py 5 2012-02-17 15:45:00Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from os import listdir
from os.path import exists, isdir, join, normpath, sep, split, splitext
from urllib import quote_plus

import Products
from AccessControl.Role import RoleManager
from AccessControl.SecurityInfo import ClassSecurityInfo
from Acquisition import Implicit
from ComputedAttribute import ComputedAttribute
from Globals import DTMLFile, ImageFile, InitializeClass
from OFS.Folder import Folder
from OFS.ObjectManager import BeforeDeleteException
from OFS.PropertyManager import PropertyManager
from OFS.SimpleItem import Item as ItemBase, Item_w__name__ as NamedItem, SimpleItem
from Products.PythonScripts.PythonScript import manage_addPythonScript
from zope.interface import implements

try:
    from OFS.OrderedFolder import OrderedFolder
except:
    OrderedFolder = Folder

try:
    from collections import Counter
except:

    class Counter(dict):
        '''Simplified Counter class'''

        def __init__(self, iterable=None):
            '''Create a new, empty Counter object.'''
            super(Counter, self).__init__()
            self.update(iterable)

        def update(self, iterable=None, **kwds):
            '''Update data and add counts instead of replacing them.'''
            if iterable is not None:
                if isinstance(iterable, Mapping):
                    if self:
                        self_get = self.get
                        for elem, count in iterable.iteritems():
                            self[elem] = self_get(elem, 0) + count
                    else:
                        super(Counter, self).update(iterable)
                else:
                    self_get = self.get
                    for elem in iterable:
                        self[elem] = self_get(elem, 0) + 1
            if kwds:
                self.update(kwds)


# ============================================================================
# Path Splitter

def split_paths(path):
    """Split a path into all its parts"""

    return normpath(path).split(sep)


# ============================================================================
# Booleans

try:
    true = True
    false = False
except:
    true = 1
    false = 0


# ============================================================================
# UUID

try:
    from uuid import uuid4
except:

    from random import randrange

    def uuid4():
        """generate uuid4"""
        return '%x%x%x%x%x%x%x%x-%x%x%x%x-%x%x%x%x-%x%x%x%x-%x%x%x%x%x%x%x%x%x%x%x%x' % map(lambda index: randrange(16), range(32))
