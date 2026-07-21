"""MetaPublisher2 - MetaPublisher2 Interface Inititalisation."""


# ============================================================================
# Module Imports

from cache import ICachePluginBase
from constraint import IConstraintPluginBase
from design import IDesignPluginBase
from entry import IEntry
from entrycontainer import IEntryContainer
from entryfield import IEntryField
from entryset import IEntrySet
from event import IEventPluginBase
from exporter import IExporterPluginBase
from expression import IExpressionPluginBase
from field import IFieldPluginBase
from frontend import IFrontendPluginBase
from identifier import IIdentifierPluginBase
from importer import IImporterPluginBase
from indexer import IIndexerPluginBase
from language import ILanguagePluginBase
from plugin import IPluginBase
from preset import IPresetPluginBase
from storage import IStoragePluginBase
from tool import IToolPluginBase
from trigger import ITriggerPluginBase
from widget import IWidgetPluginBase


# ============================================================================
# Module Exports

__all__ = [
    'ICachePluginBase',
    'IConstraintPluginBase',
    'IDesignPluginBase',
    'IEntry',
    'IEntryContainer',
    'IEntryField',
    'IEntrySet',
    'IEventPluginBase',
    'IExporterPluginBase',
    'IExpressionPluginBase',
    'IFieldPluginBase',
    'IFrontendPluginBase',
    'IIdentifierPluginBase',
    'IImporterPluginBase',
    'IIndexerPluginBase',
    'ILanguagePluginBase',
    'IPluginBase',
    'IPresetPluginBase',
    'IStoragePluginBase',
    'IToolPluginBase',
    'ITriggerPluginBase',
    'IWidgetPluginBase',
]


# TODO: interfaces/ - from zope.interface import Attribute
# TODO: interfaces/ - from zope.schema import Bool, BytesLine, List, Tuple, URI
