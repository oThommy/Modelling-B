from integer_linear_problem import Ilp
from custom_typing import NodeId
from config import Config
from tqdm import tqdm, std
import pandas as pd


FILEPATH = r'./../brightspace-locker/Data assignment parcel transport 2 Small.xlsx'
# FILEPATH = r'./../other/Data assignment parcel transport 2 very small Small.xlsx'
CONFIG = Config()
ilp = Ilp.from_excel(FILEPATH)

def get_E(hubs: set[NodeId], non_hubs: set[NodeId]) -> dict[NodeId, dict[NodeId, bool]]:
    E = {node: dict() for node in ilp.N}
    
    # non-hub to hub / hub to non-hub edges
    for non_hub in non_hubs:
        cost_dict = {hub: ilp.c[non_hub][hub] for hub in hubs} # filter on hubs
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

def get_H(hubs, non_hubs):
    return {node: 1 if node in hubs else 0 for node in ilp.N}

def complete_pbar(pbar: std.tqdm) -> None:
    pbar.n = 99
    pbar.update(1)

def intuitive_algo_2(): ...

def main():
    z_min = float('inf')
    min_hubs = set()
    remaining_hubs = ilp.N.copy()

    with tqdm(desc='calculating (sub)optimal solution', total=len(ilp.N), ncols=CONFIG.TQDM_NCOLS) as pbar:
        for _ in ilp.N:
            hub_costs = dict()

            for hub in remaining_hubs:
                hubs = min_hubs | {hub}
                non_hubs = ilp.N - hubs
                E = get_E(hubs, non_hubs)
                H = get_H(hubs, non_hubs)
                hub_costs[hub] = ilp.get_z_multiple_hubs(H, E)

            min_hub = min(hub_costs, key=hub_costs.get)
            current_z = hub_costs[min_hub]

            if current_z >= z_min:
                complete_pbar(pbar)
                break
                
            z_min = current_z
            min_hubs.add(min_hub)

            pbar.update(1)

    non_hubs = ilp.N - min_hubs

    print('Intuitive algorithm solver 2')
    print('Solution (possibly sub-optimal):')
    print(f'{z_min = }')
    print(f'{min_hubs = }')
    print(f'{non_hubs = }')



            

if __name__ == '__main__':
    main()