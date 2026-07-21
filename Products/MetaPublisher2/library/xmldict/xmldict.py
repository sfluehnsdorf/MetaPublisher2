"""XMLDict."""


from types import (
    BooleanType, ComplexType, DictType, FloatType, IntType, ListType, LongType,
    NoneType, StringType, TupleType, UnicodeType)
try:
    from elementtree.ElementTree import Element, tostring, fromstring
except ImportError:
    from xml.etree.ElementTree import Element, tostring, fromstring


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
except Exception:
    true = 1
    false = 0


# ============================================================================
# XMLDict Mix-In Class

class XMLDict:
    """XMLDict Mix-In Class."""

    def encode_XMLDict(self, mapping):
        """Encode a mapping to XMLDict."""

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
            elif (
                isinstance(value, StringType) or
                isinstance(value, UnicodeType)
            ):
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
                raise TypeError(
                    "Encoding of %s not supported (Key: %s)" % (
                        repr(value), key))
            return element

        root = Element("data")
        for key in mapping.keys():
            root.append(self.encode(key, mapping[key]))
        return tostring(root)

    def decode_XMLDict(self, xml):
        """Decode an XMLDict to mapping."""

        def decode(element):
            value = None
            element_type = element.get('type', 'none')
            if element_type == 'none':
                value = None
            elif element_type == 'bool':
                value = element.get('value') == 'true' and true or false
            elif element_type == 'complex':
                value = complex(
                    float(element.get('re')),
                    float(element.get('im')))
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
                raise TypeError(
                    'Decoding of type "%s" not supported (Source: %s)' % (
                        element_type, element))
            return element.tag, value

        result = {}
        root = fromstring(xml)
        for element in root.getchildren():
            key, value = decode(element)
            result[key] = value
        return result
