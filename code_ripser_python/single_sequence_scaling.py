def single_sequence_scaling(measure,npoints,**kwargs):
    '''
    This script generates ONE point cloud and goes through
    the usual process of generating data for a log-log plot,
    based on nested subsets of the point cloud.

    Advantage: only one distance matrix computation is needed
    for a sequence of points, so this is only
    bottlenecked only by ripser.

    Inputs:
        measure: The probability measure to sample from
        npoints: The maximum number of points to use

    Outputs:
        results: A dictionary with keys being number of points;
            values being dictionaries of bar codes in the number
            of PH dimensions.

    Optional inputs:
        seq: A sequence of integers up to npoints
            specifying the subsets of the data to work
            with. Default: [2,3,...,npoints].
        nprocs: Number of processes to use for the parallelization (default: 1)

    '''
    import re
    import multiprocessing
    import ripser_interface as ri

    global ripser_loc
    global max_dim
    global Dstr

    ripser_loc = kwargs.get('ripser_loc','../ripser/ripser')
    max_dim = kwargs.get('max_dim',1)
    nprocs = kwargs.get('nprocs',1)
    seq = kwargs.get('seq',[i+2 for i in range(npoints-2+1)])

    # pts = ri.gen_pt_cloud_from_measure(measure,npoints,**kwargs)
    pts = ri.gen_pt_cloud_from_measure(measure,npoints)
    D = ri.create_distmat(pts)

    Dstr = ri.create_distmat_str(D)

    p = multiprocessing.Pool(nprocs)

    iterobj = re.finditer(b'.*\\n.*',Dstr)
    locs = [i.start() for i in iterobj]

    all_inputs = [[seq[j],max(seq),locs[seq[j]-1]] for j in range(len(seq)) ]

    results = p.map(submit_string_ripser, all_inputs)

    return {seq[i]:results[i] for i in range(len(seq))}

#

def submit_string_ripser(inputs):
    import subprocess
    import ripser_interface as ri

    j,maxseq,cutoff = inputs

    proc = subprocess.Popen([ripser_loc,"--dim",str(max_dim)], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    result = proc.communicate(input=Dstr[:cutoff])[0]

    lines = result.decode('utf-8').split('\n')
    lines.pop(-1)   # Spare extra line

    PH_intervals = ri.read_ripser_results(lines)
    print(j,maxseq)
    return PH_intervals
#
