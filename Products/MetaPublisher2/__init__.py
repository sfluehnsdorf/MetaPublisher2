"""MetaPublisher2 Product Registry.

Zope2 Product registry, which registers all Product classes, all Product
images and the online help. The individual Product registrations are
outsourced to the products directory. For backward compatibility renamed
modules are mapped to their new names.
"""


# ============================================================================
# Module Imports


import sys
import library
import products

from library.application import basepath
from library.common import ImageFile, isdir, join, listdir, sep, splitext
from products import (
    register_MetaPublisher2, register_MetaPublisher2Designs,
    register_MetaPublisher2Frontends, register_MetaPublisher2Languages,
    register_MetaPublisher2Tools, register_MetaPublisher2Widgets)


# ============================================================================
# Product Registration


def initialize(context):
    """Register MetaPublisher2 Product and resource folders."""
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


# ----------------------------------------------------------------------------
# Product Icon Imagery

misc_ = {}
imagepath = join('resources', 'icon')
todo = listdir(join(basepath, imagepath))
while todo:
    filename = todo.pop()
    filepath = join(imagepath, filename)
    if isdir(join(basepath, filepath)):
        todo.extend(map(
            lambda subfilename: join(filename, subfilename),
            listdir(join(basepath, filepath))))
    elif splitext(filename)[1] in ('.png', '.gif', '.jpg'):
        key = '_'.join(filename.split(sep))
        misc_[key] = ImageFile(filepath, globals())


# ----------------------------------------------------------------------------
# Legacy Icon Imagery

misc_.update({
    'MP2Powered.gif': ImageFile('resources/attribution/legacy.gif', globals()),
    'Plugin.gif': ImageFile('resources/icon/plugin.png', globals()),
    'Storage.gif': ImageFile('resources/icon/storage.png', globals()),
    'Field.gif': ImageFile('resources/icon/field.png', globals()),
    'Entry.gif': ImageFile('resources/icon/entry.png', globals()),
    'Interface.gif': ImageFile('resources/icon/frontend.png', globals()),
    'Widget.gif': ImageFile('resources/icon/widget.png', globals()),
    'Entries.gif': ImageFile(
        'resources/icon/MetaPublisher2Folder.gif', globals()),
    'Interfaces.gif': ImageFile(
        'resources/icon/MetaPublisher2Folder.gif', globals()),
})


# ----------------------------------------------------------------------------
# Product Backwards Compatibility.

"""Setting __module_aliases__ failed for whatever reason, which is why I have
to directly change the sys.modules mapping here. It may not be pretty but it
seems to work.
"""

sys.modules['Products.MetaPublisher2.Library'] = (
    library.compatibility.historical)
sys.modules['Products.MetaPublisher2.Interfaces'] = (
    library.compatibility.historical)
sys.modules['Products.MetaPublisher2.MetaPublisher2'] = (
    products.metapublisher2.MetaPublisher2)


# ============================================================================


'''
TODO: …

PHASE 1 - global
PHASE 2 - library (remove xmldict & jsondict, skip pluginregistry)
PHASE 3 - interfaces/__init__.py, interfaces/plugin/
PHASE 4 - service/, system/ (except integrity)
PHASE 5 - configuration/, bases/[field,identifier,storage],
    interfaces/[field,identifier,storage]
PHASE 6 - data/, bases/[entry,entrycontainer,entryfield,entryset],
    interfaces/[entry,entrycontainer,entryfield,entryset]
PHASE 7 - inline error messages, integrity tests, jsondict, onexit handlers,
    pluginregistry, review all forms, settings.conf, tests
PHASE 8 - online services, pep8, remove DEV, test zope release compatability

# ----------------------------------------------------------------------------

global
    - verify all forms' setup tests (error dialogs)
    - check all attribute retrieval if get_MetaPublisher2 needed
    - check all calls of get_storage if they should be get_storage_by_id, then
      rename get_storage to get_source and get_storage_by_id to get_storage
    - clean up name usage of source, storage and storage_id
    - replace ambiguos getId calls with specific for plugins
    - raise errors, i.e. when get_entry or get_storage has no result

cleanup
    - all forms must display errors inline instead of simply raising
    - all forms should provide onexit handlers to avoid data loss
    - cleanup settings.conf
    - create test suite
    - review all form designs

release
    - test zope release compatability
    - remove DEV code from products/metapublisher2/MetaPublisher2.py
    - verify pep8 conformity in code
    - verify pep8 conformity in forms
    - setup online services
'''
