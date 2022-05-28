from ilp_solver import ilp_solver_pulp, ilp_solver_gurobi, ilp_solver_cplex
from intuitive_algo_1 import intuitive_algo_1
from intuitive_algo_2 import intuitive_algo_2
from integer_linear_problem import Ilp
from config import Config


def main() -> None:
    ilp = Ilp.from_excel(Config().DATA_SMALL_PATH)

    ilp_solver_pulp(ilp)
    # ilp_solver_gurobi(ilp)
    # ilp_solver_cplex(ilp)

    # intuitive_algo_1(ilp)

    # intuitive_algo_2(ilp)


if __name__ == '__main__':
    main()