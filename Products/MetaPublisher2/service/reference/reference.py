"""MetaPublisher2 - Reference Component."""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.library.application import permission_zmi
from Products.MetaPublisher2.library.common import (
    ClassSecurityInfo, DTMLFile, InitializeClass)
from Products.MetaPublisher2.library.compatibility import show_future


# ============================================================================
# Module Exports

__all__ = [
    'Reference',
]


# ============================================================================
# Reference Component Mix-In Class

class Reference:
    """Reference Component Mix-In Class."""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # Reference ZMI Forms

    if show_future:

        security.declareProtected(permission_zmi, 'reference_form')

        reference_form = DTMLFile('reference', globals())

        security.declareProtected(permission_zmi, 'reference_top_form')

        reference_top_form = DTMLFile(
            'reference_top', globals(), target='_parent')

    # ------------------------------------------------------------------------
    # Manual Retrieval API

    security.declareProtected(permission_zmi, 'get_reference_url')

    def get_reference_url(self):
        """Return the URL for the online reference service."""
        return self.get_setting('service_reference_url')


# ----------------------------------------------------------------------------
# Class Security

InitializeClass(Reference)

# TODO reference.py - implement online reference service
