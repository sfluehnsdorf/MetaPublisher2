"""MetaPublisher - Help Component.

The online help service provides access to contextual documentation of the
MetaPublisher2. As Zope's built-in contextual help system is not always fully
supported beginning with release Zope 2.12, this is a useful alternative
interface to access these help pages.

NOTE: Future releases of MetaPublisher2 will provide a replacement for Zope's
HelpSys module to reintegrate the contextual help into the ZMI, introducing
new features such as structured help pages and automatic API reference
generation.
"""


from Products.MetaPublisher2.library.application import permission_zmi
from Products.MetaPublisher2.library.common import (
    ClassSecurityInfo, DTMLFile, InitializeClass)
from Products.MetaPublisher2.library.compatibility import show_future


# ============================================================================
# Module Exports

__all__ = [
    'Help',
]


# ============================================================================
# Help Component Mix-In Class

class Help:
    """Help Component Mix-In Class."""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # Help ZMI

    if show_future:

        security.declareProtected(permission_zmi, 'help_form')

        help_form = DTMLFile('help', globals())

        security.declareProtected(permission_zmi, 'help_main_form')

        help_main_form = DTMLFile('help_main', globals())

        security.declareProtected(permission_zmi, 'help_top_form')

        help_top_form = DTMLFile('help_top', globals(), target='_parent')


# ----------------------------------------------------------------------------
# Class Security

InitializeClass(Help)

# !!! help.py - determine if to implement
# TODO help.py - implement
