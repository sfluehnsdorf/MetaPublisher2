"""MetaPublisher2 - Queries Component."""


from Products.MetaPublisher2.library.application import (
    permission_access_entries)
from Products.MetaPublisher2.library.common import (
    ClassSecurityInfo, DTMLFile, InitializeClass)
from Products.MetaPublisher2.library.compatibility import show_future


# =============================================================================
# Module Exports

__all__ = [
    'Queries',
]


# =============================================================================
# Queries Component Mix-In Class

class Queries:
    """Queries Component Mix-In Class."""

    security = ClassSecurityInfo()

    # -------------------------------------------------------------------------
    # Query Form ZMI

    if show_future:

        security.declareProtected(permission_access_entries, 'queries_form')

        queries_form = DTMLFile('queries', globals())

    # -------------------------------------------------------------------------
    # Queries Parser API

    security.declareProtected(permission_access_entries, 'parse_query')

    def parse_query(self):
        """TODO: Docstring for parse_query."""
        request = self.REQUEST
        input = request.form['input'].replace('  ', ' ').strip()
        self.set_profile_variable(
            request, 'queries_history', self.get_profile_variable(
                request, 'queries_history', default=[]) + [input, ])
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
        """TODO: Docstring for query_help."""
        if topic:
            topic = topic.strip()
            return self._format_query_lines(
                self._format_query_bright(u'Queries'),
                self._format_query_error(
                    u'!TXT! This feature is not yet available...'),
                self._format_query_normal(
                    u'!TXT! In an upcoming release you can use an SQL-like '
                    u'query language to retrieve or manipulate Storages, '
                    u'Fields and Entries contained in a MetaPublisher2, '
                    u'making it possible to automatise various tasks.'),
            )
        else:
            return self._format_query_lines(
                self._format_query_bright(u'Queries'),
                self._format_query_error(
                    u'!TXT! This feature is not yet available...'),
                self._format_query_normal(
                    u'!TXT! In an upcoming release you can use an SQL-like '
                    u'query language to retrieve or manipulate Storages, '
                    u'Fields and Entries contained in a MetaPublisher2, '
                    u'making it possible to automatise various tasks.'),
            )

    security.declareProtected(permission_access_entries, 'query_history_clear')

    def query_history_clear(self):
        """TODO: Docstring for query_history_clear."""
        self.set_profile_variable(self.REQUEST, 'queries_history', [])
        return self._format_query_lines(
            self._format_query_bright(u'!TXT! Command history cleared.'),
        )

    security.declareProtected(permission_access_entries, 'query_history')

    def query_history(self):
        """TODO: Docstring for query_history."""
        history = self.get_profile_variable(self.REQUEST, 'queries_history')
        if history:
            counter = 1
            lines = []
            for line in history:
                lines.append(
                    self._format_query_dim(u'%3d. ' % counter) +
                    self._format_query_normal(line))
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
        """TODO: Docstring for query_clear."""
        return ''

    # -------------------------------------------------------------------------
    # Queries Output API

    # !!! change this crap (maybe this could be part of settings.conf)

    def _format_query_lines(self, *lines):
        """TODO: Docstring for _format_query_lines."""
        return u'<br>'.join(lines)

    def _format_query_bright(self, text):
        """TODO: Docstring for _format_query_bright."""
        return u'<span class="terminal_bright">%s</span>' % text

    def _format_query_normal(self, text):
        """TODO: Docstring for _format_query_normal."""
        return u'<span class="terminal_normal">%s</span>' % text

    def _format_query_dim(self, text):
        """TODO: Docstring for _format_query_dim."""
        return u'<span class="terminal_dim">%s</span>' % text

    def _format_query_error(self, text):
        """TODO: Docstring for _format_query_error."""
        return u'<span class="terminal_error">%s</span>' % text

    # -------------------------------------------------------------------------
    # Queries Interpreter API

    security.declareProtected(permission_access_entries, 'query_interpreter')

    def query_interpreter(self, input):
        """TODO: Docstring for query_interpreter."""
        return self._format_query_lines(
            self._format_query_bright(u'Queries'),
            self._format_query_error(
                u'!TXT! This feature is not yet available...'),
            self._format_query_normal(
                u'!TXT! In an upcoming release you can use an SQL-like query '
                u'language to retrieve or manipulate Storages, Fields and '
                u'Entries contained in a MetaPublisher2, making it possible '
                u'to automatise various tasks.'),
        )


# -----------------------------------------------------------------------------
# Class Security


InitializeClass(Queries)


# TODO queries.py - implement
# TODO queries.py - revise command Interpreter
