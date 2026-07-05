# -*- coding: iso-8859-15 -*-
# ============================================================================
#
#                         M e t a  P u b l i s h e r  2
#
# ----------------------------------------------------------------------------
# Copyright (c) 2002-2013, Sebastian Lühnsdorf - Web-Solutions and others
# For more information see the README.txt file or visit www.metapulisher.org
# ----------------------------------------------------------------------------
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).
#
# A copy of the ZPL should accompany this distribution.
#
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE
#
# ============================================================================

__doc__ = """MetaPublisher2 Interface Inititalisation

!TXT! module info

$Id: interfaces/__init__.py 5 2013-05-10 23:42:35Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


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


# !!! interfaces/ - from zope.interface import Attribute
# !!! interfaces/ - from zope.schema import Bool, BytesLine, List, Tuple, URI
