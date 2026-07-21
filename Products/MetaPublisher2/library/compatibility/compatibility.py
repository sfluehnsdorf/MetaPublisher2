"""MetaPublisher2 - Compatibility Library.

To ensure to continued operation of deprecated resources, this module provides
wrappers and handlers for these outdated resources. It also provides an API
for logging calls to deprecated resources.
"""


from Products.MetaPublisher2.library.common import (
    ClassSecurityInfo, InitializeClass)

from deprecation import deprecated_form, deprecated_method
from future import FutureCompatibility, show_future
from historical import (
    HistoricalCompatibility, InterfacesFolder, standard_form_footer,
    standard_form_header, TestError)


# ============================================================================
# Module Exports


__all__ = [
    'Compatibility',
    'FutureCompatibility',
    'HistoricalCompatibility',
    'InterfacesFolder',
    'TestError',
    'deprecated_form',
    'deprecated_method',
    'show_future',
    'standard_form_footer',
    'standard_form_header',
]


# ============================================================================
# Compatibility Mix-In Class

class Compatibility(FutureCompatibility, HistoricalCompatibility):
    """Compatibility Mix-In Class."""

    security = ClassSecurityInfo()


# ----------------------------------------------------------------------------
# Class Security


InitializeClass(Compatibility)
