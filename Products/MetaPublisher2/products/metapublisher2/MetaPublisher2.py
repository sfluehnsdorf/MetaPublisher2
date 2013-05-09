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

__doc__ = """MetaPublisher 2 Product

The MetaPublisher 2 Product is an application made up of a range of sections
with components including...

- Data: for retrieving and mutating arbitrary data of storages and entrysets

- Configuration: for configuring and accessing data storages, fields and
  related services

- Publisher: for defining and rendering user interfaces, including forms for
  data managemenbt based on the configuration

- System: for running integrity tests, managing and sharing presets and for
  managing user profiles and plugins

- Service: for retrieving release information, for accessing the user &
  developer manual and for sending feedback

The application can be managed through the Web by Zope's Management Interface,
through an extensive API or, if desired through a user generated public
interface.

$Id: products/metapublisher2/MetaPublisher2.py 16 2013-05-08 22:55:49Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.configuration import Configuration
from Products.MetaPublisher2.data import Data
from Products.MetaPublisher2.library import ClassSecurityInfo, Compatibility, DTMLFile, Folder, InitializeClass, JSONDict, MultiTabs, quote_plus, UserInterface, XMLDict
from Products.MetaPublisher2.publisher import Publisher
from Products.MetaPublisher2.service import Service
from Products.MetaPublisher2.system import System

# !!! MetaPublisher2.py - remove DEV before release
try:
    from Products.MetaPublisher2.DEV import DEV
except:
    class DEV:
        manage_options = ()

from Products.MetaPublisher2.products.metapublisher2designs.MetaPublisher2Designs import add_MetaPublisher2Designs
from Products.MetaPublisher2.products.metapublisher2frontends.MetaPublisher2Frontends import add_MetaPublisher2Frontends
from Products.MetaPublisher2.products.metapublisher2languages.MetaPublisher2Languages import add_MetaPublisher2Languages
from Products.MetaPublisher2.products.metapublisher2tools.MetaPublisher2Tools import add_MetaPublisher2Tools
from Products.MetaPublisher2.products.metapublisher2widgets.MetaPublisher2Widgets import add_MetaPublisher2Widgets


# ============================================================================
# Module Exports

__all__ = [
    'register_MetaPublisher2',
]


# ============================================================================
# MetaPublisher2 Product Class

# !!! MetaPublisher2.py - remove DEV before release
class MetaPublisher2(Data, Configuration, Publisher, System, Service, DEV, JSONDict, XMLDict, Compatibility, UserInterface, MultiTabs, Folder):
    """!TXT! MetaPublisher2 Product Class"""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # Application Attributes

    default_batch_size = 10

    # --------------------------------------------------------------------------
    # ZMI Attributes

    meta_type = 'MetaPublisher2'

    # !!! MetaPublisher2.py - remove DEV before release

    manage_options = (
        {'label': 'Data', 'action': '', 'sub': Data.manage_options, },
        {'label': 'Configuration', 'action': '', 'sub': Configuration.manage_options, },
        {'label': 'Publisher', 'action': '', 'sub': Publisher.manage_options, },
        {'label': 'System', 'action': '', 'sub': System.manage_options, },
        {'label': 'Service', 'action': '', 'sub': Service.manage_options, },
        {'label': 'Zope', 'action': '', 'sub': Folder.manage_options, },
        {'label': 'DEV', 'action': '', 'sub': DEV.manage_options, },
    )

    _properties = Folder._properties + (
        {
            'id': 'default_batch_size',
            'type': 'int',
            'label': 'Default Batch Size'
        },
    )

    # --------------------------------------------------------------------------
    # ZMI Events

    def manage_afterAdd(self, item, container):
        """!TXT! Handle creation event"""

        # initialize profiles
        self.init_profiles()

    def __setstate__(self, state):
        """!TXT! Handle startup event"""

        Folder.inheritedAttribute('__setstate__')(self, state)

        # initialize profiles
        if not hasattr(self, '_Profiles__profiles'):
            self.init_profiles()

        # create missing new folders
        ids = self.objectIds()
        if not 'designs' in ids:
            add_MetaPublisher2Designs(self, 'designs')
        if not 'frontends' in ids:
            add_MetaPublisher2Frontends(self, 'frontends')
        if not 'languages' in ids:
            add_MetaPublisher2Languages(self, 'languages')
        if not 'tools' in ids:
            add_MetaPublisher2Tools(self, 'tools')
        if not 'widgets' in ids:
            add_MetaPublisher2Widgets(self, 'widgets')

        # move frontends from legacy location into frontends folder
        if 'interfaces' in ids and self.interfaces.meta_type == 'InterfacesFolder':
            try:
                if self.interfaces.objectIds():
                    clipboard = self.interfaces.manage_copyObjects(self.interfaces.objectIds())
                    self.frontends.manage_pasteObjects(clipboard)
                self.manage_delObjects('interfaces')
            except:
                pass

    # ------------------------------------------------------------------------
    # Instance Identity

    security.declarePublic('get_MetaPublisher2')

    def get_MetaPublisher2(self):
        """!TXT! Return this instance"""

        return self

    security.declarePublic('get_MetaPublisher2_url')

    def get_MetaPublisher2_url(self):
        """!TXT! Return this instance's absolute url"""

        return self.absolute_url()

# ----------------------------------------------------------------------------
# Class Security

InitializeClass(MetaPublisher2)


# ============================================================================
# MetaPublisher2 Constructor

add_MetaPublisher2_form = DTMLFile('add', globals())


def add_MetaPublisher2(self, id, title='', presets=[], REQUEST=None):
    """!TXT! MetaPublisher2 Constructor"""

    id = str(id)
    title = str(title)

    instance = MetaPublisher2(id)
    instance.title = title
    id = self._setObject(id, instance)
    metapublisher2 = self._getOb(id)

    add_MetaPublisher2Designs(metapublisher2, 'designs')
    add_MetaPublisher2Frontends(metapublisher2, 'frontends')
    add_MetaPublisher2Languages(metapublisher2, 'languages')
    add_MetaPublisher2Tools(metapublisher2, 'tools')
    add_MetaPublisher2Widgets(metapublisher2, 'widgets')

    if presets:
        raise NotImplemented("!TXT! Preset initialization not yet implemented!")

    if REQUEST is not None:
        try:
            url = self.DestinationURL()
        except:
            url = REQUEST['URL1']
        REQUEST.RESPONSE.redirect('%s/manage_main?update_menu=1&manage_tabs_message=%s' % (
            url, quote_plus('!TXT! New MetaPublisher2 "%s" created.' % id)
        ))


# ============================================================================
# MetaPublisher2 Product Registration

def register_MetaPublisher2(context):
    """!TXT! MetaPublisher2 Product Registration"""

    context.registerClass(
        MetaPublisher2,
        meta_type='MetaPublisher2',
        constructors=(
            add_MetaPublisher2_form,
            add_MetaPublisher2,
        ),
        icon='resources/icon/MetaPublisher2.gif'
    )
