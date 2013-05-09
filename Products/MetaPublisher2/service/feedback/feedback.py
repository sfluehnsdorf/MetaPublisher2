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

__doc__ = """Feedback Component

Simple service providing access to the Web based feedback service for a variety
of types of feedback. The ZMI forms simply include the feedback service's web
pages on the MetaPublisher website at http://metapublisher.org.

$Id: service/feedback/feedback.py 5 2013-05-09 00:08:29Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.library import ClassSecurityInfo, DTMLFile,\
    InitializeClass, permission_zmi


# ============================================================================
# Module Exports

__all__ = [
    'Feedback',
]


# ============================================================================
# Feedback Component Mix-In Class

class Feedback:
    """!TXT! Feedback Component Mix-In Class"""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # Feedback ZMI

    security.declareProtected(permission_zmi, 'feedback_form')

    feedback_form = DTMLFile('feedback', globals())

    # ------------------------------------------------------------------------
    # Feedback Retrieval API

    security.declareProtected(permission_zmi, 'get_feedback_url')

    def get_feedback_url(self):
        """!TXT! Return the URL for the online feedback service"""

        return self.get_setting('service_feedback_url')

# ----------------------------------------------------------------------------
# Class Security

InitializeClass(Feedback)

# !!! feedback.py - implement online feedback service
# !!! feedback.py - replace local form with online form (include via ajax?)
