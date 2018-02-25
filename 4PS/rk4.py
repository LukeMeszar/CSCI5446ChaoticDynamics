#Luke Meszar
#CSCI 5446
#RK4

import sympy as sy
import numpy as np
import matplotlib.pyplot as plt


#omega = sy.symbols('omega')
#theta = sy.symbols('theta')
#t = sy.symbols('t')

#Parameters

#A: 2.75, 2.565, 2.5675

m = 0.1
l = 0.1
beta = 0
g = 9.8
A = 0
alpha = 0#0.75*np.sqrt(g/l)

def plot(thetaValues, omegaValues):
    newThetaValues = []
    #for i in range(0, len(thetaValues)):
    #    modulus = int(np.floor(thetaValues[i] / (2*np.pi)))
    #    newThetaValues.append(thetaValues[i] - (modulus*2*np.pi))
    #    newThetaValues.append(thetaValues[i]%(2*np.pi))

    plt.plot(thetaValues,omegaValues, "o")
    plt.xlabel(r'$\theta$')
    plt.ylabel(r'$\omega$')
    #plt.savefig(str(theta0) + '-' + str(omega0) + '.png')
    plt.savefig('zz.png')
    #plt.savefig('test.png')
    plt.show()

def writetofile(thetaValues, omegaValues):
    for i in range(0, len(thetaValues)):
        outString = str(thetaValues[i]) + ", " + str(omegaValues[i]) + ", " + "\n"
        with open('out2put' + str(A) + '.csv', "a") as f:
            f.write(outString)

#t0: initial time
#h: time step
#n: number of iterations
#xt0: array of [theta,omega]
#f: array of f
def rk4(t0, h, n, xt0, f):
    t = t0;
    x = xt0
    thetaValues = [xt0[0]]
    omegaValues = [xt0[1]]
    thetaValuesMod = [xt0[0]%(2*np.pi)]
    for i in range(1,n):
        k1 = [0,0]
        k2 = [0,0]
        k3 = [0,0]
        k4 = [0,0]
        xi1 = [0,0]
        k1[0] = h*f[0](x[0], x[1], t)
        k1[1] = h*f[1](x[0], x[1], t)
        k2[0] = h*f[0](x[0] + 1/2 * k1[0],x[1] + 1/2*k1[1], t + h/2)
        k2[1] = h*f[1](x[0] + 1/2 * k1[0],x[1] + 1/2*k1[1], t + h/2)
        k3[0] = h*f[0](x[0] + 1/2 * k2[0],x[1] + 1/2*k2[1], t + h/2)
        k3[1] = h*f[1](x[0] + 1/2 * k2[0],x[1] + 1/2*k2[1], t + h/2)
        k4[0] = h*f[0](x[0]+k3[0], x[1]+k3[1], t + h)
        k4[1] = h*f[1](x[0]+k3[0], x[1]+k3[1], t + h)
        x[0] = x[0]+1/6*(k1[0]+2*k2[0]+2*k3[0]+k4[0])
        x[1] = x[1]+1/6*(k1[1]+2*k2[1]+2*k3[1]+k4[1])
        omegaValues.append(x[1])
        #print("theta: {} omega: {}".format(x[0], x[1]))
        thetaValues.append(x[0])
        thetaValuesMod.append(x[0]%(2*np.pi))

        #print('theta:{}, omega:{}\n'.format(x[0],x[1]))
        t += h
    plot(thetaValuesMod, omegaValues)
    writetofile(thetaValuesMod, omegaValues)





def ftheta(theta, omega, t): return omega
def fomega(theta, omega, t):
    return (A*np.cos(alpha * t)/(m*l))-(beta/m)*omega - (g/l)*np.sin(theta)

f = [ftheta, fomega]
theta0 = 0.1
omega0 = 0
xt0 = [theta0,omega0]
timestep = 0.005
rk4(0,timestep, 800, xt0, f)
