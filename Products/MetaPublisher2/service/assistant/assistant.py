"""MetaPublisher2 - Assistant Component.

Guidance service that assists in configuring the MetaPublisher2 by leading the
user through the various steps. Users can select one of the three experience
levels "novice", "intermediate" and "expert". This customises the information
and the form of the presentation.
"""


from Products.MetaPublisher2.library.application import permission_manage
from Products.MetaPublisher2.library.common import (
    ClassSecurityInfo, DTMLFile, InitializeClass)
from Products.MetaPublisher2.library.compatibility import show_future


# ============================================================================
# Module Exports

__all__ = [
    'Assistant',
]


# ============================================================================
# Assistant Component Mix-In Class

class Assistant:
    """Assistant Component Mix-In Class."""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # Assistant ZMI Forms

    if show_future:

        security.declareProtected(permission_manage, 'assistant_form')

        assistant_form = DTMLFile('assistant', globals())


# ----------------------------------------------------------------------------
# Class Security

InitializeClass(Assistant)

# TODO assistant.py - implement
