"""MetaPublisher2 - Triggers Component."""


from Products.MetaPublisher2.library.application import (
    permission_access_configuration)
from Products.MetaPublisher2.library.common import (
    ClassSecurityInfo, DTMLFile, InitializeClass)
from Products.MetaPublisher2.library.compatibility import show_future


# ============================================================================
# Module Exports


__all__ = [
    'Triggers',
]


# ==============================================================================
# Triggers Component Mix-In Class

class Triggers:
    """Triggers Component Mix-In Class."""

    security = ClassSecurityInfo()

    # --------------------------------------------------------------------------
    # Trigger ZMI

    if show_future:

        security.declareProtected(
            permission_access_configuration, 'triggers_form')

        triggers_form = DTMLFile('triggers', globals())


# ------------------------------------------------------------------------------
# Class Security


InitializeClass(Triggers)


# TODO triggers.py - implement
