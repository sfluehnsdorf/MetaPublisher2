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

__doc__ = """MetaPublisher2 Product Registry

Zope2 Product registry, which registers all Product classes, all Product
images and the online help. The individual Product registrations are
outsourced to the products directory. For backward compatibility renamed
modules are mapped to their new names.

$Id: __init__.py 9 2013-05-07 18:02:26Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from library import basepath, ImageFile, isdir, join, listdir, sep, splitext
from products import *


# ============================================================================
# Product Registration

def initialize(context):
    """Register MetaPublisher2 Product and resource folders"""

    # register MetaPublisher2 Product
    register_MetaPublisher2(context)

    # register MetaPublisher2 Product resource folders
    register_MetaPublisher2Designs(context)
    register_MetaPublisher2Frontends(context)
    register_MetaPublisher2Languages(context)
    register_MetaPublisher2Tools(context)
    register_MetaPublisher2Widgets(context)

    # register Product help
    context.registerHelp(directory='help')
    context.registerHelpTitle('MetaPublisher2')


# ============================================================================
# Product Imagery

# ------------------------------------------------------------------------------
# Product Icon Imagery

misc_ = {}
imagepath = join('resources', 'icon')
todo = listdir(join(basepath, imagepath))
while todo:
    filename = todo.pop()
    filepath = join(imagepath, filename)
    if isdir(join(basepath, filepath)):
        todo.extend(map(lambda subfilename: join(filename, subfilename), listdir(join(basepath, filepath))))
    elif splitext(filename)[1] in ('.png', '.gif', '.jpg'):
        key = '_'.join(filename.split(sep))
        misc_[key] = ImageFile(filepath, globals())

# ------------------------------------------------------------------------------
# Legacy Icon Imagery

misc_.update({
    'MP2Powered.gif': ImageFile('resources/attribution/legacy.gif', globals()),
    'Plugin.gif': ImageFile('resources/icon/plugin.png', globals()),
    'Storage.gif': ImageFile('resources/icon/storage.png', globals()),
    'Field.gif': ImageFile('resources/icon/field.png', globals()),
    'Entry.gif': ImageFile('resources/icon/entry.png', globals()),
    'Interface.gif': ImageFile('resources/icon/frontend.png', globals()),
    'Widget.gif': ImageFile('resources/icon/widget.png', globals()),
    'Entries.gif': ImageFile('resources/icon/MetaPublisher2Folder.gif', globals()),
    'Interfaces.gif': ImageFile('resources/icon/MetaPublisher2Folder.gif', globals()),
})


# ==============================================================================
# Product Backwards Compatibility

# Setting __module_aliases__ failed for whatever reason, which is why I have to
# directly change the sys.modules mapping here. It may not be pretty but it
# seems to work.

import sys

import library
import products

sys.modules['Products.MetaPublisher2.Library'] = library.compatibility.historical
sys.modules['Products.MetaPublisher2.Interfaces'] = library.compatibility.historical
sys.modules['Products.MetaPublisher2.MetaPublisher2'] = products.metapublisher2.MetaPublisher2

# !!! PHASE 1 - global
# !!! PHASE 2 - library (except jsondict, pluginregistry)
# !!! PHASE 3 - interfaces/__init__.py, interfaces/plugin/
# !!! PHASE 4 - service/, system/ (except integrity)
# !!! PHASE 5 - configuration/, bases/[field,identifier,storage], interfaces/[field,identifier,storage]
# !!! PHASE 6 - data/, bases/[entry,entrycontainer,entryfield,entryset], interfaces/[entry,entrycontainer,entryfield,entryset]
# !!! PHASE 7 - frontends/, bases/[design,frontend,widget], interfaces/[design,frontend,widget]
# !!! PHASE 8 - inline error messages, integrity tests, jsondict, onexit handlers, pluginregistry, review all forms, settings.conf, tests
# !!! PHASE 9 - online services, pep8, remove DEV, test zope release compatability

# !!! global - mark (all) class doc strings with !TXT!
# !!! global - mark (all) def doc strings with !TXT!
# !!! global - mark (all) redirect messages with !TXT!
# !!! global - update all !TXT! markers
# !!! global - update all TODO markers

# !!! global - check all attribute retrieval if get_MetaPublisher2 needed
# !!! global - check all calls of get_storage if they should be get_storage_by_id, then rename get_storage to get_source and get_storage_by_id to get_storage
# !!! global - check all href's if they start with get_MetaPublisher2_url
# !!! global - check all redirects
# !!! global - clean up name usage of source, storage and storage_id
# !!! global - either add <form> to all forms or include in header/footer
# !!! global - raise errors, i.e. when get_entry or get_storage has no result
# !!! global - replace <dtml-var ...>
# !!! global - replace ambiguos getId calls with specific for plugins
# !!! global - verify all forms' setup tests (error dialogs) and replace dialogs

# !!! cleanup - all forms must display errors inline instead of simply raising
# !!! cleanup - all forms should provide onexit handlers to avoid data loss
# !!! cleanup - cleanup settings.conf
# !!! cleanup - create test suite
# !!! cleanup - review all form designs

# !!! release - test zope release compatability
# !!! release - remove DEV code from products/metapublisher2/MetaPublisher2.py
# !!! release - verify pep8 conformity in code
# !!! release - verify pep8 conformity in forms
# !!! release - setup online services
