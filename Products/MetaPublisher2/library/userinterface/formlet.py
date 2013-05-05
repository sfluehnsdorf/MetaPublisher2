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

__doc__ = """UserInterface Formlets

!TXT! module info

$Id: library/userinterface/formlet.py 6 2013-05-05 18:01:53Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.library.application import permission_zmi
from Products.MetaPublisher2.library.common import ClassSecurityInfo, DTMLFile, InitializeClass


# ============================================================================
# Module Exports

__all__ = [
    'Formlet',
]


# ============================================================================
# Formlet Mix-In Class

class Formlet:
    """Formlet Mix-In Class"""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # Selection Formlet

    selection_formlet = DTMLFile('dtml/selection_formlet', globals())

    # ------------------------------------------------------------------------
    # Data Table Formlet

    datatable_formlet = DTMLFile('dtml/formlet_datatable', globals())

    def format_datatable_field(self, row, column):
        """!TXT! Display a row's columns's value."""

        def get_value(self, row, column):
            marker = []
            try:
                result = row.get(column, marker)
            except:
                pass
            if result is marker:
                result = getattr(row, column, marker)
            if result is marker:
                return '<span class="error">Error retrieving value</span>'
            else:
                return callable(result) and str(result()) or str(result)

        return column.get('template', '%s') % tuple(map(lambda value: get_value(row, value), column.get('values', [column['value']])))

    def process_datatable_options(self, form_id, columns, rows, request):
        """!TXT! Process options for data table formlet"""

        form = request.form
        cookies = request.cookies
        correct_form = form.get('form_id', form_id) == form_id and true or false

        # number of rows and size of batches
        rows_len = len(rows)
        default_batch_size = cookies.get(form_id + '_batch_size', self.default_batch_size)
        batch_size = int(correct_form and form.get('batch_size', default_batch_size) or default_batch_size)

        # first row to show (batch start)
        request_batch_start = correct_form and form.get('batch_start', None) or None
        if request_batch_start == 'first_batch':
            batch_start = 1
        elif request_batch_start == 'prev_batch':
            batch_start = max(1, int(cookies.get(form_id + '_batch_start', 1)) - batch_size)
        elif request_batch_start == 'next_batch':
            batch_start = min(rows_len, int(cookies.get(form_id + '_batch_start', 1)) + batch_size)
        elif request_batch_start == 'last_batch':
            batch_start = rows_len
        else:
            default_batch_start = cookies.get(form_id + '_batch_start', 1)
            batch_start = correct_form and form.get('batch_start', default_batch_start) or default_batch_start
        batch_start = int((float(batch_start) - 1) / batch_size) * batch_size + 1

        # sortable columns and which column to order by
        sortable_columns = filter(lambda column: column.get('sortable', None), columns)
        sortable_column_values = map(lambda column: column['value'], sortable_columns)
        if sortable_columns:
            default_order_by = cookies.get(form_id + '_order_by', sortable_column_values[0])
            order_by = correct_form and form.get('order_by', default_order_by) or default_order_by
        else:
            default_order_by = ''
            order_by = ''

        # columns, which may be and are hidden
        hideable_columns = filter(lambda column: 'hidden' in column, columns)
        hidden_columns = filter(lambda column: column.get('hidden', None), hideable_columns)
        default_select_column_values = map(lambda column: column['value'], filter(lambda column: column.get('hidden', None) is false, hideable_columns))
        if correct_form and form_id in form:
            selected_columns = filter(lambda column: column['value'] in form.get('show_columns', []), hideable_columns)
        elif form_id + '_show_columns' in cookies:
            selected_columns = filter(lambda column: column['value'] in cookies[form_id + '_show_columns'].split(','), hideable_columns)
        else:
            selected_columns = filter(lambda column: column.get('hidden', None) is false, hideable_columns)
        if correct_form and 'set_show_column' in form:
            value = form['set_show_column']
            selected_columns = filter(lambda column: column in selected_columns or column.get('value', None) == value, hideable_columns)
        elif correct_form and 'unset_show_column' in form:
            value = form['unset_show_column']
            selected_columns = filter(lambda column: column.get('value', None) != value, selected_columns)
        selected_column_values = map(lambda column: column['value'], selected_columns)

        # columns to display and how
        revealed_columns = filter(lambda column: column.get('hidden', None) is None or column in selected_columns, columns)
        revealed_column_values = map(lambda column: column['value'], revealed_columns)
        major_columns = filter(lambda column: not(column.get('minor', None)), revealed_columns)
        minor_columns = filter(lambda column: column.get('minor', None), revealed_columns)

        # the result data
        result = {
            'batch_end': min(batch_start + batch_size - 1, rows_len),
            'batch_size': batch_size,
            'batch_start': batch_start,
            'hideable_columns': hideable_columns,
            'major_columns': major_columns,
            'minor_columns': minor_columns,
            'order_by': order_by,
            'revealed_column_values': revealed_column_values,
            'rows_len': rows_len,
            'sortable_columns': sortable_columns,
            'sortable_column_values': sortable_column_values,
        }

        # store some inputs persistantly in cookies
        self.setProfileSetting(form_id + '_batch_start', batch_start, 1)
        self.setProfileSetting(form_id + '_batch_size', batch_size, self.default_batch_size)
        self.setProfileSetting(form_id + '_show_columns', ','.join(selected_column_values), ','.join(default_select_column_values))
        self.setProfileSetting(form_id + '_order_by', order_by, default_order_by)

        return result

    # ------------------------------------------------------------------------
    # Storage Selection Formlet

    security.declareProtected(permission_zmi, 'storage_selection_formlet')

    storage_selection_formlet = DTMLFile('formlet_storage_selection', globals())

    # ------------------------------------------------------------------------
    # Entry List Formlet

    security.declareProtected(permission_zmi, 'entry_list_formlet')

    entry_list_formlet = DTMLFile('formlet_entry_list', globals())

    # ------------------------------------------------------------------------
    # Frontend Path Formlet

    security.declareProtected(permission_zmi, 'frontend_path_formlet')

    frontend_path_formlet = DTMLFile('formlet_frontend_path', globals())

# ------------------------------------------------------------------------------
# Class Security

InitializeClass(Formlet)

# !!! formlet.py - add table header & footer to be able to remove continued flags
# !!! formlet.py - create list_formlet for storages, fields, etc.
