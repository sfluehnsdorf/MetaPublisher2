"""MetaPublisher2 - Presets Component.

Presets are XML files describing the Configuration, Entries and/or Publisher
components of a MetaPublisher 2. They can be used for backup, transfer and
upgrade purposes. This service features both forward and backward
compatibility so that Presets can exchanged with older and newer versions of
MetaPublisher.
"""


from Products.MetaPublisher2.library.application import (
    permission_load_presets, permission_manage_presets,
    permission_save_presets, permission_upload_presets)
from Products.MetaPublisher2.library.common import (
    ClassSecurityInfo, DTMLFile, InitializeClass)
from Products.MetaPublisher2.library.compatibility import show_future


# ============================================================================
# Module Exports

__all__ = [
    'Presets',
]


# ============================================================================
# Presets Component Mix-In Class

class Presets:
    """Presets Component Mix-In Class."""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # Presets ZMI Forms

    if show_future:

        security.declareProtected(permission_manage_presets, 'presets_form')

        presets_form = DTMLFile('presets', globals())

        security.declareProtected(
            permission_manage_presets, 'duplicate_presets_form')

        duplicate_presets_form = DTMLFile('duplicate_presets', globals())

        security.declareProtected(
            permission_manage_presets, 'delete_presets_form')

        delete_presets_form = DTMLFile('delete_presets', globals())

        security.declareProtected(
            permission_manage_presets, 'download_preset_form')

        download_preset_form = DTMLFile('download_preset', globals())

        security.declareProtected(permission_load_presets, 'load_preset_form')

        load_preset_form = DTMLFile('load_preset', globals())

        security.declareProtected(
            permission_load_presets, 'load_preset_options_form')

        load_preset_options_form = DTMLFile('load_preset_options', globals())

        security.declareProtected(
            permission_manage_presets, 'preview_preset_form')

        preview_preset_form = DTMLFile('preview_preset', globals())

        security.declareProtected(
            permission_manage_presets, 'rename_presets_form')

        rename_presets_form = DTMLFile('rename_presets', globals())

        security.declareProtected(permission_save_presets, 'save_preset_form')

        save_preset_form = DTMLFile('save_preset', globals())

        security.declareProtected(
            permission_save_presets, 'save_preset_options_form')

        save_preset_options_form = DTMLFile('save_preset_options', globals())

        security.declareProtected(
            permission_upload_presets, 'upload_preset_form')

        upload_preset_form = DTMLFile('upload_preset', globals())

    # -------------------------------------------------------------------------
    # Preset Retrieval API

    def _parse_preset(self, xmldata):
        """Parse XML Preset definition into a mapping object."""
        raise NotImplementedError

    security.declareProtected(permission_manage_presets, 'describe_preset')

    def describe_preset(self, filename):
        """Read Preset file and return description of its contents."""
        raise NotImplementedError

    security.declareProtected(permission_manage_presets, 'download_preset')

    def download_preset(self, url, REQUEST=None):
        """Download Preset file from the online repository and save locally."""
        raise NotImplementedError

    security.declareProtected(permission_manage_presets, 'get_preset')

    def get_preset(self, filename):
        """Return the contents of the specified Preset file."""
        raise NotImplementedError

    security.declareProtected(permission_manage_presets, 'get_preset_metadata')

    def get_preset_metadata(self, filename):
        """Return the metadata of the specified Preset file."""
        raise NotImplementedError

    security.declareProtected(permission_manage_presets, 'has_preset')

    def has_preset(self, filename):
        """Return True if the specified Preset file exists."""
        return filename in self.preset_ids()

    security.declareProtected(permission_load_presets, 'include_preset')

    def include_preset(self, filename, options, REQUEST=None):
        """Load a Preset file from a local file, extending current settings."""
        # TODO presets.py - include_preset - specify options parameter to map
        # plugins, fields, etc.

        raise NotImplementedError

    security.declareProtected(permission_load_presets, 'load_preset')

    def load_preset(self, filename, options, REQUEST=None):
        """Load a Preset file from a local file, replacing current settings."""
        # TODO presets.py - load_preset - specify options parameter to map
        # plugins, fields, etc.
        raise NotImplementedError

    security.declareProtected(permission_manage_presets, 'preset_ids')

    def preset_ids(self):
        """Return filenames of Presets files."""
        return map(lambda item: item[0], self.preset_items())

    security.declareProtected(permission_manage_presets, 'preset_items')

    def preset_items(self):
        """Return tuples of filename, metadata of Presets files."""
        raise NotImplementedError

    security.declareProtected(permission_manage_presets, 'preset_values')

    def preset_values(self):
        """Return metadata of Presets files."""
        return map(lambda item: item[1], self.preset_items())

    # -------------------------------------------------------------------------
    # Preset Mutation API

    def _encode_preset(self, options):
        """Encode a mapping object into XML preset definition."""
        raise NotImplementedError

    security.declareProtected(permission_manage_presets, 'duplicate_preset')

    def duplicate_preset(self, preset_id, new_id, REQUEST=None):
        """Duplicate the specified Preset file."""
        raise NotImplementedError

    security.declareProtected(permission_manage_presets, 'duplicate_presets')

    def duplicate_presets(self, preset_ids, new_ids, REQUEST=None):
        """Duplicate the specified Preset files.

        Both id lists must have the same length or ValueError is raised.
        """
        raise NotImplementedError

    security.declareProtected(permission_manage_presets, 'delete_preset')

    def delete_preset(self, preset_id, REQUEST=None):
        """Rename the specified Preset file."""
        raise NotImplementedError

    security.declareProtected(permission_manage_presets, 'delete_presets')

    def delete_presets(self, preset_ids=[], REQUEST=None):
        """Rename the specified Preset files."""
        raise NotImplementedError

    security.declareProtected(permission_manage_presets, 'rename_preset')

    def rename_preset(self, preset_id, new_id, REQUEST=None):
        """Rename the specified Preset file."""
        raise NotImplementedError

    security.declareProtected(permission_manage_presets, 'rename_presets')

    def rename_presets(self, preset_ids, new_ids, REQUEST=None):
        """Rename the specified Preset files.

        Both id lists must have the same length or ValueError is raised.
        """
        raise NotImplementedError

    security.declareProtected(permission_save_presets, 'save_preset')

    def save_preset(self, filename, options, REQUEST=None):
        """Save a Preset file to a local file."""
        # TODO presets.py - save_preset - specify options parameter to specify
        # which entries, configuration, frontends, etc. to include
        raise NotImplementedError

    security.declareProtected(permission_upload_presets, 'upload_preset')

    def upload_preset(
        self, filename, title, description, version, author, REQUEST=None
    ):
        """Upload a Preset file to the online Preset repository."""
        # TODO presets.py - upload_preset -  specify how to authenticate
        raise NotImplementedError


# ------------------------------------------------------------------------------
# Class Security

InitializeClass(Presets)


# TODO presets.py - implement
# TODO presets.py - realize backup system
# TODO presets.py - define file format
#      Title,Type,Author,Version,Vendor,Description,Homepage,File Name,Created,
#      Last Modified
#      store attributes in profile for reusability?
