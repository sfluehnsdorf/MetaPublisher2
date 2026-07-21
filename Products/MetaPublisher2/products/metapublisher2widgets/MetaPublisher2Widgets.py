"""MetaPublisher2Widgets Product."""


from Products.MetaPublisher2.interfaces import IWidgetPluginBase
from Products.MetaPublisher2.library.common import (
    ClassSecurityInfo, DTMLFile, Folder, InitializeClass, true, quote_plus)


# ============================================================================
# Module Exports

__all__ = [
    'register_MetaPublisher2Widgets',
]


# ============================================================================
# MetaPublisher2Widgets Product Class

class MetaPublisher2Widgets(Folder):
    """MetaPublisher2Widgets Product Class."""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # ZMI Attributes

    meta_type = 'MetaPublisher2 Widgets'

    manage_options = (
        {'label': 'Warning!', 'action': 'warning_form'},
    ) + Folder.manage_options

    # ------------------------------------------------------------------------
    # ZMI Forms

    warning_form = DTMLFile('warning', globals())

    # ------------------------------------------------------------------------
    # ZMI Events

    def all_meta_types(self, interfaces=None):
        """Return list of containable object types."""
        interfaces = (
            interfaces and
            list(interfaces) or
            []
        ) + [IWidgetPluginBase,]
        return Folder.all_meta_types(self, interfaces)

    # ------------------------------------------------------------------------
    # Instance Identity

    security.declarePublic('get_MetaPublisher2Widgets')

    def get_MetaPublisher2Widgets(self):
        """Return this instance."""
        return self

    security.declarePublic('get_MetaPublisher2Widgets_url')

    def get_MetaPublisher2Widgets_url(self):
        """Return this instance's absolute url."""
        return self.absolute_url()


# ------------------------------------------------------------------------------
# initialize class security

InitializeClass(MetaPublisher2Widgets)


# ==============================================================================
# MetaPublisher2Widgets ZMI Constructor

add_MetaPublisher2Widgets_form = DTMLFile('add', globals())


def add_MetaPublisher2Widgets(self, id, title='Widgets Folder', REQUEST=None):
    """Add new MetaPublisher2Widgets."""
    if not container_filter(self.this()):
        raise TypeError(
            "!TXT! Can't add a MetaPublisher2Widgets Folder outside of a "
            "MetaPublisher2")
    id = str(id)
    title = str(title)
    instance = MetaPublisher2Widgets(id)
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
            quote_plus('!TXT! New MetaPublisher2Widgets "%s" created.' % id)
        )
        REQUEST.RESPONSE.redirect(url)


# ==============================================================================
# MetaPublisher2 Widgets Content Filter

def container_filter(folder):
    """Ensure metatype of parent."""
    if folder.meta_type == 'MetaPublisher2':
        return true


# ==============================================================================
# MetaPublisher2 Widgets Registration

def register_MetaPublisher2Widgets(context):
    """Register MetaPublisher2Widgets Product."""
    try:
        context.registerClass(
            MetaPublisher2Widgets,
            constructors=(
                (
                    'add_MetaPublisher2Widgets_form',
                    add_MetaPublisher2Widgets_form),
                ('add_MetaPublisher2Widgets', add_MetaPublisher2Widgets),
            ),
            icon='resources/icon/MetaPublisher2Folder.gif',
            container_filter=container_filter
        )
    except Exception:
        context.registerClass(
            MetaPublisher2Widgets,
            constructors=(
                (
                    'add_MetaPublisher2Widgets_form',
                    add_MetaPublisher2Widgets_form),
                ('add_MetaPublisher2Widgets', add_MetaPublisher2Widgets),
            ),
            icon='resources/icon/MetaPublisher2Folder.gif'
        )
