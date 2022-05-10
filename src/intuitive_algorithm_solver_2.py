from custom_typing import DataFrame, NodeId, Series
from integer_linear_problem import Ilp
from config import Config
from tqdm import tqdm
import pandas as pd


FILEPATH = r'./../brightspace-locker/Data assignment parcel transport 2 Small.xlsx'
# FILEPATH = r'./../other/Data assignment parcel transport 2 very small Small.xlsx'
CONFIG = Config()
ILP = Ilp.from_excel(FILEPATH)

def get_E(hubs: set[NodeId], non_hubs: set[NodeId]) -> DataFrame[NodeId, Series[NodeId, bool]]:
    E = {node: dict() for node in ILP.N}
    
    # non-hub to hub / hub to non-hub edges
    for non_hub in non_hubs:
        cost_dict = {hub: ILP.c[non_hub][hub] for hub in hubs} # filter on hubs
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

    return pd.DataFrame.from_dict(E)

def main():
    z_min = float('inf')
    hub_costs = dict()

    with tqdm(desc='getting costs for single hub', total=len(ILP.N), ncols=CONFIG.TQDM_NCOLS) as pbar:
        for hub in ILP.N:
            pbar.update(1)

            hubs = {hub}
            non_hubs = ILP.N
            hub_costs[hub] = ILP.get_z(hubs, non_hubs)
    
    min_hub = min(hub_costs, key=hub_costs.get)
    z_min = hub_costs[min_hub]
    hubs = {min_hub}
    del hub_costs[min_hub]
    sorted_remaining_hubs = sorted(hub_costs, key=hub_costs.get)

    print(hub_costs)
    print(min_hub)
    print(sorted_remaining_hubs)

    with tqdm(desc='optimal hub selection', total=len(ILP.N) - 1, ncols=CONFIG.TQDM_NCOLS) as pbar:
        for hub in sorted_remaining_hubs:
            pbar.update(1)

            hubs.add(hub)
            non_hubs = ILP.N - hubs
            E = get_E(hubs, non_hubs)
            cur_z = ILP.get_z(hubs, non_hubs, E)

            if cur_z < z_min:
                z_min = cur_z
                continue
            else:
                pbar.n = 100 # FIXME: not correct value prolly
                pbar.last_print_n = 100
                break

    print('Intuitive algorithm solver 2')
    print('Solution (possibly sub-optimal):')
    print(f'{z_min = }')
    print(f'{hubs = }')
    print(f'{non_hubs = }')

            

if __name__ == '__main__':
    main()