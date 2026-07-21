"""MetaPublisher2 - Configuration Section.

Module providing a mix-in class for the MetaPublisher 2's Configuration
section.
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.library.common import (
    ClassSecurityInfo, InitializeClass)

from constraints import Constraints
from fields import Fields
from identifiers import Identifiers
from indexing import Indexing
from inheritance import Inheritance
from relations import Relations
from storages import Storages
from triggers import Triggers


# ============================================================================
# Module Exports

__all__ = [
    'Configuration',
]


# ============================================================================
# Configuration Section Mix-In Class

class Configuration(
    Storages, Fields, Identifiers, Constraints, Relations, Triggers,
    Inheritance, Indexing
):
    """Configuration Section Mix-In Class."""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # Configuration ZMI Management Tabs

    manage_options = (
        {'label': 'Storages', 'action': 'storages_form'},
        {'label': 'Fields', 'action': 'fields_form'},
        {'label': 'Identifiers', 'action': 'identifiers_form'},
        {'label': 'Constraints', 'action': 'constraints_form'},
        {'label': 'Relations', 'action': 'relations_form'},
        {'label': 'Triggers', 'action': 'triggers_form'},
        {'label': 'Inheritance', 'action': 'inheritance_form'},
        {'label': 'Indexing', 'action': 'indexing_form'},
    )


# ----------------------------------------------------------------------------
# Class Security

InitializeClass(Configuration)
