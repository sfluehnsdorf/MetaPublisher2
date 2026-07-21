"""MetaPublisher2 - Inheritance Component."""


from Products.MetaPublisher2.library.application import (
    permission_access_configuration)
from Products.MetaPublisher2.library.common import (
    ClassSecurityInfo, DTMLFile, InitializeClass)
from Products.MetaPublisher2.library.compatibility import show_future


# ============================================================================
# Module Exports

__all__ = [
    'Inheritance',
]


# ==============================================================================
# Inheritance Component Mix-In Class

class Inheritance:
    """Inheritance Component Mix-In Class."""

    security = ClassSecurityInfo()

    # --------------------------------------------------------------------------
    # Inheritance ZMI

    if show_future:

        security.declareProtected(
            permission_access_configuration, 'inheritance_form')

        inheritance_form = DTMLFile('inheritance', globals())


# ------------------------------------------------------------------------------
# Class Security


InitializeClass(Inheritance)


# TODO inheritance.py - implement
