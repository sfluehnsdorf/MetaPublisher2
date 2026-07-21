"""MetaPublisher2 - Languages Component."""


from Products.MetaPublisher2.library.application import (
    permission_manage_designs)
from Products.MetaPublisher2.library.common import (
    ClassSecurityInfo, DTMLFile, InitializeClass)
from Products.MetaPublisher2.library.compatibility import show_future


# ============================================================================
# Module Exports

__all__ = [
    'Languages',
]


# ============================================================================
# Languages Component Mix-In Class

class Languages:
    """Languages Component Mix-In Class."""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # Languages ZMI Forms

    if show_future:

        security.declareProtected(permission_manage_designs, 'languages_form')

        languages_form = DTMLFile('languages', globals())


# ----------------------------------------------------------------------------
# Class Security

InitializeClass(Languages)

# TODO languages.py - implement
