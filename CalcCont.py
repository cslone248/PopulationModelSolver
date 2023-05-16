# calculate values to plot for continuous system
# using closed form solutions

import numpy as np

def CalcCont(eigvals,eigvecs,const):

    s = np.linspace(0,10,500)

    # different calculations based on whether the eigenvalues are complex or not
    if np.iscomplex(eigvals[0]) == True:
        # extract the real and imaginary parts of the constants, evecs, and evals
        cR = np.real(const[0])
        cI = np.imag(const[0])
        wRx = np.real(eigvecs[0][0])
        wIx = np.imag(eigvecs[0][0])
        wRy = np.real(eigvecs[1][0])
        wIy = np.imag(eigvecs[1][0])
        lR = np.real(eigvals[0])
        lI = np.imag(eigvals[0])

        cxt = 2*np.exp(lR*s) * [ np.cos(lI*s)*( cR*wRx - cI*wIx ) - np.sin(lI*s)*( cR*wIx + cI*wRx ) ]
        cyt = 2*np.exp(lR*s) * [ np.cos(lI*s)*( cR*wRy - cI*wIy ) - np.sin(lI*s)*( cR*wIy + cI*wRy ) ]

    elif np.iscomplex(eigvals[0]) == False:
        cxt = const[0]*np.exp(eigvals[0]*s)*eigvecs[0][0] + const[1]*np.exp(eigvals[1]*s)*eigvecs[0][1]
        cyt = const[0]*np.exp(eigvals[1]*s)*eigvecs[1][0] + const[1]*np.exp(eigvals[1]*s)*eigvecs[1][1]



    return [cxt,cyt]