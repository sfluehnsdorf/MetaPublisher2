"""==================================================================

               M e t a   A d m i n   I n t e r f a c e
  -----------------------------------------------------------------

    Copyright (c) 2005, Sebastian Luehnsdorf - Web-Solutions Gbr.
    http://zopemeta.com - http://luehnsdorf.de

    This software is subject to the provisions of the
    Zope Public License, Version 2.0 (ZPL).

    A copy of the ZPL should accompany this distribution.

    THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR
    IMPLIED WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED
    TO, THE IMPLIED WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST
    INFRINGEMENT, AND FITNESS FOR A PARTICULAR PURPOSE.

=================================================================="""


from MetaAdminInterface import (
  MetaAdminInterface, manage_addMetaAdminInterfaceForm,
  manage_addMetaAdminInterface)
from MetaAdminInterfaces import (
  MetaAdminInterfaces, manage_addMetaAdminInterfacesForm,
  manage_addMetaAdminInterfaces)


# ===================================================================


def initialize(context):
    """Initialize MetaAdminInterface"""

    context.registerClass(
        MetaAdminInterface,
        constructors=(
            manage_addMetaAdminInterfaceForm,
            manage_addMetaAdminInterface,
        ),
        visibility='ZMP2InterfacePlugin'
        )

    context.registerClass(
        MetaAdminInterfaces,
        constructors=(
            manage_addMetaAdminInterfacesForm,
            manage_addMetaAdminInterfaces,
        ),
        visibility='ZMP2InterfacePlugin'
        )
