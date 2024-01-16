def alg3(cost_array: Array, max_iter: int, t: float, z: float, q: float, h: float, b: float):
    #
    # cost_array : NxN array of floating point numbers representing gain
    # max_iter : the integer at which iteration stops, regardless of convergence
    # t : floating point perturbation size
    # z : exponent of N in scaling sequence
    # q : offset in scaling sequence
    # h : factor in tanh numerator in scaling sequence
    # b : factor to increase t
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

    # creates a smoothing sequence to scale movements by
    # avoids storing sequence in memory
    scalers = ((q + (N**z)*np.tanh(h*i/(max_iter))) for i in range(max_iter))
    j = 0 # used to track updates on t

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

        test_vector[max_col] += (maxmax - minmax)/next(scalers)
        test_vector = test_vector/np.sum(test_vector)
        if test_vector[max_col] < 0:
            test_vector[max_col] = 0

        values.append(max((test_vector @ cost_array)))
        if values[-1] < op_max:
            op_max, p = values[-1], test_vector
            j = i
        if j + max_iter/100 < i:
            j, t = i, t*(1+b)
    return p, values