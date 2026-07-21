"""MetaPublisher2 - Expression Groupers Component."""


from Products.MetaPublisher2.library.common import (
    ClassSecurityInfo, InitializeClass)


# ============================================================================
# Module Exports


__all__ = [
    'Groupers',
]


# ============================================================================
# Groupers Components Mix-In Class


class Groupers:
    """Groupers Component Mix-In Class."""

    security = ClassSecurityInfo()


# ----------------------------------------------------------------------------
# Class Security


InitializeClass(Groupers)


# TODO groupers.py - implement
