"""MetaPublisher2 Resources."""


from Products.MetaPublisher2.library.application import basepath
from Products.MetaPublisher2.library.common import (
    ClassSecurityInfo, DTMLFile, ImageFile, InitializeClass, isdir, join,
    listdir, sep, splitext)


# ============================================================================
# Module Exports


__all__ = [
    'Resources',
]


# ============================================================================
# MetaPublisher2 Resources Mix-In Class


class Resources:
    """MetaPublisher2 Resources Mix-In Class."""

    security = ClassSecurityInfo()


# ------------------------------------------------------------------------------
# Class Security


InitializeClass(Resources)


# ------------------------------------------------------------------------------
# Resources Image Loader


resourcespath = join(basepath, 'resources')
todo = listdir(resourcespath)
while todo:
    filename = todo.pop()
    filepath = join(resourcespath, filename)
    if isdir(filepath):
        todo.extend(map(lambda x: join(filename, x), listdir(filepath)))
    else:
        attribute = '_'.join(filename.split(sep))
        extension = splitext(filename)[1]
        if extension in ('.gif', '.jpg', '.jpeg', '.png', '.bmp'):
            setattr(Resources, attribute, ImageFile(filepath, globals()))
            setattr(Resources, '%s__roles__' % attribute, None)
        elif extension == '.dtml':
            setattr(
                Resources, attribute[: -5],
                DTMLFile(filepath[: -5], globals()))
            setattr(Resources, '%s__roles__' % attribute[: -5], None)
