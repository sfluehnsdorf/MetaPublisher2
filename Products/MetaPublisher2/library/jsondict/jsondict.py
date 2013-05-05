# -*- coding: iso-8859-15 -*-
# ============================================================================
#
#                                J S O N  D i c t
#
# ----------------------------------------------------------------------------
# Copyright (c) 2013, Sebastian Lühnsdorf - Web-Solutions and others
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

__doc__ = """!TXT!

!TXT!

$Id: library/jsondict/jsondict.py 2 2013-04-25 02:31:34Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Exports

__all__ = [
    'JSONDict',
]


# ============================================================================
# JSONDict Mix-In Class

class JSONDict:
    """!TXT!"""

    # !!! jsondict.py - implement encode_JSONDict

    def encode_JSONDict(self, mapping):
        """!TXT!"""

        raise NotImplemented

    # !!! jsondict.py - implement decode_JSONDict

    def decode_JSONDict(self, json):
        """!TXT!"""

        raise NotImplemented
