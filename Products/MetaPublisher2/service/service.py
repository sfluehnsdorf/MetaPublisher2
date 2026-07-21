"""MetaPublisher2 - Service Section."""


from Products.MetaPublisher2.library.common import (
    ClassSecurityInfo, InitializeClass)

from assistant import Assistant
from community import Community
from feedback import Feedback
from help import Help
from manual import Manual
from reference import Reference
from release import Release


# ============================================================================
# Module Exports

__all__ = [
    'Service',
]


# ============================================================================
# Service Section Mix-In Class

class Service(
    Assistant, Release, Community, Manual, Help, Reference, Feedback
):
    """Service Section Mix-In Class."""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # Service ZMI Management Tabs

    manage_options = (
        {'label': 'Assistant', 'action': 'assistant_form'},
        {'label': 'Release', 'action': 'release_form'},
        {'label': 'Community', 'action': 'community_form'},
        {'label': 'Manual', 'action': 'manual_form'},
        {'label': 'Help', 'action': 'help_form'},
        {'label': 'Reference', 'action': 'reference_form'},
        {'label': 'Feedback', 'action': 'feedback_form'},
    )


# ----------------------------------------------------------------------------
# Class Security

InitializeClass(Service)
