from typing import Dict, List, Set, Tuple
from pyvis.network import Network
import pandas as pd
import numpy as np
import json
import os

NodeId = int

def get_max_edges(nodes: Set[NodeId]) -> Tuple[NodeId, NodeId]:
    remaining_nodes = nodes.copy()
    for node in nodes:
        remaining_nodes.remove(node)
        for neighbour_node in remaining_nodes:
            yield (node, neighbour_node)

def get_max_edges_amount(nodes: Set[NodeId]) -> int:
    n = len(nodes)
    return n / 2 * (n - 1)

def visualise_graph(N: Set[NodeId], H: Dict[NodeId, bool], E: Dict[NodeId, Dict[NodeId, bool]], c: Dict[NodeId, Dict[NodeId, int]]) -> None:
    hubs = {node for node, isHub in H.items() if isHub}
    non_hubs = N - hubs

    # g = Network(width='1920px', height='1080px')
    g = Network()
    
    non_hub_edges = {hub: 0 for hub in hubs}
    connected_hub = dict()
    for non_hub in non_hubs:
        # count amount of edges from hub to non_hub
        print(E)
        print(E[non_hub])
        hub = max(E[non_hub], key=E[non_hub].get) # get hub with value equal to 1
        non_hub_edges[hub] += 1

        # store connected hub for every non_hub
        connected_hub[non_hub] = hub

    # add nodes
    g.add_nodes(list(non_hubs), size=[1 for _ in range(len(non_hubs))])
    max_edges = get_max_edges_amount(hubs)
    for hub in hubs:
        g.add_node(hub, value=max_edges + non_hub_edges[hub])

    # add all edges between hubs
    for src, target in get_max_edges(hubs):
        g.add_edge(src, target, value=c[src][target])

    # add all edges from non_hub to hub
    for src in non_hubs:
        target = connected_hub[src]
        g.add_edge(src, target, value=c[src][target])
    



    g.show_buttons()
    g.show('example.html')

visualise_graph(
    {1, 2, 3, 4, 5, 6, 7, 8, 9, 10},
    {
        "1": 0,
        "2": 0,
        "3": 1,
        "4": 0,
        "5": 0,
        "6": 1,
        "7": 1,
        "8": 0,
        "9": 0,
        "10": 0
    },
    {
        "1": {
            "3": 1,
            "6": 0,
            "7": 0
        },
        "2": {
            "3": 0,
            "6": 1,
            "7": 0
        },
        "4": {
            "3": 0,
            "6": 1,
            "7": 0
        },
        "5": {
            "3": 1,
            "6": 0,
            "7": 0
        },
        "8": {
            "3": 0,
            "6": 1,
            "7": 0
        },
        "9": {
            "3": 0,
            "6": 0,
            "7": 1
        },
        "10": {
            "3": 0,
            "6": 0,
            "7": 1
        }
    },
    {
        "1": {
            "1": 0,
            "2": 20,
            "3": 16,
            "4": 23,
            "5": 23,
            "6": 30,
            "7": 32,
            "8": 33,
            "9": 36,
            "10": 36
        },
        "2": {
            "1": 20,
            "2": 0,
            "3": 20,
            "4": 13,
            "5": 25,
            "6": 19,
            "7": 30,
            "8": 25,
            "9": 38,
            "10": 31
        },
        "3": {
            "1": 16,
            "2": 20,
            "3": 0,
            "4": 14,
            "5": 7,
            "6": 19,
            "7": 16,
            "8": 18,
            "9": 21,
            "10": 21
        },
        "4": {
            "1": 23,
            "2": 13,
            "3": 14,
            "4": 0,
            "5": 14,
            "6": 7,
            "7": 18,
            "8": 13,
            "9": 27,
            "10": 18
        },
        "5": {
            "1": 23,
            "2": 25,
            "3": 7,
            "4": 14,
            "5": 0,
            "6": 16,
            "7": 9,
            "8": 13,
            "9": 14,
            "10": 14
        },
        "6": {
            "1": 30,
            "2": 19,
            "3": 19,
            "4": 7,
            "5": 16,
            "6": 0,
            "7": 16,
            "8": 8,
            "9": 25,
            "10": 13
        },
        "7": {
            "1": 32,
            "2": 30,
            "3": 16,
            "4": 18,
            "5": 9,
            "6": 16,
            "7": 0,
            "8": 9,
            "9": 10,
            "10": 7
        },
        "8": {
            "1": 33,
            "2": 25,
            "3": 18,
            "4": 13,
            "5": 13,
            "6": 8,
            "7": 9,
            "8": 0,
            "9": 18,
            "10": 5
        },
        "9": {
            "1": 36,
            "2": 38,
            "3": 21,
            "4": 27,
            "5": 14,
            "6": 25,
            "7": 10,
            "8": 18,
            "9": 0,
            "10": 14
        },
        "10": {
            "1": 36,
            "2": 31,
            "3": 21,
            "4": 18,
            "5": 14,
            "6": 13,
            "7": 7,
            "8": 5,
            "9": 14,
            "10": 0
        }
    }
)
    