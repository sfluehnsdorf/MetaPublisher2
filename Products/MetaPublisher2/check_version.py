#!/Users/sfl/zope/zope213/bin/python

from datetime import datetime
from os import listdir, stat, utime
from os.path import exists, isdir, join, splitext
from re import findall, match, MULTILINE, search
from time import gmtime

from pytz import utc

# ----------------------------------------------------------------------------

print '=' * 80
print 'checking and updating release, version and revision numbers and dates'
print

python_id = '''\$Id: (.*?) (\d+) (\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2}):(\d{2})Z (.*) \$'''
python_version = '''__version__ = '\$Revision: (\d+)\.(\d+) \$'\[11:-2\]'''

version_string = 'MetaPublisher2 %s.%s.%s'
release = 0
version = 0
revision = 0

filehandle = open('VERSION.txt')
old_version_lines = filehandle.readlines()
filehandle.close()

# ----------------------------------------------------------------------------

print 'checking and updating all python files'
counter = 0
todos = listdir('.')
match_items = []
while todos:
    filename = todos.pop(0)
    counter = counter + 1
    if isdir(filename):
        subfilenames = listdir(filename)
        if 'VERSION.txt' in subfilenames:
            print '    %-50s *** not processing Products within Products' % filename
        else:
            todos.extend(map(lambda subfilename: join(filename, subfilename), subfilenames))
    elif splitext(filename)[-1] == '.py':
        filehandle = open(filename)
        lines = filehandle.readlines()
        filehandle.close()
        matches_id = search(python_id, ''.join(lines))
        matches_version = search(python_version, ''.join(lines))
        if matches_id is None or matches_version is None:
            print '    %-50s *** no version information' % filename
        else:
            file_release, file_version = int(matches_version.group(1)), int(matches_version.group(2))
            release = max(release, file_release)
            version = max(version, file_version)
            file_filename, file_revision, file_year, file_month, file_day, file_hour, file_minute, file_second, file_user = matches_id.group(1), int(matches_id.group(2)), int(matches_id.group(3)), int(matches_id.group(4)), int(matches_id.group(5)), int(matches_id.group(6)), int(matches_id.group(7)), int(matches_id.group(8)), matches_id.group(9)
            mtime = int(stat(filename)[8])
            timestruct_stat = gmtime(mtime)
            datetime_stat = datetime(timestruct_stat[0], timestruct_stat[1], timestruct_stat[2], timestruct_stat[3], timestruct_stat[4], timestruct_stat[5], tzinfo=utc)
            datetime_file = datetime(int(matches_id.group(3)), int(matches_id.group(4)), int(matches_id.group(5)), int(matches_id.group(6)), int(matches_id.group(7)), int(matches_id.group(8)), tzinfo=utc)
            file_timedelta = datetime_stat - datetime_file
            if file_timedelta.days * 86400 + file_timedelta.seconds > 5:
                file_revision = file_revision + 1
                index = 0
                for index in range(len(lines)):
                    matches = search(python_id, lines[index])
                    if matches:
                        lines[index] = '''$Id: %s %s %4d-%02d-%02d %02d:%02d:%02dZ %s $\n''' % (
                            matches.group(1),
                            file_revision,
                            datetime_stat.year,
                            datetime_stat.month,
                            datetime_stat.day,
                            datetime_stat.hour,
                            datetime_stat.minute,
                            datetime_stat.second,
                            matches.group(9),
                        )
                        filehandle = open(filename, 'w')
                        filehandle.write(''.join(lines))
                        filehandle.close()
                        utime(filename, (mtime, mtime))
                        print '    %-50s +++ file upadted' % filename
            else:
                print '    %-50s --- file unchanged' % filename
            revision = revision + file_revision
            match_items.append((filename, file_filename, '%s.%s' % (file_release, file_version)))
print

# ----------------------------------------------------------------------------

print 'checking release and version for files'
for item in match_items:
    if item[0] != item[1]:
        print '    %-50s *** mismatch filename %s' % (item[0], item[1])
    if '%s.%s' % (release, version) != item[2]:
        print '    %-50s *** version %s mismatches %s' % (item[0], item[2], '%s.%s' % (release, version))
print

# ----------------------------------------------------------------------------

print 'processed %d files' % counter
print

print 'old product version'
for old_version_line in old_version_lines:
    print '    ' + old_version_line.strip()
print

print 'new product version'
print '    ' + version_string % (release, version, revision)
print
filehandle = open('VERSION.txt', 'w')
filehandle.write(version_string % (release, version, revision))
filehandle.close()
