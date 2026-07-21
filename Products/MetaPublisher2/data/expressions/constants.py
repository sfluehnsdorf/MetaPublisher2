"""MetaPublisher2 - Expression Constants Component."""


from Products.MetaPublisher2.library.common import (
    ClassSecurityInfo, InitializeClass)


# ============================================================================
# Module Exports


__all__ = [
    'Constants',
]


# ============================================================================
# Constants Component Mix-In Class


class Constants:
    """Constants Component Mix-In Class."""

    security = ClassSecurityInfo()


# ----------------------------------------------------------------------------
# Class Security


InitializeClass(Constants)


# TODO constants.py - implement
