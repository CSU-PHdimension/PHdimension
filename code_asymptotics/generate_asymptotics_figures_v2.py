
from matplotlib import pyplot
import numpy as np
from extrapolate_asymptotics import extrapolate_asymptotics

np.random.seed(1248163264) # for reproducibility

# Make an example with known scaling and some noise.
x = np.arange(200,20001,200)
y = (100*x**1 + 1/10*x**2)*(1 + 0.1*np.random.randn(len(x)))

result = extrapolate_asymptotics(x,y)

# Take a look at the log-error of the
# power estimates over all values of (p,q).
fig2,ax2 = pyplot.subplots(1,1)
logabserr = np.log10(np.abs(result.A[:,4]-2.))

# blerp = ax2[0].scatter(result.A[:,2], result.A[:,3], c=logabserr,
#         cmap=pyplot.cm.viridis, vmin=-3, vmax=0., s=20, marker='s')

blerp = ax2.scatter(result.A[:,2], result.A[:,3], c=result.A[:,4],
        cmap=pyplot.cm.bwr_r, vmin=0., vmax=4., s=5, marker='s')

def colorbar2(mappable):
    # behaves a little better with funny aspect ratio figures.
    # taken from:
    # https://joseph-long.com/writing/colorbars/
    from mpl_toolkits.axes_grid1 import make_axes_locatable
    myax = mappable.axes
    fig = myax.figure
    divider = make_axes_locatable(myax)
    mycax = divider.append_axes("right", size="3%", pad=0.1)
    return fig.colorbar(mappable, cax=mycax)
#

ax2.plot([0,x.max()],[0,x.max()], ls='--', c='k')
ax2.set_title(r'Least squares approximations $\hat{\alpha}$', fontsize=16)
ax2.set_xlabel(r'Minimum data point $p$', fontsize=14)
ax2.set_ylabel(r'Minimum data point $q$', fontsize=14)

colorbar2(blerp)
ax2.axis('square')
fig2.tight_layout()

ax2.set_xticks(np.arange(0,20001,5000))
ax2.set_yticks(np.arange(0,20001,5000))

##
if False:
    fig,ax = pyplot.subplots(1,1)
    ax.scatter(x,y, s=10, label=r'$(100x + \frac{1}{10}x^2)(1+\varepsilon(x))$')
    ax.set_xscale('log')
    ax.set_yscale('log')
    #ax.axis('square')

    result = extrapolate_asymptotics(x,y)

    fit = np.exp(result.C) * x**result.alpha
    ax.plot(x,fit, c='r', label=r'Calculated fit $%.2f x^{%.2f}$'%(np.exp(result.C), result.alpha), fontsize=14 )
    ax.legend(loc='upper left')
else:
    from mpl_toolkits.axes_grid1.inset_locator import inset_axes
    ax = inset_axes(ax2,
                    width="40%", # width = 30% of parent_bbox
                    height="40%", # height : 1 inch
                    loc='lower right')

    ax.scatter(x,y, s=40, marker='o', color=[0,0,0,0], edgecolor='b', zorder=-100)

    ax.annotate(r'$f(x)$', (2*10**2,2*10**5))
    ax.annotate(r'Fit $%.2f x^{%.2f}$'%(np.exp(result.C), result.alpha), (4*10**2,10**4))

    ax.set_xscale('log')
    ax.set_yscale('log')
    #ax.axis('square')

    fit = np.exp(result.C) * x**result.alpha
    ax.plot(x,fit, c='k', lw=3, zorder=0)
    ax.plot(x,fit, c='w', lw=5, zorder=-50)

    ax.set_xticklabels([])
    ax.set_yticklabels([])

#

#######

if True:
    fig3a = pyplot.figure(figsize=(9,4))
    # with the 12 units, allocate space accordingly.
    padx = 1 # left/middle padding. Note we are giving
                # a bit of space for the colorbar on the right.
    pady = 0.5 # top/bottom padding
    wx = (9 - padx*3)/2.
    wy = (4 - pady*2)

    padx /= 9.
    wx /= 9.
    pady /= 4.
    wy /= 4.

    ax3a = fig3a.add_axes([padx,pady,wx,wy])
    ax3b = fig3a.add_axes([2*padx+wx,pady,wx,wy])
    ax3c = fig3a.add_axes([2.25*padx+2*wx,pady,0.15*padx,wy])
else:
    fig3a,(ax3a,ax3b) = pyplot.subplots(1,2, figsize=(8,4))
#
# ax3c = fig3a.add_axes([2*padx+2*wx,pady,padx*0.5,wy])

#fig3,ax3 = pyplot.subplots(1,1, figsize=(5,5))
#fig4,ax4 = pyplot.subplots(1,1, figsize=(6,5))

blerp1 = ax3a.scatter(result.A[:,2], result.A[:,3], c=logabserr,
        cmap=pyplot.cm.viridis, vmin=-3, vmax=0., s=2, marker='s')

ax3a.set_xlabel(r'Minimum data point $p$', fontsize=14)
ax3a.set_ylabel(r'Minimum data point $q$', fontsize=14)

blerp2 = ax3b.scatter(1./result.A[:,2], 1./result.A[:,3], c=logabserr,
        cmap=pyplot.cm.viridis, vmin=-3, vmax=0., s=2, marker='s')

#colorbar2(blerp2)

fig3a.colorbar(blerp1, cax=ax3c)

ax3b.set_xscale('log')
ax3b.set_yscale('log')
ax3b.set_xlim([0.5/(result.A[:,2].max()),1.5/(result.A[:,2].min())])
ax3b.set_ylim([0.5/(result.A[:,3].max()),1.5/(result.A[:,3].min())])

fig3a.suptitle(r'Log-error in asymptotic exponent; $\log_{10}(|\hat{\alpha} - \alpha|)$', fontsize=16)

ax3b.set_xlabel(r'Inversion $1/p$', fontsize=14)
ax3b.set_ylabel(r'Inversion $1/q$', fontsize=14)

#fig3a.colorbar(blerp2)

ax3b.axis('square')
ax3b.set_xlim([4*10**-5,10**-2])
ax3b.set_ylim([4*10**-5,10**-2])

ax3a.axis('square')
ax3a.set_xticks(np.arange(0,20001,5000))
ax3a.set_yticks(np.arange(0,20001,5000))


pyplot.show(block=False)

if True:
    fig2.savefig('alpha_pq_grid.eps', bbox_inches='tight', dpi=120)
    fig2.savefig('alpha_pq_grid.png', bbox_inches='tight', dpi=120)

    fig3a.savefig('log-error_alpha_pq_grid.png', bbox_inches='tight', dpi=120)
    fig3a.savefig('log-error_alpha_pq_grid.eps', bbox_inches='tight', dpi=120)

#fig4.savefig('log-error_alpha_pq_grid_right.png', bbox_inches='tight', dpi=120)
#fig4.savefig('log-error_alpha_pq_grid_right.eps', bbox_inches='tight', dpi=120)

#fig2.savefig('alpha_pq_grid.png', bbox_inches='tight', dpi=120)
#fig3.savefig('log-error_alpha_pq_grid.png', bbox_inches='tight', dpi=120)#
