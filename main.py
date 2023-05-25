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
initlist = re.findall(r'-?\d+(?:\.\d+)?', initstr)
initlist = [float(x) for x in initlist]

# error handling
if len(initlist) > 2:
    print("You supplied too many initial conditions. Only the first two will be used.")
if len(initlist) < 2:
    print("You did not supply enough initial conditions. Please enter two initial conditions: ")
    initstr = input()
    initlist = re.findall(r'-?\d+(?:\.\dt+)?', initstr)
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

# determine system behavior based on eigenvalues


if np.isreal(eigvals[0]) == True:
    # handle special cases first
    if eigvals[1] == 0 or eigvals[1] == 0:
        contcap = "One or more of the eigenvalues is zero. This is a degenerative case and no firm conclusion can be drawn."
        discap = contcap # degenerative case the same for both cont/disc
    elif eigvals[1] == 1 or eigvals[1] == 1:
        contcap = "One or more of the eigenvalues is one. Further analysis is required to determine system behavior."
        discap = contcap # degenerative case the same for both cont/disc
    # figure out max magnitude eigenvalue
    if np.abs(eigvals[0]) > np.abs(eigvals[1]):
        maxmag = eigvals[0]
    else:
        maxmag = eigvals[1]
    # handle continuous case first
    if eigvals[0] > 0 and eigvals[1] > 0:
        contcap = "Both eigenvalues are real and positive, the origin is an unstable source. Population growth is to infinity."
    elif eigvals[0] < 0 and eigvals[1] < 0:
        contcap = "Both eigenvalues are real and negative, the origin is a stable sink. Population decay is to zero."
    else:
        contcap = "The eigenvalues are real and of opposite sign, the origin is an unstable saddle. Population growth will follow the eigenvector corresponding to the larger magnitude eigenvalue of " + str(maxmag) + "."
    # now handle discrete case
    if np.abs(eigvals[0]) > 1 and np.abs(eigvals[1]) > 1:
        discap = "The eigenvalues both have magnitude larger than one. The origin is an unstable source and population growth is unbounded. Population growth will follow the eigenvector corresponding to the larger magnitude eigenvalue of " + str(maxmag) + "."
    elif np.abs(eigvals[0]) < 1 and np.abs(eigvals[1]) < 1:
        discap = "The eigenvalues both have magnitude less than one. The origin is a stable sink and population decay is to zero."
    elif (np.abs(eigvals[0]) > 1 and np.abs(eigvals[1]) < 1) or (np.abs(eigvals[0]) < 1 and np.abs(eigvals[1]) > 1):
        discap = "One eigenvalue has magnitude larger than one and the other has magnitude less than one. The origin is a saddle and population growth will follow the eigenvector corresponding to the larger magnitude eigenvalue of " + str(maxmag) + "."
else:
    if np.real(eigvals[0]) == 0:
        contcap = "The eigenvalues are complex conjugates with real part equal to zero. This is a degenerative case and no firm conclusion can be drawn."
    elif np.abs(eigvals[0]) > 1:
        contcap = "The eigenvalues are complex conjugates with magnitude larger than one. The origin is an unstable source with population growth towards infinity."
    elif np.abs(eigvals[0]) < 1:
        contcap = "The eigenvalues are complex conjugates with magnitude smaller than one. The origin is a stable sink with population decay towards zero."
    else:
        contcap = "The eigenvalues are complex conjugates with magnitude equal to one. Population growth is periodic."
    discap = contcap # analysis is the same for cont/disc when eigenvalues are complex

print("\nFor the continuous system:\n" + contcap)

print("\nFor the discrete system: " + discap)
    
t = np.linspace(0,10,100)


discvals = CalcDisc(coefmat,init)
contvals = CalcCont(eigvals,eigvecs,const)

# create the solution plots
fig, axs = plt.subplots(1,2,figsize=(10,5)) 

axs[0].plot(contvals[0],contvals[1])
axs[0].set_xlim(0,np.max(contvals[0]))
axs[0].set_ylim(0,np.max(contvals[1])*2)
axs[0].set_title("The continuous solution")

axs[1].scatter(discvals[0],discvals[1])
axs[1].set_title("The discrete solution")

# Enable interactive mode
plt.ion()

# Continuously update the plot based on user zooming
while True:
    # Display the plot
    plt.show()

    # Wait for user interaction
    plt.waitforbuttonpress()

    # Get the current axis limits
    xlim = axs[0].get_xlim()
    ylim = axs[0].get_ylim()

    # Modify the zoom window by a factor of 0.5
    x_range = xlim[1] - xlim[0]
    #y_range = ylim[1] - ylim[0]
    y_range = np.max(contvals[1]) - np.min(contvals[1])
    xlim = (xlim[0] + 0.85 * x_range, xlim[1] - 0.85 * x_range)
    ylim = (ylim[0] + 0.85 * y_range, ylim[1] - 0.85 * y_range)

    # Set the updated limits for the x-axis and y-axis
    axs[0].set_xlim(xlim)
    axs[0].set_ylim(ylim)



#plt.show()

