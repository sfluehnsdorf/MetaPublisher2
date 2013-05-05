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

__doc__ = """Application Exceptions

Custom Exception resources, including an ExceptionBase that can be initialized
with arbitrary attributes. Custom Exceptions include:

- ConfigurationError for errors in the configuration file
- ConnectionError for unavailable Storages
- ConstraintError for EntryField values which exceed limits or quotas
- UnsupportedError for accessed features which are not supported
- ImmutableError for values which may not be altered
- UnreadableError for values which may not be queried

$Id: library/application/exceptions.py 3 2012-02-17 15:45:00Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ==============================================================================
# Module Exports

__all__ = [
    'AmbiguityError',
    'ConfigurationError',
    'ConnectionError',
    'ConstraintError',
    'ImmutableError',
    'RenderError',
    'UnsupportedError',
    'UnreadableError',
]


# ============================================================================
# ExceptionBase

class ExceptionBase(Exception):
    """Exception Base Class

    Exception base class that can be initialized with arbitrary attributes.
    """

    def __init__(self, msg, **args):
        assert msg
        self.msg = msg
        for key in args.keys():
            setattr(self, key, args[key])

    def __str__(self):
        return self.msg


# ============================================================================
# Ambiguity Error Exception

class AmbiguityError(ExceptionBase):
    """Ambiguity Error Exception

    Ambiguity errors are caused when available parameters are insufficient for
    decision making.
    """

    pass


# ==============================================================================
# Configuration Error Exception

class ConfigurationError(ExceptionBase):
    """Configuration Error Exception

    Configuration errors are caused by parser errors of the settings.conf file
    or by invalid values of settings.
    """

    pass


# ==============================================================================
# Connection Error Exception

class ConnectionError(ExceptionBase):
    """Connection Error Exception

    Connection errors are caused by unavailable remote data sources, i.e. when
    an SQL database is not connected.
    """

    pass


# ==============================================================================
# Constraint Error Exception

class ConstraintError(ExceptionBase):
    """Constraint Error Exception

    Constraint errors are caused when quotas are exceeded, i.e. when a value is
    outside of predefined limit of a Field or the maximum number of Entries a
    Storage may hold is reached, or when another condition is broken.
    """

    pass


# ==============================================================================
# Immutable Error Exception

class ImmutableError(ExceptionBase):
    """Immutable Error Exception

    Immutable errors are caused by actions on immutable data, such as modifying
    Entries of a read-only Storage.
    """

    pass


# ==============================================================================
# Unreadable Error Exception

class UnreadableError(ExceptionBase):
    """Unreadable Error Exception

    Unreadable errors are caused by actions on unreadable data, such as
    retrieving Entries from a write-only Storage.
    """

    pass


# ==============================================================================
# Unsupported Error Exception

class UnsupportedError(ExceptionBase):
    """Unsupported Error Exception

    Unsupported errors are caused by action which are not provided by a
    particular plugin, such as ordering Entries of an unordered Storage.
    """

    pass


# ==============================================================================
# Render Error Exception

class RenderError(ExceptionBase):
    """Render Error Exception

    Render errors are raised when Frontend rendering fails for whatever reason.
    """

    pass
