"""MetaPublisher2 - Relations Component."""


from Products.MetaPublisher2.library.application import (
    permission_access_configuration, permission_change_configuration)
from Products.MetaPublisher2.library.common import (
    ClassSecurityInfo, DTMLFile, InitializeClass)
from Products.MetaPublisher2.library.compatibility import show_future


# ============================================================================
# Module Exports

__all__ = [
    'Relations',
]


# ==============================================================================
# Relations Component Mix-In Class

class Relations:
    """Relations Component Mix-In Class."""

    security = ClassSecurityInfo()

    # --------------------------------------------------------------------------
    # !TXT!

    if show_future:

        security.declareProtected(
            permission_access_configuration, 'relations_form')

        relations_form = DTMLFile('relations', globals())

        security.declareProtected(
            permission_change_configuration, 'add_relation_form')

        add_relation_form = DTMLFile('add_relation', globals())

        security.declareProtected(
            permission_change_configuration, 'delete_relations_form')

        delete_relations_form = DTMLFile('delete_relations', globals())

        security.declareProtected(
            permission_change_configuration, 'duplicate_relations_form')

        duplicate_relations_form = DTMLFile('duplicate_relations', globals())

        security.declareProtected(
            permission_change_configuration, 'edit_relation_form')

        edit_relation_form = DTMLFile('edit_relation', globals())

        security.declareProtected(
            permission_change_configuration, 'rename_relations_form')

        rename_relations_form = DTMLFile('rename_relations', globals())


# ------------------------------------------------------------------------------
# Class Security


InitializeClass(Relations)


# !!! relations.py - implement
#     relation types (move to base?): unidirectional, bidirectional, weighted,
#         conditional, 1:1, 1:m, m:1, m:n
#     The heart of the database consists of these primary components: Items,
#         Relations
#     An Item consists of:
#     - A unique ID
#     - A block of data, which can be any content-type, such as text/plain,
#       text/html, image/gif.
#     - A parent ID if it is a derivative of a previous Item
#     - Date of creation
#     - The number of times it has been accessed
#     - The times at which these accesses occured
#     A Relation consists of:
#     - A unique ID
#     - An item ID
#     - An second item ID that the first item ID is related to
#     - Date of relation creation
#     - The number of times it has been accessed
#     - The times at which these accesses occured
