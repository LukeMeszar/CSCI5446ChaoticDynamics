#Luke Meszar
#CSCI 5446
#RK4

#import sympy as sy
import numpy as np
import matplotlib.pyplot as plt
import random


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

def plot(x_values, y_values, initialConditions,i,tol):
    plt.plot(x_values,y_values, '-', markersize = 0.5)
    plt.xlabel(r'$x$')
    plt.ylabel(r'$z$')
    #plt.savefig(str(theta0) + '-' + str(omega0) + '.png')
    #plt.savefig('lorenz'+str(r[i])+'-'+str(initialConditions[0])+'-'+str(initialConditions[1])+'-'+str(initialConditions[2])+'.png')
    plt.savefig('lorenz'+str(tol)+'.png')
    plt.clf()

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

#x: array of current points
#h: current timestep
#n: dimension of system
#non-autonomous
def trajectories(x,h,n,f):
    k1 = []
    k2 = []
    k3 = []
    k4 = []
    xi1 = []
    for i in range(n):
        k1.append(h*f[i](x))
    for i in range(n):
        xi1.append(x[i] + k1[i]*0.5)
    for i in range(n):
        k2.append(f[i](xi1)*h)
    for i in range(n):
        xi1[i] = x[i] + k2[i]*0.5
    for i in range(n):
        k3.append(f[i](xi1)*h)
    for i in range(n):
        xi1[i] = x[i] + k3[i]
    for i in range(n):
        k4.append(f[i](xi1)*h)
    for i in range(n):
        xi1[i] = x[i] + (k1[i] + 2*(k2[i] + k3[i]) + k4[i])/6
    return xi1

def rk4(t0, h, n, n_dims, xt0, f):
    x = xt0
    trajectory1 = []
    trajectory2 = []
    trajectory1.append(x[0])
    trajectory2.append(x[2])
    for i in range(n):
        x_new = trajectories(x, h, n_dims, f)
        x = x_new
        trajectory1.append(x_new[0])
        trajectory2.append(x_new[2])
    #print("trajectory1: {}".format(trajectory1[0:250]))
    plot(trajectory1,trajectory2,[0,0,0],0)


def adaptiveRK4(t0, h_1, n, n_dims, xt0, f, tol, initialConditions,counter):
    x = xt0
    trajectory1 = []
    trajectory2 = []
    trajectory1.append(x[0])
    trajectory2.append(x[2])
    h_0 = h_1
    for i in range(n):
        x_fullstep = trajectories(x, h_1, n_dims, f)
        x_halfstep1 = trajectories(x,h_1/2,n_dims, f)
        x_halfstep2 = trajectories(x_halfstep1,h_1/2,n_dims, f)
        x_distance = []
        h_values = []
        for i in range(n_dims):
            x_distance.append(abs(x_fullstep[i]-x_halfstep2[i]))
        l_infinity = max(x_distance)
        h_est = h_1*(abs(tol/l_infinity))**(0.2 if tol >= l_infinity else 0.25)
        h_0 = h_est

        x_final = trajectories(x, h_0, n_dims, f)
        h_1 = h_0
        trajectory1.append(x_final[0])
        trajectory2.append(x_final[2])
        x = x_final

    plot(trajectory1,trajectory2,initialConditions,counter,tol)
    #for i in range(len(h_values)):
    #    print(h_values[i])
    #print("trajectory1: {}".format(trajectory1[0:250]))


#def ftheta(x):
#    return x[1]

#def fomega(x):
#    A = 0
#    alpha = 0
#    beta = 0
#    l = .1
#    m = .1
#    g = 9.8
#    return ((A * np.cos(alpha))-(beta*l*x[1])-(m*g*np.sin(x[0])))/(m*l)

#f = [ftheta, fomega]
#theta0 = 3
#omega0 = 0.1
#xt0 = [theta0,omega0]
#timestep = 0.005
#rk4(0,timestep, 500,len(f), xt0, f)
#adaptiveRK4(0,timestep, 2000,len(f), xt0, f, 0.0001)

def lorenz(a,r,b,x0,y0,z0,i):
    def fx(x):
        return a*(x[1]-x[0])
    def fy(x):
        return r*x[0]-x[1]-x[0]*x[2]
    def fz(x):
        return x[0]*x[1]-b*x[2]

    f = [fx, fy, fz]
    x = [x0,y0,z0]
    timestep = 0.005
    tol = 10
    adaptiveRK4(100,timestep,200,len(f), x, f, tol, x,i)
    #rk4(0,timestep,200,len(f),x,f)


def rossler(a,b,c,x0,y0,z0,i):
    def fx(x):
        return -(x[1]+x[2])
    def fy(x):
        return x[0]+a*x[1]
    def fz(x):
        return b + x[2]*(x[0]-c)

    f = [fx,fy,fz]
    x = [x0,y0,z0]
    timestep = 0.005
    tol = 0.015
    adaptiveRK4(0,timestep,3000,len(f), x, f, tol, x,i)


r = [0,0.25,0.5,0.75,1,13.5,13.6,13.7,13.8,13.9,14,23,23.5,24,24.5,25,25.5,26,26.5,27,27.5,28,28.5,29,29.5,30]

def runLorenz(r):
    initialX = []
    initialY = []
    initialZ = []
    k=0
    while k < 5:
        x0 = random.randint(-25,25)
        initialX.append(x0)
        y0 = random.randint(-25,25)
        initialY.append(y0)
        z0 = random.randint(-25,25)
        initialZ.append(z0)
        k+=1
    for i in range(len(r)):
        for j in range(len(initialX)):
            lorenz(16,r[i],4,initialX[j],initialY[j],initialZ[j],i)

#runLorenz(r)
lorenz(16,45,4,-13,-12,52,0)
#rossler(.398,2,4,8,3,6,0)
