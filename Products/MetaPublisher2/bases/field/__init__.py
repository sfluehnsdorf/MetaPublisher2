"""MetaPublisher2 - Field Plugin Base Initialisation."""


from field import FieldPluginBase
from legacyfield import LegacyFieldPlugin


# ============================================================================
# Module Exports

__all__ = [
    'FieldPluginBase',
    'LegacyFieldPlugin',
]


# !!! bases/field/__init__.py - import all field type bases and register
#     their autoregistries
