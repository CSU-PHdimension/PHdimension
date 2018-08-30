def run_ripser_sim(cloud,**kwargs):
    '''
    Calls create_distmat_file, calls ripser, gets the results,
    returns the PH_intervals dictionary.

    Inputs:
        cloud: n-by-d array of n points in d dimensions of the 
            point cloud.
    Outputs:
        PH_intervals: dictionary whose keys are PH dimensions 
            (0, 1, etc, as integers) and keys are the corresponding 
            birth/death times for that dimension.

    optional arguments:
        fname: intermediate file's name. Used for running in parallel
            to prevent overlap.
        ripser_loc: string indicating location of the ripser executable.
            Defaults to a "../ripser/ripser".
        save_input: Boolean, whether to keep the distance matrix from the
            input to ripser.
            Defaults to False.
        save_output: Boolean; whether to keep the file from the calculation
            or just delete it after calculation.
            Defaults to False.
        max_dim: maximum persistent homology dimension to compute.
            Defaults to 1.
    '''
    # from create_distmat_file import create_distmat_file as cdf
    from create_distmat_str import create_distmat_str as cds
    from create_distmat import create_distmat
    from read_ripser_results import read_ripser_results as rrr
    from ripser_misc import generate_unique_id as gid

    import subprocess,os

    fgid = gid()
    fname = kwargs.get('fname',fgid+'.txt')
    ripser_loc = kwargs.get('ripser_loc','../ripser/ripser')
    save_input = kwargs.get('save_input',False)
    save_output = kwargs.get('save_output',False)
    max_dim = kwargs.get('max_dim',1)

    D = create_distmat(cloud)
    Dstr = cds(D)
    p = subprocess.Popen([ripser_loc,"--dim",str(max_dim)], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    result = p.communicate(input=Dstr)[0]

    lines = result.decode('utf-8').split('\n')
    lines.pop(-1)   # Spare extra line

    if save_output:
        f = open(fgid+'_results.txt','wb')
        f.write(result)
        f.close()
    #
    # if not save_input:
    #     os.remove(fname)
    # #
    if save_input:
        f = open(fgid+'.txt','wb')
        f.write(Dstr)
        f.close()
    #

    try:
        PH_intervals = rrr(lines)
    except:
        print('There was an error parsing the results; returning the raw result.')
        return lines
    #

    return PH_intervals
#
