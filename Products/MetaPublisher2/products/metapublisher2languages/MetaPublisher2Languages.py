"""MetaPublisher2Languages Product."""


from Products.MetaPublisher2.interfaces import ILanguagePluginBase
from Products.MetaPublisher2.library.common import (
    ClassSecurityInfo, DTMLFile, Folder, InitializeClass, true, quote_plus)


# ============================================================================)
# Module Exports

__all__ = [
    'register_MetaPublisher2Languages',
]


# =============================================================================
# MetaPublisher2Languages Product Class

class MetaPublisher2Languages(Folder):
    """Add new MetaPublisher2Languages."""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # ZMI Attributes

    meta_type = 'MetaPublisher2 Languages'

    manage_options = (
        {'label': 'Warning!', 'action': 'warning_form'},
    ) + Folder.manage_options

    # ------------------------------------------------------------------------
    # ZMI Forms

    warning_form = DTMLFile('warning', globals())

    # ------------------------------------------------------------------------
    # ZMI Events

    def all_meta_types(self, interfaces=None):
        """!TXT! Return list of containable object types."""
        interfaces = (
            interfaces and
            list(interfaces) or
            []
        ) + [ILanguagePluginBase]
        return Folder.all_meta_types(self, interfaces)

    # ------------------------------------------------------------------------
    # Instance Identity

    security.declarePublic('get_MetaPublisher2Languages')

    def get_MetaPublisher2Languages(self):
        """!TXT! Return this instance."""
        return self

    security.declarePublic('get_MetaPublisher2Languages_url')

    def get_MetaPublisher2Languages_url(self):
        """!TXT! Return this instance's absolute url."""
        return self.absolute_url()


# ------------------------------------------------------------------------------
# initialize class security

InitializeClass(MetaPublisher2Languages)


# =============================================================================
# MetaPublisher2Languages ZMI Constructor

add_MetaPublisher2Languages_form = DTMLFile('add', globals())


def add_MetaPublisher2Languages(
    self, id, title='Languages Folder', REQUEST=None
):
    """!TXT! ZMI constructor for MetaPublisher2Languages."""
    if not container_filter(self.this()):
        raise TypeError(
            "!TXT! Can't add a MetaPublisher2Languages Folder outside of a "
            "MetaPublisher2")
    id = str(id)
    title = str(title)
    instance = MetaPublisher2Languages(id)
    instance.id = id
    instance.title = title
    id = self._setObject(id, instance)
    if REQUEST:
        try:
            url = self.DestinationURL()
        except Exception:
            url = REQUEST['URL1']
        url = '%s/manage_main?update_menu=1&manage_tabs_message=%s' % (
            url,
            quote_plus('!TXT! New MetaPublisher2Languages "%s" created.' % id)
        )
        REQUEST.RESPONSE.redirect(url)


# =============================================================================
# MetaPublisher2 Languages Content Filter

def container_filter(folder):
    """Ensure metatype of parent."""
    if folder.meta_type == 'MetaPublisher2':
        return true


# =============================================================================
# MetaPublisher2 Languages Registration

def register_MetaPublisher2Languages(context):
    """Register MetaPublisher2Languages Product."""
    try:
        context.registerClass(
            MetaPublisher2Languages,
            constructors=(
                (
                    'add_MetaPublisher2Languages_form',
                    add_MetaPublisher2Languages_form),
                ('add_MetaPublisher2Languages', add_MetaPublisher2Languages),
            ),
            icon='resources/icon/MetaPublisher2Folder.gif',
            container_filter=container_filter
        )
    except Exception:
        context.registerClass(
            MetaPublisher2Languages,
            constructors=(
                (
                    'add_MetaPublisher2Languages_form',
                    add_MetaPublisher2Languages_form),
                ('add_MetaPublisher2Languages', add_MetaPublisher2Languages),
            ),
            icon='resources/icon/MetaPublisher2Folder.gif'
        )
