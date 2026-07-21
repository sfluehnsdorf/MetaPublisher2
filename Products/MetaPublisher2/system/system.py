"""MetaPublisher2."""


from Products.MetaPublisher2.library.common import (
    ClassSecurityInfo, InitializeClass)

from events import Events
from integrity import Integrity
from plugins import Plugins
from presets import Presets
from profiles import Profiles
from settings import Settings
from tools import Tools


# ============================================================================
# Module Exports

__all__ = [
    'System',
]


# ============================================================================
# System Section Mix-In Class

class System(Tools, Integrity, Presets, Events, Profiles, Settings, Plugins):
    """System Section Mix-In Class."""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # System ZMI Management Tabs

    manage_options = (
        {'label': 'Integrity', 'action': 'integrity_form'},
        {'label': 'Tools', 'action': 'tools_form'},
        {'label': 'Presets', 'action': 'presets_form'},
        {'label': 'Events', 'action': 'events_form'},
        {'label': 'Profiles', 'action': 'profiles_form'},
        {'label': 'Settings', 'action': 'settings_form'},
        {'label': 'Plugins', 'action': 'plugins_form'},
    )


# ----------------------------------------------------------------------------
# Class Security

InitializeClass(System)
