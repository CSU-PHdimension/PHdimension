def create_distmat_file(D,fname):
    '''
    Given a distance matrix, export to text file as a csv.
    
    Inputs:
        D: n-by-n distance matrix, presumably generated 
            by create_distmat() (but not necessarily).
        fname: string indicating where to save the lower 
            triangular component of D which ripser can read.
    Outputs:
        None
    '''

    n = len(D)
    f = open(fname,'w')

    for i in range(n):
        line = ''
        for j in range(i):
            line += '%.15f,'%D[i,j]
        #
        line += '\n'
        f.write(line)
    #
    f.close()
    return
#

if __name__=="__main__":
    # Try an example with the hypothesized 3D
    # MDS embedding of the circle.
    import numpy as np
    from matplotlib import pyplot

    n = 31
    t = np.linspace(0,2*np.pi,n, endpoint=False)
    cloud = np.zeros((n,3))

    for i,tv in enumerate(t):
        cloud[i] = [np.cos(tv),np.sin(tv),np.sqrt(2.)/3.*np.cos(3*tv)]
    #
    D = create_distmat_file(cloud,'test.txt')

#    pyplot.contourf(D+D.T)
#    pyplot.show(block=False)

#
