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

__doc__ = """Release Component

Retrieval service of the MetaPublisher2 release information text files and
online release version check service.

$Id: service/release/release.py 5 2013-05-05 18:00:52Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.library import basepath, ClassSecurityInfo, DTMLFile, exists, false, InitializeClass, join, permission_release_check, permission_zmi, split, true


# ============================================================================
# Module Exports

__all__ = [
    'Release',
]


# ============================================================================
# Release Mix-In Class

class Release:
    """Release Mix-In Class"""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # Release ZMI Forms

    security.declareProtected(permission_zmi, 'release_form')

    release_form = DTMLFile('release', globals())

    # ------------------------------------------------------------------------
    # Release Retrieval API

    def _read_release_file(self, filename):
        filename = join(basepath, split(filename)[1])
        if exists(filename):
            filehandle = open(filename)
            lines = filehandle.readlines()
            filehandle.close()
            return u''.join(map(lambda line: unicode(line, 'utf8'), lines))
        return u''

    security.declareProtected(permission_zmi, 'get_release_version')

    def get_release_version(self):
        """Return the contents of the VERSION.txt file"""

        return self._read_release_file('VERSION.txt')

    security.declareProtected(permission_zmi, 'get_release_readme')

    def get_release_readme(self):
        """Return the contents of the README.txt file"""

        return self._read_release_file('README.txt')

    security.declareProtected(permission_zmi, 'get_release_changes')

    def get_release_changes(self):
        """Return the contents of the CHANGES.txt file"""

        return self._read_release_file('CHANGES.txt')

    security.declareProtected(permission_zmi, 'get_release_history')

    def get_release_history(self):
        """Return the contents of the HISTORY.txt file"""

        return self._read_release_file('HISTORY.txt')

    security.declareProtected(permission_zmi, 'get_release_license')

    def get_release_license(self):
        """Return the contents of the LICENSE.txt file"""

        return self._read_release_file('LICENSE.txt')

    security.declareProtected(permission_zmi, 'may_check_release')

    def may_check_release(self, REQUEST):
        """Return true if user may use the online release check service"""

        return REQUEST.AUTHENTICATED_USER.has_permission(permission_release_check, self) and true or false

    security.declareProtected(permission_release_check, 'get_release_check_url')

    def get_release_check_url(self):
        """Return the URL for the online release check service"""

        return self.get_setting('service_release_check_url')

# ----------------------------------------------------------------------------
# Class Security

InitializeClass(Release)

# !!! release.py - implement online update service
