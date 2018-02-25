import numpy as np
import matplotlib.pyplot as plt
import sympy as sy


def trajectories(x, h, n, f, t):
    k1 = []
    k2 = []
    k3 = []
    k4 = []
    xi1 = []
    for i in range(n):
        k1.append(h*f[i](x, t))
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
        k4.append(f[i](xi1, t + h)*h)
    for i in range(n):
        xi1[i] = x[i] + (k1[i] + 2*(k2[i] + k3[i]) + k4[i])/6
    return xi1


def rk4(t0, h, n, n_dims, xt0, f):
    x = xt0
    trajectory = []
    t = t0
    for i in range(n):
        x_new = trajectories(x, h, n_dims, f, t)
        x = x_new
        trajectory.append(x)
        t += h
    return trajectory


def variation(a, r, b, x0, y0, z0):
    def fx(x, t):
        return a*(x[1]-x[0])

    def fy(x, t):
        return r*x[0]-x[1]-x[0]*x[2]

    def fz(x, t):
        return x[0]*x[1]-b*x[2]

    def xx(x, t):
        return -a*x[3]+a*x[6]

    def yx(x, t):
        return -a*x[4]+a*x[7]

    def zx(x, t):
        return -a*x[5]+a*x[8]

    def xy(x, t):
        return (r-x[2])*x[3]-x[6]-x[0]*x[9]

    def yy(x, t):
        return (r-x[2])*x[4]-x[7] - x[0]*x[10]

    def zy(x, t):
        return (r-x[2])*x[5]-x[8]-x[0]*x[11]

    def xz(x, t):
        return x[1]*x[3]+x[0]*x[6]-b*x[9]

    def yz(x, t):
        return x[1]*x[4]+x[0]*x[7]-b*x[10]

    def zz(x, t):
        return x[1]*x[5]+x[0]*x[8]-b*x[11]

    f = [fx, fy, fz, xx, yx, zx, xy, yy, zy, xz, yz, zz]
    x = [x0, y0, z0, 1, 0, 0, 0, 1, 0, 0, 0, 1]
    timestep = 0.001
    #rk4(t0, h, n, n_dims, xt0, f):
    output = rk4(0, timestep, 2000, len(f), x, f)
    evolvedState = output[-1]
    variationMatrix = evolvedState[3:len(evolvedState)]
    index = 0
    print(evolvedState[0:3])
    outputText = "{"
    for i in range(3):
        outputText += "{" + str(variationMatrix[index]) + "," + str(variationMatrix[index+1]) + "," + str(variationMatrix[index+2]) + "},"
        index += 3
    outputText += "\b}"
    print(outputText)

print("problem a")
variation(16, 45, 4, 10, 5, -2)
#print("problem b")
#variation(16, 45, 4, 10, -5, 2)
#print("problem c")
#variation(16, 45, 4, 0, -1, 2)
