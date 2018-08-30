'''

A collection of things used to generate Sierpinski arrowhead 
curves; see 

    https://en.wikipedia.org/wiki/L-system#Example_5:_Sierpinski_triangle

for the definition and recursive construction.
The primary functions in this file are l_iters() and 
drawcurve() which are used to ultimately generate the 
collection of line segments and draw them, respectively.

'''
import numpy as np

maps = {
'A': 'B-A-B',
'B': 'A+B+A',
'+': '+',
'-': '-'
}

def rotmat(angle):
    rad = angle*np.pi/180.
    return np.array([[np.cos(rad),-np.sin(rad)],[np.sin(rad),np.cos(rad)]])
#

def turn(direction,angle):
    return np.dot(rotmat(angle),direction)
#

def l_iter(strin):
    strout = ''
    for l in strin:
        strout += maps[l]
    #
    return strout
#

def l_iters(n,**kwargs):
    verb = kwargs.get('verbosity',0)
    strin = kwargs.get('strin','A')
    strout = str(strin)
    if verb>0: print(strout)

    for i in range(n):
        strout = l_iter(strout)
        if verb>0: print(strout)
    #
    return strout
#

def drawcurve(strin,**kwargs):
    rescale = kwargs.get('rescale',False)
    drawnow = kwargs.get('drawnow',False)

    curve = [[0,0]] # Starting point
    pos = curve[0]
    orientation = np.array([1,0])
    for l in strin:
        if l in ['A','B']:
            pos = [pos[0]+orientation[0], pos[1]+orientation[1]]
            curve.append(pos)
        else:
            angle = {'-':-60,'+':60}[l]
            orientation = turn(orientation,angle)
        #
    #
    curve = np.array(curve)

    if rescale:
        # rescale coordinates so that enclosing equilateral triangle has area one.
        curve = curve*(np.sqrt(4./np.sqrt(3)))/(curve[:,0].max())
    #
    if drawnow:
        from matplotlib import pyplot
        pyplot.plot(curve[:,0],curve[:,1],c='k')
        pyplot.show(block=False)
    #
    return curve
#

if __name__=="__main__":
    from matplotlib import pyplot
    for i in range(0,13,2):
        cstr = l_iters(i)
        c = drawcurve(cstr, rescale=True)

        pyplot.plot(c[:,0],c[:,1],c='k',alpha=(12-i)/12.)
    pyplot.xlim([0,1.519671371])
    pyplot.ylim([0,1.519671371*np.sqrt(3)/2])
    pyplot.show(block=False)
