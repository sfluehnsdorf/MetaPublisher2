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

__doc__ = """!TXT! Deprecation Information

!TXT! module info

$Id: library/compatibility/deprecation.py 5 2013-05-08 20:14:59Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from logging import getLogger
from warnings import warn


# ============================================================================
# Module Exports

__all__ = [
    'deprecated_form',
    'deprecated_method',
]


# ============================================================================
# Logger Initialization

logger = getLogger('MetaPublisher2')


# ============================================================================
# Deprecated Forms

def deprecated_form(form_name):
    """!TXT!"""

    message = 'The "%s" form is deprecated and will be removed in a future release!' % form_name

    logger.info(message)
    warn(message, category=DeprecationWarning, stacklevel=2)


# ============================================================================
# Deprecated Methods

def deprecated_method(method_name):
    """!TXT!"""

    message = 'The "%s" method is deprecated and will be removed in a future release!' % method_name

    logger.info(message)
    warn(message, category=DeprecationWarning, stacklevel=2)
