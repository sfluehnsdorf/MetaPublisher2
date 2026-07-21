"""MetaPublisher2 - Publisher Section.

Module providing a mix-in class for the MetaPublisher 2's Publisher section.
"""


from Products.MetaPublisher2.library.common import (
    ClassSecurityInfo, InitializeClass)

from audit import Audit
from caching import Caching
from designs import Designs
from frontends import Frontends
from languages import Languages
from renderer import Renderer
from widgets import Widgets


# ============================================================================
# Module Exports

__all__ = [
    'Publisher',
]


# ============================================================================
# Publisher Section Mix-In Class

class Publisher(
    Frontends, Widgets, Designs, Languages, Caching, Audit, Renderer
):
    """Publisher Section Mix-In Class."""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # Publisher ZMI Management Tabs

    manage_options = (
        {'label': 'Frontends', 'action': 'frontends_form'},
        {'label': 'Widgets', 'action': 'widgets_form'},
        {'label': 'Designs', 'action': 'designs_form'},
        {'label': 'Languages', 'action': 'languages_form'},
        {'label': 'Caching', 'action': 'caching_form'},
        {'label': 'Audit', 'action': 'audit_form'},
        {'label': 'Renderer', 'action': 'renderer_form'},
    )


# ----------------------------------------------------------------------------
# Class Security

InitializeClass(Publisher)
