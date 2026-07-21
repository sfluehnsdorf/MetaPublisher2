"""MetaPublisher2 - Reports Component."""


from Products.MetaPublisher2.library.application import (
    permission_access_entries)
from Products.MetaPublisher2.library.common import (
    ClassSecurityInfo, DTMLFile, InitializeClass)


# ============================================================================
# Module Exports

__all__ = [
    'Reports',
]


# ============================================================================
# Reports Component Mix-In Class

class Reports:
    """Reports Component Mix-In Class."""

    security = ClassSecurityInfo()

    # -----------------------------------------------------------------------
    # Reports ZMI

    security.declareProtected(permission_access_entries, 'reports_form')

    reports_form = DTMLFile('reports', globals())


# ----------------------------------------------------------------------------
# Class Security


InitializeClass(Reports)
