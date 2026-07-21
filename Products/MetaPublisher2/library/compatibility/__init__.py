"""MetaPublisher2 - Compatibility Library Initialisation.

To avoid incompatobilities with previous and future release of the
application, MetaPublisher2 provides wrappers and handlers for outdated and
upcoming resources. Calls to any such resource is logged by functions provided
by this module.
"""


from compatibility import (
    Compatibility, FutureCompatibility, HistoricalCompatibility,
    InterfacesFolder, TestError, deprecated_form, deprecated_method,
    show_future, standard_form_footer, standard_form_header)


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
