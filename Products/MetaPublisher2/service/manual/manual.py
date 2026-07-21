"""MetaPublisher2 - Manual Component.

Simple service providing access to the Web based manual for both end users and
developers. The ZMI forms simply include the manual's web pages on the
MetaPublisher website at http://metapublisher.org.
"""


from Products.MetaPublisher2.library.application import permission_zmi
from Products.MetaPublisher2.library.common import (
    ClassSecurityInfo, DTMLFile, InitializeClass)
from Products.MetaPublisher2.library.compatibility import show_future


# ============================================================================
# Module Exports

__all__ = [
    'Manual',
]


# ============================================================================
# Manual Component Mix-In Class

class Manual:
    """Manual Component Mix-In Class."""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # Manual ZMI

    if show_future:

        security.declareProtected(permission_zmi, 'manual_form')

        manual_form = DTMLFile('manual', globals())

        security.declareProtected(permission_zmi, 'manual_top_form')

        manual_top_form = DTMLFile('manual_top', globals(), target='_parent')

    # ------------------------------------------------------------------------
    # Manual Retrieval API

    security.declareProtected(permission_zmi, 'get_manual_url')

    def get_manual_url(self):
        """Return the URL for the online manual service."""
        return self.get_setting('service_manual_url')


# ----------------------------------------------------------------------------
# initialize class security

InitializeClass(Manual)

# TODO manual.py - implement online manual service
