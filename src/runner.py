import ilp_solver
from intuitive_algo_1 import intuitive_algo_1
from intuitive_algo_2 import intuitive_algo_2
from integer_linear_problem import Ilp
from solution import Flags
from config import Config


def main() -> None:
    ilp = Ilp.from_excel(Config().DATA_LARGE_PATH)

    ilp_solver.gurobi_v1(ilp, annotation='testing with E[i][i] == H[i] constraint removed')


if __name__ == '__main__':
    main()