"""MetaPublisher2 - Audit Component."""


from Products.MetaPublisher2.library.application import (
    permission_manage_frontends)
from Products.MetaPublisher2.library.common import (
    ClassSecurityInfo, DTMLFile, InitializeClass)
from Products.MetaPublisher2.library.compatibility import show_future


# ============================================================================
# Module Exports

__all__ = [
    'Audit',
]


# ============================================================================
# Audit Component Mix-In Class

class Audit:
    """Audit Component Mix-In Class."""

    security = ClassSecurityInfo()

    # --------------------------------------------------------------------------
    # Audit ZMI Forms

    if show_future:

        security.declareProtected(permission_manage_frontends, 'audit_form')

        audit_form = DTMLFile('audit', globals())


# ------------------------------------------------------------------------------
# Class Audit

InitializeClass(Audit)

# TODO audit.py - implement
#      The Audit displays a summary of Permission settings to help find
#      security problems), security map, permissions, roles, ownership, ...
#      owners, permissions, proxies, roles, users
