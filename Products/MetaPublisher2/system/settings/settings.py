"""MetaPublisher2."""


from Products.MetaPublisher2.library.application import (
    permission_manage, settings)
from Products.MetaPublisher2.library.common import (
    ClassSecurityInfo, DTMLFile, InitializeClass)


# ============================================================================
# Module Exports

__all__ = [
    'Settings',
]


# ============================================================================
# Settings Component Mix-In Class

class Settings:
    """Settings Component Mix-In Class."""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # Settings ZMI Forms

    security.declareProtected(permission_manage, 'settings_form')

    settings_form = DTMLFile('settings', globals())

    # ------------------------------------------------------------------------
    # Settings Retrieval

    security.declareProtected(permission_manage, 'list_settings')

    def list_settings(self):
        """List all settings."""
        result = []
        for key, value in settings.items():
            result.append({'key': key, 'value': value})
        return result
        result = settings.items()
        result.sort()
        return settings.items()

    security.declareProtected(permission_manage, 'get_setting')

    def get_setting(self, key):
        """Return the value for the specified setting."""
        return settings[key]


# ----------------------------------------------------------------------------
# Class Security

InitializeClass(Settings)
