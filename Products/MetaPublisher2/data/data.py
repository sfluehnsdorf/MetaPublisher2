"""MetaPublisher2 - Data Section.

Module providing a mix-in class for the MetaPublisher 2's Data section.
"""


from Products.MetaPublisher2.library.common import (
    ClassSecurityInfo, InitializeClass)

from entries import Entries
from exports import Exports
from expressions import Expressions
from imports import Imports
from queries import Queries
from reports import Reports
from search import Search
from transfers import Transfers


# ============================================================================
# Module Exports

__all__ = [
    'Data',
]


# ============================================================================
# Data Section Mix-In Class

class Data(
    Entries, Expressions, Reports, Search, Queries, Imports, Exports, Transfers
):
    """Data Section Mix-In Class."""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # Data ZMI Management Tabs

    manage_options = (
        {'label': 'Entries', 'action': 'entries_form'},
        {'label': 'Reports', 'action': 'reports_form'},
        {'label': 'Search', 'action': 'search_form'},
        {'label': 'Queries', 'action': 'queries_form'},
        {'label': 'Imports', 'action': 'imports_form'},
        {'label': 'Exports', 'action': 'exports_form'},
        {'label': 'Transfers', 'action': 'transfers_form'},
    )


# ----------------------------------------------------------------------------
# Class Security

InitializeClass(Data)
