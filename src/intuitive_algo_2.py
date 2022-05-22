from integer_linear_problem import Ilp
from solution import Solution
from config import Config
from tqdm import tqdm
import algo_funcs
import utils


def intuitive_algo_2(ilp: Ilp) -> Solution:
    '''intuitive algorithm 2'''

    z_min = float('inf')
    min_hubs = set()
    remaining_hubs = ilp.N.copy()

    with tqdm(desc='calculating (sub)optimal solution', total=len(ilp.N), ncols=Config().TQDM_NCOLS) as pbar:
        for _ in ilp.N:
            hub_costs = dict()

            for hub in remaining_hubs:
                hubs = min_hubs | {hub}
                non_hubs = ilp.N - hubs
                H = algo_funcs.get_H(hubs, ilp.N)
                E = algo_funcs.get_E(hubs, non_hubs, ilp.N, ilp.c)
                hub_costs[hub] = ilp.get_z_multiple_hubs(H, E)

            min_hub = min(hub_costs, key=hub_costs.get)
            current_z = hub_costs[min_hub]

            if current_z >= z_min:
                utils.complete_pbar(pbar)
                break
                
            z_min = current_z
            min_hubs.add(min_hub)

            pbar.update(1)

    non_hubs = ilp.N - min_hubs

    E = algo_funcs.get_E(min_hubs, non_hubs, ilp.N, ilp.c)
    solution = Solution(z_min, min_hubs, non_hubs, E, ilp)
    solution.print()
    solution.visualise()
    solution.save()

    return solution

def main() -> None:
    ilp = Ilp.from_excel(Config().DATA_VERY_SMALL_PATH)
    intuitive_algo_2(ilp)


if __name__ == '__main__':
    main()