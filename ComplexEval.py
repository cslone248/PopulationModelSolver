# Calculate values to plot when eigenvalues are complex

import numpy as np

def CalcComplex(coefmat,init,const):

    cxt = dxt = [init.xval]
    cyt = dyt = [init.yval]

    i = 1
    while i < 200:
        # discrete
        dxt.append(coefmat[0][0]*dxt[i-1] + coefmat[0][1]*dyt[i-1])
        dyt.append(coefmat[1][0]*dxt[i-1] + coefmat[1][1]*dyt[i-1])

        i=i+1
    
    # now continuous
    # evals = \alpha \pm \beta i, evecs = w_R \pm w_I i, const = c_R \pm c_I i
    # solution is: v(t) = 2\exp(\alpha t) * [ cos(\beta t)(c_Rw_R - c_Iw_I) - sin(\beta t)(c_Rw_I + c_Iw_R) ]

    s = np.linspace(0,100,500)
    cxt = const[0]*np.exp(eigvals[0]*t)*eigvecs[0][0] + const[1]*np.exp(eigvals[1]*t)*eigvecs[0][1]

    cxt = 2*np.exp(np.real(const[0])*s) * [ np.cos(np.imag(const[0])*s)() ]
    cxt.append(coefmat[0][0]*cxt[i-1] + coefmat[0][1]*cyt[i-1])
    cyt.append(coefmat[1][0]*cxt[i-1] + coefmat[1][1]*cyt[i-1])
    
    return [cxt,cyt,dxt,dyt]
