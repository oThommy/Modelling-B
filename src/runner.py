import ilp_solver
from intuitive_algo_1 import intuitive_algo_1
from intuitive_algo_2 import intuitive_algo_2
from integer_linear_problem import Ilp
from config import Config


def main() -> None:
    ilp = Ilp.from_excel(r'src\in\Data assignment parcel transport 2 TEST.xlsx')

    # ilp_solver.pulp_v1(ilp)
    ilp_solver.gurobi_v1(ilp)
    # ilp_solver.cplex_v1(ilp)

    # intuitive_algo_1(ilp)

    intuitive_algo_2(ilp)


if __name__ == '__main__':
    main()