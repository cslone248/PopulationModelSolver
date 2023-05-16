# calculate values for discrete system
# just iterate for desired number of steps

def CalcDisc(coefmat,init):
    dxt = [init.xval]
    dyt = [init.yval]

    i = 1
    while i < 500:
        dxt.append(coefmat[0][0]*dxt[i-1] + coefmat[0][1]*dyt[i-1])
        dyt.append(coefmat[1][0]*dxt[i-1] + coefmat[1][1]*dyt[i-1])

        i=i+1

    return [dxt,dyt]