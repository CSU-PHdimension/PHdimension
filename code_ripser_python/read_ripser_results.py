def read_ripser_results(fname):
    '''
    Reads the raw output of ripser and returns
    a data structure with the results in a useable format.

    if input is of type list, it's assumed the file has already
    been read, and this is a list of the lines in the output.
    '''
    import re
    import numpy as np

    if type(fname)==str:
        f = open(fname,'r')
        lines = f.readlines()
        f.close()
    elif type(fname)==list:
        lines = fname
    #

    expr_header = 'distance matrix with ([\d]*) points'
    expr_PHdim = 'persistence intervals in dim ([\d]):'
    expr_interval = '\ \[(.*),(.*)\)'

    prog_header = re.compile(expr_header)
    prog_PHdim = re.compile(expr_PHdim)
    prog_interval = re.compile(expr_interval)

        # m = prog.match(string)
        # return m.group(1),m.group(2)

    PH_intervals = {}
    match = prog_header.match(lines[0])
    n = int(match.group(1))

    for line in lines[2:]:

        m = prog_PHdim.match(line)
        if m!=None:
            # initialize a new dictionary entry for the new PH dimension
            dim = int(m.group(1))
            PH_intervals[dim] = []
        else:

            m = prog_interval.match(line)
            left = np.double(m.group(1))
            right = np.double(m.group(2)) if m.group(2)!=' ' else np.inf
            PH_intervals[dim].append([left,right])
        #
    #
    for key in PH_intervals.keys():
        PH_intervals[key] = np.array(PH_intervals[key], dtype=np.double)
    #
    return PH_intervals
#


if __name__=="__main__":
    PH_intervals = read_ripser_results('results.txt')
    fig,ax = plot_PH_results(PH_intervals[0])
