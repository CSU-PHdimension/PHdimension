'''

This is a collection of measures that can be used 
with the gen_pt_cloud_from_measure() function. 

In addition to uniform measures on some simple shapes, 
Cantor interval, and some of the other examples we 
studied in the paper, there are functions to sample 
uniformly from a piecewise linear collection of curves
(this is how the sierpinski arrowhead curve at a given 
level is defined).

'''
# import numpy as np
from numpy import pi,dot,arange,sqrt,array,zeros
from numpy.random import rand,choice,randint
from numpy.linalg import norm

# Stuff for balls
maxr2d = sqrt(1./pi)            # Radius for area one disk
maxr3d = (3./(4.*pi))**(1./3)   # Radius for volume one sphere

# Stuff for sierpinski
sf = sqrt(4./sqrt(3))/2.
v0 = sf*array([1,0])
v1 = sf*array([0.5,sqrt(3)/2.])

smap = {0:array([0,0]), 1:v0, 2:v1}

def cantor(d=60):
    '''
    Generates a point from the Cantor set with an
    optional cutoff to the ternary sequence.

    Note d=40 corresponds to roughly 19 digits of precision,
    based on the tail of a geometric series with r=1/3.
    '''
    a = choice([0,2],d)
    b = 3.**arange(-1,-d-1,-1)
    return dot(a,b)
#

def interval():
    '''Generates a point on U([0,1]).'''
    return rand()
#

def cantor_cross_interval(d=60):
    '''
    Generates a point on C x U([0,1]) with
    an optional cutoff to the ternary sequence.
    '''
    return [cantor(d=d),interval()]
#

def cantor_dust_2d(d=60):
    '''
    Generates a point on CxC with
    an optional cutoff to the ternary sequence.
    '''
    return [cantor(d=d),cantor(d=d)]
#

def cantor_dust_3d(d=60):
    '''
    Generates a point on CxCxC with
    an optional cutoff to the ternary sequence.
    '''
    return [cantor(d=d),cantor(d=d),cantor(d=d)]
#

def square():
    '''Generates a point on U([0,1])xU([0,1]).'''
    return [interval(),interval()]
#

def cube():
    '''Generates a point in the unit cube.'''
    return [interval(),interval(),interval()]
#

def disk():
    '''
    Generates a point on the area-one disk using
    rejection sampling.
    '''
    candidate = [(2*interval()-1)*maxr2d,(2*interval()-1)*maxr2d]
    while norm(candidate) > maxr2d:
        candidate = [(2*interval()-1)*maxr2d,(2*interval()-1)*maxr2d]
    #
    return candidate
#

def solid_sphere():
    '''
    Generates a point on the volume-one solid sphere using
    rejection sampling.
    '''
    candidate = [(2*interval()-1)*maxr3d,(2*interval()-1)*maxr3d,(2*interval()-1)*maxr3d]
    while norm(candidate) > maxr3d:
        candidate = [(2*interval()-1)*maxr3d,(2*interval()-1)*maxr3d,(2*interval()-1)*maxr3d]
    #
    return candidate
#

def sample_piecewise(curve):
    '''
    Given a list of points defining the vertices of a piecewise linear
    curve, sample a point uniformly from the curve.
    '''
    n = len(curve)-1
    t = n*interval()
    v0 = int(t)
    v1 = v0+1
    return list(curve[v0] + (t-v0)*(array(curve[v1])-array(curve[v0])))
#

def sierpinski_v1(d=60):
    '''
    Samples points from the Sierpinski triangle.
    More precisely, samples points
    from the bottom left endpoints of the triangles
    in the Sierpinski triangle at a specified level.

    Python implementation of Henry Adam's matlab code.
    '''

    import numpy as np

    point = zeros(2)
    binarySequence = randint(3,size=d)

    for i in range(d):
        point += smap[binarySequence[i]]/(2.**i)
    #
    return point
#
