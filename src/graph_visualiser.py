from typing import Dict, List, Set, Tuple
from pyvis.network import Network
import pandas as pd
import numpy as np
import pathlib
import json
import os

NodeId = int

GRAPHS_DIR= os.path.abspath(r'./graphs')
MIN_NODE_SIZE = 20
MAX_NODE_SIZE = 55
MIN_EDGE_WIDTH = 7
MAX_EDGE_WIDTH = 25
# TODO: color for hub and color for non-hub
GRAPH_OPTIONS = {
    'nodes': {
        'borderWidthSelected': 3,
        'color': {
            'border': 'rgba(43,124,233,1)',
            'background': 'rgba(151,194,252,1)',
            'highlight': {
                'border': 'rgba(43,124,233,1)',
                'background': 'rgba(210,229,255,1)'
            },
            'hover': {
                'border': 'rgba(43,124,233,1)',
                'background': 'rgba(210,229,255,1)'
            }
        },
        'scaling': {
            'min': MIN_NODE_SIZE,
            'max': MAX_NODE_SIZE,
        },
        "font": {
            "size": 20
        }
    },
    'edges': {
        'color': {
            'inherit': False,
            'color': 'rgba(43,124,233,1)',
            'highlight': 'rgba(114,166,229,1)',
            'hover': 'rgba(114,166,229,1)'
        },
        'hoverWidth': 1.5,
        'smooth': False,
        'scaling': {
            'min': MIN_EDGE_WIDTH,
            'max': MAX_EDGE_WIDTH
        },
        'smooth': {
            'type': 'discrete',
            'roundness': 0.6
        },
    },
    'physics': {
        'hierarchicalRepulsion': {
            'centralGravity': 0,
            'springLength': 150,
            'springConstant': 0.01,
            'damping': 0.09,
            'nodeDistance': 300
        },
        'minVelocity': 0.75,
        'solver': 'hierarchicalRepulsion'
    },
    # 'physics': {
    #     'barnesHut': {
    #         'centralGravity': 0,
    #         'springLength': 300,
    #         'springConstant': 0.01,
    #         'damping': 0.09,
    #     },
    #     'minVelocity': 0.75,
    #     'solver': 'barnesHut'
    # }
}

# returns all possible edges between nodes
def get_max_edges(nodes: Set[NodeId]) -> Tuple[NodeId, NodeId]:
    remaining_nodes = nodes.copy()
    for node in nodes:
        remaining_nodes.remove(node)
        for neighbour_node in remaining_nodes:
            yield (node, neighbour_node)

# returns max degree when considering only hubs
def get_max_hub_deg(nodes: Set[NodeId]) -> int:
    return len(nodes) - 1

# TODO: make non-linear line (also for get_scaled_edge_width) and maybe calculate min and max edge with from used edges
def get_scaled_node_size(connections: int, max_connections: int, min_connections: int=1) -> float:
    return (MAX_NODE_SIZE - MIN_NODE_SIZE) / (max_connections - min_connections) * (connections - min_connections) + MIN_NODE_SIZE

def get_scaled_edge_width(cost: int, min_cost: int, max_cost: int) -> float:
    return (MAX_EDGE_WIDTH - MIN_EDGE_WIDTH) / (max_cost - min_cost) * (cost - min_cost) + MIN_EDGE_WIDTH

def visualise_graph(N: Set[NodeId], H: Dict[NodeId, bool], E: Dict[NodeId, Dict[NodeId, bool]], c: Dict[NodeId, Dict[NodeId, int]], filepath: str=None) -> None:
    hubs = {node for node, isHub in H.items() if isHub}
    non_hubs = N - hubs

    if filepath is not None:
        filename = pathlib.Path(filepath).stem
        graph_path = os.path.join(GRAPHS_DIR, fr'graph_{filename}.html')
    else:
        graph_path = os.path.join(GRAPHS_DIR, r'graph.html')

    # g = Network(bgcolor='#222222', font_color='white')
    g = Network(width='100%', height='100%', bgcolor='#222222', font_color='white')
    
    max_hub_deg = get_max_hub_deg(hubs)
    hub_connections = {hub: max_hub_deg for hub in hubs} # every hub has at least max_hub_deg edges, but may additionally have edges to non-hubs
    connected_hub = dict()
    for non_hub in non_hubs:
        # count amount of edges from hub to non_hub
        hub = max(E[non_hub], key=E[non_hub].get) # get hub with value equal to 1
        hub_connections[hub] += 1

        # store connected hub for every non_hub
        connected_hub[non_hub] = hub

    # add non-hubs nodes
    g.add_nodes(list(non_hubs), size=[get_scaled_node_size(1, len(N)) for _ in range(len(non_hubs))])
    
    # add hub nodes
    max_connections = max(hub_connections.values())
    for hub in hubs:
        g.add_node(hub, size=get_scaled_node_size(hub_connections[hub], max_connections))

    c_arr = pd.DataFrame(c).to_numpy()
    min_cost = np.min(c_arr[np.nonzero(c_arr)]) # ignore costs of 0
    max_cost = c_arr.max()

    # add all edges between hubs
    for src, target in get_max_edges(hubs):
        g.add_edge(src, target, width=get_scaled_edge_width(c[src][target], min_cost, max_cost))

    # add all edges from non_hub to hub
    for src in non_hubs:
        target = connected_hub[src]
        g.add_edge(src, target, width=get_scaled_edge_width(c[src][target], min_cost, max_cost))
    
    if True:
        g.set_options(json.dumps(GRAPH_OPTIONS))
    else:
        g.show_buttons(filter_=['edges', 'physics'])
    g.show(graph_path)

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
        },
        r'demo'
    )

if __name__ == '__main__':
    main()
        