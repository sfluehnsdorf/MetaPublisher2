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

__doc__ = """MetaPublisher2Tools Product

!TXT! module info

$Id: products/metapublisher2tools/MetaPublisher2Tools.py 2 2013-05-05 18:01:53Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.interfaces import IToolPluginBase
from Products.MetaPublisher2.library import BeforeDeleteException, ClassSecurityInfo, DTMLFile, Folder, InitializeClass, UserInterface, true, quote_plus


# ============================================================================
# Module Exports

__all__ = [
    'register_MetaPublisher2Tools',
]


# ==============================================================================
# MetaPublisher2Tools Product Class

class MetaPublisher2Tools(Folder):
    """MetaPublisher2Tools Product Class"""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # ZMI Attributes

    meta_type = 'MetaPublisher2 Tools'

    manage_options = (
        {'label': 'Warning!', 'action': 'warning_form'},
    ) + Folder.manage_options

    # ------------------------------------------------------------------------
    # ZMI Forms

    warning_form = DTMLFile('warning', globals())

    # ------------------------------------------------------------------------
    # ZMI Events

    def all_meta_types(self, interfaces=None):
        """Return list of containable object types"""

        interfaces = (interfaces and list(interfaces) or []) + [IToolPluginBase, ]
        return Folder.all_meta_types(self, interfaces)

    # ------------------------------------------------------------------------
    # Instance Identity

    security.declarePublic('get_MetaPublisher2Tools')

    def get_MetaPublisher2Tools(self):
        """Return this instance"""

        return self

    security.declarePublic('get_MetaPublisher2Tools_url')

    def get_MetaPublisher2Tools_url(self):
        """Return this instance's absolute url"""

        return self.absolute_url()

# ------------------------------------------------------------------------------
# initialize class security

InitializeClass(MetaPublisher2Tools)


# ==============================================================================
# MetaPublisher2Tools ZMI Constructor

add_MetaPublisher2Tools_form = DTMLFile('add', globals())


def add_MetaPublisher2Tools(self, id, title='Tools Folder', REQUEST=None):
    """ZMI constructor for MetaPublisher2Tools"""

    if not container_filter(self.this()):
        raise TypeError("Can't add a MetaPublisher2Tools Folder outside of a MetaPublisher2")

    id = str(id)
    title = str(title)

    instance = MetaPublisher2Tools(id)
    instance.id = id
    instance.title = title
    id = self._setObject(id, instance)

    if REQUEST:
        try:
            url_base = self.DestinationURL()
        except:
            url_base = REQUEST['URL1']
        url = '%s/%s?update_menu=1&manage_tabs_message=%s' % (
            url_base,
            quote_plus('New MetaPublisher2Tools "%s" created.' % id)
        )
        REQUEST.RESPONSE.redirect(url)


# ==============================================================================
# MetaPublisher2 Tools Content Filter

def container_filter(folder):

    if folder.meta_type == 'MetaPublisher2':
        return true


# ==============================================================================
# MetaPublisher2 Tools Registration

def register_MetaPublisher2Tools(context):

    try:
        context.registerClass(
            MetaPublisher2Tools,
            constructors=(
                ('add_MetaPublisher2Tools_form', add_MetaPublisher2Tools_form),
                ('add_MetaPublisher2Tools', add_MetaPublisher2Tools),
            ),
            icon='resources/icon/MetaPublisher2Folder.gif',
            container_filter=container_filter
        )

    except:
        context.registerClass(
            MetaPublisher2Tools,
            constructors=(
                ('add_MetaPublisher2Tools_form', add_MetaPublisher2Tools_form),
                ('add_MetaPublisher2Tools', add_MetaPublisher2Tools),
            ),
            icon='resources/icon/MetaPublisher2Folder.gif'
        )
