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


from MetaStringWidget import (
    MetaStringWidget, manage_addMetaStringWidget,
    manage_MetaStringWidget_AddFormlet, manage_MetaStringWidget_EditFormlet,
    manage_MetaStringWidget_ListFormlet, manage_MetaStringWidget_ViewFormlet)
from MetaTextWidget import (
    MetaTextWidget, manage_addMetaTextWidget,
    manage_MetaTextWidget_AddFormlet, manage_MetaTextWidget_EditFormlet,
    manage_MetaTextWidget_ListFormlet, manage_MetaTextWidget_ViewFormlet)
from MetaLinesWidget import (
    MetaLinesWidget, manage_addMetaLinesWidget,
    manage_MetaLinesWidget_AddFormlet, manage_MetaLinesWidget_EditFormlet,
    manage_MetaLinesWidget_ListFormlet, manage_MetaLinesWidget_ViewFormlet)
from MetaBooleanWidget import (
    MetaBooleanWidget, manage_addMetaBooleanWidget,
    manage_MetaBooleanWidget_AddFormlet, manage_MetaBooleanWidget_EditFormlet,
    manage_MetaBooleanWidget_ListFormlet, manage_MetaBooleanWidget_ViewFormlet)
from MetaNumberWidget import (
    MetaNumberWidget, manage_addMetaNumberWidget,
    manage_MetaNumberWidget_AddFormlet, manage_MetaNumberWidget_EditFormlet,
    manage_MetaNumberWidget_ListFormlet, manage_MetaNumberWidget_ViewFormlet)
from MetaDateTimeWidget import (
    MetaDateTimeWidget, manage_addMetaDateTimeWidget,
    manage_MetaDateTimeWidget_AddFormlet,
    manage_MetaDateTimeWidget_EditFormlet,
    manage_MetaDateTimeWidget_ListFormlet,
    manage_MetaDateTimeWidget_ViewFormlet, MetaDateTimeWidget_getLanguages,
    MetaDateTimeWidget_getLanguage, MetaDateTimeWidget_getFormats)
from MetaFileWidget import (
    MetaFileWidget, manage_addMetaFileWidget,
    manage_MetaFileWidget_AddFormlet, manage_MetaFileWidget_EditFormlet,
    manage_MetaFileWidget_ListFormlet, manage_MetaFileWidget_ViewFormlet)
from MetaImageWidget import (
    MetaImageWidget, manage_addMetaImageWidget,
    manage_MetaImageWidget_AddFormlet, manage_MetaImageWidget_EditFormlet,
    manage_MetaImageWidget_ListFormlet, manage_MetaImageWidget_ViewFormlet)


# =============================================================================


def initialize(context):
    """Initialize ZopeMetaWidgets"""
    context.registerClass(
        MetaStringWidget,
        constructors=(
            manage_addMetaStringWidget,
            (
                'manage_MetaStringWidget_AddFormlet',
                manage_MetaStringWidget_AddFormlet),
            (
                'manage_MetaStringWidget_EditFormlet',
                manage_MetaStringWidget_EditFormlet),
            (
                'manage_MetaStringWidget_ListFormlet',
                manage_MetaStringWidget_ListFormlet),
            (
                'manage_MetaStringWidget_ViewFormlet',
                manage_MetaStringWidget_ViewFormlet)),
        visibility='ZMP2WidgetPlugin'
        )
    context.registerClass(
        MetaTextWidget,
        constructors=(
            manage_addMetaTextWidget,
            (
                'manage_MetaTextWidget_AddFormlet',
                manage_MetaTextWidget_AddFormlet),
            (
                'manage_MetaTextWidget_EditFormlet',
                manage_MetaTextWidget_EditFormlet),
            (
                'manage_MetaTextWidget_ListFormlet',
                manage_MetaTextWidget_ListFormlet),
            (
                'manage_MetaTextWidget_ViewFormlet',
                manage_MetaTextWidget_ViewFormlet)),
        visibility='ZMP2WidgetPlugin'
        )
    context.registerClass(
        MetaLinesWidget,
        constructors=(
            manage_addMetaLinesWidget,
            (
                'manage_MetaLinesWidget_AddFormlet',
                manage_MetaLinesWidget_AddFormlet),
            (
                'manage_MetaLinesWidget_EditFormlet',
                manage_MetaLinesWidget_EditFormlet),
            (
                'manage_MetaLinesWidget_ListFormlet',
                manage_MetaLinesWidget_ListFormlet),
            (
                'manage_MetaLinesWidget_ViewFormlet',
                manage_MetaLinesWidget_ViewFormlet)),
        visibility='ZMP2WidgetPlugin'
        )
    context.registerClass(
        MetaBooleanWidget,
        constructors=(
            manage_addMetaBooleanWidget,
            (
                'manage_MetaBooleanWidget_AddFormlet',
                manage_MetaBooleanWidget_AddFormlet),
            (
                'manage_MetaBooleanWidget_EditFormlet',
                manage_MetaBooleanWidget_EditFormlet),
            (
                'manage_MetaBooleanWidget_ListFormlet',
                manage_MetaBooleanWidget_ListFormlet),
            (
                'manage_MetaBooleanWidget_ViewFormlet',
                manage_MetaBooleanWidget_ViewFormlet)),
        visibility='ZMP2WidgetPlugin'
        )
    context.registerClass(
        MetaNumberWidget,
        constructors=(
            manage_addMetaNumberWidget,
            (
                'manage_MetaNumberWidget_AddFormlet',
                manage_MetaNumberWidget_AddFormlet),
            (
                'manage_MetaNumberWidget_EditFormlet',
                manage_MetaNumberWidget_EditFormlet),
            (
                'manage_MetaNumberWidget_ListFormlet',
                manage_MetaNumberWidget_ListFormlet),
            (
                'manage_MetaNumberWidget_ViewFormlet',
                manage_MetaNumberWidget_ViewFormlet)),
        visibility='ZMP2WidgetPlugin'
        )
    context.registerClass(
        MetaDateTimeWidget,
        constructors=(
            manage_addMetaDateTimeWidget,
            (
                'manage_MetaDateTimeWidget_AddFormlet',
                manage_MetaDateTimeWidget_AddFormlet),
            (
                'manage_MetaDateTimeWidget_EditFormlet',
                manage_MetaDateTimeWidget_EditFormlet),
            (
                'manage_MetaDateTimeWidget_ListFormlet',
                manage_MetaDateTimeWidget_ListFormlet),
            (
                'manage_MetaDateTimeWidget_ViewFormlet',
                manage_MetaDateTimeWidget_ViewFormlet),
            (
                'manage_MetaDateTimeWidget_getLanguages',
                MetaDateTimeWidget_getLanguages),
            (
                'manage_MetaDateTimeWidget_getLanguage',
                MetaDateTimeWidget_getLanguage),
            (
                'manage_MetaDateTimeWidget_getFormats',
                MetaDateTimeWidget_getFormats)),
        visibility='ZMP2WidgetPlugin'
        )
    context.registerClass(
        MetaFileWidget,
        constructors=(
            manage_addMetaFileWidget,
            (
                'manage_MetaFileWidget_AddFormlet',
                manage_MetaFileWidget_AddFormlet),
            (
                'manage_MetaFileWidget_EditFormlet',
                manage_MetaFileWidget_EditFormlet),
            (
                'manage_MetaFileWidget_ListFormlet',
                manage_MetaFileWidget_ListFormlet),
            (
                'manage_MetaFileWidget_ViewFormlet',
                manage_MetaFileWidget_ViewFormlet)),
        visibility='ZMP2WidgetPlugin'
        )
    context.registerClass(
        MetaImageWidget,
        constructors=(
            manage_addMetaImageWidget,
            (
                'manage_MetaImageWidget_AddFormlet',
                manage_MetaImageWidget_AddFormlet),
            (
                'manage_MetaImageWidget_EditFormlet',
                manage_MetaImageWidget_EditFormlet),
            (
                'manage_MetaImageWidget_ListFormlet',
                manage_MetaImageWidget_ListFormlet),
            (
                'manage_MetaImageWidget_ViewFormlet',
                manage_MetaImageWidget_ViewFormlet)),
        visibility='ZMP2WidgetPlugin'
        )


'''
TODO0
from MetaRelationWidget import (
    MetaRelationWidget, manage_addMetaRelationWidget,
    manage_MetaRelationWidget_AddFormlet,
    manage_MetaRelationWidget_EditFormlet,
    manage_MetaRelationWidget_ListFormlet,
    manage_MetaRelationWidget_ViewFormlet)
from MetaRelationsWidget import (
    MetaRelationsWidget, manage_addMetaRelationsWidget,
    manage_MetaRelationsWidget_AddFormlet,
    manage_MetaRelationsWidget_EditFormlet,
    manage_MetaRelationsWidget_ListFormlet,
    manage_MetaRelationsWidget_ViewFormlet)
from MetaSelectionWidget import (
    MetaSelectionWidget, manage_addMetaSelectionWidget,
    manage_MetaSelectionWidget_AddFormlet,
    manage_MetaSelectionWidget_EditFormlet,
    manage_MetaSelectionWidget_ListFormlet,
    manage_MetaSelectionWidget_ViewFormlet)
from MetaSelectionsWidget import (
    MetaSelectionsWidget, manage_addMetaSelectionsWidget,
    manage_MetaSelectionsWidget_AddFormlet,
    manage_MetaSelectionsWidget_EditFormlet,
    manage_MetaSelectionsWidget_ListFormlet,
    manage_MetaSelectionsWidget_ViewFormlet)
'''
