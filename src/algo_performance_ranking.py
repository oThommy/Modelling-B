from integer_linear_problem import Ilp
from config import Config
import pandas as pd
import numpy as np
import math
import scipy.stats as stats
import matplotlib.pyplot as plt
from ilp_solver import ilp_solver_gurobi
from intuitive_algo_2 import intuitive_algo_2


def gen_ilp(n, w_mu, w_sigma, c_mu, c_sigma, f_mu, f_sigma, collection, transfer, distribution):
    w_arr = np.random.normal(loc=w_mu, scale=w_sigma, size=n**2).astype(int)

    # ensure all values are >= 0
    while any(w_arr < 0):
        w_arr[w_arr < 0] = np.random.normal(loc=w_mu, scale=w_sigma, size=sum(w_arr < 0)).astype(int)

    w_iter = iter(w_arr)
    w_dct = dict()
    for i in range(1, n + 1):
        w_dct[i] = dict()
        for j in range(1, n + 1):
            w_dct[i][j] = next(w_iter)

    c_arr = np.random.normal(loc=c_mu, scale=c_sigma, size=n**2 - n).astype(int) # FIXME: the mean and standard deviation don't seem to converge to mu and sigma, https://stackoverflow.com/questions/27831923/python-random-number-generator-with-mean-and-standard-deviation

    # ensure all values are > 0
    # FIXME: this throws the mean and std even more off...
    while any(c_arr <= 0):
        c_arr[c_arr <= 0] = np.random.normal(loc=c_mu, scale=c_sigma, size=sum(c_arr <= 0)).astype(int)

    c_iter = iter(c_arr)
    c_dct = dict()
    for i in range(1, n + 1):
        c_dct[i] = dict()
        for j in range(1, n + 1):
            if i == j:
                c_dct[i][j] = 0
            else:
                c_dct[i][j] = next(c_iter)

    f_arr = np.random.normal(loc=f_mu, scale=f_sigma, size=n).astype(int)

    # ensure all values are > 0
    while any(f_arr <= 0):
        f_arr[f_arr <= 0] = np.random.normal(loc=f_mu, scale=f_sigma, size=sum(f_arr <= 0)).astype(int)

    f_iter = iter(f_arr)
    f_dct = {i: next(f_iter) for i in range(1, n + 1)}

    N = set(range(1, n + 1))
    ilp = Ilp(N, collection, transfer, distribution, w_dct, c_dct, f_dct)

    return ilp

def rank_algos(min_dataset_n = 10, max_dataset_n = 15, samples = 20):
    ilp_small = Ilp.from_excel(Config().DATA_SMALL_PATH)
    ilp_large = Ilp.from_excel(Config().DATA_LARGE_PATH)

    # merge small and large data set (also make them of the same size) and calculate mean and standard deviation seperately for flow, costs and fixed costs
    w_small_ser = ilp_small.w_df.stack()
    w_large_ser = ilp_large.w_df.stack()
    
    w_small_ser = pd.concat([w_small_ser] * math.ceil(len(w_large_ser) / len(w_small_ser)))
    w_small_ser = w_small_ser[:len(w_large_ser)]

    w_ser = pd.concat([w_small_ser, w_large_ser])
    w_mu = w_ser.mean()
    w_sigma = w_ser.std()

    # exclude zeros for mean and std
    c_small_ser = ilp_small.c_df.stack()
    c_small_ser = c_small_ser[c_small_ser != 0]
    c_large_ser = ilp_large.c_df.stack()
    c_large_ser = c_large_ser[c_large_ser != 0]

    c_small_ser = pd.concat([c_small_ser] * math.ceil(len(c_large_ser) / len(c_small_ser)))
    c_small_ser = c_small_ser[:len(c_large_ser)]

    c_ser = pd.concat([c_small_ser, c_large_ser])
    c_mu = c_ser.mean()
    c_sigma = c_ser.std()

    f_small_ser = ilp_small.f_ser
    f_large_ser = ilp_large.f_ser

    f_small_ser = pd.concat([f_small_ser] * math.ceil(len(f_large_ser) / len(f_small_ser)))
    f_small_ser = f_small_ser[:len(f_large_ser)]

    f_ser: pd.Series = pd.concat([f_small_ser, f_large_ser])
    f_mu = f_ser.mean()
    f_sigma = f_ser.std()

    # calculate and display average error percentage for different sizes n of the data sets # TODO: how to calculate this?
    error_df = pd.DataFrame(
        np.zeros((max_dataset_n - min_dataset_n + 1, samples)), 
        index=range(min_dataset_n, max_dataset_n + 1),
    )
    for n in range(min_dataset_n, max_dataset_n + 1):
        for i in range(samples):
            ilp = gen_ilp(n, w_mu, w_sigma, c_mu, c_sigma, f_mu, f_sigma, ilp_small.collection, ilp_small.transfer, ilp_small.distribution)
            sol_gurobi = ilp_solver_gurobi(ilp, False)
            sol_heuristic_2 = intuitive_algo_2(ilp, False)
            error_df.loc[n][i] = (sol_gurobi.z - sol_heuristic_2.z) / sol_heuristic_2.z * 100

    print(error_df)
    print(error_df.stack().describe())

    avg_error_ser = pd.Series(np.zeros((max_dataset_n - min_dataset_n + 1,)), index=range(min_dataset_n, max_dataset_n + 1))
    for index, row in error_df.iterrows():
        avg_error_ser[index] = row.mean()
    print(avg_error_ser)
    print(avg_error_ser.describe())

def main() -> None:
    rank_algos(10, 13, 20)


if __name__ == '__main__':
    main()