"""MetaPublisher2 - Release Component.

Retrieval service of the MetaPublisher2 release information text files and
online release version check service.
"""


from Products.MetaPublisher2.library.application import (
    basepath, permission_release_check, permission_zmi)
from Products.MetaPublisher2.library.common import (
    ClassSecurityInfo, DTMLFile, exists, false, InitializeClass, join, split,
    true)


# ============================================================================
# Module Exports

__all__ = [
    'Release',
]


# ============================================================================
# Release Component Mix-In Class

class Release:
    """Release Component Mix-In Class."""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # Release ZMI Forms

    security.declareProtected(permission_zmi, 'release_form')

    release_form = DTMLFile('release', globals())

    # ------------------------------------------------------------------------
    # Release Retrieval API

    def _read_release_file(self, filename):
        """Read release files."""
        filename = join(basepath, split(filename)[1])
        if exists(filename):
            filehandle = open(filename)
            lines = filehandle.readlines()
            filehandle.close()
            return u''.join(map(lambda line: unicode(line, 'utf8'), lines))
        return u''

    security.declareProtected(permission_zmi, 'get_release_version')

    def get_release_version(self):
        """Return the contents of the VERSION.txt file."""
        return self._read_release_file('VERSION.txt')

    security.declareProtected(permission_zmi, 'get_release_readme')

    def get_release_readme(self):
        """Return the contents of the README.txt file."""
        return self._read_release_file('README.txt')

    security.declareProtected(permission_zmi, 'get_release_changes')

    def get_release_changes(self):
        """Return the contents of the CHANGES.txt file."""
        return self._read_release_file('CHANGES.txt')

    security.declareProtected(permission_zmi, 'get_release_history')

    def get_release_history(self):
        """Return the contents of the HISTORY.txt file."""
        return self._read_release_file('HISTORY.txt')

    security.declareProtected(permission_zmi, 'get_release_license')

    def get_release_license(self):
        """Return the contents of the LICENSE.txt file."""
        return self._read_release_file('LICENSE.txt')

    security.declareProtected(permission_zmi, 'may_check_release')

    def may_check_release(self, REQUEST):
        """Return true if user may use the online release check service."""
        return REQUEST.AUTHENTICATED_USER.has_permission(
            permission_release_check, self) and true or false

    security.declareProtected(
        permission_release_check, 'get_release_check_url')

    def get_release_check_url(self):
        """Return the URL for the online release check service."""
        return self.get_setting('service_release_check_url')


# ----------------------------------------------------------------------------
# Class Security

InitializeClass(Release)

# !!! release.py - implement online update service
