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
    


    g.show_buttons() # TODO: note verbinding internet readme
    g.show('example.html') # TODO: change name with os

def main():
    print('Visualised graph demo.')
    visualise_graph(
        {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15},
        {
            1: 1,
            2: 1,
            3: 1,
            4: 1,
            5: 1,
            6: 1,
            7: 1,
            8: 0,
            9: 0,
            10: 0,
            11: 0,
            12: 0,
            13: 0,
            14: 0,
            15: 0
        },
        {
            8: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
                6: 0,
                7: 1
            },
            9: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 1,
                6: 0,
                7: 0
            },
            10: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
                6: 0,
                7: 1
            },
            11: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
                6: 0,
                7: 1
            },
            12: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
                6: 0,
                7: 1
            },
            13: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 1,
                6: 0,
                7: 0
            },
            14: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 1,
                6: 0,
                7: 0
            },
            15: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
                6: 0,
                7: 1
            }
        },
        {
            1: {
                1: 0,
                2: 12,
                3: 18,
                4: 37,
                5: 16,
                6: 18,
                7: 23,
                8: 32,
                9: 21,
                10: 25,
                11: 30,
                12: 37,
                13: 27,
                14: 32,
                15: 33
            },
            2: {
                1: 12,
                2: 0,
                3: 10,
                4: 26,
                5: 20,
                6: 15,
                7: 19,
                8: 26,
                9: 25,
                10: 24,
                11: 27,
                12: 32,
                13: 30,
                14: 33,
                15: 32
            },
            3: {
                1: 18,
                2: 10,
                3: 0,
                4: 19,
                5: 18,
                6: 9,
                7: 10,
                8: 16,
                9: 22,
                10: 17,
                11: 18,
                12: 22,
                13: 25,
                14: 26,
                15: 25
            },
            4: {
                1: 37,
                2: 26,
                3: 19,
                4: 0,
                5: 35,
                6: 25,
                7: 22,
                8: 17,
                9: 37,
                10: 28,
                11: 25,
                12: 21,
                13: 39,
                14: 36,
                15: 33
            },
            5: {
                1: 16,
                2: 20,
                3: 18,
                4: 35,
                5: 0,
                6: 10,
                7: 15,
                8: 24,
                9: 5,
                10: 13,
                11: 18,
                12: 27,
                13: 11,
                14: 17,
                15: 18
            },
            6: {
                1: 18,
                2: 15,
                3: 9,
                4: 25,
                5: 10,
                6: 0,
                7: 6,
                8: 15,
                9: 13,
                10: 9,
                11: 12,
                12: 19,
                13: 16,
                14: 18,
                15: 17
            },
            7: {
                1: 23,
                2: 19,
                3: 10,
                4: 22,
                5: 15,
                6: 6,
                7: 0,
                8: 10,
                9: 16,
                10: 7,
                11: 8,
                12: 14,
                13: 17,
                14: 17,
                15: 15
            },
            8: {
                1: 32,
                2: 26,
                3: 16,
                4: 17,
                5: 24,
                6: 15,
                7: 10,
                8: 0,
                9: 24,
                10: 13,
                11: 9,
                12: 6,
                13: 24,
                14: 20,
                15: 16
            },
            9: {
                1: 21,
                2: 25,
                3: 22,
                4: 37,
                5: 5,
                6: 13,
                7: 16,
                8: 24,
                9: 0,
                10: 11,
                11: 16,
                12: 25,
                13: 6,
                14: 12,
                15: 15
            },
            10: {
                1: 25,
                2: 24,
                3: 17,
                4: 28,
                5: 13,
                6: 9,
                7: 7,
                8: 13,
                9: 11,
                10: 0,
                11: 5,
                12: 14,
                13: 11,
                14: 9,
                15: 8
            },
            11: {
                1: 30,
                2: 27,
                3: 18,
                4: 25,
                5: 18,
                6: 12,
                7: 8,
                8: 9,
                9: 16,
                10: 5,
                11: 0,
                12: 9,
                13: 15,
                14: 11,
                15: 8
            },
            12: {
                1: 37,
                2: 32,
                3: 22,
                4: 21,
                5: 27,
                6: 19,
                7: 14,
                8: 6,
                9: 25,
                10: 14,
                11: 9,
                12: 0,
                13: 24,
                14: 18,
                15: 14
            },
            13: {
                1: 27,
                2: 30,
                3: 25,
                4: 39,
                5: 11,
                6: 16,
                7: 17,
                8: 24,
                9: 6,
                10: 11,
                11: 15,
                12: 24,
                13: 0,
                14: 8,
                15: 11
            },
            14: {
                1: 32,
                2: 33,
                3: 26,
                4: 36,
                5: 17,
                6: 18,
                7: 17,
                8: 20,
                9: 12,
                10: 9,
                11: 11,
                12: 18,
                13: 8,
                14: 0,
                15: 4
            },
            15: {
                1: 33,
                2: 32,
                3: 25,
                4: 33,
                5: 18,
                6: 17,
                7: 15,
                8: 16,
                9: 15,
                10: 8,
                11: 8,
                12: 14,
                13: 11,
                14: 4,
                15: 0
            }
        }
    )

if __name__ == '__main__':
    main()
        