"""MetaPublisher2 - Product Class Repository."""


from metapublisher2 import register_MetaPublisher2
from metapublisher2designs import register_MetaPublisher2Designs
from metapublisher2frontends import register_MetaPublisher2Frontends
from metapublisher2languages import register_MetaPublisher2Languages
from metapublisher2tools import register_MetaPublisher2Tools
from metapublisher2widgets import register_MetaPublisher2Widgets


# ============================================================================
# Module Exports

__all__ = [
    'register_MetaPublisher2',
    'register_MetaPublisher2Designs',
    'register_MetaPublisher2Frontends',
    'register_MetaPublisher2Languages',
    'register_MetaPublisher2Tools',
    'register_MetaPublisher2Widgets',
]
