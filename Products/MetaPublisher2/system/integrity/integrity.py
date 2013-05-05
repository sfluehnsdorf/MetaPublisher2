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

__doc__ = """Integrity Component

!TXT! module info
Reporting service, which tests the integrity of the MetaPublisher 2 components
and reports inconsistencies in the configuration.

$Id: system/integrity/integrity.py 5 2013-05-05 18:00:40Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.library import ClassSecurityInfo, DTMLFile, InitializeClass, permission_manage


# ============================================================================
# Module Exports

__all__ = [
    'Integrity',
]


# ==============================================================================
# Integrity Mix-In Class

class Integrity:
    """Integrity Mix-In Class"""

    security = ClassSecurityInfo()

    # --------------------------------------------------------------------------
    # Integrity ZMI Forms

    security.declareProtected(permission_manage, 'integrity_form')

    integrity_form = DTMLFile('integrity', globals())

    # --------------------------------------------------------------------------
    # Integrity Test API

    security.declareProtected(permission_manage, 'test_integrity')

    def test_integrity(self, REQUEST):
        """Perform integrity tests with specified options."""

        result = []

        # entries
        for storage_id in REQUEST.get('integrity_entries', []):
            result.extend(self._test_entries_integrity(storage_id))

        # configuration
        if REQUEST.get('integrity_storages', 0):
            result.extend(self._test_storages_integrity())
        for storage_id in REQUEST.get('integrity_fields', []):
            result.extend(self._test_fields_integrity(storage_id))
        if REQUEST.get('integrity_indexing', 0):
            result.extend(self._test_indexing_integrity())

        # publisher
        if REQUEST.get('integrity_frontends', 0):
            result.extend(self._test_frontends_integrity())
        if REQUEST.get('integrity_widgets', 0):
            result.extend(self._test_widgets_integrity())
        if REQUEST.get('integrity_designs', 0):
            result.extend(self._test_designs_integrity())

        # system
        if REQUEST.get('integrity_presets', 0):
            result.extend(self._test_presets_integrity())
        if REQUEST.get('integrity_profiles', 0):
            result.extend(self._test_profiles_integrity())
        if REQUEST.get('integrity_plugins', 0):
            result.extend(self._test_plugins_integrity())

        return result

    # --------------------------------------------------------------------------
    # Integrity Subsystem Test API

    def _test_designs_integrity(self):
        """Perform integrity tests on all Designs."""

        # TODO: implement designs integrity tests

        return []

    def _test_entries_integrity(self, storage_id):
        """Perform integrity tests on all Entries in the specified Storage."""

        # !!! integrity.py - implement entries integrity tests

        return []

    def _test_fields_integrity(self, storage_id):
        """Perform integrity tests on all Fields in the specified Storage."""

        # !!! integrity.py - implement fields integrity tests

        return []

    def _test_frontends_integrity(self):
        """Perform integrity tests on all Frontends."""

        # TODO: implement frontends integrity tests

        return []

    def _test_indexing_integrity(self):
        """Perform integrity tests on all Indexes."""

        # TODO: implement indexing integrity tests

        return []

    def _test_plugins_integrity(self):
        """Perform integrity tests on all Plugins."""

        result = []
        if not(self.has_storageplugins()):
            result.append(('info', 'Plugins', 'No Storage Plugins installed.'))
        if not(self.has_fieldplugins()):
            result.append(('info', 'Plugins', 'No Field Plugins installed.'))
        if not(self.has_frontendplugins()):
            result.append(('info', 'Plugins', 'No Frontend Plugins installed.'))
        if not(self.has_widgetplugins()):
            result.append(('info', 'Plugins', 'No Widget Plugins installed.'))
        for plugin_id, plugin in self.plugin_items():
            if hasattr(plugin['instance'], 'pluginName'):
                result.append(('info', 'Plugins', 'Legacy Plugin "%s" is based on deprecated API which will be removed in a future version.' % plugin_id))
        return result

    def _test_presets_integrity(self):
        """Perform integrity tests on all Presets."""

        # TODO: implement presets integrity tests

        return []

    def _test_profiles_integrity(self):
        """Perform integrity tests on all Profiles."""

        # !!! integrity.py - implement profiles integrity tests

        return []

    def _test_storages_integrity(self):
        """Perform integrity tests on all Storages."""

        # !!! integrity.py - implement storages integrity tests

        return []

    def _test_widgets_integrity(self):
        """Perform integrity tests on all Widgets."""

        # TODO: implement widgets integrity tests

        return []

# ------------------------------------------------------------------------------
# Class Security

InitializeClass(Integrity)
