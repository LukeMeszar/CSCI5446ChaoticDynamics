import numpy as np
import matplotlib.pyplot as plt
import sympy as sy

def plot(x_values, y_values, initialConditions,i):
    plt.plot(x_values,y_values, 'o', markersize = 0.5)
    plt.xlabel(r'$x$')
    plt.ylabel(r'$z$')
    #plt.savefig(str(theta0) + '-' + str(omega0) + '.png')
    #plt.savefig('lorenz'+str(r[i])+'-'+str(initialConditions[0])+'-'+str(initialConditions[1])+'-'+str(initialConditions[2])+'.png')
    plt.savefig('testing.png')
    plt.clf()

def plotPoincare(x_values, y_values, T, typeName, timestep=-1, option=-1):
    plt.plot(x_values,y_values, 'o', markersize = 0.5)
    plt.xlabel(r'$x$')
    plt.ylabel(r'$z$')
    #plt.xlim([9,17.5])
    #plt.ylim([18,55])
    #plt.xlim([-0.1,0.])
    #plt.ylim([18,55])
    plt.savefig('poincareSpatial' + str(T) + typeName + str(option) + str(timestep) +'.png')
    plt.clf()

def writetofile(thetaValues, omegaValues):
    for i in range(0, len(thetaValues)):
        outString = str(thetaValues[i]) + ", " + str(omegaValues[i]) + ", " + "\n"
        with open('output' + str(runningCounter) + '.csv', "a") as f:
            f.write(outString)

def trajectories(x,h,n,f,t):
    k1 = []
    k2 = []
    k3 = []
    k4 = []
    xi1 = []
    for i in range(n):
        k1.append(h*f[i](x,t))
    for i in range(n):
        xi1.append(x[i] + k1[i]*0.5)
    for i in range(n):
        k2.append(f[i](xi1, t + h/2)*h)
    for i in range(n):
        xi1[i] = x[i] + k2[i]*0.5
    for i in range(n):
        k3.append(f[i](xi1, t + h/2)*h)
    for i in range(n):
        xi1[i] = x[i] + k3[i]
    for i in range(n):
        k4.append(f[i](xi1, t +h)*h)
    for i in range(n):
        xi1[i] = x[i] + (k1[i] + 2*(k2[i] + k3[i]) + k4[i])/6
    return xi1


def rk4(t0, h, n, n_dims, xt0, f, system):
    x = xt0
    trajectory1 = []
    trajectory2 = []
    trajectory3 = []
    timeStamp = []
    trajectory1.append(x[0])
    trajectory2.append(x[1])
    timeStamp.append(t0)
    t = t0
    for i in range(n):
        x_new = trajectories(x, h, n_dims, f, t)
        x = x_new
        trajectory1.append(x_new[0])
        trajectory2.append(x_new[1])
        if system > 0:
            trajectory3.append(x_new[2])
        timeStamp.append(t+h)
        t += h
    #print("trajectory1: {}".format(trajectory1[0:250])
    if system == 0:
        newTrajectory1 = []
        for i in range(len(trajectory1)):
            newTrajectory1.append(trajectory1[i]%(2*np.pi))
        plot(newTrajectory1,trajectory2,[0,0,0],0)
        return[newTrajectory1, trajectory2, timeStamp]
    else:
        return [trajectory1, trajectory2, trajectory3]


def poincare(T):
    trajectoryVector = rk4(0,timestep, int(1000/timestep),len(f), xt0, f,0)
    poincare1 = []
    poincare2 = []
    n = 1
    threshHold = T
    helper = 0
    checker = 0.0
    pointCounter = 0
    while (helper < len(trajectoryVector[2])):
        checker += timestep
        if (checker > threshHold*pointCounter):
            pointCounter += 1
            poincare1.append(trajectoryVector[0][helper])
            poincare2.append(trajectoryVector[1][helper])
        helper += 1

    print(pointCounter)
    #writetofile(poincare1, poincare2)
    plotPoincare(poincare1, poincare2, T, 'temporal', timestep)


def poincareInterpolation(T):
    trajectoryVector = rk4(0,timestep, int(1000/timestep),len(f), xt0, f,0)
    poincare1 = []
    poincare2 = []
    n = 1
    threshHold = T
    helper = 0
    checker = 0.0
    pointCounter = 0
    while (helper < len(trajectoryVector[2])):
        checker += timestep
        if (checker > threshHold*pointCounter):
            # t = sy.symbols('t')
            # prevPoint = [trajectoryVector[0][helper-1],trajectoryVector[1][helper-1]]
            # nextPoint = [trajectoryVector[0][helper],trajectoryVector[1][helper]]
            # xt = prevPoint[0]+(prevPoint[0]-nextPoint[0])*t
            # yt = prevPoint[1]+(prevPoint[1]-nextPoint[1])*t
            # point_on_plane = [xt.subs(t,threshHold*pointCounter),yt.subs(t,threshHold*pointCounter)]
            t_prev_to_plane = np.abs(threshHold*pointCounter - trajectoryVector[2][helper-1])
            point_on_plane = trajectories([trajectoryVector[0][helper-1],trajectoryVector[1][helper-1]],t_prev_to_plane, 2, f, trajectoryVector[2][helper-1])
            poincare1.append(point_on_plane[0])
            poincare2.append(point_on_plane[1])
            pointCounter += 1
            poincare1.append(point_on_plane[0])
            poincare2.append(point_on_plane[1])
        helper += 1

    print(pointCounter)
    writetofile(poincare1, poincare2)
    plotPoincare(poincare1, poincare2, T, 'temporal-intp', timestep)


def poincareSpatial(option, f,x):
    t = sy.symbols('t')
    xx = sy.symbols('xx')
    y = sy.symbols('y')
    trajectoryVector = rk4(0,timestep, 10000,3, x, f,1)
    poincare1 = []
    poincare2 = []
    n = 1
    if option == 0:
        norm = [0,1,0]
        x_sigma = [0,20,0]
    else:
        norm = [-2,1,0]
        x_sigma = [2,4,0]
    pointCounter = 0
    for i in range(len(trajectoryVector[0])-2):
        prevPoint = [trajectoryVector[0][i],trajectoryVector[1][i],trajectoryVector[2][i]]
        nextPoint = [trajectoryVector[0][i+1],trajectoryVector[1][i+1],trajectoryVector[2][i+1]]
        d_prevPoint = [trajectoryVector[0][i]-x_sigma[0],trajectoryVector[1][i]-x_sigma[1],trajectoryVector[2][i]-x_sigma[2]]
        d_nextPoint = [trajectoryVector[0][i+1]-x_sigma[0],trajectoryVector[1][i+1]-x_sigma[1],trajectoryVector[2][i+1]-x_sigma[2]]
        #print(prevPoint,nextPoint)
        dot1 = np.dot(d_prevPoint,norm)
        dot2 = np.dot(d_nextPoint, norm)
        #print(dot1,dot2)
        print(dot2)
        if np.sign(dot1) <= 0 and np.sign(dot2) > 0:
            pointCounter += 1
            xt = prevPoint[0]+(prevPoint[0]-nextPoint[0])*t
            yt = prevPoint[1]+(prevPoint[1]-nextPoint[1])*t
            zt = prevPoint[2]+(prevPoint[2]-nextPoint[2])*t
            intersection_point = 0
            point_on_plane = []
            if option == 0:
                intersection_point = sy.solve(yt-0*xt+0*zt-20, t)
                point_on_plane = [xt.subs(t,intersection_point[0]),yt.subs(t,intersection_point[0]),zt.subs(t,intersection_point[0])]
            else:
                intersection_point = sy.solve(yt-2*xt+0*zt, t)
                point_on_plane = [xt.subs(t,intersection_point[0]),yt.subs(t,intersection_point[0]),zt.subs(t,intersection_point[0])]
            poincare1.append(point_on_plane[0])
            poincare2.append(point_on_plane[2])
    print(pointCounter)
    print(poincare1)
    #writetofile(poincare1, poincare2)
    plotPoincare(poincare1, poincare2, 0, 'spatial-intp', option)



def ftheta(x,t):
    return x[1]

def fomega(x,t):
    l = .1
    m = .1
    g = 9.8
    A = 0.9
    #A = 0
    alpha = 0.75*np.sqrt(g/l)
    beta = 0.25
    #beta = 0
    return ((A * np.cos(alpha*t))-(beta*l*x[1])-(m*g*np.sin(x[0])))/(m*l)

f = [ftheta, fomega]
theta0 = 0.01
omega0 = 0
xt0 = [theta0,omega0,0]
timestep = 0.1
#rk4(0,timestep, 10000,len(f), xt0, f)
l = .1
m = .1
g = 9.8
def lorenz(a,r,b,x0,y0,z0):
    def fx(x,t):
        return a*(x[1]-x[0])
    def fy(x,t):
        return r*x[0]-x[1]-x[0]*x[2]
    def fz(x,t):
        return x[0]*x[1]-b*x[2]

    f = [fx, fy, fz]
    x = [x0,y0,z0]
    timestep = 0.005
    tol = 10
    poincareSpatial(1,f,x)
    #rk4(0,timestep,200,len(f),x,f)
#poincare(0.75*2*np.pi*np.sqrt(l/g))
#poincareInterpolation(0.75*2*np.pi*np.sqrt(l/g))
#poincare(2)
#runningCounter = input('Number:')
lorenz(16,50,4,-13,-13,52)

#poincareInterpolation(0.75*2*np.pi*np.sqrt(l/g))
