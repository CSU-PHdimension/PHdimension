def gen_pt_cloud_from_measure(measure,npoints,*args,**kwargs):
    '''
    Generates a point cloud of npoints sampled
    from an input measure which samples from that
    measure ONCE. All *args and **kwargs are passed 
    directly to the measure function.

    Inputs:
        measure: a function which takes in a collection of 
            optional arguments and outputs a single point 
            sampled from that measure.
        npoints: integer; the number of points to sample.
    Outputs:
        cloud: an npoints-by-d numpy array of points in 
            d dimensions sampled from the measure.
    Optional inputs:
        The form of the inputs depends on optional inputs 
        that the measure accepts.
    '''
    import numpy as np

    cloud = []
    for i in range(npoints):
        cloud.append( measure(*args,**kwargs) )
    #
    return np.array(cloud)
#
