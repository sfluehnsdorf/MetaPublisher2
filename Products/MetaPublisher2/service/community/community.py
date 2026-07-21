"""MetaPublisher2 - Community Component.

Simple service providing access to the Web based community service. The ZMI
forms simply include the community service's web pages on the MetaPublisher
website at http://metapublisher.org.
"""


from Products.MetaPublisher2.library.application import permission_zmi
from Products.MetaPublisher2.library.common import (
    ClassSecurityInfo, DTMLFile, InitializeClass)
from Products.MetaPublisher2.library.compatibility import show_future


# ============================================================================
# Module Exports

__all__ = [
    'Community',
]


# ============================================================================
# Community Component Mix-In Class

class Community:
    """Community Component Mix-In Class."""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # Community ZMI

    if show_future:

        security.declareProtected(permission_zmi, 'community_form')

        community_form = DTMLFile('community', globals())

        security.declareProtected(permission_zmi, 'community_top_form')

        community_top_form = DTMLFile(
            'community_top', globals(), target='_parent')

    # ------------------------------------------------------------------------
    # Community Retrieval API

    security.declareProtected(permission_zmi, 'get_community_url')

    def get_community_url(self):
        """Return the URL for the online community service."""
        return self.get_setting('service_community_url')


# ----------------------------------------------------------------------------
# initialize class security

InitializeClass(Community)

# TODO community.py - implement online community service
