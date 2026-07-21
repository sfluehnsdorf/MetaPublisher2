"""MetaPublisher2 ZMI."""


from Products.MetaPublisher2.library.application import permission_zmi
from Products.MetaPublisher2.library.common import (
    ClassSecurityInfo, DTMLFile, InitializeClass)


# ============================================================================
# Module Exports


__all__ = [
    'ZMI',
]


# ============================================================================
# MetaPublisher2 ZMI Mix-In Class

class ZMI:
    """MetaPublisher2 ZMI Mix-In Class."""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # Custom ZMI

    security.declareProtected(permission_zmi, 'manage_MetaPublisher2_header')

    manage_MetaPublisher2_header = DTMLFile('zmi_header', globals())

    security.declareProtected(permission_zmi, 'manage_MetaPublisher2_footer')

    manage_MetaPublisher2_footer = DTMLFile('zmi_footer', globals())

    security.declareProtected(permission_zmi, 'manage_MetaPublisher2_css')

    manage_MetaPublisher2_css = DTMLFile('zmi_css', globals())

    security.declareProtected(permission_zmi, 'manage_MetaPublisher2_js')

    manage_MetaPublisher2_js = DTMLFile('zmi_js', globals())


# ----------------------------------------------------------------------------
# Class Security


InitializeClass(ZMI)
