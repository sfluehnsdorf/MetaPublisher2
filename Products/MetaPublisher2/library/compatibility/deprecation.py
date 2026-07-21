"""MetaPublisher2 - Deprecation Information."""


from logging import getLogger
from warnings import warn


# ============================================================================
# Module Exports

__all__ = [
    'deprecated_form',
    'deprecated_method',
]


# ============================================================================
# Logger Initialization

logger = getLogger('MetaPublisher2')


# ============================================================================
# Deprecated Forms

def deprecated_form(form_name):
    """Report use of a deprecated form."""
    message = (
        'The "%s" form is deprecated and will be removed in a future '
        'release!' % form_name)
    logger.info(message)
    warn(message, category=DeprecationWarning, stacklevel=2)


# ============================================================================
# Deprecated Methods

def deprecated_method(method_name):
    """Report use of a deprecated method."""
    message = (
        'The "%s" method is deprecated and will be removed in a future '
        'release!' % method_name)
    logger.info(message)
    warn(message, category=DeprecationWarning, stacklevel=2)
