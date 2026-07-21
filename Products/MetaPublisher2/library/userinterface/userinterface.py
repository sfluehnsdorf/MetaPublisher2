"""MetaPublisher2 User Interface."""


from Products.MetaPublisher2.library.application import permission_zmi
from Products.MetaPublisher2.library.common import (
    ClassSecurityInfo, false, InitializeClass, quote_plus, url_quote)

from dialogs import Dialogs
from formlets import Formlets
from resources import Resources
from zmi import ZMI


# ============================================================================
# Module Exports


__all__ = [
    'UserInterface',
    'permission_zmi',
    'quote_plus',
]


# ============================================================================
# MetaPublisher2 User Interface Mix-In Class


class UserInterface(Formlets, Dialogs, Resources, ZMI):
    """MetaPublisher2 User Interface Mix-In Class."""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # ZMI Redirect Helper

    def redirect(self, REQUEST, url, message='', update_menu=false, **kw):
        """!TXT! Redirect to the specified URL."""
        if REQUEST:
            if message:
                kw['manage_tabs_message'] = message
            if update_menu:
                kw['update_menu'] = 1
            REQUEST.RESPONSE.redirect('%s/%s%s' % (
                self.get_MetaPublisher2_url(), url,
                kw and
                ('?' + '&'.join(map(
                    lambda item: '%s=%s' % (
                        url_quote(item[0]), url_quote(item[1])),
                    kw.items()
                ))) or
                ''
            ))


# ----------------------------------------------------------------------------
# Class Security


InitializeClass(UserInterface)


# !!! userinterface.py - add error widget for form error handling
