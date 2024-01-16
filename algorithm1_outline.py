# Outline of Algoritm 1
import numpy as np
import matplotlib.pyplot as plt
from typing import TypeVar, Tuple, List

def alg1(cost_array: Array, max_iter: int, t: float):
    #
    # cost_array : NxN array of floating point numbers representing gain
    # max_iter : the integer at which iteration stops, regardless of convergence
    # t : floating point perturbation size
    #
    # Computes the ideal probability vector, p, that should be shown to an opponent
    # so as to minimize the maximal gain he could achieve by selecting the optimal
    # column of the input array
    #
    # return: probability vector p, list of opponent optimal values at each iteration
    
    N = cost_array.shape[0] # dimension of input
    test_vector = np.array([1 for _ in range(N)])/N # instantiate test vector
    values = [max((test_vector @ cost_array))] # instantiate result list

    # store best prob vector, smallest opponent max
    p = test_vector
    op_max = max((test_vector @ cost_array))

    for i in range(max_iter):

        # examine effect of perturbation in each column of test vector
        max_col, minmax, maxmax = 0, float('inf'), 0
        for col in range(N):
            test_vector[col] += t
            m = max(test_vector @ cost_array)
            test_vector[col] -= t
        # update tracker variables
        if m < minmax:
            max_col, minmax = col, m
        if m > maxmax:
            maxmax = m
        test_vector[max_col] += (maxmax - minmax)
        if test_vector[max_col] < 0:
            test_vector[max_col] = 0
        test_vector = test_vector/np.sum(test_vector)

        values.append(max((test_vector @ cost_array)))
        if values[-1] < op_max:
            op_max, p = values[-1], test_vector
    return p, values