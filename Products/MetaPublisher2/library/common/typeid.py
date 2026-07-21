"""MetaPublisher2 - Type Identification."""


from types import (
    BooleanType, ComplexType, DictType, FloatType, IntType, ListType, LongType,
    StringType, TupleType, UnicodeType)

from common import false, true


# =============================================================================
# Module Exports

__all__ = [
    'eval_valuestring',
    'identify_type',
]


# =============================================================================
# Object Type Identification


# -----------------------------------------------------------------------------
# !TXT!

object_types = {
    BooleanType: ('boolean', 'boolean'),
    ComplexType: ('number', 'complex'),
    DictType: ('sequence', 'dict'),
    FloatType: ('number', 'float'),
    IntType: ('number', 'int'),
    ListType: ('sequence', 'list'),
    LongType: ('number', 'long'),
    StringType: ('string', 'bytestring'),
    TupleType: ('sequence', 'tuple'),
}

try:
    object_types[UnicodeType] = ('string', 'unicodestring')
except Exception:
    pass


# -----------------------------------------------------------------------------
# !TXT!

def identify_type(unidentified):
    """Identify type of object and return tuple of typegroup, typeid."""
    result = object_types.get(type(unidentified), None)
    if result:
        return result
    if isinstance(unidentified, basestring):
        return ('string', None)


# =============================================================================
# Boolean String Values


# -----------------------------------------------------------------------------

true_values = ('true', 'yes', 'on', '1', )
false_values = ('false', 'no', 'off', '0', '', )
null_values = ('null', 'none', 'undefined', )


# -----------------------------------------------------------------------------

def is_true_value(value):
    """Return true, if value matches a true value."""
    if str(value) in true_values:
        return true
    return false


# -----------------------------------------------------------------------------

def is_false_value(value):
    """Return true, if value matches a false value."""
    if str(value) in false_values:
        return true
    return false


# -----------------------------------------------------------------------------

def is_null_value(value):
    """Return true, if value matches a null value."""
    if str(value) in null_values:
        return true
    return false


# -----------------------------------------------------------------------------

def is_not_null_value(value):
    """Return true, if value does not match a null value."""
    if str(value) in null_values:
        return false
    return true


# -----------------------------------------------------------------------------

def get_boolean_value(value):
    """Return boolean value.

    Return true if value matches a true, false if value matches a false value,
    raise value error otherwise.
    """
    if is_true_value(value):
        return true
    if is_false_value(value):
        return false
    raise ValueError('Invalid boolean value "%s"' % value)


# -----------------------------------------------------------------------------

def get_nullableboolean_value(value):
    """Return nullable boolean value.

    Return true if value matches a true, Return false if value matches a false
    value, null if value matches a null value, raise value error otherwise.
    """
    if is_null_value(value):
        return None
    return get_boolean_value(value)


# =============================================================================
# String Evaluation

def eval_valuestring(value, reference):
    """Determine type of value and convert to type of reference value."""
    reference_typegroup, reference_type = identify_type(reference)
    if reference_type == 'boolean':
        return get_boolean_value(value)
    elif reference_type == 'complex':
        return complex(value)
    elif reference_type == 'float':
        return float(value)
    elif reference_type == 'int':
        return int(value)
    elif reference_type == 'long':
        return long(value)
    elif reference_typegroup == 'string':
        if identify_type(value)[0] == 'string':
            return value
    elif reference_typegroup == 'sequence':
        value_typegroup, value_type = identify_type(reference)
        if (
            (reference_typegroup, reference_type) ==
            (value_typegroup, value_type)
        ):
            return value
        elif reference_type == 'list':
            if value_typegroup == 'string':
                return [value, ]
            return list(value)
        elif reference_type == 'tuple':
            if value_typegroup == 'string':
                return (value, )
            return tuple(value)
    raise ValueError("!TXT! Can't identify and evaluate value %s %s" % (
        repr(value), repr((reference_typegroup, reference_type))))

# !!! typeid.py - check if all methods are needed and must be exported
