"""MetaPublisher2 - Expression Aggregates Component."""


from Products.MetaPublisher2.library.common import (
    ClassSecurityInfo, InitializeClass)


# ============================================================================
# Module Exports


__all__ = [
    'Aggregates',
]


# ============================================================================
# Aggregates Component Mix-In Class


class Aggregates:
    """Aggregates Component Mix-In Class."""

    security = ClassSecurityInfo()


# ----------------------------------------------------------------------------
# Class Security


InitializeClass(Aggregates)


# TODO aggregates.py - implement
