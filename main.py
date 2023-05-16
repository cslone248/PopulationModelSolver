# Discrete and continuous population model solver
# for a 2x2 system

import numpy as np
import re
import matplotlib.pyplot as plt
from State import State
from CalcDisc import CalcDisc
from CalcCont import CalcCont

print("This is a discrete and continuous population model solver for linear, 2x2 systems.\n")

print("Enter your 2x2 coefficient matrix by row: ")
coefstr = input()

# convert string input to floats
coeflist = re.findall(r'-?\d+(?:\.\d+)?', coefstr)
coeflist = [float(x) for x in coeflist]

# error handling
if len(coeflist) > 4:
    print("You supplied too many entries. Only the first four will be used.")
if len(coeflist) < 4:
    print("You did not supply enough entries. Please enter four values for the 2x2 coefficient matrix: ")
    coefstr = input()
    coeflist = re.findall(r'-?\d+(?:\.\dt+)?', coefstr)
    coeflist = [float(x) for x in coeflist]

print("Enter your initial conditions as \'x_0, y_0\': ")
initstr = input()

# convert string input to floats
initlist = re.findall(r'-?\d+(?:\.\d+)?', coefstr)
initlist = [float(x) for x in initlist]

# error handling
if len(initlist) > 4:
    print("You supplied too many initial conditions. Only the first two will be used.")
if len(initlist) < 4:
    print("You did not supply enough initial conditions. Please enter two initial conditions: ")
    initstr = input()
    initlist = re.findall(r'-?\d+(?:\.\dt+)?', coefstr)
    initlist = [float(x) for x in initlist]


# coefficient matrix and initial values
coefmat = [[coeflist[0],coeflist[1]],[coeflist[2],coeflist[3]]]
init = State(initlist[0],initlist[1])

print("The coefficient matrix and initial conditions are:")
print(coefmat)
print("x_0 = " + str(init.xval) + ", y_0 = " + str(init.yval) + "\n")

# now to solve the system

# collect eigvals and eigvecs. round to 3 decimal places
eigvals = np.round(np.linalg.eig(coefmat)[0],3)
eigvecs = np.round(np.linalg.eig(coefmat)[1],3)

print("The eigenvectors and eigenvalues are:")
print(str(eigvals)+"\n")
print(str(eigvecs)+"\n")

const = np.round(np.linalg.solve(eigvecs,[init.xval,init.yval]),3)

print("The constants are:")
print(const)

# different calculations based on whether the eigenvalues are complex or not
#if np.iscomplex(eigvals[0]) == True:
#    plotvals = CalcComplex(coefmat,init)
#elif np.iscomplex(eigvals[0]) == False:
#    plotvals = CalcReal(eigvals,eigvecs,const)
    
t = np.linspace(0,100,100)


discvals = CalcDisc(coefmat,init)
contvals = CalcCont(eigvals,eigvecs,const)

# create the solution plots
fig, axs = plt.subplots(1,2,figsize=(10,5)) 

axs[0].plot(contvals[0],contvals[1])
axs[0].set_xlim(np.min(contvals[0]),np.max(contvals[0]))
axs[0].set_title("The continuous solution")

axs[1].scatter(discvals[0],discvals[1])
axs[1].set_title("The discrete solution")

plt.show()

