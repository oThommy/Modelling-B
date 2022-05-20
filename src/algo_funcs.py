from integer_linear_problem import Ilp
from custom_typing import NodeId


def get_E(
    hubs: set[NodeId], 
    non_hubs: set[NodeId], 
    N: set[NodeId], 
    c: dict[NodeId, dict[NodeId, int]]
) -> dict[NodeId, dict[NodeId, bool]]:

    '''generate E dictionary by connecting every non_hub to the hub with the minimal cost'''
    
    E = {node: dict() for node in N}
    
    # non-hub to hub / hub to non-hub edges
    for non_hub in non_hubs:
        cost_dict = {hub: c[non_hub][hub] for hub in hubs} # filter on hubs
        min_cost_hub = min(cost_dict, key=cost_dict.get)
        for hub in hubs:
            E[non_hub][hub] = 1 if hub == min_cost_hub else 0
            E[hub][non_hub] = 1 if hub == min_cost_hub else 0 # since E_ij = E_ji for all i =/= j

    # non-hub to non-hub edges (including itself)
    for non_hub1 in non_hubs:
        for non_hub2 in non_hubs:
            E[non_hub1][non_hub2] = 0

    # hub to hub edges (including itself)
    for hub1 in hubs:
        for hub2 in hubs:
            E[hub1][hub2] = 1

    return E

def get_H(hubs: set[NodeId], N: set[NodeId]) -> dict[NodeId, bool]:
    '''convert hubs to H dictionary'''

    return {node: 1 if node in hubs else 0 for node in N}