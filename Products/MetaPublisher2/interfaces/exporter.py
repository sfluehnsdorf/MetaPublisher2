"""MetaPublisher2 - Exporter Plugin Interface."""


from zope.interface import Interface


# ============================================================================
# Module Exports

__all__ = [
    'IExporterPluginBase',
]


# ============================================================================
# Exporter Plugin Base Interface

class IExporterPluginBase(Interface):
    """Exporter Plugin Base Interface."""

    pass

# TODO implement/exporter.py - implement
