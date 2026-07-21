"""MetaPublisher - Common Library.

Central repository for Python and Zope resources, including imports, constants
and API's. By providing these resources in a central location, it is easy to
adapt calls to these resources to the various implementations of the Zope
server and the Python programming language.
"""


from collections import Mapping
from os import listdir
from os.path import exists, isdir, join, normpath, sep, split, splitext
from urllib import quote_plus

import Products
from AccessControl.Role import RoleManager
from AccessControl.SecurityInfo import ClassSecurityInfo
from AccessControl.class_init import InitializeClass
from Acquisition import Implicit
from App.ImageFile import ImageFile
from App.special_dtml import DTMLFile
from ComputedAttribute import ComputedAttribute
from DocumentTemplate.DT_Var import url_quote
from OFS.Folder import Folder
from OFS.ObjectManager import BeforeDeleteException
from OFS.PropertyManager import PropertyManager
from OFS.SimpleItem import (
    Item as ItemBase, Item_w__name__ as NamedItem, SimpleItem)
from Products.PythonScripts.PythonScript import manage_addPythonScript
from zope.interface import implements

try:
    from OFS.OrderedFolder import OrderedFolder
except Exception:
    OrderedFolder = Folder

try:
    from collections import Counter
except Exception:

    class Counter(dict):
        """Simplified Counter class."""

        def __init__(self, iterable=None):
            """Create a new, empty Counter object."""
            super(Counter, self).__init__()
            self.update(iterable)

        def update(self, iterable=None, **kwds):
            """Update data and add counts instead of replacing them."""
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
    'exists',
    'false',
    'implements',
    'isdir',
    'join',
    'listdir',
    'manage_addPythonScript',
    'normpath',
    'quote_plus',
    'sep',
    'split',
    'split_paths',
    'splitext',
    'true',
    'url_quote',
    'uuid4',
]


# ============================================================================
# Path Splitter

def split_paths(path):
    """Split a path into all its parts."""
    return normpath(path).split(sep)


# ============================================================================
# Booleans

try:
    true = True
    false = False
except Exception:
    true = 1
    false = 0


# ============================================================================
# UUID

try:
    from uuid import uuid4
except Exception:
    from random import randrange

    def uuid4():
        """Generate a (fake) UUID4."""
        return (
            '%x%x%x%x%x%x%x%x-%x%x%x%x-%x%x%x%x-%x%x%x%x-'
            '%x%x%x%x%x%x%x%x%x%x%x%x' % map(
                lambda index: randrange(16),
                range(32)
            )
        )

# !!! common.py - insert module exports
