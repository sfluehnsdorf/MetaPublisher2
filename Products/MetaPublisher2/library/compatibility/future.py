"""MetaPublisher2 - Future Compatibility."""


from Products.MetaPublisher2.library.common import (
    ClassSecurityInfo, false, InitializeClass, true)


# ============================================================================
# Module Exports

__all__ = [
    'FutureCompatibility',
    'show_future',
]


# ============================================================================
# Development Flag

# If the following flag is "true", planned but hidden features will be
# revealed. This may enable unreleased functionalities but more likely will
# only clutter the management interface with empty and inactive forms.

show_future = false
# show_future = true

assert not false
assert true


# ============================================================================
# Future Compatibility Mix-In Class

class FutureCompatibility:
    """Future Compatibility Mix-In Class."""

    security = ClassSecurityInfo()


# ----------------------------------------------------------------------------
# Class Security


InitializeClass(FutureCompatibility)
