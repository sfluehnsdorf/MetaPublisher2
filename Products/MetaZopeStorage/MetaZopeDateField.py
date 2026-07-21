"""Meta Zope Storage."""


from App.special_dtml import DTMLFile
from ZPublisher.Converters import field2date_international

from DateTime.DateTime import DateTime
from Products.MetaPublisher2.bases.field.legacyfield import (
    LegacyFieldPlugin as FieldPlugin)


# ===================================================================


class MetaZopeDateField(FieldPlugin):
    """DateField."""

    pluginName = 'DateField'
    pluginAuthor = 'Sebastian Luehnsdorf - Web-Solutions GbR.'
    pluginVersion = '1.0.9'
    pluginInfo = 'This a Date Field for the MetaZopeStorage.'

    storageTypeId = 'MetaZopeStorage'
    fieldTypeId = 'Date'

    # -------------------------------------------------------------------------

    default = None

    _properties = FieldPlugin._properties + (
        {'id': 'default', 'type': 'date', 'mode': 'w'},
    )

    # -------------------------------------------------------------------------

    manage_configureFieldForm = DTMLFile(
        'dtml/editMetaZopeDateField', globals())

    def manage_configureField(self, REQUEST=None):
        """Change Field's configuration parameters."""
        self.title = REQUEST.get('title', '')
        self.default = self._testValue(REQUEST.get('default', ''))
        if REQUEST is not None:
            REQUEST.RESPONSE.redirect(
                self.zmp2URL() + '/manage_fieldsBrowserForm?storageId=' +
                self.getStorageId() + '&message=Changes+saved')

    # -------------------------------------------------------------------------

    def getFieldInfo(self):
        """Return information about this Field if available."""
        pass

    def getEntryObject(self, entryId):
        """Return the entry object."""
        return self.storage_getEntryObject(entryId)

    # -------------------------------------------------------------------------

    def setDefault(self, entryId):
        """Set the default value for this Field in the Entry."""
        if self.default:
            self.setValue(entryId, self.default)

    def setData(self, entryId, data):
        """Set the value inside data for this Field in the Entry."""
        fieldId = self.getId()
        if (
            data.has_key(fieldId + '_year') and
            data.has_key(fieldId + '_month') and
            data.has_key(fieldId + '_day') and
            data.has_key(fieldId + '_hour') and
            data.has_key(fieldId + '_minute') and
            data.has_key(fieldId + '_second')
        ):
            datetime = '%04d/%02d/%02d %02d:%02d:%02d' % (
                int(data[fieldId + '_year']),
                int(data[fieldId + '_month']),
                int(data[fieldId + '_day']),
                int(data[fieldId + '_hour']),
                int(data[fieldId + '_minute']),
                int(data[fieldId + '_second']))
            self.setValue(entryId, datetime)
        elif (
            data.has_key(fieldId + '_year') and
            data.has_key(fieldId + '_month') and
            data.has_key(fieldId + '_day')
        ):
            datetime = '%04d/%02d/%02d' % (
                int(data[fieldId + '_year']),
                int(data[fieldId + '_month']),
                int(data[fieldId + '_day']))
            self.setValue(entryId, datetime)
        elif (
            data.has_key(fieldId + '_hour') and
            data.has_key(fieldId + '_minute') and
            data.has_key(fieldId + '_second')
        ):
            datetime = '%02d:%02d:%02d' % (
                int(data[fieldId + '_hour']),
                int(data[fieldId + '_minute']),
                int(data[fieldId + '_second']))
            self.setValue(entryId, datetime)
        elif data.has_key(fieldId):
            try:
                datetimeObject = DateTime(float(data[fieldId]))
            except Exception:
                datetimeObject = DateTime(data[fieldId])
            datetime = '%04d/%02d/%02d %02d:%02d:%02d' % (
                datetimeObject.year(), datetimeObject.month(),
                datetimeObject.day(), datetimeObject.hour(),
                datetimeObject.minute(), datetimeObject.second())
            self.setValue(entryId, datetime)

    # -------------------------------------------------------------------------

    def _getValue(self, entryId, default):
        """Retrieve a value from an entry."""
        fieldId = self.getId()
        entry = self.getEntryObject(entryId)
        return entry.getProperty(fieldId, default)

    def _setValue(self, entryId, value):
        """Store a value in an entry."""
        fieldId = self.getId()
        entry = self.getEntryObject(entryId)
        if entry.hasProperty(fieldId):
            entry._setPropValue(fieldId, value)
        else:
            entry._setProperty(fieldId, value, 'date')

    def _hasValue(self, entryId):
        """Return 1 if Entry has a value stored for this Field, 0 otherwise."""
        fieldId = self.getId()
        entry = self.getEntryObject(entryId)
        if entry.hasProperty(fieldId):
            return 1
        return 0

    def _testValue(self, value, options={}):
        """Test a value for validity."""
        return field2date_international(value)

    # -------------------------------------------------------------------------

    _monthNames = [
        'January', 'February', 'March', 'April', 'May', 'June', 'July',
        'August', 'September', 'October', 'November', 'December']

    def renderAdd(self):
        """Return a html code for adding an Entry with this Field."""
        fieldId = self.getId()
        monthNames = self._monthNames
        if self.default:
            thisDate = DateTime(self.default)
        else:
            thisDate = DateTime()
        thisYear = thisDate.year()
        thisMonth = thisDate.month()
        thisDay = thisDate.day()
        thisHour = thisDate.hour()
        thisMinute = thisDate.minute()
        thisSecond = thisDate.second()

        result = '<select name="%s_year">' % fieldId
        for year in range(1901, 2100 + 1):
            if year == thisYear:
                result = result + '<option value="%04d" selected>%04d' % (
                    year, year)
            else:
                result = result + '<option value="%04d">%04d' % (year, year)
        result = result + '</select>\n'

        result = result + '<select name="%s_month">' % fieldId
        for month in range(1, 12 + 1):
            if month == thisMonth:
                result = result + '<option value="%d" selected>%s' % (
                    month, monthNames[month - 1])
            else:
                result = result + '<option value="%d">%s' % (
                    month, monthNames[month - 1])
        result = result + '</select>\n'

        result = result + '<select name="%s_day">' % fieldId
        for day in range(1, 31 + 1):
            if day == thisDay:
                result = result + '<option value="%d" selected>%d' % (day, day)
            else:
                result = result + '<option value="%d">%d' % (day, day)
        result = result + '</select> &nbsp; '

        result = result + '<select name="%s_hour">' % fieldId
        for hour in range(0, 24):
            if hour == thisHour:
                result = result + '<option value="%d" selected>%02d' % (
                    hour, hour)
            else:
                result = result + '<option value="%d">%02d' % (hour, hour)
        result = result + '</select>:'

        result = result + '<select name="%s_minute">' % fieldId
        for minute in range(0, 60):
            if minute == thisMinute:
                result = result + '<option value="%d" selected>%02d' % (
                    minute, minute)
            else:
                result = result + '<option value="%d">%02d' % (minute, minute)
        result = result + '</select>:'

        result = result + '<select name="%s_second">' % fieldId
        for second in range(0, 60):
            if second == thisSecond:
                result = result + '<option value="%d" selected>%02d' % (
                    second, second)
            else:
                result = result + '<option value="%d">%02d' % (second, second)
        result = result + '</select>'

        return result

    def renderEdit(self, entryId):
        """Return a html code for editing an Entry with this Field."""
        fieldId = self.getId()
        monthNames = self._monthNames
        value = self.getValue(entryId)
        if value is None:
            thisDate = DateTime()
        else:
            thisDate = DateTime(value)
        thisYear = thisDate.year()
        thisMonth = thisDate.month()
        thisDay = thisDate.day()
        thisHour = thisDate.hour()
        thisMinute = thisDate.minute()
        thisSecond = thisDate.second()

        result = '<select name="%s_year">' % fieldId
        for year in range(1901, 2100 + 1):
            if year == thisYear:
                result = result + '<option value="%04d" selected>%04d' % (
                    year, year)
            else:
                result = result + '<option value="%04d">%04d' % (year, year)
        result = result + '</select>\n'

        result = result + '<select name="%s_month">' % fieldId
        for month in range(1, 12 + 1):
            if month == thisMonth:
                result = result + '<option value="%d" selected>%s' % (
                    month, monthNames[month - 1])
            else:
                result = result + '<option value="%d">%s' % (
                    month, monthNames[month - 1])
        result = result + '</select>\n'

        result = result + '<select name="%s_day">' % fieldId
        for day in range(1, 31 + 1):
            if day == thisDay:
                result = result + '<option value="%d" selected>%d' % (day, day)
            else:
                result = result + '<option value="%d">%d' % (day, day)
        result = result + '</select> &nbsp; '

        result = result + '<select name="%s_hour">' % fieldId
        for hour in range(0, 24):
            if hour == thisHour:
                result = result + '<option value="%d" selected>%02d' % (
                    hour, hour)
            else:
                result = result + '<option value="%d">%02d' % (hour, hour)
        result = result + '</select>:'

        result = result + '<select name="%s_minute">' % fieldId
        for minute in range(0, 60):
            if minute == thisMinute:
                result = result + '<option value="%d" selected>%02d' % (
                    minute, minute)
            else:
                result = result + '<option value="%d">%02d' % (minute, minute)
        result = result + '</select>:'

        result = result + '<select name="%s_second">' % fieldId
        for second in range(0, 60):
            if second == thisSecond:
                result = result + '<option value="%d" selected>%02d' % (
                    second, second)
            else:
                result = result + '<option value="%d">%02d' % (second, second)
        result = result + '</select>'

        return result

    def renderView(self, entryId):
        """Return a html code for viewing an Entry with this Field."""
        value = self.getValue(entryId)
        if value is not None:
            return value
        return '<em>n/a</em>'

    # -------------------------------------------------------------------------

    def manage_afterAdd(self, item, container):
        """Update old entries."""
        if item is self:
            # update old entries
            default = self.default
            if default:
                for entryId in self.storage_entryIds():
                    self.setValue(entryId, default)


# =============================================================================


manage_addMetaZopeDateFieldForm = DTMLFile(
    'dtml/addMetaZopeDateField', globals())


def manage_addMetaZopeDateField(
    self, id, title='', default_year='', default_month='', default_day='',
    default_hour='', default_minute='', default_second='', REQUEST=None
):
    """Add new MetaZopeDateField."""
    instance = MetaZopeDateField(id)
    instance.title = title
    if default_year and default_month and default_day:
        instance.default = instance._testValue('%s/%s/%s %s:%s:%s' % (
            default_year, default_month, default_day, default_hour,
            default_minute, default_second))
    else:
        instance.default = instance._testValue(DateTime().Date())
    id = self._setObject(id, instance)

    if REQUEST is not None:
        REQUEST.RESPONSE.redirect(
            self.zmp2URL() + '/manage_fieldsBrowserForm?storageId=' +
            self.getStorageId())
