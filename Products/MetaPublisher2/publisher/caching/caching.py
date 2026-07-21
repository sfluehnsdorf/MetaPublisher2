"""MetaPublisher2 - Caching Component."""


from Products.MetaPublisher2.library.application import (
    permission_manage_frontends)
from Products.MetaPublisher2.library.common import (
    ClassSecurityInfo, DTMLFile, InitializeClass)
from Products.MetaPublisher2.library.compatibility import show_future


# ============================================================================
# Module Exports

__all__ = [
    'Caching',
]


# ============================================================================
# Caching Component Mix-In Class

class Caching:
    """Caching Component Mix-In Class."""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # Caching ZMI Forms

    if show_future:

        security.declareProtected(permission_manage_frontends, 'caching_form')

        caching_form = DTMLFile('caching', globals())


# ----------------------------------------------------------------------------
# Class Security

InitializeClass(Caching)

# TODO caching.py - implement
