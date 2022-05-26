from custom_typing import IlpSolverData
from integer_linear_problem import Ilp
from solution import Solution
from typing import Optional
from config import Config
import pulp as plp
import utils


def ilp_solver(ilp: Ilp, solver: Optional[plp.LpSolver_CMD] = None, ilp_solver_type: Optional[str] = None) -> Solution:
    '''General ILP Solver'''

    timer = utils.Timer()
    timer.start()

    # create parcel delivery model object
    ParDe: plp.LpProblem = plp.LpProblem('Parcel Delivery', sense=plp.LpMinimize)

    # create input variables
    E = plp.LpVariable.dicts('E', (ilp.N, ilp.N), cat=plp.LpBinary)
    H = plp.LpVariable.dicts('H', ilp.N, cat=plp.LpBinary)
    t1 = plp.LpVariable.dicts('t1', (ilp.N, ilp.N), cat=plp.LpBinary)
    t2 = plp.LpVariable.dicts('t2', (ilp.N, ilp.N, ilp.N), cat=plp.LpBinary)
    t3 = plp.LpVariable.dicts('t3', (ilp.N, ilp.N, ilp.N, ilp.N), cat=plp.LpBinary)

    # add objective z function
    ParDe += plp.lpSum([ilp.f[i] * H[i] for i in ilp.N]) + \
    plp.lpSum([t1[i][j] * ilp.w[i][j] * ilp.transfer * ilp.c[i][j] \
        for i in ilp.N for j in ilp.N]) + \
    plp.lpSum([t2[i][j][k] * (ilp.w[i][j] * (ilp.collection * ilp.c[i][k] + ilp.transfer * ilp.c[k][j]) + ilp.w[j][i] * (ilp.transfer * ilp.c[j][k] + ilp.distribution * ilp.c[k][i])) \
        for i in ilp.N for j in ilp.N for k in ilp.N]) + \
    plp.lpSum([t3[i][j][k][l] * ilp.w[i][j] * (ilp.collection * ilp.c[i][k] + ilp.transfer * ilp.c[k][l] + ilp.distribution * ilp.c[l][j]) \
        for i in ilp.N for j in ilp.N for k in ilp.N for l in ilp.N])

    # add constraints
    ParDe += plp.lpSum([H[i] for i in ilp.N]) >= 1

    for i in ilp.N:
        ParDe += E[i][i] == H[i]

    for i in ilp.N:
        for j in ilp.N:
            ParDe += E[i][j] >= t1[i][j]

    for i in ilp.N:
        ParDe += plp.lpSum([E[i][j] for j in ilp.N]) <= 1 + (len(ilp.N) - 1) * H[i]
        ParDe += plp.lpSum([E[i][j] for j in ilp.N]) >= 1
        
    for i in ilp.N:
        for j in ilp.N:
            ParDe += t1[i][j] <= H[i]
            ParDe += t1[i][j] <= H[j]
            ParDe += t1[i][j] >= H[i] + H[j] - 1

    for i in ilp.N:
        for j in ilp.N:
            for k in ilp.N:
                ParDe += t2[i][j][k] <= 1 - H[i]
                ParDe += t2[i][j][k] <= H[j]
                ParDe += t2[i][j][k] <= E[i][k]
                ParDe += t2[i][j][k] >= 1 - H[i] + H[j] + E[i][k] - 2

    for i in ilp.N:
        for j in ilp.N:
            for k in ilp.N:
                for l in ilp.N:
                    ParDe += t3[i][j][k][l] <= 1 - H[i]
                    ParDe += t3[i][j][k][l] <= 1 - H[j]
                    ParDe += t3[i][j][k][l] <= E[i][k]
                    ParDe += t3[i][j][k][l] <= E[l][j]
                    ParDe += t3[i][j][k][l] >= 1 - H[i] + 1 - H[j] + E[i][k] + E[l][j] - 3

    for i in ilp.N:
        for j in ilp.N:
            ParDe += H[i] + H[j] >= E[i][j]
            ParDe += E[i][j] == E[j][i]

    # solve problem    
    if solver is None:
        ParDe.solve()
    else:
        ParDe.solve(solver)

    E = {i: {j: int(plp.value(E[i][j])) for j in ilp.N} for i in ilp.N}
    H = {i: int(plp.value(H[i])) for i in ilp.N}
    z = int(plp.value(ParDe.objective))
    hubs = {hub for hub, is_hub in H.items() if is_hub}
    non_hubs = ilp.N - hubs
    ilp_solver_data = {
        'type': ilp_solver_type or 'UNKNOWN',
        'status': plp.LpStatus[ParDe.status]
    }

    timer.stop()

    solution = Solution(z, hubs, non_hubs, E, ilp, timer, ilp_solver_data)
    solution.print()
    solution.visualise()
    solution.save()

    return solution

def ilp_solver_pulp(ilp: Ilp) -> Solution:
    '''PuLP ILP Solver'''

    return ilp_solver(ilp, None, 'PuLP')

def ilp_solver_gurobi(ilp: Ilp) -> Solution:
    '''Gurobi ILP Solver'''
    
    return ilp_solver(ilp, plp.GUROBI_CMD(), 'Gurobi')

def ilp_solver_cplex(ilp: Ilp) -> Solution:
    '''Cplex ILP Solver'''

    return ilp_solver(ilp, plp.CPLEX_CMD(), 'Cplex')

def main() -> None:
    ilp = Ilp.from_excel(Config().DATA_LARGE_PATH)
    # ilp_solver_pulp(ilp)
    # ilp_solver_gurobi(ilp)
    ilp_solver_cplex(ilp)


if __name__ == '__main__':
    main()