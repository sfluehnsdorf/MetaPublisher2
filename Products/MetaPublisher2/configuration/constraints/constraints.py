"""MetaPublisher2 - Constraints Component."""


from Products.MetaPublisher2.library.application import (
    permission_access_configuration)
from Products.MetaPublisher2.library.common import (
    ClassSecurityInfo, DTMLFile, InitializeClass)


# ============================================================================
# Module Exports

__all__ = [
    'Constraints',
]


# ==============================================================================
# Constraints Component Mix-In Class

class Constraints:
    """Constraints Component Mix-In Class."""

    security = ClassSecurityInfo()

    # --------------------------------------------------------------------------
    # Indexing ZMI

    security.declareProtected(
        permission_access_configuration, 'constraints_form')

    constraints_form = DTMLFile('constraints', globals())


# ------------------------------------------------------------------------------
# Class Security


InitializeClass(Constraints)


# !!! constraints.py - implement
