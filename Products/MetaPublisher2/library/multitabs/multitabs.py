# -*- coding: iso-8859-15 -*-
# ============================================================================
#
#                               M u l t i  T a b s
#
# ----------------------------------------------------------------------------
# Copyright (c) 2009-2012, Sebastian Lühnsdorf - Web-Solutions
# For more information see the README.txt file or visit www.zope.biz
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

__doc__ = """MultiTabs

Mix-in service allowing for grouped, structured Zope management tabs in
multiple levels. This service is backward compatible to Zope's regular
management tabs. The management tab definition accepts an additional attribute
named 'sub' which stores another set management options, for example:

class Fruit:
    '''Fruit Product'''

    manage_options = (

        # first management tab on the first level
        {
            'label': 'Apples',
            'action': 'Apples_form',
            'sub': (

                # first management tab on the second level of the apple's tab
                {
                    'label': 'McIntosh',
                    'action': 'Apples_McIntosh_form',
                },

            # second management tab on the second level of the apple's tab
            {
                'label': 'Granny Smith',
                'action': 'Apples_GrannySmith_form',
            },

          ),

      },

      # second management tab on the first level
      {
        ...
      }

Just like the regular management tabs, unavailable and restricted actions are
purged. If only one child exists with the same action as its parent, the list
will automatically collapse. If a parent's action is an empty string, it will
be filled with the first child's action.

$Id: multitabs/multitabs.py 8 2013-04-13 02:39:56Z sfluehnsdorf $
"""

__version__ = '$Revision: 1.3 $'[11:-2]


# ============================================================================
# Module Imports

from AccessControl import ClassSecurityInfo
from AccessControl.Permissions import view_management_screens
from Globals import DTMLFile, InitializeClass

try:
    from zExceptions import Unauthorized
except:
    Unauthorized = 'Unauthorized'

try:
    from zExceptions import Redirect
except:
    Redirect = 'Redirect'


# ============================================================================
# Module Exports

__all__ = [
    'MultiTabs',
]


# ============================================================================
# Booleans

try:
    true = True
    false = False
except:
    true = 1
    false = 0


# ============================================================================
# MultiTabs Mix-In Class

class MultiTabs:
    """!TXT! MultiTabs Mix-In Class

    This class overwrites the standard Zope management tabs with tabs that
    provide multiple levels for complex applications.
    """

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # MultiTabs ZMI Form

    security.declarePublic('manage_tabs')
    manage_tabs = DTMLFile('multitabs', globals())

    # ------------------------------------------------------------------------
    # !TXT MultiTabs Manage Workspace Method

    security.declarePublic('manage_workspace')

    def manage_workspace(self, REQUEST):
        """!TXT! Dispatch to first interface in manage_options"""

        options = self.filtered_manage_options(REQUEST)

        try:
            action = options[0][0]['action']
            if action == 'manage_workspace':
                raise TypeError
        except (IndexError, KeyError):
            raise Unauthorized('You are not authorized to view this object.')

        if action.find('/'):
            raise Redirect("%s/%s" % (REQUEST['URL1'], action))

        return getattr(self, action)(self, REQUEST)

    # ------------------------------------------------------------------------
    # !TXT MultiTabs Manage Workspace Method

    def _get_manage_options_map(self, REQUEST):
        """!TXT!"""

        try:
            options = tuple(self.manage_options)
        except:
            options = tuple(self.manage_options())

        management_view_path = REQUEST.get(
            'management_view_path',
            REQUEST.get('URL', '').split('/')[-1].split('?')[0]
        )
        if REQUEST.get('management_view', None):
            management_view = REQUEST['management_view']
            management_view_path = []
        else:
            management_view = []

        # remap and filter options

        mapped_options = {}
        todo = {}

        index = 0
        for option in options:
            todo[str(index)] = option
            index = index + 1

        while todo.keys():
            id = todo.keys()[0]
            option = todo[id]
            del todo[id]
            if 'sub' in option:
                index = 0
                for sub in option['sub']:
                    todo['%s_%s' % (id, index)] = sub
                    index = index + 1
            filter = option.get('filter', None)
            if filter is not None and not filter(self):
                continue
            path = option.get('path', None)
            if path is None:
                path = option.get('action', '')
            object = self.restrictedTraverse(path, None)
            if object is None:
                continue
            mapped_options[id] = option

        # find active option

        keys = mapped_options.keys()
        keys.sort()

        active_id = None
        for key in keys:
            option = mapped_options[key]
            if option.get('path', option.get('action', '')) == management_view_path or option.get('label', '') == management_view:
                active_id = key

        if not active_id:
            for key in keys:
                option = mapped_options[key]
                if option.get('path', option.get('action', '')):
                    active_id = key
                    break

        return mapped_options, active_id

    # ------------------------------------------------------------------------
    # !TXT MultiTabs Manage Workspace Method

    security.declarePublic('_get_manage_options_map')

    def get_active_manage_option(self, REQUEST=None):
        """!TXT! Return the active management tab"""

        # initialize

        if REQUEST is None:
            REQUEST = self.REQUEST

        mapped_options, active_id = self._get_manage_options_map(REQUEST)

        return mapped_options[active_id]

    # ------------------------------------------------------------------------
    # !TXT MultiTabs Manage Workspace Method

    security.declarePublic('filtered_manage_options')

    def filtered_manage_options(self, REQUEST=None):
        """!TXT! Return the list of available management tabs"""

        # initialize

        if REQUEST is None:
            REQUEST = self.REQUEST

        mapped_options, active_id = self._get_manage_options_map(REQUEST)

        keys = mapped_options.keys()
        keys.sort()

        # set parent actions

        for key in keys:
            parent_key = '_'.join(key.split('_')[: -1])
            if parent_key in mapped_options and not mapped_options[parent_key].get('action', ''):
                mapped_options[parent_key]['action'] = mapped_options[key]['action']

        # format and return result

        result = []
        active_id_parts = active_id.split('_')
        keys = mapped_options.keys()
        keys.sort()
        for index in range(len(active_id_parts)):
            level_options = []
            level_parent_id = '_'.join(active_id_parts[: index])
            level_id = '_'.join(active_id_parts[: index + 1])
            for key in keys:
                if len(key.split('_')) == index + 1 and key.startswith(level_parent_id):
                    if key == level_id:
                        mapped_options[key]['active'] = true
                    else:
                        mapped_options[key]['active'] = false
                    level_options.append(mapped_options[key])
            result.append(level_options)
        return result

# ------------------------------------------------------------------------------
# initialize class security

InitializeClass(MultiTabs)
