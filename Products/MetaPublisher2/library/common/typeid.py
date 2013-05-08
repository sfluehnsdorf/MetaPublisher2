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

__doc__ = """!TXT! Type Identification

!TXT! module info
Resources for type identification of variables.

$Id: library/common/typeid.py 6 2013-05-08 20:15:03Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from types import StringTypes, BooleanType, ComplexType, DictType, FloatType, IntType, ListType, LongType, StringType, TupleType, UnicodeType


# ============================================================================
# Module Exports

__all__ = [
    'eval_valuestring',
    'identify_type',
]


# ============================================================================
# Object Type Identification


# ----------------------------------------------------------------------------
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
except:
    pass


# ----------------------------------------------------------------------------
# !TXT!

def identify_type(unidentified):
    """!TXT! identify type of object and return tuple of typegroup, typeid"""

    result = object_types.get(type(unidentified), None)
    if result:
        return result
    if isinstance(unidentified, basestring):
        return ('string', None)


# ============================================================================
# Boolean String Values


# ----------------------------------------------------------------------------
# !TXT!

true_values = ('true', 'yes', 'on', '1', )
false_values = ('false', 'no', 'off', '0', '', )
null_values = ('null', 'none', 'undefined', )


# ----------------------------------------------------------------------------
# !TXT!

def is_true_value(value):
    """!TXT! return true, if value matches a true value"""

    if str(value) in true_values:
        return true
    return false


# ----------------------------------------------------------------------------
# !TXT!

def is_false_value(value):
    """!TXT! return true, if value matches a false value"""

    if str(value) in false_values:
        return true
    return false


# ----------------------------------------------------------------------------
# !TXT!

def is_null_value(value):
    """!TXT! return true, if value matches a null value"""

    if str(value) in null_values:
        return true
    return false


# ----------------------------------------------------------------------------
# !TXT!

def is_not_null_value(value):
    """!TXT! return true, if value does not match a null value"""

    if str(value) in null_values:
        return false
    return true


# ----------------------------------------------------------------------------
# !TXT!

def get_boolean_value(value):
    """!TXT! return true if value matches a true, false if value matches a false value, raise value error otherwise"""

    if is_true_value(value):
        return true
    if is_false_value(value):
        return false
    raise ValueError('Invalid boolean value "%s"' % value)


# ----------------------------------------------------------------------------
# !TXT!

def get_nullableboolean_value(value):
    """!TXT! return true if value matches a true, false if value matches a false value, null if value matches a null value, raise value error otherwise"""

    if is_null_value(value):
        return None
    return get_boolean_value(value)


# ============================================================================
# String Evaluation

def eval_valuestring(value, reference):
    """!TXT! determine type of value and cast it based on type of reference value"""

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
        if (reference_typegroup, reference_type) == (value_typegroup, value_type):
            return value
        elif reference_type == 'list':
            if value_typegroup == 'string':
                return [value, ]
            return list(value)
        elif reference_type == 'tuple':
            if value_typegroup == 'string':
                return (value, )
            return tuple(value)
    raise ValueError("Can't identify and evaluate value %s %s" % (repr(value), repr((reference_typegroup, reference_type))))

# !!! typeid.py - check if all methods are needed and must be exported
