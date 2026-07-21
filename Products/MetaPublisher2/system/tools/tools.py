"""MetaPublisher2."""


from Products.MetaPublisher2.library.application import permission_manage
from Products.MetaPublisher2.library.common import (
    ClassSecurityInfo, DTMLFile, InitializeClass)
from Products.MetaPublisher2.library.compatibility import show_future


# ============================================================================
# Module Exports

__all__ = [
    'Tools',
]


# ============================================================================
# Tools Component Mix-In Class

class Tools:
    """Tools Component Mix-In Class."""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # Tools ZMI Forms

    if show_future:

        security.declareProtected(permission_manage, 'tools_form')

        tools_form = DTMLFile('tools', globals())


# ----------------------------------------------------------------------------
# Class Security

InitializeClass(Tools)

# TODO tools.py - implement
