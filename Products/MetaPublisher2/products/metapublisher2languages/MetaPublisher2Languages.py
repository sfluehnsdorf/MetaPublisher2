# -*- coding: iso-8859-15 -*-
# ============================================================================
#
#                         M e t a  P u b l i s h e r  2
#
# ----------------------------------------------------------------------------
# Copyright (c) 2002-2013, Sebastian L�hnsdorf - Web-Solutions and others
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

__doc__ = """MetaPublisher2Languages Product

!TXT! module info

$Id: products/metapublisher2languages/MetaPublisher2Languages.py 10 2013-05-14 22:16:41Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.interfaces import ILanguagePluginBase
from Products.MetaPublisher2.library import BeforeDeleteException, ClassSecurityInfo, DTMLFile, Folder, InitializeClass, UserInterface, true, quote_plus


# ============================================================================
# Module Exports

__all__ = [
    'register_MetaPublisher2Languages',
]


# ==============================================================================
# MetaPublisher2Languages Product Class

class MetaPublisher2Languages(Folder):
    """!TXT! MetaPublisher2Languages Product Class"""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # ZMI Attributes

    meta_type = 'MetaPublisher2 Languages'

    manage_options = (
        {'label': 'Warning!', 'action': 'warning_form'},
    ) + Folder.manage_options

    # ------------------------------------------------------------------------
    # ZMI Forms

    warning_form = DTMLFile('warning', globals())

    # ------------------------------------------------------------------------
    # ZMI Events

    def all_meta_types(self, interfaces=None):
        """!TXT! Return list of containable object types"""

        interfaces = (interfaces and list(interfaces) or []) + [ILanguagePluginBase, ]
        return Folder.all_meta_types(self, interfaces)

    # ------------------------------------------------------------------------
    # Instance Identity

    security.declarePublic('get_MetaPublisher2Languages')

    def get_MetaPublisher2Languages(self):
        """!TXT! Return this instance"""

        return self

    security.declarePublic('get_MetaPublisher2Languages_url')

    def get_MetaPublisher2Languages_url(self):
        """!TXT! Return this instance's absolute url"""

        return self.absolute_url()

# ------------------------------------------------------------------------------
# initialize class security

InitializeClass(MetaPublisher2Languages)


# ==============================================================================
# MetaPublisher2Languages ZMI Constructor

add_MetaPublisher2Languages_form = DTMLFile('add', globals())


def add_MetaPublisher2Languages(self, id, title='Languages Folder', REQUEST=None):
    """!TXT! ZMI constructor for MetaPublisher2Languages"""

    if not container_filter(self.this()):
        raise TypeError("!TXT! Can't add a MetaPublisher2Languages Folder outside of a MetaPublisher2")

    id = str(id)
    title = str(title)

    instance = MetaPublisher2Languages(id)
    instance.id = id
    instance.title = title
    id = self._setObject(id, instance)

    if REQUEST:
        try:
            url = self.DestinationURL()
        except:
            url = REQUEST['URL1']
        url = '%s/manage_main?update_menu=1&manage_tabs_message=%s' % (
            url,
            quote_plus('!TXT! New MetaPublisher2Languages "%s" created.' % id)
        )
        REQUEST.RESPONSE.redirect(url)


# ==============================================================================
# MetaPublisher2 Languages Content Filter

def container_filter(folder):
    """!TXT!"""

    if folder.meta_type == 'MetaPublisher2':
        return true


# ==============================================================================
# MetaPublisher2 Languages Registration

def register_MetaPublisher2Languages(context):
    """!TXT!"""

    try:
        context.registerClass(
            MetaPublisher2Languages,
            constructors=(
                ('add_MetaPublisher2Languages_form', add_MetaPublisher2Languages_form),
                ('add_MetaPublisher2Languages', add_MetaPublisher2Languages),
            ),
            icon='resources/icon/MetaPublisher2Folder.gif',
            container_filter=container_filter
        )

    except:
        context.registerClass(
            MetaPublisher2Languages,
            constructors=(
                ('add_MetaPublisher2Languages_form', add_MetaPublisher2Languages_form),
                ('add_MetaPublisher2Languages', add_MetaPublisher2Languages),
            ),
            icon='resources/icon/MetaPublisher2Folder.gif'
        )
