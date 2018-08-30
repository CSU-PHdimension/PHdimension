
def create_distmat(cloud):
    '''
    Create distance matrix. outputs np array.
    
    The current form of this is an interface to 
    the scikit-learn function, which is much faster 
    than a naive implementation (commented in the source code).

    Inputs:
        cloud: n-by-d array of n points in d dimensions
    Outputs: 
        D: n-by-n distance matrix of all pairwise 2-norm 
            distances of the points in cloud.
    '''
    # import numpy as np
    import sklearn.metrics

    # n = len(cloud)
    # D = np.zeros((n,n))
    #
    # for i in range(n):
    #     for j in range(i):
    #         D[i,j] = np.linalg.norm(cloud[i]-cloud[j])
    # #
    D = sklearn.metrics.pairwise.pairwise_distances(cloud)
    return D
#
