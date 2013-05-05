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

__doc__ = """Application Permissions

git rm -r MetaPublisher2 specific permission's names are defined here, ensuring
consistency in the naming of permission.

$Id: library/application/permissions.py 5 2012-02-17 15:45:00Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from AccessControl.Permissions import view_management_screens
from AccessControl.SecurityInfo import ACCESS_NONE, ACCESS_PRIVATE

from exceptions import ConfigurationError
from settings import settings


# ==============================================================================
# Module Exports

__all__ = [
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
]

# ============================================================================
# Standard Permissions

permission_zmi = view_management_screens

permission_manage = 'MetaPublisher2 - Manage Instance'


# ============================================================================
# Configurable Permissions

def configure_permission(setting, permission):
    """Return parameter for access control based on setting"""

    if settings[setting + '_security'] == 'protected':
        return permission
    elif settings[setting + '_security'] == 'private':
        return ACCESS_PRIVATE
    elif settings[setting + '_security'] == 'none':
        return ACCESS_NONE
    else:
        raise ConfigurationError('Invalid value "%s" for security setting "%s"' % (settings[setting + '_security'], setting))

# ----------------------------------------------------------------------------
# !TXT!

permission_access_entries = configure_permission('data_access_entries', 'MetaPublisher2 - Access Entries & EntryFields')

permission_create_entries = configure_permission('data_create_entries', 'MetaPublisher2 - Create Entries & EntryFields')

permission_change_entries = configure_permission('data_change_entries', 'MetaPublisher2 - Change Entries & EntryFields')

permission_import_entries = configure_permission('data_import_entries', 'MetaPublisher2 - Import Entries')

permission_export_entries = configure_permission('data_export_entries', 'MetaPublisher2 - Export Entries')

# ----------------------------------------------------------------------------
# !TXT!

permission_access_configuration = configure_permission('configuration_access_configuration', 'MetaPublisher2 - Access Storages & Fields')

permission_change_configuration = configure_permission('configuration_change_configuration', 'MetaPublisher2 - Change Storages & Fields')

# ----------------------------------------------------------------------------
# !TXT!

permission_manage_frontends = configure_permission('publisher_manage_frontends', 'MetaPublisher2 - Manage Frontends & Widgets')

permission_manage_designs = configure_permission('publisher_manage_designs', 'MetaPublisher2 - Manage & Setup Designs')

permission_publish_frontends = configure_permission('publisher_publish_frontends', 'MetaPublisher2 - Render Frontends')

# ----------------------------------------------------------------------------
# !TXT!

permission_test_integrity = configure_permission('system_test_integrity', 'MetaPublisher2 - Test Integrity')

permission_manage_presets = configure_permission('system_manage_presets', 'MetaPublisher2 - Manage Presets')

permission_load_presets = configure_permission('system_load_presets', 'MetaPublisher2 - Load Presets')

permission_save_presets = configure_permission('system_save_presets', 'MetaPublisher2 - Save Presets')

permission_upload_presets = configure_permission('system_upload_presets', 'MetaPublisher2 - Upload Presets')

permission_manage_system = configure_permission('system_manage_system', 'MetaPublisher2 - Manage System')

# ----------------------------------------------------------------------------
# !TXT!

permission_release_check = configure_permission('service_release_check', 'MetaPublisher2 - Check Release For Updates')
