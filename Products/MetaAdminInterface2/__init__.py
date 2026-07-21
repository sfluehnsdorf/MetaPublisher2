"""MetaAdminInterface."""


from MetaAdminInterface import (
  MetaAdminInterface, manage_addMetaAdminInterfaceForm,
  manage_addMetaAdminInterface)
from MetaAdminInterfaces import (
  MetaAdminInterfaces, manage_addMetaAdminInterfacesForm,
  manage_addMetaAdminInterfaces)


# =============================================================================


def initialize(context):
    """Initialize MetaAdminInterface."""
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
