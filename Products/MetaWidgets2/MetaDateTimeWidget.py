# -*- coding: iso-8859-15 -*-
"""==================================================================

                                             M e t a   W i d g e t s
    -----------------------------------------------------------------

        Copyright (c) 2005, Sebastian Luehnsdorf - Web-Solutions GbR.
        http://zopemeta.com - http://luehnsdorf.de

        This software is subject to the provisions of the
        Zope Public License, Version 2.0 (ZPL).

        A copy of the ZPL should accompany this distribution.

        THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR
        IMPLIED WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED
        TO, THE IMPLIED WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST
        INFRINGEMENT, AND FITNESS FOR A PARTICULAR PURPOSE.

=================================================================="""

from math import ceil
from types import TupleType, StringType

from DateTime import DateTime
from Globals import DTMLFile
from Products.MetaPublisher2.Library import WidgetPlugin

from dt_definitions import formats, languageData, languages


# =============================================================================


def MetaDateTimeWidget_getLanguages(self):
    """Return list of languages"""
    return languages


# -----------------------------------------------------------------------------


def MetaDateTimeWidget_getLanguage(self, languageId=None):
    """Return names dictionary of language"""
    if languageId not in MetaDateTimeWidget_getLanguages(self):
        try:
            languageId = self.language
        except Exception:
            languageId = 'English'
    return languageData[languageId]


# -----------------------------------------------------------------------------

def __parseFormat(self, format, dt=None, languageId=None):
    """Parse format into a human readable display"""
    if isinstance(dt, StringType):
        dt = DateTime(dt)
    if dt is None:
        dt = DateTime()

    day = dt.day()
    if str(day) == '1':
        th = 'st'
    if str(day) == '2':
        th = 'nd'
    if str(day) == '3':
        th = 'rd'
    else:
        th = 'th'

    if languageId not in MetaDateTimeWidget_getLanguages(self):
        try:
            languageId = self.language
        except Exception:
            languageId = 'English'
    languageData = MetaDateTimeWidget_getLanguage(self, languageId)

    result = format

    for code, value in [
        ('$YEAR', dt.year()),
        ('$YY', dt.yy()),
        ('$MONTH', languageData['months'][dt.month()]),
        ('$MON', dt.month()),
        ('$MM', dt.mm()),
        ('$WDAY', languageData['weekdays'][dt.dow()]),
        ('$DOW1', dt.dow_1()),
        ('$DOW', dt.dow()),
        ('$WOY', ceil(float(dt.dayOfYear()) / 7)),
        ('$DAY', day),
        ('$DD', dt.dd()),
        ('$DOY', dt.dayOfYear()),
        ('$TH', th),
        ('$HOUR12', dt.h_12()),
        ('$HH12', '%02d' % dt.h_12()),
        ('$HOUR', dt.hour()),
        ('$HH', '%02d' % dt.hour()),
        ('$MI', '%02d' % dt.minute()),
        ('$SE', '%02d' % dt.second()),
        ('$AMPM', dt.ampm()),
        ('$TZ', dt.timezone()),
    ]:
        while result.find(code) > -1:
            result = result.replace(code, str(value))
        while result.find(code.lower()) > -1:
            result = result.replace(code.lower(), str(value))
    return result


# -----------------------------------------------------------------------------


def MetaDateTimeWidget_getFormats(self, dt=None, languageId=None):
    """Return list of tuples for select tag"""
    if isinstance(dt, StringType):
        dt = DateTime(dt)
    if dt is None:
        dt = DateTime()
    if languageId not in MetaDateTimeWidget_getLanguages(self):
        try:
            languageId = self.language
        except Exception:
            languageId = 'English'
    languageData = MetaDateTimeWidget_getLanguage(self, languageId)
    result = []
    for format in formats:
        if format == '---':
            result.append(('', '-' * 50))
        elif format == '$LANGUAGE':
            languageFormats = list(languageData.get('formats', []))
            if len(languageFormats):
                result.append(('', 'Language Specific'))
                for languageFormat in languageFormats:
                    value = __parseFormat(self, languageFormat, dt, languageId)
                    if value:
                        value = '&nbsp; ' + value
                    result.append((languageFormat, value))
                result = result + [('', ''), ('', '-' * 50), ('', '')]
        elif isinstance(format, TupleType):
            value = __parseFormat(self, format[1], dt, languageId)
            if format[0] and value:
                value = '&nbsp; ' + value
            result.append((format[0], value))
        else:
            value = __parseFormat(self, format, dt, languageId)
            if value:
                value = '&nbsp; ' + value
            result.append((format, value))
    return result


# =============================================================================


class MetaDateTimeWidget(WidgetPlugin):
    """MetaDateTimeWidget"""

    meta_type = 'MetaDateTimeWidget'

    # -------------------------------------------------------------------------

    pluginName = 'MetaDateTimeWidget'
    pluginAuthor = 'Sebastian Luehnsdorf - Web-Solutions GbR.'
    pluginVersion = '1.0.1'
    pluginInfo = 'Basic Web Interface that allows users to add new Entries.'

    formTypeIds = ['Add', 'Edit', 'View', 'List']
    fieldTypeIds = ['Date', 'Integer', 'Long', 'Float', 'String']

    # -------------------------------------------------------------------------

    displayMode = 'defaultMode'

    align = 'left'
    alignOptions = ['left', 'center', 'right', 'justify']
    valign = 'top'
    valignOptions = ['top', 'middle', 'bottom']

    case = 'normal'
    caseOptions = ['normal', 'lower', 'upper', 'capitalize']

    language = 'English'
    format = '$YEAR-$MM-$DD $HH:$MI:$SE'

    # -------------------------------------------------------------------------

    _properties = WidgetPlugin._properties + (
        {'id': 'displayMode', 'type': 'string', 'mode': 'w'},
        {
            'id': 'align', 'type': 'selection', 'mode': 'w',
            'select_variable': 'alignOptions'},
        {
            'id': 'valign', 'type': 'selection', 'mode': 'w',
            'select_variable': 'valignOptions'},
        {
            'id': 'case', 'type': 'selection', 'mode': 'w',
            'select_variable': 'caseOptions'},
        {
            'id': 'language', 'type': 'selection', 'mode': 'w',
            'select_variable': 'languages'},
        {'id': 'format', 'type': 'string', 'mode': 'w'},
    )

    # -------------------------------------------------------------------------

    def getWidgetId(self):
        """Return Plugin Identifier"""
        return 'MetaWidgets.' + self.meta_type

    # -------------------------------------------------------------------------

    def setWidgetData(self, formTypeId, data={}):
        """Configure Widget according to passed data"""
        if data.get('pluginId__', '') == self.getWidgetId():
            self.formTypeId = formTypeId
            self.displayMode = data['displayMode']
            self.align = data.get('align', 'left')
            self.valign = data.get('valign', 'top')
            self.case = data.get('case', 'normal')
            self.language = data.get('language', 'English')
            self.format = data.get('format', '$YEAR-$MM-$DD $HH:$MI:$SE')
        else:
            raise TypeError(
                'Invalid Widget data: "%s" <> "%s"' % (
                    self.getWidgetId(), data.get('pluginId__', '')))

    def getWidgetData(self, formTypeId):
        """Return the data of this Widget"""
        return {
            'pluginId__':  'MetaWidgets.' + self.meta_type,
            'displayMode': self.displayMode,
            'align': self.align,
            'valign': self.valign,
            'case': self.case,
            'language': self.language,
            'format': self.format,
        }

    # -------------------------------------------------------------------------

    def renderWidget(self, elementId, field, entryName=''):
        """Render widget according to configuration"""
        fieldId = field.getId()
        formTypeId = self.formTypeId
        displayMode = self.displayMode
        result = {
            'align': self.align,
            'valign': self.valign,
            'title': field.title or fieldId
            }

        def addInputOptions(self):
            options = ' size="%s"' % self.inputSize
            if self.inputClass:
                options = options + ' class="%s"' % self.inputClass
            if self.inputStyle:
                options = options + ' style="%s"' % self.inputStyle
            return options

        def addShowOptions(self):
            options = ''
            if self.case != 'normal':
                options = options + ' ' + self.case
            return options

        def dtmlParseFormat(self, dt, format, languageId=None):
            """Parse format into a DTML renderable display"""
            if languageId not in MetaDateTimeWidget_getLanguages(self):
                try:
                    languageId = self.language
                except Exception:
                    languageId = 'English'
            languageData = MetaDateTimeWidget_getLanguage(self, languageId)
            result = "'''%s'''" % format
            for code, value in [
                ('$YEAR', """''' + str( dt.year() ) + '''"""),
                ('$YY', """''' + str( dt.yy() ) ) + '''"""),
                ('$MONTH', """''' + monthNames[ dt.month() - 1 ] + '''"""),
                ('$MON', """''' + str( dt.month() ) + '''"""),
                ('$MM', """''' + str( dt.mm() ) + '''"""),
                ('$WDAY', """''' + wdayNames[ dt.dow() ] + '''"""),
                ('$DOW1', """''' + str( dt.dow_1() ) + '''"""),
                ('$DOW', """''' + str( dt.dow() ) + '''"""),
                (
                    '$WOY',
                    "''' + str( ceil( float( dt.dayOfYear() ) / 7 ) ) + '''"),
                ('$DAY', """''' + dt_day + '''"""),
                ('$DD', """''' + str( dt.dd() ) + '''"""),
                ('$DOY', """''' + str( dt.dayOfYear() ) + '''"""),
                (
                    '$TH',
                    "''' + ( ( dt_day == '1' and 'st' ) or ( dt_day == '2' "
                    "and 'nd' ) or ( dt_day == '3' and 'rd' ) or 'th' ) "
                    "+ '''"),
                ('$HOUR12', """''' + str( dt.h_12() ) + '''"""),
                ('$HH12', """''' + '%%02d' %% dt.h_12() + '''"""),
                ('$HOUR', """''' + str( dt.hour() ) + '''"""),
                ('$HH', """''' + '%%02d' %% dt.hour() + '''"""),
                ('$MI', """''' + '%%02d' %% dt.minute() + '''"""),
                ('$SE', """''' + '%%02d' %% dt.second() + '''"""),
                ('$AMPM', """''' + str( dt.ampm() ) + '''"""),
                ('$TZ', """''' + str( dt.timezone() ) + '''"""),
            ]:
                while result.find(code) > -1:
                    result = result.replace(code, str(value))
                while result.find(code.lower()) > -1:
                    result = result.replace(code.lower(), str(value))
            while result.find(" + '''''' + ") > -1:
                result = result.replace(" + '''''' + ", " + ")
            while result.find(" + ''''''") > -1:
                result = result.replace(" + ''''''", " ")
            while result.find("'''''' + ") > -1:
                result = result.replace("'''''' + ", " ")
            result = (
                '<dtml-let dt="ZopeTime(%s )" dt_day="str(dt.day() )" '
                'monthNames="%s" wdayNames="%s"><dtml-var "''' % (
                    dt, languageData['months'], languageData['weekdays']) +
                result + '"' + addShowOptions(self) + '></dtml-let>')
            return result

        def addDateInput(self, fieldId):
            return (

                '<select name="%s_year">'
                '<dtml-in "range( 1901, 2100 )" prefix=year>'
                '<option value="&dtml-year_item;"'
                '<dtml-if "now.year() == year_item"> selected</dtml-if>>'
                '&dtml-year_item;</option>'
                '</dtml-in>'
                '</select>'

                '<select name="%s_month">'
                '<dtml-in "range( 1, 13 )" prefix=month>'
                '''<option value="<dtml-var "'%%%%02d' %%%% month_item">"'''
                '<dtml-if "now.month() == month_item"> selected</dtml-if>>'
                '&dtml-month_item;</option>'
                '</dtml-in>'
                '</select>'

                '<select name="%s_day">'
                '<dtml-in "range( 1, 32 )" prefix=day>'
                '''<option value="<dtml-var "'%%%%02d' %%%% day_item">"'''
                '<dtml-if "now.day() == day_item"> selected</dtml-if>>'
                '&dtml-day_item;</option>'
                '</dtml-in>'
                '</select>'

                '&nbsp;'

                '<select name="%s_hour">'
                '<dtml-in "range( 0, 24 )" prefix=hour>'
                '''<option value="<dtml-var "'%%%%02d' %%%% hour_item">"'''
                '<dtml-if "now.hour() == hour_item"> selected</dtml-if>>'
                '&dtml-hour_item;</option>'
                '</dtml-in>'
                '</select>:'

                '<select name="%s_minute">'
                '<dtml-in "range( 0, 60 )" prefix=minute>'
                '''<option value="<dtml-var "'%%%%02d' %%%% minute_item">"'''
                '<dtml-if "now.minute() == minute_item"> selected</dtml-if>>'
                '&dtml-minute_item;</option>'
                '</dtml-in>'
                '</select>:'

                '<select name="%s_second">'
                '<dtml-in "range( 0, 60 )" prefix=second>'
                '''<option value="<dtml-var "'%%%%02d' %%%% second_item">"'''
                '<dtml-if "int( now.second() ) == second_item"> selected'
                '</dtml-if>>&dtml-second_item;</option>'
                '</dtml-in>'
                '</select>'

            ) % (fieldId, fieldId, fieldId, fieldId, fieldId, fieldId)

        if formTypeId == 'List':
            if displayMode == 'defaultMode':
                result['field'] = dtmlParseFormat(self, "%s['%s']" % (
                    entryName, fieldId), self.format, self.language)
            elif displayMode == 'showDefault':
                result['field'] = dtmlParseFormat(
                    self, "getZMP2().getField('%s', '%s').default" % (
                        self.storageId, fieldId), self.format, self.language)
            elif displayMode == 'showNow':
                result['field'] = dtmlParseFormat(
                    self, "", self.format, self.language)
        elif formTypeId == 'View':
            if displayMode == 'defaultMode':
                result['field'] = dtmlParseFormat(
                    self, "%s['%s']" % (
                        entryName, fieldId), self.format, self.language)
            elif displayMode == 'showDefault':
                result['field'] = dtmlParseFormat(
                    self, "getZMP2().getField('%s', '%s').default" % (
                        self.storageId, fieldId), self.format, self.language)
            elif displayMode == 'showNow':
                result['field'] = dtmlParseFormat(
                    self, "", self.format, self.language)

        elif formTypeId == 'Add':
            if displayMode == 'defaultMode':
                result['field'] = (
                    '''<dtml-let now="ZopeTime( getZMP2().getField('''
                    """'%s', '%s').default )">""" % (
                        self.storageId, fieldId) +
                    addDateInput(self, fieldId) + '''</dtml-let>''')
            elif displayMode == 'inputNow':
                result['field'] = (
                    '''<dtml-let now=ZopeTime>''' +
                    addDateInput(self, fieldId) + '''</dtml-let>''')
            elif displayMode == 'showDefault':
                result['field'] = dtmlParseFormat(
                    self, "getZMP2().getField('%s', '%s').default" % (
                        self.storageId, fieldId), self.format, self.language)
                result['hidden'] = (
                    '''<input type="hidden" name="%s"'''
                    ''' value="<dtml-var "getZMP2().getField('''
                    """'%s', '%s').default">">""" % (
                        fieldId, self.storageId, fieldId))
            elif displayMode == 'hiddenDefault':
                result['hidden'] = (
                    '''<input type="hidden" name="%s" value="'''
                    '''<dtml-var "getZMP2().getField('''
                    ''''%s', '%s').default">">''' % (
                        fieldId, self.storageId, fieldId))
            elif displayMode == 'showNow':
                result['field'] = dtmlParseFormat(
                    self, "", self.format, self.language)
                result['hidden'] = (
                    '<input type="hidden" name="%s" value="'
                    '<dtml-var ZopeTime>">' % fieldId)
            elif displayMode == 'hiddenNow':
                result['hidden'] = (
                    '<input type="hidden" name="%s" value="'
                    '<dtml-var ZopeTime>">' % fieldId)

        elif formTypeId == 'Edit':
            if displayMode == 'defaultMode':
                result['field'] = (
                    '''<dtml-let now="ZopeTime( %s['%s'] )">''' % (
                        entryName, fieldId) +
                    addDateInput(self, fieldId) +
                    '''</dtml-let>''')
            elif displayMode == 'inputDefault':
                result['field'] = (
                    '''<dtml-let now="ZopeTime( getZMP2().getField('''
                    """'%s', '%s').default )">""" % (
                        self.storageId, fieldId) +
                    addDateInput(self, fieldId) +
                    '''</dtml-let>''')
            elif displayMode == 'inputNow':
                result['field'] = (
                    '''<dtml-let now=ZopeTime>''' +
                    addDateInput(self, fieldId) + '''</dtml-let>''')
            elif displayMode == 'showValue':
                result['field'] = dtmlParseFormat(self, "%s['%s']" % (
                    entryName, fieldId), self.format, self.language)
                result['hidden'] = (
                    '''<input type="hidden" name="%s" value="'''
                    '''<dtml-var "%s['%s']">">''' % (
                        fieldId, entryName, fieldId))
            elif displayMode == 'hiddenValue':
                result['hidden'] = (
                    '''<input type="hidden" name="%s" value="'''
                    '''<dtml-var "%s['%s']">">''' % (
                        fieldId, entryName, fieldId))
            elif displayMode == 'showDefault':
                result['field'] = dtmlParseFormat(
                    self, "getZMP2().getField('%s', '%s').default" % (
                        self.storageId, fieldId), self.format, self.language)
                result['hidden'] = (
                    '''<input type="hidden" name="%s" value="'''
                    '''<dtml-var "getZMP2().getField('%s', '%s')'''
                    '''.default">">''' % (
                        fieldId, self.storageId, fieldId))
            elif displayMode == 'hiddenDefault':
                result['hidden'] = (
                    '''<input type="hidden" name="%s" value="'''
                    '''<dtml-var "getZMP2().getField('%s', '%s')'''
                    '''.default">">''' % (
                        fieldId, self.storageId, fieldId))
            elif displayMode == 'showNow':
                result['field'] = dtmlParseFormat(
                    self, "", self.format, self.language)
                result['hidden'] = (
                    '<input type="hidden" name="%s" value="'
                    '<dtml-var ZopeTime>">' % fieldId)
            elif displayMode == 'hiddenNow':
                result['hidden'] = (
                    '<input type="hidden" name="%s" value="'
                    '<dtml-var ZopeTime>">' % fieldId)

        return result

    # -------------------------------------------------------------------------

    addFormlet = 'manage_MetaDateTimeWidget_AddFormlet'
    editFormlet = 'manage_MetaDateTimeWidget_EditFormlet'
    listFormlet = 'manage_MetaDateTimeWidget_ListFormlet'
    viewFormlet = 'manage_MetaDateTimeWidget_ViewFormlet'


# -----------------------------------------------------------------------------


manage_MetaDateTimeWidget_AddFormlet = DTMLFile(
    'dtml/MetaDateTimeWidget_AddFormlet', globals())
manage_MetaDateTimeWidget_EditFormlet = DTMLFile(
    'dtml/MetaDateTimeWidget_EditFormlet', globals())
manage_MetaDateTimeWidget_ListFormlet = DTMLFile(
    'dtml/MetaDateTimeWidget_ListFormlet', globals())
manage_MetaDateTimeWidget_ViewFormlet = DTMLFile(
    'dtml/MetaDateTimeWidget_ViewFormlet', globals())


# =============================================================================


def manage_addMetaDateTimeWidget(self, id, formTypeId, data={}, REQUEST=None):
    """ZMI constructor for MetaDateTimeWidget"""
    instance = MetaDateTimeWidget(id)
    instance.setWidgetData(formTypeId, data)
    id = self._setObject(id, instance)
    if REQUEST is not None:
        REQUEST.RESPONSE.redirect(
            self.zmp2URL() + '/manage_interfacesBrowserForm')
