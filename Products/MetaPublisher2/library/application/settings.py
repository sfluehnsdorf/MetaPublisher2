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

__doc__ = """Application Settings

!TXT! module info

$Id: library/application/settings.py 10 2013-05-07 17:08:24Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from ConfigParser import SafeConfigParser
from types import IntType, FloatType

from Products.MetaPublisher2.library.common import false, join, true

from exceptions import ConfigurationError
from paths import basepath


# ==============================================================================
# Module Exports

__all__ = [
    'settings',
]


# ============================================================================
# Default Settings

settings = {
    'data_access_entries_security': 'none',
    'data_create_entries_security': 'none',
    'data_change_entries_security': 'none',
    'data_import_entries_security': 'none',
    'data_export_entries_security': 'none',
    'configuration_access_configuration_security': 'none',
    'configuration_change_configuration_security': 'none',
    'publisher_manage_frontends_security': 'none',
    'publisher_manage_designs_security': 'none',
    'publisher_publish_frontends_security': 'none',
    'system_test_integrity_security': 'none',
    'system_manage_presets_security': 'none',
    'system_load_presets_security': 'none',
    'system_save_presets_security': 'none',
    'system_upload_presets_security': 'none',
    'system_manage_system_security': 'none',
    'service_release_check_security': 'none',
    'service_release_check_url': 'http://metapublisher.org/service/2.3/update',
    'service_community_url': 'http://metapublisher.org/service/2.3/community',
    'service_manual_url': 'http://metapublisher.org/service/2.3/manual',
    'service_reference_url': 'http://metapublisher.org/service/2.3/reference',
    'service_feedback_url': 'http://metapublisher.org/service/2.3/feedback',
}


# ============================================================================
# Configuration File

parser = SafeConfigParser()
parser.read(join(basepath, 'settings.conf'))
for section in parser.sections():
    for option, value in parser.items(section):
        key = '%s_%s' % (section, option)
        if not key in settings:
            raise ConfigurationError('Unknown configuration option "%s" in section "%s"' % (option, section))
        if option.endswith('_security'):
            value = parser.get(section, option)
            if not value in ['protected', 'private', 'none']:
                raise ConfigurationError('Invalid value "%s" for security option "%s" in section "%s"' % (value, option, section))
        elif settings[key] in [true, false]:
            value = parser.getboolean(section, option)
        elif isinstance(settings[key], IntType):
            value = parser.getint(section, option)
        elif isinstance(settings[key], FloatType):
            value = parser.getfloat(section, option)
        else:
            value = parser.get(section, option)
        settings[key] = value
