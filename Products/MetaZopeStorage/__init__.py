"""==================================================================

    M e t a   Z o p e   S t o r a g e
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


from MetaZopeStorage import (
    MetaZopeStorage, manage_addMetaZopeStorageForm,
    manage_addMetaZopeStorage)
from MetaZopeBooleanField import (
    MetaZopeBooleanField, manage_addMetaZopeBooleanFieldForm,
    manage_addMetaZopeBooleanField)
from MetaZopeDateField import (
    MetaZopeDateField, manage_addMetaZopeDateFieldForm,
    manage_addMetaZopeDateField)
from MetaZopeFileField import (
    MetaZopeFileField, manage_addMetaZopeFileFieldForm,
    manage_addMetaZopeFileField)
from MetaZopeFloatField import (
    MetaZopeFloatField, manage_addMetaZopeFloatFieldForm,
    manage_addMetaZopeFloatField)
from MetaZopeImageField import (
    MetaZopeImageField, manage_addMetaZopeImageFieldForm,
    manage_addMetaZopeImageField)
from MetaZopeIntegerField import (
    MetaZopeIntegerField, manage_addMetaZopeIntegerFieldForm,
    manage_addMetaZopeIntegerField)
from MetaZopeLinesField import (
    MetaZopeLinesField, manage_addMetaZopeLinesFieldForm,
    manage_addMetaZopeLinesField)
from MetaZopeLongField import (
    MetaZopeLongField, manage_addMetaZopeLongFieldForm,
    manage_addMetaZopeLongField)
from MetaZopeStringField import (
    MetaZopeStringField, manage_addMetaZopeStringFieldForm,
    manage_addMetaZopeStringField)
from MetaZopeTextField import (
    MetaZopeTextField, manage_addMetaZopeTextFieldForm,
    manage_addMetaZopeTextField)
from MetaZopeULinesField import (
    MetaZopeULinesField, manage_addMetaZopeULinesFieldForm,
    manage_addMetaZopeULinesField)
from MetaZopeUStringField import (
    MetaZopeUStringField, manage_addMetaZopeUStringFieldForm,
    manage_addMetaZopeUStringField)
from MetaZopeUTextField import (
    MetaZopeUTextField, manage_addMetaZopeUTextFieldForm,
    manage_addMetaZopeUTextField)


# =============================================================================


def initialize(context):
    """Initialize MetaZopeStorage"""
    context.registerClass(
        MetaZopeStorage,
        constructors=(
            manage_addMetaZopeStorageForm, manage_addMetaZopeStorage,),
        visibility='ZMP2StoragePlugin')
    context.registerClass(
        MetaZopeBooleanField,
        meta_type='MetaZopeStorage BooleanField',
        permission="Add Boolean Fields",
        constructors=(
            manage_addMetaZopeBooleanFieldForm,
            manage_addMetaZopeBooleanField),
        icon='www/FieldBoolean.gif',
        visibility='ZMP2FieldPlugin')
    context.registerClass(
        MetaZopeDateField,
        meta_type='MetaZopeStorage DateField',
        permission="Add Date Intl Fields",
        constructors=(
            manage_addMetaZopeDateFieldForm, manage_addMetaZopeDateField),
        icon='www/FieldDate.gif',
        visibility='ZMP2FieldPlugin')
    context.registerClass(
        MetaZopeFileField,
        meta_type='MetaZopeStorage FileField',
        permission="Add File Fields",
        constructors=(
            manage_addMetaZopeFileFieldForm, manage_addMetaZopeFileField),
        icon='www/FieldFile.gif',
        visibility='ZMP2FieldPlugin')
    context.registerClass(
        MetaZopeFloatField,
        meta_type='MetaZopeStorage FloatField',
        permission="Add Float Fields",
        constructors=(
            manage_addMetaZopeFloatFieldForm, manage_addMetaZopeFloatField),
        icon='www/FieldFloat.gif',
        visibility='ZMP2FieldPlugin')
    context.registerClass(
        MetaZopeImageField,
        meta_type='MetaZopeStorage ImageField',
        permission="Add Image Fields",
        constructors=(
            manage_addMetaZopeImageFieldForm, manage_addMetaZopeImageField),
        icon='www/FieldImage.gif',
        visibility='ZMP2FieldPlugin')
    context.registerClass(
        MetaZopeIntegerField,
        meta_type='MetaZopeStorage IntegerField',
        permission="Add Integer Fields",
        constructors=(
            manage_addMetaZopeIntegerFieldForm,
            manage_addMetaZopeIntegerField),
        icon='www/FieldInteger.gif',
        visibility='ZMP2FieldPlugin')
    context.registerClass(
        MetaZopeLinesField,
        meta_type='MetaZopeStorage LinesField',
        permission="Add Lines Fields",
        constructors=(
            manage_addMetaZopeLinesFieldForm, manage_addMetaZopeLinesField),
        icon='www/FieldLines.gif',
        visibility='ZMP2FieldPlugin')
    context.registerClass(
        MetaZopeLongField,
        meta_type='MetaZopeStorage LongField',
        permission="Add Long Fields",
        constructors=(
            manage_addMetaZopeLongFieldForm, manage_addMetaZopeLongField),
        icon='www/FieldLong.gif',
        visibility='ZMP2FieldPlugin')
    context.registerClass(
        MetaZopeStringField,
        meta_type='MetaZopeStorage StringField',
        permission="Add String Fields",
        constructors=(
            manage_addMetaZopeStringFieldForm, manage_addMetaZopeStringField),
        icon='www/FieldString.gif',
        visibility='ZMP2FieldPlugin')
    context.registerClass(
        MetaZopeTextField,
        meta_type='MetaZopeStorage TextField',
        permission="Add Text Field Fields",
        constructors=(
            manage_addMetaZopeTextFieldForm, manage_addMetaZopeTextField),
        icon='www/FieldText.gif',
        visibility='ZMP2FieldPlugin')
    context.registerClass(
        MetaZopeULinesField,
        meta_type='MetaZopeStorage UnicodeLineField',
        permission="Add Unicode Line Fields",
        constructors=(
            manage_addMetaZopeULinesFieldForm, manage_addMetaZopeULinesField),
        icon='www/FieldULines.gif',
        visibility='ZMP2FieldPlugin')
    context.registerClass(
        MetaZopeUStringField,
        meta_type='MetaZopeStorage UnicodeStringField',
        permission="Add Unicode String Fields",
        constructors=(
            manage_addMetaZopeUStringFieldForm,
            manage_addMetaZopeUStringField),
        icon='www/FieldUString.gif',
        visibility='ZMP2FieldPlugin')
    context.registerClass(
        MetaZopeUTextField,
        meta_type='MetaZopeStorage UnicodeTextField',
        permission="Add Unicode Text Fields",
        constructors=(
            manage_addMetaZopeUTextFieldForm, manage_addMetaZopeUTextField),
        icon='www/FieldUText.gif',
        visibility='ZMP2FieldPlugin')


'''
TODO:
from MetaZopeComplexField import (
    MetaZopeComplexField, manage_addMetaZopeComplexFieldForm,
    manage_addMetaZopeComplexField)
from MetaZopeFolderField import (
    MetaZopeFolderField, manage_addMetaZopeFolderFieldForm,
    manage_addMetaZopeFolderField)
from MetaZopeRelationField import (
    MetaZopeRelationField, manage_addMetaZopeRelationFieldForm,
    manage_addMetaZopeRelationField)
from MetaZopeRelationsField import (
    MetaZopeRelationsField, manage_addMetaZopeRelationsFieldForm,
    manage_addMetaZopeRelationsField)
from MetaZopeSelectionField import (
    MetaZopeSelectionField, manage_addMetaZopeSelectionFieldForm,
    manage_addMetaZopeSelectionField)
from MetaZopeSelectionsField import (
    MetaZopeSelectionsField, manage_addMetaZopeSelectionsFieldForm,
    manage_addMetaZopeSelectionsField)
'''
