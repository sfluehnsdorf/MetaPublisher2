"""MetaPublisher2 - Expression Sorters Component."""


from Products.MetaPublisher2.library.common import (
    ClassSecurityInfo, InitializeClass)


# ============================================================================
# Module Exports


__all__ = [
    'Sorters',
]


# ============================================================================
# Sorters Component Mix-In Class


class Sorters:
    """Sorters Component Mix-In Class."""

    security = ClassSecurityInfo()


# ----------------------------------------------------------------------------
# Class Security


InitializeClass(Sorters)


# TODO sorters.py - implement
