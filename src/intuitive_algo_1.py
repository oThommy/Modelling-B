from integer_linear_problem import Ilp
from solution import Solution, Flags
from typing import Optional
from config import Config
from tqdm import tqdm
import algo_funcs
import utils
import copy

def powerset(s: set) -> set:
    bitmasks = [1 << i for i in range(len(s))] # 1 << i is basically equal to 2^i
    # the n-th digits in the binary representation of bit_selection dictates whether the n-th item is selected (1 = selected, 0 = not selected)
    for bit_selection in range(1, 1 << len(s)): # start with 1 to prevent empty set
        yield {el for el, bitmask in zip(s, bitmasks) if bit_selection & bitmask}

def intuitive_algo_1(ilp: Ilp, flags: Flags = Flags.DEFAULT, annotation: Optional[str] = None) -> Solution:
    '''Intuitive algorithm 1'''

    timer = utils.Timer()
    timer.start()

    z_min = float('inf')

    with tqdm(total=(1 << len(ilp.N)) - 1, ncols=Config().TQDM_NCOLS) as pbar:
        for hubs in powerset(ilp.N):
            pbar.update(1)

            non_hubs = ilp.N - hubs

            H = algo_funcs.get_H(hubs, ilp.N)
            E = algo_funcs.get_E(hubs, non_hubs, ilp.N, ilp.c)

            current_z = ilp.get_z_multiple_hubs(H, E)
            if current_z >= z_min:
                continue

            z_min = current_z
            hubs_min = copy.deepcopy(hubs)
            non_hubs_min = copy.deepcopy(non_hubs)
            E_min = copy.deepcopy(E)

    timer.stop()

    solution = Solution(
        z=z_min,
        hubs=hubs_min,
        non_hubs=non_hubs_min,
        E=E_min,
        ilp=ilp,
        algo_file=__file__,
        timer=timer,
        annotation=annotation,
    )
    solution.run(flags)

    return solution

def main() -> None:
    ilp = Ilp.from_excel(Config().DATA_SMALL_PATH)
    intuitive_algo_1(ilp)


if __name__ == '__main__':
    main()