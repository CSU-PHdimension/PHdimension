'''
Implementation of extrapolate_asymptotics.m
in Python, with the full functionality
described in Appendix C implemented.
(all S_pq are calculated).
'''

import numpy as np

class Dummy:
    def __init__(self):
        self.alpha = None
        self.C = None
        self.A = None
        return
#

def extrapolate_asymptotics(seqx, seqy):
    '''
    Calculates all possible power-law fits
    of subsets of (seqx,seqy), then uses
    linear extrapolation on (1/seqx,1/seqy, alphahat)
    to get an extrapolant (0,0,alpha).
    Similarly for C.


    Inputs:
        seqx: list-like of x coordinates
        seqy: list-like of y coordinates
    Outputs:
        result: an object with entries:

        result.alpha    : approximated power
        result.C        : approximated coeff
        result.A        : m-by-6 array whose rows are
                        [i,j,p,q, alphahat, chat]
                        from which the "true"
                        asymptotics are extrapolated.
    '''

    # Reorder in increasing x.
    order = np.argsort(seqx)
    x = np.array(seqx)[order]
    y = np.array(seqy)[order]

    # Compute all possible fits.
    A = []
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            p, q = x[i], x[j]
            logxs = np.log( x[i:j] )
            logys = np.log( y[i:j] )
            if len(logxs)<2:
                continue
            else:
                pfit = np.polyfit(logxs,logys, deg=1)
                alphahat,chat = pfit

                A.append([i,j,p,q, alphahat, chat])
    #
    A = np.array(A)

    m = A.shape[0]

    # Now fit a linear function to the data
    # (xi,eta,zeta) = (1/p, 1/q, alphahat) of
    # the form zeta = a[0] + a[1]*xi + a[2]*eta, and use
    # the value of a[0] as the estimate (xi=eta=0).

    result = Dummy()

    designmat = np.hstack([ np.ones((m,1)), 1./A[:,2].reshape(m,1), 1./A[:,3].reshape(m,1) ])
    rhs_alpha = A[:,4].reshape(m,1)
    rhs_C = A[:,5].reshape(m,1)

    fit_alpha = np.linalg.lstsq(designmat, rhs_alpha)
    result.alpha = fit_alpha[0][0][0]

    fit_C = np.linalg.lstsq(designmat, rhs_C)
    result.C = fit_C[0][0][0]

    result.A = A

    return result
#

if __name__=="__main__":
    from matplotlib import pyplot
    import numpy as np

    # Make an example with known scaling and some noise.
    x = np.arange(100,10001,100)
    y = 100*x**1 + 1/10*x**2*(1 + 0.1*np.random.randn(len(x)))

    fig,ax = pyplot.subplots(1,1)
    ax.scatter(x,y, s=10, label=r'$x^2$')
    ax.set_xscale('log')
    ax.set_yscale('log')

    result = extrapolate_asymptotics(x,y)

    fit = np.exp(result.C) * x**result.alpha
    ax.plot(x,fit, c='r', label=r'Asymptotic fit $%.2f x^{%.2f}$'%(np.exp(result.C), result.alpha) )
    ax.legend(loc='upper left')

    # Take a look at the log-error of the
    # power estimates over all values of (p,q).
    fig2,ax2 = pyplot.subplots(1,1)
    logabserr = np.log10(np.abs(result.A[:,4]-2.))

    # blerp = ax2[0].scatter(result.A[:,2], result.A[:,3], c=logabserr,
    #         cmap=pyplot.cm.viridis, vmin=-3, vmax=0., s=20, marker='s')

    blerp = ax2.scatter(result.A[:,2], result.A[:,3], c=result.A[:,4],
            cmap=pyplot.cm.RdYlBu, vmin=0., vmax=4., s=20, marker='s')


    ax2.plot([0,x.max()],[0,x.max()], ls='--', c='k')
    ax2.set_title(r'Least squares approximations $\hat{\alpha}$', fontsize=16)
    ax2.set_xlabel(r'Minimum data point $p$', fontsize=14)
    ax2.set_ylabel(r'Minimum data point $q$', fontsize=14)

    fig2.colorbar(blerp)
    fig2.tight_layout()

    fig3,ax3 = pyplot.subplots(1,2, figsize=(10,5))

    ax3[0].scatter(result.A[:,2], result.A[:,3], c=logabserr,
            cmap=pyplot.cm.viridis, vmin=-3, vmax=0., s=2, marker='s')

    ax3[0].set_xlabel(r'Minimum data point $p$', fontsize=14)
    ax3[0].set_ylabel(r'Minimum data point $q$', fontsize=14)

    blerp2 = ax3[1].scatter(1./result.A[:,2], 1./result.A[:,3], c=logabserr,
            cmap=pyplot.cm.viridis, vmin=-3, vmax=0., s=2, marker='s')

    ax3[1].set_xscale('log')
    ax3[1].set_yscale('log')
    ax3[1].set_xlim([0.5/(result.A[:,2].max()),1.5/(result.A[:,2].min())])
    ax3[1].set_ylim([0.5/(result.A[:,3].max()),1.5/(result.A[:,3].min())])

    fig3.suptitle(r'Log-error in asymptotic exponent; $\log_{10}(|\hat{\alpha} - \alpha|)$', fontsize=16)

    ax3[1].set_xlabel(r'Inversion $1/p$', fontsize=14)
    ax3[1].set_ylabel(r'Inversion $1/q$', fontsize=14)

    fig3.colorbar(blerp2)

    fig3.tight_layout()
    fig3.subplots_adjust(top=0.9)

    pyplot.show(block=False)

    fig2.savefig('alpha_pq_grid.png', bbox_inches='tight', dpi=120)
    fig3.savefig('log-error_alpha_pq_grid.png', bbox_inches='tight', dpi=120)
#
