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

__doc__ = """MetaPublisher2Frontends Product

!TXT! module info

$Id: products/metapublisher2frontends/MetaPublisher2Frontends.py 5 2012-02-17 15:45:00Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.interfaces import IFrontendPluginBase
from Products.MetaPublisher2.library import BeforeDeleteException, ClassSecurityInfo, DTMLFile, Folder, InitializeClass, UserInterface, true, quote_plus


# ============================================================================
# Module Exports

__all__ = [
    'register_MetaPublisher2Frontends',
]


# ==============================================================================
# MetaPublisher2Frontends Product Class

class MetaPublisher2Frontends(Folder):
    """MetaPublisher2Frontends Product Class"""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # ZMI Attributes

    meta_type = 'MetaPublisher2 Frontends'

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

        interfaces = (interfaces and list(interfaces) or []) + [IFrontendPluginBase, ]
        return Folder.all_meta_types(self, interfaces)

    # ------------------------------------------------------------------------
    # Instance Identity

    security.declarePublic('get_MetaPublisher2Frontends')

    def get_MetaPublisher2Frontends(self):
        """Return this instance"""

        return self

    security.declarePublic('get_MetaPublisher2Frontends_url')

    def get_MetaPublisher2Frontends_url(self):
        """Return this instance's absolute url"""

        return self.absolute_url()

# ------------------------------------------------------------------------------
# initialize class security

InitializeClass(MetaPublisher2Frontends)


# ==============================================================================
# MetaPublisher2Frontends ZMI Constructor

add_MetaPublisher2Frontends_form = DTMLFile('add', globals())


def add_MetaPublisher2Frontends(self, id, title='Frontends Folder', REQUEST=None):
    """ZMI constructor for MetaPublisher2Frontends"""

    if not container_filter(self.this()):
        raise TypeError("Can't add a MetaPublisher2Frontends Folder outside of a MetaPublisher2")

    id = str(id)
    title = str(title)

    instance = MetaPublisher2Frontends(id)
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
            quote_plus('New MetaPublisher2Frontends "%s" created.' % id)
        )
        REQUEST.RESPONSE.redirect(url)


# ==============================================================================
# MetaPublisher2 Frontends Content Filter

def container_filter(folder):

    if folder.meta_type == 'MetaPublisher2':
        return true


# ==============================================================================
# MetaPublisher2 Frontends Registration

def register_MetaPublisher2Frontends(context):

    try:
        context.registerClass(
            MetaPublisher2Frontends,
            constructors=(
                ('add_MetaPublisher2Frontends_form', add_MetaPublisher2Frontends_form),
                ('add_MetaPublisher2Frontends', add_MetaPublisher2Frontends),
            ),
            icon='resources/icon/MetaPublisher2Folder.gif',
            container_filter=container_filter
        )

    except:
        context.registerClass(
            MetaPublisher2Frontends,
            constructors=(
                ('add_MetaPublisher2Frontends_form', add_MetaPublisher2Frontends_form),
                ('add_MetaPublisher2Frontends', add_MetaPublisher2Frontends),
            ),
            icon='resources/icon/MetaPublisher2Folder.gif'
        )
