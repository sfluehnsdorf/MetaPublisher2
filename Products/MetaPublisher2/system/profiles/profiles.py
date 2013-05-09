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

__doc__ = """Profiles Component

User profiles are settings that are stored transparently and persistently.
This service removes the need to pass settings through the REQUEST and ensures
that these settings are available any time, even after logout or server
restart. Each profile is stored on a per-user level, identified by user name
and the physical path to the user's UserFolder object.

$Id: system/profiles/profiles.py 14 2013-05-09 17:21:24Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.library import ClassSecurityInfo, eval_valuestring, false, DTMLFile, identify_type, InitializeClass, permission_manage, permission_zmi, true


# ============================================================================
# Module Exports

__all__ = [
    'Profiles',
]


# ============================================================================
# Profiles Component Mix-In Class

class Profiles:
    """!TXT! Profiles Component Mix-In Class"""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # Profile Module Initialisation

    def init_profiles(self):
        self.__profiles = {}

    # ------------------------------------------------------------------------
    # Profiles ZMI Forms

    security.declareProtected(permission_manage, 'profiles_form')

    profiles_form = DTMLFile('profiles', globals())

    # ------------------------------------------------------------------------
    # Profile Retrieval API

    def _get_profile_id(self, user):
        """!TXT! Return the Profile id based on the user object."""

        return '%s/%s' % ('/'.join(user.aq_parent.getPhysicalPath()), user.getUserName())

    security.declareProtected(permission_manage, 'get_profile_variable')

    def get_profile_variable(self, request, key, default=None):
        """!TXT! Return the value of the specified variable from the user's profile."""

        profile_id = self._get_profile_id(request.AUTHENTICATED_USER)
        settings = self.__profiles.get(profile_id, {})
        return settings.get(key, default)

    def list_profile_variables(self, request):
        """!TXT! Return a list of the profile's settings."""

        profile_id = self._get_profile_id(request.AUTHENTICATED_USER)
        settings = self.__profiles.get(profile_id, {})
        result = []
        keys = settings.keys()
        keys.sort()
        for key in keys:
            value = settings[key]
            result.append((key, value, identify_type(value)))
        return result

    # ------------------------------------------------------------------------
    # Profile Mutation API

    security.declareProtected(permission_manage, 'delete_own_profile')

    def save_profile_changes(self, REQUEST):
        """!TXT! Save changes to the user's profile."""

        profile_id = self._get_profile_id(request.AUTHENTICATED_USER)
        settings = self.__profiles.get(profile_id, {})

        for formkey in REQUEST.form.keys():
            if formkey.startswith('value_'):
                key = formkey[6:]
                value = eval_valuestring(REQUEST[formkey], settings[key])
                if value:
                    settings[key] = value

        for key in REQUEST.get('delete_keys', []):
            del settings[key]

        profiles = self.__profiles
        profiles[profile_id] = settings
        self.__profiles = profiles

        self.redirect(
            REQUEST,
            'profiles_form',
            message='!TXT! The changes to your profile have been saved.',
        )

    security.declareProtected(permission_manage, 'delete_own_profile')

    def delete_own_profile(self, REQUEST):
        """!TXT! Delete the user's Profile."""

        profile_id = self._get_profile_id(request.AUTHENTICATED_USER)
        profiles = self.__profiles
        profiles[profile_id] = {}
        self.__profiles = profiles

        self.redirect(
            REQUEST,
            'profiles_form',
            message='!TXT! Your profile has been removed.',
        )

    security.declareProtected(permission_manage, 'delete_unused_profiles')

    def delete_unused_profiles(self, REQUEST=None):
        """!TXT! Delete all Profiles for whose Users object no longer exist."""

        profiles = self.__profiles

        counter = 0
        for key in self.__profiles.keys():
            try:
                key_parts = key.split('/')
                object = self.getPhysicalRoot()
                for key_part in key_parts[1: -1]:
                    object = object._getOb(key_part)
                user = object.getUser(key_parts[-1])
                if user is None:
                    raise
            except:
                del profiles[key]
                counter = counter + 1

        if counter:
            self.__profiles = profiles
            message = '!TXT! Found and purged %d unused profile%s.' % (counter, counter > 1 and 's' or '')
        else:
            message = '!TXT! No unused profiles found.'

        self.redirect(
            REQUEST,
            'profiles_form',
            message=message,
        )

    security.declareProtected(permission_manage, 'set_profile_variable')

    def set_profile_variable(self, request, key, value):
        """!TXT! Set the value of the specified variable in the User's profile."""

        profile_id = self._get_profile_id(request.AUTHENTICATED_USER)
        settings = self.__profiles.get(profile_id, {})
        if key in settings:
            value = eval_valuestring(value, settings[key])
            if not value:
                return

        settings[key] = value
        profiles = self.__profiles
        profiles[profile_id] = settings
        self.__profiles = profiles

    security.declareProtected(permission_zmi, 'update_profile')

    def update_profile(self, request, variables):
        """!TXT! Set the value of the specified variable in the User's profile."""

        form = request.form
        form_has_key = form.has_key
        profile_id = self._get_profile_id(request.AUTHENTICATED_USER)
        settings = self.__profiles.get(profile_id, {})
        settings_changed = false

        for key, default in variables:
            value = eval_valuestring(form.get(key, settings.get(key, default)), default)
            if value is not None:
                request.set(key, value)
                if value != settings.get(key, None):
                    settings_changed = true
                    settings[key] = value

        if settings_changed:
            profiles = self.__profiles
            profiles[profile_id] = settings
            self.__profiles = profiles

# ------------------------------------------------------------------------------
# Class Security

InitializeClass(Profiles)

# !!! profiles.py - review api use and implementation

# !!! profiles.py - refactor getProfileSetting -> get_profile_variable

    #def getProfileSetting(self, key, default=None):
    #    """!TXT!"""

    #    request = self.REQUEST
    #    default_value = request.cookies.get(key, default)
    #    value = request.form.get(key, default_value)
    #    if value != default_value:
    #        request.RESPONSE.setCookie(key, value, path='/', expires=0)
    #    request.set(key, value)
    #    return value

# !!! profiles.py - refactor setProfileSetting -> set_profile_variable

    #def setProfileSetting(self, key, value, default=None):
    #    """!TXT!"""

    #    request = self.REQUEST
    #    if value != request.cookies.get(key, default):
    #        request.RESPONSE.setCookie(key, value, path='/', expires=0)
    #    return value
