"""MetaPublisher2 - Expression Functions Component."""


from Products.MetaPublisher2.library.common import (
    ClassSecurityInfo, InitializeClass)


# ============================================================================
# Module Exports


__all__ = [
    'Functions',
]


# ============================================================================
# Functions Component Mix-In Class


class Functions:
    """Functions Component Mix-In Class."""

    security = ClassSecurityInfo()


# ----------------------------------------------------------------------------
# Class Security


InitializeClass(Functions)


# TODO functions.py - implement
