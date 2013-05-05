# -*- coding: iso-8859-15 -*-
# ============================================================================
#
#                                 X M L  D i c t
#
# ----------------------------------------------------------------------------
# Copyright (c) 2011-2013, Sebastian Lühnsdorf - Web-Solutions and others
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

__doc__ = """XMLDict

$Id: xmldict/xmldict.py 5 2012-02-17 15:45:00Z sfluehnsdorf $
"""

__version__ = '$Revision: 1.2 $'[11:-2]


# ============================================================================
# Module Imports

from types import BooleanType, ComplexType, DictType, FloatType, IntType, ListType, LongType, NoneType, StringType, TupleType, UnicodeType
try:
    from elementtree.ElementTree import Element, tostring, fromstring
except ImportError:
    try:
        from xml.etree.ElementTree import Element, tostring, fromstring
    except ImportError:
        from etree.ElementTree import Element, tostring, fromstring


# ============================================================================
# Module Exports

__all__ = [
    'XMLDict',
]


# ============================================================================
# Booleans

try:
    true = True
    false = False
except:
    true = 1
    false = 0


# ============================================================================
# XMLDict Mix-In Class

class XMLDict:
    """!TXT!"""

    def encode_XMLDict(self, mapping):
        """!TXT!"""

        def encode(key, value):
            element = Element(key)
            if isinstance(value, NoneType):
                element.attrib['type'] = 'none'
            elif isinstance(value, BooleanType):
                element.attrib['type'] = 'bool'
                element.attrib['value'] = value and 'true' or 'false'
            elif isinstance(value, ComplexType):
                element.attrib['type'] = 'complex'
                element.attrib['re'] = repr(value.real)
                element.attrib['im'] = repr(value.imag)
            elif isinstance(value, FloatType):
                element.attrib['type'] = 'float'
                element.attrib['value'] = repr(value)
            elif isinstance(value, IntType):
                element.attrib['type'] = 'int'
                element.attrib['value'] = repr(value)
            elif isinstance(value, LongType):
                element.attrib['type'] = 'long'
                element.attrib['value'] = repr(value)
            elif isinstance(value, StringType) or isinstance(value, UnicodeType):
                element.attrib['type'] = 'cdata'
                element.text = u"<![CDATA[%s]]>" % value
            elif isinstance(value, DictType):
                element.attrib['type'] = 'dict'
                for key in value.keys():
                    element.append(encode(key, value[key]))
            elif isinstance(value, ListType):
                element.attrib['type'] = 'list'
                for subvalue in value:
                    element.append(encode('value', subvalue))
            elif isinstance(value, TupleType):
                element.attrib['type'] = 'tuple'
                for subvalue in value:
                    element.append(encode('value', subvalue))
            else:
                raise TypeError("Encoding of %s not supported (Key: %s)" % (repr(value), key))
            return element

        root = Element("data")
        for key in mapping.keys():
            root.append(self.encode(key, mapping[key]))
        return tostring(root)

    def decode_XMLDict(self, xml):
        """!TXT!"""

        def decode(element):
            value = None
            element_type = element.get('type', 'none')
            if element_type == 'none':
                value = None
            elif element_type == 'bool':
                value = element.get('value') == 'true' and true or false
            elif element_type == 'complex':
                value = complex(float(element.get('re')), float(element.get('im')))
            elif element_type == 'float':
                value = float(element.get('value'))
            elif element_type == 'int':
                value = int(element.get('value'))
            elif element_type == 'long':
                value = long(element.get('value'))
            elif element_type == 'str':
                value = unicode(element.text)
            elif element_type == 'cdata':
                value = unicode(element.text)[9: -3]
            elif element_type == 'dict':
                value = {}
                for subelement in element.getchildren():
                    subname, subvalue = decode(subelement)
                    value[subname] = subvalue
            elif element_type == 'list':
                value = []
                for subelement in element.getchildren():
                    subname, subvalue = decode(subelement)
                    value.append(subvalue)
            elif element_type == 'tuple':
                value = []
                for subelement in element.getchildren():
                    subname, subvalue = decode(subelement)
                    value.append(subvalue)
                value = tuple(value)
            else:
                raise TypeError('Decoding of type "%s" not supported (Source: %s)' % (element_type, element))
            return element.tag, value

        result = {}
        root = fromstring(xml)
        for element in root.getchildren():
            key, value = decode(element)
            result[key] = value
        return result
