"""MetaPublisher2Tools Product."""


from Products.MetaPublisher2.interfaces import IToolPluginBase
from Products.MetaPublisher2.library.common import (
    ClassSecurityInfo, DTMLFile, Folder, InitializeClass, true, quote_plus)


# ============================================================================
# Module Exports

__all__ = [
    'register_MetaPublisher2Tools',
]


# ==============================================================================
# MetaPublisher2Tools Product Class

class MetaPublisher2Tools(Folder):
    """!TXT! MetaPublisher2Tools Product Class."""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # ZMI Attributes

    meta_type = 'MetaPublisher2 Tools'

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
            interfaces and list(interfaces) or []
        ) + [IToolPluginBase]
        return Folder.all_meta_types(self, interfaces)

    # ------------------------------------------------------------------------
    # Instance Identity

    security.declarePublic('get_MetaPublisher2Tools')

    def get_MetaPublisher2Tools(self):
        """!TXT! Return this instance."""
        return self

    security.declarePublic('get_MetaPublisher2Tools_url')

    def get_MetaPublisher2Tools_url(self):
        """!TXT! Return this instance's absolute url."""
        return self.absolute_url()


# ------------------------------------------------------------------------------
# initialize class security

InitializeClass(MetaPublisher2Tools)


# ==============================================================================
# MetaPublisher2Tools ZMI Constructor

add_MetaPublisher2Tools_form = DTMLFile('add', globals())


def add_MetaPublisher2Tools(self, id, title='Tools Folder', REQUEST=None):
    """Add new MetaPublisher2Tools."""
    if not container_filter(self.this()):
        raise TypeError(
            "!TXT! Can't add a MetaPublisher2Tools Folder outside of a "
            "MetaPublisher2")
    id = str(id)
    title = str(title)
    instance = MetaPublisher2Tools(id)
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
            quote_plus('!TXT! New MetaPublisher2Tools "%s" created.' % id)
        )
        REQUEST.RESPONSE.redirect(url)


# ==============================================================================
# MetaPublisher2 Tools Content Filter

def container_filter(folder):
    """Ensure metatype of parent."""
    if folder.meta_type == 'MetaPublisher2':
        return true


# ==============================================================================
# MetaPublisher2 Tools Registration

def register_MetaPublisher2Tools(context):
    """Register MetaPublisher2Tools Product."""
    try:
        context.registerClass(
            MetaPublisher2Tools,
            constructors=(
                ('add_MetaPublisher2Tools_form', add_MetaPublisher2Tools_form),
                ('add_MetaPublisher2Tools', add_MetaPublisher2Tools),
            ),
            icon='resources/icon/MetaPublisher2Folder.gif',
            container_filter=container_filter
        )
    except Exception:
        context.registerClass(
            MetaPublisher2Tools,
            constructors=(
                ('add_MetaPublisher2Tools_form', add_MetaPublisher2Tools_form),
                ('add_MetaPublisher2Tools', add_MetaPublisher2Tools),
            ),
            icon='resources/icon/MetaPublisher2Folder.gif'
        )
