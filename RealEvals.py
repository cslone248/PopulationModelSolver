# calculate values to plot when eigenvalues are real

import numpy as np

def CalcReal(eigvals,eigvecs,const):

    # different time steps for the discrete and continuous systems
    t = np.linspace(0,100,100)
    s = np.linspace(0,100,100)

    cxt = const[0]*np.exp(eigvals[0]*t)*eigvecs[0][0] + const[1]*np.exp(eigvals[1]*t)*eigvecs[0][1]
    cyt = const[0]*np.exp(eigvals[1]*t)*eigvecs[1][0] + const[1]*np.exp(eigvals[1]*t)*eigvecs[1][1]

    dxt = const[0]*(eigvals[0]**s)*eigvecs[0][0] + const[1]*(eigvals[1]**s)*eigvecs[0][1]
    dyt = const[0]*(eigvals[1]**s)*eigvecs[1][0] + const[1]*(eigvals[1]**s)*eigvecs[1][1]

    return [cxt,cyt,dxt,dyt]