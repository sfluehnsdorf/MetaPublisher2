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

__doc__ = """MetaPublisher2 Library Inititalisation

The library of the MetaPublisher2 is a collection of resources, used by the
main application and by its plugins. Please check each of the modules inside
#for detailed information on these resources.

$Id: library/__init__.py 3 2013-05-08 18:46:33Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from application import (
    AmbiguityError, ConfigurationError, ConnectionError, ConstraintError,
    ImmutableError, PluginRegistry, RenderError, UnreadableError,
    UnsupportedError, basepath, permission_access_configuration,
    permission_access_entries, permission_change_configuration,
    permission_change_entries, permission_create_entries,
    permission_export_entries, permission_import_entries,
    permission_load_presets, permission_manage, permission_manage_designs,
    permission_manage_frontends, permission_manage_presets,
    permission_manage_system, permission_publish_frontends,
    permission_release_check, permission_save_presets,
    permission_test_integrity, permission_upload_presets,
    permission_zmi, settings)
from common import (
    BeforeDeleteException, ClassSecurityInfo, ComputedAttribute, Counter,
    DTMLFile, Folder, ImageFile, Implicit, InitializeClass, ItemBase,
    NamedItem, OrderedFolder, Products, PropertyManager, RoleManager,
    SimpleItem, eval_valuestring, exists, false, identify_type, implements,
    isdir, join, listdir, log, manage_addPythonScript, normpath, quote_plus,
    sep, split, split_paths, splitext, true, uuid4)
from compatibility import (
    Compatibility, FutureCompatibility, HistoricalCompatibility,
    InterfacesFolder, TestError, deprecated_form, deprecated_method,
    show_future, standard_form_footer, standard_form_header)
from jsondict import JSONDict
from multitabs import MultiTabs
from userinterface import UserInterface
from xmldict import XMLDict


# ============================================================================
# Module Exports

__all__ = [
    'AmbiguityError',
    'BeforeDeleteException',
    'ClassSecurityInfo',
    'Compatibility',
    'ComputedAttribute',
    'ConfigurationError',
    'ConnectionError',
    'ConstraintError',
    'Counter',
    'DTMLFile',
    'Folder',
    'FutureCompatibility',
    'HistoricalCompatibility',
    'ImageFile',
    'ImmutableError',
    'Implicit',
    'InitializeClass',
    'InterfacesFolder',
    'ItemBase',
    'JSONDict',
    'MultiTabs',
    'NamedItem',
    'OrderedFolder',
    'PluginRegistry',
    'Products',
    'PropertyManager',
    'RenderError',
    'RoleManager',
    'SimpleItem',
    'TestError',
    'UnreadableError',
    'UnsupportedError',
    'UserInterface',
    'XMLDict',
    'basepath',
    'deprecated_form',
    'deprecated_method',
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
    'permission_access_configuration',
    'permission_access_entries',
    'permission_change_configuration',
    'permission_change_entries',
    'permission_create_entries',
    'permission_export_entries',
    'permission_import_entries',
    'permission_load_presets',
    'permission_manage',
    'permission_manage_designs',
    'permission_manage_frontends',
    'permission_manage_presets',
    'permission_manage_system',
    'permission_publish_frontends',
    'permission_release_check',
    'permission_save_presets',
    'permission_test_integrity',
    'permission_upload_presets',
    'permission_zmi',
    'quote_plus',
    'sep',
    'settings',
    'show_future',
    'split',
    'split_paths',
    'splitext',
    'standard_form_footer',
    'standard_form_header',
    'true',
    'uuid4',
]
