"""MetaPublisher2 - Application Exceptions.

Custom Exception resources, including an ExceptionBase that can be initialized
with arbitrary attributes. Custom Exceptions include:

- ConfigurationError for errors in the configuration file
- ConnectionError for unavailable Storages
- ConstraintError for EntryField values which exceed limits or quotas
- UnsupportedError for accessed features which are not supported
- ImmutableError for values which may not be altered
- UnreadableError for values which may not be queried
"""


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
# Exception Base Class

class ExceptionBase(Exception):
    """Exception Base Class.

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
    """Ambiguity Error Exception.

    Ambiguity errors are caused when available parameters are insufficient for
    decision making.
    """

    pass


# ==============================================================================
# Configuration Error Exception

class ConfigurationError(ExceptionBase):
    """Configuration Error Exception.

    Configuration errors are caused by parser errors of the settings.conf file
    or by invalid values of settings.
    """

    pass


# ==============================================================================
# Connection Error Exception

class ConnectionError(ExceptionBase):
    """Connection Error Exception.

    Connection errors are caused by unavailable remote data sources, i.e. when
    an SQL database is not connected.
    """

    pass


# ==============================================================================
# Constraint Error Exception

class ConstraintError(ExceptionBase):
    """Constraint Error Exception.

    Constraint errors are caused when quotas are exceeded, i.e. when a value is
    outside of predefined limit of a Field or the maximum number of Entries a
    Storage may hold is reached, or when another condition is broken.
    """

    pass


# ==============================================================================
# Immutable Error Exception

class ImmutableError(ExceptionBase):
    """Immutable Error Exception.

    Immutable errors are caused by actions on immutable data, such as modifying
    Entries of a read-only Storage.
    """

    pass


# ==============================================================================
# Unreadable Error Exception

class UnreadableError(ExceptionBase):
    """Unreadable Error Exception.

    Unreadable errors are caused by actions on unreadable data, such as
    retrieving Entries from a write-only Storage.
    """

    pass


# ==============================================================================
# Unsupported Error Exception

class UnsupportedError(ExceptionBase):
    """Unsupported Error Exception.

    Unsupported errors are caused by action which are not provided by a
    particular plugin, such as ordering Entries of an unordered Storage.
    """

    pass


# ==============================================================================
# Render Error Exception

class RenderError(ExceptionBase):
    """Render Error Exception.

    Render errors are raised when Frontend rendering fails for whatever reason.
    """

    pass
