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

__doc__ = """MetaPublisher2 Dialogs

!TXT! module info

$Id: library/userinterface/dialogs.py 8 2013-05-08 21:18:33Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.library.application import permission_zmi
from Products.MetaPublisher2.library.common import ClassSecurityInfo, DTMLFile, InitializeClass


# ============================================================================
# Module Exports

__all__ = [
    'Dialogs',
]


# ============================================================================
# MetaPublisher2 Dialogs Mix-In Class

class Dialogs:
    """!TXT! MetaPublisher2 Dialogs Mix-In Class"""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # ZMI Dialog

    dialog_formlet = DTMLFile('dialog', globals())

    # ------------------------------------------------------------------------
    # General Dialogs

    security.declareProtected(permission_zmi, 'not_available_dialog')

    not_available_dialog = DTMLFile(
        'dialog', globals(),
        headline=u'''Feature Not Available!''',
        message=u'''This feature is not available in this release and will become available in a later release.\n\nPlease visit <a href="http://metapublisher.org" target="_blank">www.metapublisher.org</a> for more information.'''
    )

    # ------------------------------------------------------------------------
    # Warning Dialogs

    security.declareProtected(permission_zmi, 'designsfolder_warning_dialog')

    designsfolder_warning_dialog = DTMLFile(
        'dialog', globals(),
        headline=u'''Warning!''',
        message=u'''You should not manage any objects stored in the MetaPublisher2 Designs Folder directly.\n\nPlease use the MetaPublisher2's <a href="../designs_form">Design management</a> instead.''',
        buttons=[
            {'name': u'../designs_form:method', 'label': u'Design Management'},
        ]
    )

    security.declareProtected(permission_zmi, 'frontendsfolder_warning_dialog')

    frontendsfolder_warning_dialog = DTMLFile(
        'dialog', globals(),
        headline=u'''Warning!''',
        message=u'''You should not manage any objects stored in the MetaPublisher2 Frontends Folder directly.\n\nPlease use the MetaPublisher2's <a href="../frontends_form">Frontend management</a> instead.''',
        buttons=[
            {'name': u'../frontends_form:method', 'label': u'Frontend Management'},
        ]
    )

    security.declareProtected(permission_zmi, 'languagesfolder_warning_dialog')

    languagesfolder_warning_dialog = DTMLFile(
        'dialog', globals(),
        headline=u'''Warning!''',
        message=u'''You should not manage any objects stored in the MetaPublisher2 Languages Folder directly.\n\nPlease use the MetaPublisher2's <a href="../languages_form">Language management</a> instead.''',
        buttons=[
            {'name': u'../languages_form:method', 'label': u'Language Management'},
        ]
    )

    security.declareProtected(permission_zmi, 'toolsfolder_warning_dialog')

    toolsfolder_warning_dialog = DTMLFile(
        'dialog', globals(),
        headline=u'''Warning!''',
        message=u'''You should not manage any objects stored in the MetaPublisher2 Tools Folder directly.\n\nPlease use the MetaPublisher2's <a href="../tools_form">Tool management</a> instead.''',
        buttons=[
            {'name': u'../tools_form:method', 'label': u'Tool Management'},
        ]
    )

    security.declareProtected(permission_zmi, 'widgetsfolder_warning_dialog')

    widgetsfolder_warning_dialog = DTMLFile(
        'dialog', globals(),
        headline=u'''Warning!''',
        message=u'''You should not manage any objects stored in the MetaPublisher2 Widgets Folder directly.\n\nPlease use the MetaPublisher2's <a href="../widgets_form">Widget management</a> instead.''',
        buttons=[
            {'name': u'../widgets_form:method', 'label': u'Widget Management'},
        ]
    )

    # ------------------------------------------------------------------------
    # Data Dialogs

    security.declareProtected(permission_zmi, 'no_entries_dialog')

    no_entries_dialog = DTMLFile(
        'dialog', globals(),
        headline=u'''No Entries Added Yet!''',
        message=u'''You must <a href="add_entry_form">add at least one Entry</a>, before you can proceed.''',
        buttons=[
            {'name': u'add_entry_form:method', 'label': u'Add Entry'},
        ]
    )

    # ------------------------------------------------------------------------
    # Configuration Dialogs

    security.declareProtected(permission_zmi, 'no_storages_dialog')

    no_storages_dialog = DTMLFile(
        'dialog', globals(),
        headline=u'''No Storages Added Yet!''',
        message=u'''You must <a href="add_storage_form">add at least one Storage</a>, before you can proceed.''',
        buttons=[
            {'name': u'add_storage_form:method', 'label': u'Add Storage'},
        ]
    )

    security.declareProtected(permission_zmi, 'no_fields_dialog')

    no_fields_dialog = DTMLFile(
        'dialog', globals(),
        headline=u'''No Fields Added Yet!''',
        message=u'''You must <a href="add_field_form">add at least one Field</a>, before you can proceed.''',
        buttons=[
            {'name': u'add_field_form:method', 'label': u'Add Field'},
        ]
    )

    # ------------------------------------------------------------------------
    # Publisher Dialogs

    security.declareProtected(permission_zmi, 'no_frontends_dialog')

    no_frontends_dialog = DTMLFile(
        'dialog', globals(),
        headline=u'''No Frontends Added Yet!''',
        message=u'''You must <a href="add_frontend_form">add at least one Frontend</a>, before you can proceed.''',
        buttons=[
            {'name': u'add_frontend_form:method', 'label': u'Add Frontend'},
        ]
    )

    security.declareProtected(permission_zmi, 'no_widgets_dialog')

    no_widgets_dialog = DTMLFile(
        'dialog', globals(),
        headline=u'''No Widgets Added Yet!''',
        message=u'''You must <a href="add_widget_form">add at least one Widget</a>, before you can proceed.''',
        buttons=[
            {'name': u'add_widget_form:method', 'label': u'Add Widget'},
        ]
    )

    security.declareProtected(permission_zmi, 'no_designs_dialog')

    no_designs_dialog = DTMLFile(
        'dialog', globals(),
        headline=u'''No Designs Added Yet!''',
        message=u'''You must <a href="add_design_form">add at least one Design</a>, before you can proceed.''',
        buttons=[
            {'name': u'add_design_form:method', 'label': u'Add Design'},
        ]
    )

    # ------------------------------------------------------------------------
    # System Dialogs

    security.declareProtected(permission_zmi, 'no_plugins_dialog')

    no_plugins_dialog = DTMLFile(
        'dialog', globals(),
        headline=u'''No Plugins Installed!''',
        message=u'''You must <a href="plugins_form">install plugins</a> to work with MetaPublisher2.\n\nYou can <a href="http://metapublisher.org" target="_blank">download plugins from www.metapublisher.org</a>.'''
    )

    security.declareProtected(permission_zmi, 'no_storageplugins_dialog')

    no_storageplugins_dialog = DTMLFile(
        'dialog', globals(),
        headline=u'''No Storage Plugins Installed!''',
        message=u'''You must <a href="plugins_form">install plugins</a> to work with MetaPublisher2.\n\nYou can <a href="http://metapublisher.org" target="_blank">download plugins from www.metapublisher.org</a>.'''
    )

    security.declareProtected(permission_zmi, 'no_fieldplugins_dialog')

    no_fieldplugins_dialog = DTMLFile(
        'dialog', globals(),
        headline=u'''No Field Plugins Installed!''',
        message=u'''You must <a href="plugins_form">install plugins</a> to work with MetaPublisher2.\n\nYou can <a href="http://metapublisher.org" target="_blank">download plugins from www.metapublisher.org</a>.'''
    )

    security.declareProtected(permission_zmi, 'no_frontendplugins_dialog')

    no_frontendplugins_dialog = DTMLFile(
        'dialog', globals(),
        headline=u'''No Frontend Plugins Installed!''',
        message=u'''You must <a href="plugins_form">install plugins</a> to work with MetaPublisher2.\n\nYou can <a href="http://metapublisher.org" target="_blank">download plugins from www.metapublisher.org</a>.'''
    )

    security.declareProtected(permission_zmi, 'no_widgetplugins_dialog')

    no_widgetplugins_dialog = DTMLFile(
        'dialog', globals(),
        headline=u'''No Widget Plugins Installed!''',
        message=u'''You must <a href="plugins_form">install plugins</a> to work with MetaPublisher2.\n\nYou can <a href="http://metapublisher.org" target="_blank">download plugins from www.metapublisher.org</a>.'''
    )

    security.declareProtected(permission_zmi, 'no_designplugins_dialog')

    no_designplugins_dialog = DTMLFile(
        'dialog', globals(),
        headline=u'''No Dialog Plugins Installed!''',
        message=u'''You must <a href="plugins_form">install plugins</a> to work with MetaPublisher2.\n\nYou can <a href="http://metapublisher.org" target="_blank">download plugins from www.metapublisher.org</a>.'''
    )

# ----------------------------------------------------------------------------
# Class Security

InitializeClass(Dialogs)

# !!! dialog.py - check dialogs if they need buttons
# !!! dialog.py - revise dialog messages' wording
