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

__doc__ = """Queries Component

!TXT! module info

$Id: data/queries/queries.py 7 2013-05-08 23:54:34Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.library import ClassSecurityInfo, DTMLFile, InitializeClass, permission_access_entries, show_future


# ============================================================================
# Module Exports

__all__ = [
    'Queries',
]


# ============================================================================
# Queries Component Mix-In Class

class Queries:
    """!TXT! Queries Component Mix-In Class"""

    security = ClassSecurityInfo()

    # -----------------------------------------------------------------------
    # Query Form ZMI

    if show_future:

        security.declareProtected(permission_access_entries, 'queries_form')

        queries_form = DTMLFile('queries', globals())

    # ------------------------------------------------------------------------
    # Queries Parser API

    security.declareProtected(permission_access_entries, 'parse_query')

    def parse_query(self):
        """!TXT!"""

        result = u''
        request = self.REQUEST
        input = request.form['input'].replace('  ', ' ').strip()
        self.set_profile_variable(request, 'queries_history', self.get_profile_variable(request, 'queries_history', default=[]) + [input, ])
        if input == 'clear':
            return u'*clear#'
        elif input == 'help':
            return self.query_help()
        elif input.startswith('help '):
            return self.query_help(input[5:])
        elif input == 'history':
            return self.query_history()
        elif input == 'history clear':
            return self.query_history_clear()
        else:
            return self.query_interpreter(input)

    security.declareProtected(permission_access_entries, 'query_help')

    def query_help(self, topic=None):
        """!TXT!"""

        if topic:
            topic = topic.strip()
            return self._format_query_lines(
                self._format_query_bright(u'Queries'),
                self._format_query_error(u'!TXT! This feature is not yet available...'),
                self._format_query_normal(u'!TXT! In an upcoming release you can use an SQL-like query language to retrieve or manipulate Storages, Fields and Entries contained in a MetaPublisher2, making it possible to automatise various tasks.'),
            )
        else:
            return self._format_query_lines(
                self._format_query_bright(u'Queries'),
                self._format_query_error(u'!TXT! This feature is not yet available...'),
                self._format_query_normal(u'!TXT! In an upcoming release you can use an SQL-like query language to retrieve or manipulate Storages, Fields and Entries contained in a MetaPublisher2, making it possible to automatise various tasks.'),
            )

    security.declareProtected(permission_access_entries, 'query_history_clear')

    def query_history_clear(self):
        """!TXT!"""

        self.set_profile_variable(self.REQUEST, 'queries_history', [])

        return self._format_query_lines(
            self._format_query_bright(u'!TXT! Command history cleared.'),
        )

    security.declareProtected(permission_access_entries, 'query_history')

    def query_history(self):
        """!TXT!"""

        history = self.get_profile_variable(self.REQUEST, 'queries_history')

        if history:
            counter = 1
            lines = []
            for line in history:
                lines.append(self._format_query_dim(u'%3d. ' % counter) + self._format_query_normal(line))
                counter = counter + 1
            return self._format_query_lines(
                self._format_query_bright(u'Command history'),
                u'<br>'.join(lines),
            )
        else:
            return self._format_query_lines(
                self._format_query_bright(u'Command history'),
                self._format_query_normal(u'!TXT! No command history...'),
            )

    security.declareProtected(permission_access_entries, 'query_history')

    def query_clear(self):
        """!TXT!"""

        return ''

    # ------------------------------------------------------------------------
    # Queries Output API

    # !!! change this crap (maybe this could be part of settings.conf)

    def _format_query_lines(self, *lines):
        return u'<br>'.join(lines)

    def _format_query_bright(self, text):
        return u'<span class="terminal_bright">%s</span>' % text

    def _format_query_normal(self, text):
        return u'<span class="terminal_normal">%s</span>' % text

    def _format_query_dim(self, text):
        return u'<span class="terminal_dim">%s</span>' % text

    def _format_query_error(self, text):
        return u'<span class="terminal_error">%s</span>' % text

    # ------------------------------------------------------------------------
    # Queries Interpreter API

    security.declareProtected(permission_access_entries, 'query_interpreter')

    def query_interpreter(self, input):
        """!TXT!"""

        return self._format_query_lines(
            self._format_query_bright(u'Queries'),
            self._format_query_error(u'!TXT! This feature is not yet available...'),
            self._format_query_normal(u'!TXT! In an upcoming release you can use an SQL-like query language to retrieve or manipulate Storages, Fields and Entries contained in a MetaPublisher2, making it possible to automatise various tasks.'),
        )

# ----------------------------------------------------------------------------
# Class Security

InitializeClass(Queries)

# TODO queries.py - implement
# TODO queries.py - revise command Interpreter
