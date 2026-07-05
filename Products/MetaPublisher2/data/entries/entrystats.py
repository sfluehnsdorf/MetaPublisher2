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

__doc__ = """Entry Stats Component

!TXT! module info

$Id: data/entries/entrystats.py 4 2013-05-08 21:41:54Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.library import ClassSecurityInfo, InitializeClass


# ============================================================================
# Module Exports

__all__ = [
    'EntryStats',
]


# ============================================================================
# Entry Stats Component Mix-In Class

class EntryStats:
    """!TXT! Entry Stats Component Mix-In Class"""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # Entry Stats Retrieval

    def stat_entry(self, source, entry_id):
        """!TXT!"""
        raise NotImplementedError

    def stat_entries(self, source, entry_ids=None, conditions=None):
        """!TXT!"""
        raise NotImplementedError

    def get_entry_stat_size(self, source, entry_id):
        """!TXT!"""
        raise NotImplementedError

    def get_entry_stat_ctime(self, source, entry_id):
        """!TXT!"""
        raise NotImplementedError

    def get_entry_stat_cuser(self, source, entry_id):
        """!TXT!"""
        raise NotImplementedError

    def get_entry_stat_mtime(self, source, entry_id):
        """!TXT!"""
        raise NotImplementedError

    def get_entry_stat_muser(self, source, entry_id):
        """!TXT!"""
        raise NotImplementedError

    def get_entry_stat_atime(self, source, entry_id):
        """!TXT!"""
        raise NotImplementedError

    def get_entry_stat_auser(self, source, entry_id):
        """!TXT!"""
        raise NotImplementedError

    # ------------------------------------------------------------------------
    # Entry Stats Retrieval

    def touch_entry(self, source, entry_id):
        """!TXT!"""
        raise NotImplementedError

    def touch_entries(self, source, entry_ids=None, conditions=None):
        """!TXT!"""
        raise NotImplementedError

    def access_entry(self, source, entry_id):
        """!TXT!"""
        raise NotImplementedError

    def access_entries(self, source, entry_ids=None, conditions=None):
        """!TXT!"""
        raise NotImplementedError


# ----------------------------------------------------------------------------
# Class Security

InitializeClass(EntryStats)

# !!! entrystats.py - implement
