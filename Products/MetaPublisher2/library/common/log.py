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

__doc__ = """Logging Service

!TXT! module info

$Id: library/common/log.py 3 2013-05-05 18:01:53Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Exports

__all__ = [
    'log',
]


# ============================================================================
# Logging

try:

    from logging import getLogger
    logger = getLogger('MetaPublisher2')

    def log(message):
        """MetaPublisher2 log writer method"""

        logger.info(message)

except:

    from zLOG import LOG, INFO

    def log(message):
        """MetaPublisher2 log writer method"""

        LOG('MetaPublisher2', INFO, message)
