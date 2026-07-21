"""MetaPublisher2 - Application Paths."""


from Products.MetaPublisher2.library.common import split


# ============================================================================
# Module Exports

__all__ = [
    'basepath',
]


# ============================================================================
# Product Basepath

basepath = split(split(split(__file__)[0])[0])[0]
