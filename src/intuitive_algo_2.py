from pathlib import Path
from integer_linear_problem import Ilp
from solution import Solution, Flags
from typing import Optional
from config import Config
from tqdm import tqdm
import algo_funcs
import utils


def intuitive_algo_2(ilp: Ilp, flags: Flags = Flags.DEFAULT, algo_dir_path: Optional[Path] = None, annotation: Optional[str] = None) -> Solution:
    '''intuitive algorithm 2'''

    timer = utils.Timer()
    timer.start()

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

            if current_z > z_min:
                utils.complete_pbar(pbar)
                break
                
            z_min = current_z
            min_hubs.add(min_hub)
            remaining_hubs.remove(min_hub)

            pbar.update(1)

    non_hubs = ilp.N - min_hubs
    E = algo_funcs.get_E(min_hubs, non_hubs, ilp.N, ilp.c)

    timer.stop()

    if algo_dir_path is None:
        solution = Solution(z_min, min_hubs, non_hubs, E, ilp, timer, algo_file=__file__, annotation=annotation)
    else:
        solution = Solution(z_min, min_hubs, non_hubs, E, ilp, timer, algo_dir_path=algo_dir_path, annotation=annotation)
    solution.run(flags)

    return solution

def main() -> None:
    ilp = Ilp.from_excel(Config().DATA_SMALL_PATH)
    intuitive_algo_2(ilp)


if __name__ == '__main__':
    main()