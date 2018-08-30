def pointsSierpinski2D(n,l):
    '''
    Samples points from the Sierpinski triangle.
    More precisely, samples points
    from the bottom left endpoints of the triangles
    in the Sierpinski triangle at a specified level.

    Based on ternary sequences.

    Python implementation of Henry Adam's matlab code.
    '''
    import numpy as np

    points = np.zeros((n,2))
    binarySequences = np.random.randint(3,size=(n,l))

    v0 = np.array([1,0])
    v0.shape = (1,2)
    v1 = np.array([0.5,np.sqrt(3)/2.])
    v1.shape = (1,2)

    for i in range(l):
        loc0 = (binarySequences[:,i]==1)
        loc0.shape = (len(loc0),1)
        loc1 = (binarySequences[:,i]==2)
        loc1.shape = (len(loc1),1)
        points += (np.dot(loc0,v0) + np.dot(loc1,v1))/(2.**i)
    #
    return points
#
