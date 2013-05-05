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

__doc__ = """UserInterface Resources

!TXT! module info

$Id: library/userinterface/resources.py 2 2012-08-09 19:48:00Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.library.application import basepath
from Products.MetaPublisher2.library.common import ClassSecurityInfo, DTMLFile, ImageFile, InitializeClass, isdir, join, listdir, sep, splitext


# ============================================================================
# Module Exports

__all__ = [
    'Resources',
]


# ============================================================================
# Imagery

# ------------------------------------------------------------------------------
# Resources Mix-In Class

class Resources:
    """Resources Mix-In Class"""

    security = ClassSecurityInfo()

# ------------------------------------------------------------------------------
# Class Security

InitializeClass(Resources)

# ------------------------------------------------------------------------------
# Resources Image Loader

resourcespath = join(basepath, 'resources')
todo = listdir(resourcespath)
while todo:
    filename = todo.pop()
    filepath = join(resourcespath, filename)
    if isdir(filepath):
        todo.extend(map(lambda x: join(filename, x), listdir(filepath)))
    else:
        attribute = '_'.join(filename.split(sep))
        extension = splitext(filename)[1]
        if extension in ('.gif', '.jpg', '.jpeg', '.png', '.bmp'):
            setattr(Resources, attribute, ImageFile(filepath, globals()))
            setattr(Resources, '%s__roles__' % attribute, None)
        elif extension == '.dtml':
            setattr(Resources, attribute[: -5], DTMLFile(filepath[: -5], globals()))
            setattr(Resources, '%s__roles__' % attribute[: -5], None)
