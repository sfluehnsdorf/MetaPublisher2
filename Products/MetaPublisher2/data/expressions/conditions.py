"""MetaPublisher2 - Expression Conditions Component."""


from Products.MetaPublisher2.library.common import (
    ClassSecurityInfo, InitializeClass)


# ============================================================================
# Module Exports


__all__ = [
    'Conditions',
]


# ============================================================================
# Conditions Component Mix-In Class


class Conditions:
    """Conditions Component Mix-In Class."""

    security = ClassSecurityInfo()


# ----------------------------------------------------------------------------
# Class Security


InitializeClass(Conditions)


# TODO conditions.py - implement
