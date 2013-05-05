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

__doc__ = """EntryGraphs Component

$Id: data/entries/entrygraphs.py 4 2012-08-09 19:48:00Z sfluehnsdorf $
"""

__version__ = '$Revision: 2.3 $'[11:-2]


# ============================================================================
# Module Imports

from Products.MetaPublisher2.library import ClassSecurityInfo, InitializeClass, permission_access_entries, permission_change_entries


# ============================================================================
# Module Exports

__all__ = [
    'EntryGraphs',
]


# ============================================================================
# EntryGraphs Mix-In Class

class EntryGraphs:
    """EntryGraphs Mix-In Class"""

    security = ClassSecurityInfo()

    # ------------------------------------------------------------------------
    # Entry Graph Retrieval API

    # TODO: realise graphs via field? methods accept a field_id to identify that field
    #def has_edge(self, source, graph_field_id, entry_id, destination_entry_id=None):
    #def has_any_edges(self, source, graph_field_id, entry_id, destination_entry_ids=None):
    #def has_all_edges(self, source, graph_field_id, entry_id, destination_entry_ids=None):
    #def get_edges(self, source, graph_field_id, entry_id):
    #def get_edge(self, source, graph_field_id, entry_id, destination_entry_id):
    #def find_path(self, source, graph_field_id, entry_id, destination_entry_id):
    #def find_paths(self, source, graph_field_id, entry_id, destination_entry_id):
    #def find_shortest_path(self, source, graph_field_id, entry_id, destination_entry_id):
    #def find_longest_path(self, source, graph_field_id, entry_id, destination_entry_id):

    # ------------------------------------------------------------------------
    # Entry Graph Mutation API

    # TODO: realise graphs via field? methods accept a field_id to identify that field
    #def add_edge(self, source, graph_field_id, entry_id, weight=1.0, direction=0):
    #def edit_edge(self, source, graph_field_id, entry_id, weight=None, direction=None):
    #def delete_edge(self, source, graph_field_id, entry_id, destination_entry_id):
    #def delete_edges(self, source, graph_field_id, entry_id, destination_entry_ids=[]):
    #def clear_edges(self, source, graph_field_id, entry_id):

    #def duplicate_edge():
    #def duplicate_edges():
    #def move_edge():
    #def move_edges():
    #def weigh_edge(self, source, graph_field_id, entry_id, destination_entry_id, weight):
    #def point_edge(self, source, graph_field_id, entry_id, destination_entry_id, new_entry_id):
    #def contract_edge():
    #def contract_edges():

    # - möglicherweise: ermitteln ob zwei knoten benachbart, verbunden oder adjazent sind
    # - möglicherweise: ermitteln ob ein knoten ein vorgänger oder nachfolger eines anderen ist
    # - möglicherweise: ermitteln ob ein knoten isoliert ist
    # - möglicherweise: ermitteln des grads zweier knoten
    # - möglicherweise: ermitteln ob der graph zusammenhängend, bipartit, planar, eulersch, hamiltonisch ist
    # - möglicherweise: kantenkontraktion (schwierig, da die zusammenführung der kanten ein "vermengen" der daten der kanten erfordert)
    # - möglicherweise: erstellen eines kantengraphes
    # - möglicherweise: erstellen eines kantendigraphes
    # - möglicherweise: erstellen eines komplementärgraphens
    # - möglicherweise: operationen auf teilgraphen

    # def create_line_graph
    # def create_line_digraph
    # def create_complement_graph

# ----------------------------------------------------------------------------
# Class Security

InitializeClass(EntryGraphs)

# !!! entrygraphs.py - define api
