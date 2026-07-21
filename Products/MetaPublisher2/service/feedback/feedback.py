"""MetaPublisher2 - Feedback Component.

Simple service providing access to the Web based feedback service for a variety
of types of feedback. The ZMI forms simply include the feedback service's web
pages on the MetaPublisher website at http://metapublisher.org.
"""


from Products.MetaPublisher2.library.application import permission_zmi
from Products.MetaPublisher2.library.common import (
    ClassSecurityInfo, DTMLFile, InitializeClass)


# ============================================================================
# Module Exports

__all__ = [
    'Feedback',
]


# ============================================================================
# Feedback Component Mix-In Class

class Feedback:
    """Feedback Component Mix-In Class."""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # Feedback ZMI

    security.declareProtected(permission_zmi, 'feedback_form')

    feedback_form = DTMLFile('feedback', globals())

    # ------------------------------------------------------------------------
    # Feedback Retrieval API

    security.declareProtected(permission_zmi, 'get_feedback_url')

    def get_feedback_url(self):
        """Return the URL for the online feedback service."""
        return self.get_setting('service_feedback_url')


# ----------------------------------------------------------------------------
# Class Security

InitializeClass(Feedback)

# !!! feedback.py - implement online feedback service
# !!! feedback.py - replace local form with online form (include via ajax?)
