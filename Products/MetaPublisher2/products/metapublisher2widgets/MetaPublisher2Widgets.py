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

__doc__ = """MetaPublisher2Widgets Product

$Id: products/metapublisher2widgets/MetaPublisher2Widgets.py 1 2012-02-17 15:45:00Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.interfaces import IWidgetPluginBase
from Products.MetaPublisher2.library import BeforeDeleteException, ClassSecurityInfo, DTMLFile, Folder, InitializeClass, UserInterface, true, quote_plus


# ============================================================================
# Module Exports

__all__ = [
    'register_MetaPublisher2Widgets',
]


# ============================================================================
# MetaPublisher2Widgets Product Class

class MetaPublisher2Widgets(Folder):
    """MetaPublisher2Widgets Product Class"""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # ZMI Attributes

    meta_type = 'MetaPublisher2 Widgets'

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

        interfaces = (interfaces and list(interfaces) or []) + [IWidgetPluginBase, ]
        return Folder.all_meta_types(self, interfaces)

    # ------------------------------------------------------------------------
    # Instance Identity

    security.declarePublic('get_MetaPublisher2Widgets')

    def get_MetaPublisher2Widgets(self):
        """Return this instance"""

        return self

    security.declarePublic('get_MetaPublisher2Widgets_url')

    def get_MetaPublisher2Widgets_url(self):
        """Return this instance's absolute url"""

        return self.absolute_url()

# ------------------------------------------------------------------------------
# initialize class security

InitializeClass(MetaPublisher2Widgets)


# ==============================================================================
# MetaPublisher2Widgets ZMI Constructor

add_MetaPublisher2Widgets_form = DTMLFile('add', globals())


def add_MetaPublisher2Widgets(self, id, title='Widgets Folder', REQUEST=None):
    """ZMI constructor for MetaPublisher2Widgets"""

    if not container_filter(self.this()):
        raise TypeError("Can't add a MetaPublisher2Widgets Folder outside of a MetaPublisher2")

    id = str(id)
    title = str(title)

    instance = MetaPublisher2Widgets(id)
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
            quote_plus('New MetaPublisher2Widgets "%s" created.' % id)
        )
        REQUEST.RESPONSE.redirect(url)


# ==============================================================================
# MetaPublisher2 Widgets Content Filter

def container_filter(folder):

    if folder.meta_type == 'MetaPublisher2':
        return true


# ==============================================================================
# MetaPublisher2 Widgets Registration

def register_MetaPublisher2Widgets(context):

    try:
        context.registerClass(
            MetaPublisher2Widgets,
            constructors=(
                ('add_MetaPublisher2Widgets_form', add_MetaPublisher2Widgets_form),
                ('add_MetaPublisher2Widgets', add_MetaPublisher2Widgets),
            ),
            icon='resources/icon/MetaPublisher2Folder.gif',
            container_filter=container_filter
        )

    except:
        context.registerClass(
            MetaPublisher2Widgets,
            constructors=(
                ('add_MetaPublisher2Widgets_form', add_MetaPublisher2Widgets_form),
                ('add_MetaPublisher2Widgets', add_MetaPublisher2Widgets),
            ),
            icon='resources/icon/MetaPublisher2Folder.gif'
        )
