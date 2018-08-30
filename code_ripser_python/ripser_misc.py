'''
This is a collection of miscellaneous functions 
which may be useful when working with persistent homology, 
or just file management in the code.

Contains:
    generate_unique_id(): generates a "random" number used 
        to make unique files to avoid overwriting issues.
    plot_PH_results(): generates a barcode plot using an 
        array of birth/death times.
    sum_PH_bars(): Takes in a dictionary which encodes 
        barcodes for topological dimensions and outputs 
        the Sum of (death - birth) over all barcodes in 
        that dimension.
    save_thing(), load_thing(): an interface to the pickle 
        package which makes it so that only a "thing" - 
        array, dictionary, etc, and the name of the 
        input/output file are needed.

'''

from numpy import random
import time
def generate_unique_id():
    '''
    Makes a "unique" id, to be used for filenames to avoid overlap with
    parallel computation.

    Inputs: None
    Outputs: a string with a lot of digits.
    '''
    prefix = str(time.mktime(time.localtime())+time.clock())
    suffix = '_'+str(random.randint(100))
    out = prefix+suffix
    return ''.join(str(out).split('.')) # Removes decimal points
#


def plot_PH_results(arr):
    '''
    Makes the traditional PH plot using the given
    array of birth/death times (n-by-2).

    Returns a fig,ax pair and does a pyplot.show(block=False).

    Inputs:
        arr: n-by-2 array of birth/death times.
    Outputs:
        fig,ax: a figure/axes pair generated from pyplot.subplots(1,1) 
            which has the barcode plot.

    Optional inputs:
        show_plot: Boolean (True/False) determining whether 
            this function should pyplot.show(block=False) the 
            fig,ax that it generates. (Default: False)
    '''
    import numpy as np
    from matplotlib import pyplot
    from matplotlib import patches

    n = len(arr)
    dh = 1./(n)
    r = 0.1 # Relative padding between consecutive intervals

    rh = dh-r*dh
    fig,ax = pyplot.subplots(1,1)

    dolater = []

    for i,interval in enumerate(arr):
        l,r = interval
        if r == np.inf:
            dolater.append([i,interval])
        else:
            rw = r-l
            # Rectangular patches are given as (left,bottom), width, height.j
            # print((l,i*dh), rw, rh)
            ax.add_patch(patches.Rectangle( (l,i*dh), rw, rh ))
        #
    #

    inds = np.isfinite(arr[:,1])
    ax.set_xlim([0,arr[inds,1].max()*1.05])

    if kwargs.get('show_plot', False):
        pyplot.show(block=False)
    #

    return fig,ax
#

def sum_PH_bars(PH_dict,dim=0):
    '''
    Returns the ``definite integral" of the barcode; the sum of
    the lengths of each interval in the dictionary. 
    Throws out infinite lengths.

    By default, this is done for PH_0.

    Inputs:
        PH_dict: a dictionary whose keys are PH dimensions 
            (0,1, etc, as integers) and values are n-by-2 arrays of 
            birth/death times for that dimension.
    Outputs:
        sumlen: a float; the sum of the lengths of the barcodes.

    Optional inputs:
        dim: which PH dimension to perform this on (default: 0)

    '''
    import numpy as np
    lens = np.diff(PH_dict[dim]).flatten()
    return np.sum(lens[np.isfinite(lens)])
#

def save_thing(thing,fname):
    '''
    automates calling pickle.dump.

    Inputs:
        thing: whatever you want. It's assumed this is a pickleable thing.
        fname: string, where the file should be saved on disk.
    Outputs: 
        None.
    
    NOTE: Pickling isn't exactly a good idea for long term 
    storage because pickldump() and pickle.load() can depend on the 
    versions of any code/package/module dependencies. For instance, 
    if you pickle a numpy array, in the distant future it's 
    possible that something fundamental about the numpy array 
    structure is changed that makes a pickle.load() of an old 
    numpy array impossible.

    That said it's pretty handy for short term storage.


    '''
    import pickle
    f = open(fname,'wb')
    pickle.dump(thing,f)
    f.close()
    return
#

def load_thing(fname):
    '''
    automates calling pickle.load.

    Inputs:
        fname: string, where the file to be loaded is on disk.
    Outputs:
        thing: whatever happens to be in the pickle file.
    
    NOTE: Pickling isn't exactly a good idea for long term 
    storage because pickldump() and pickle.load() can depend on the 
    versions of any code/package/module dependencies. For instance, 
    if you pickle a numpy array, in the distant future it's 
    possible that something fundamental about the numpy array 
    structure is changed that makes a pickle.load() of an old 
    numpy array impossible.

    That said it's pretty handy for short term storage.

    '''
    import pickle
    f = open(fname,'rb')
    thing = pickle.load(f)
    f.close()
    return thing
#

#def export_results_to_hdf(results,fname):
#    '''
#    Dumps the results of a many-realization results into an
#    HDF file which can be read by both python and matlab.
#
#    Inputs: 
#        results: 
#    '''
#    import h5py
#    import numpy as np
#
#    h = h5py.File(fname,'w')
#    ns = np.array([result[0] for result in results])
#    nsu = np.unique(ns)
#
#    phs = []
#    for result in results:
#        vals = list(result[1].keys())
#        for val in vals:
#            if val not in phs:
#                phs.append(val)
#    #
#    for ph in phs:
#        h.create_group('/PH_%i'%ph)
#    #
#
#    counter = np.zeros(ns.shape)
#    for i,result in enumerate(results):
#        nsuu = result[0]
#        which = np.where(nsuu==nsu)[0][0]
#        bddict = result[1]
#        phs = list(bddict.keys())
#        for j,ph in enumerate(phs):
#            dsetname = '/PH_%i/n%i_%i'%(ph,nsuu,counter[which])
#            print(dsetname)
#            h.create_dataset(dsetname, data=bddict[ph])
#            counter[which]+=1
#        #
#    #
##
