def create_distmat_str(D):
    '''
    Converts a lower triangular matrix to a raw string csv.
    Functionally similar to create_distmat_file() but outputs 
    the raw string which would be used to write the file. 

    Useful if you want to pass D in to ripser without needing 
    to read/write a file to disk (this can be slow).

    Inputs: 
        D: n-by-n distance matrix
    Outputs:
        outstr: string corresponding to the lower triangular 
            component of D, to be fed to ripser directly 
            (circumventing the need to write to hard disk).
    '''

    n = len(D)
    outstr = ''

    for i in range(n):
        line = ''
        for j in range(i):
            line += '%.15f,'%D[i,j]
        #
        line += '\n'
        outstr += line
    #
    outstr = outstr.encode()
    return outstr
#
