'''
Loops over number of points and a fixed measure
(Sierpinski arrowhead at a given level as an 
  approximations to the Sierpinski triangle)
and dumps the results as a large collection of 
pickle files.

Be careful running this script! This currently 
takes a large amount of memory to succeed; 
the largest number of points has been changed to 
3325, but even this may require a few hundred 
gigabytes of RAM. The original version 
went up to 1.5**24; roughly 16834 points.
'''

import ripser_interface as ri
import pickle
import numpy as np

#################################
#
# Parameters
#
nprocs = 2 # Note that storing the string inputs 
           # for inputing to ripser can take a large 
           # amount of memory as well - recommended not 
           # to actually use a large number of procs 
           # unless the max number of points is kept small.

seq = np.array( 1.5**np.arange(8,20), dtype=int)
npoints = seq.max()

# Generate the curve approximating sierpinski
# at a given scale. Use even numbers.
level = 6

#############################################

cstr = ri.l_systems.sierpinski.l_iters(level)
c = ri.l_systems.sierpinski.drawcurve(cstr, rescale=True)

def s_measure():
    return ri.test_measures.sample_piecewise(c)
#

results = ri.single_sequence_scaling(s_measure, npoints, seq=seq, nprocs=nprocs)

f = open('sierpinski_lvl%i_n%i.pkl'%(level,npoints),'wb')
pickle.dump(results,f)
f.close()
