import sys
import matplotlib.pyplot as plt
import numpy as np
import random
import math

def readFile():
    with open(sys.argv[1]) as f:
        content = f.readlines()
    #content = [x.strip() for x in content]
    data = []
    for i in range(len(content)):
        split_line = content[i].split()
        point = []
        point = [float(split_line[0]), float(split_line[1]), float(split_line[2])]
        data.append(point)
    return data

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


def Wolf(state_space, epsilon, theiler_window, M):
    n = len(state_space)
    x_index = random.randint(int(n/20),int(n/10))
    original_x_index = x_index
    x = state_space[x_index]
    Li_array = []
    Lip_array = []
    total_counter = 0
    for i in range(M):
        val = compute_nearest_neighbor(state_space, x, x_index, theiler_window)
        #print(val)
        z_index = val[0]
        Li = val[1]
        Li_array.append(Li)#initial Li
        counter = 0
        while Li <= epsilon and x_index + counter < len(state_space) and z_index + counter < len(state_space): #loop until distance > epsilon
            Li = np.sqrt((state_space[x_index + counter][0]-state_space[z_index+counter][0])**2 + (state_space[x_index + counter][1]-state_space[z_index+counter][1])**2 + (state_space[x_index + counter][2]-state_space[z_index+counter][2])**2)
            #print(Li)
            counter += 1
            total_counter += 1
        Lip = Li
        print(Lip)
        Lip_array.append(Lip)
        if x_index + counter < len(state_space): #make sure we don't go past end of array
            x_index = x_index + counter
            x = state_space[x_index]
        else:
            break
    sum_value = 0
    #print(Lip_array)
    #print("\n\n\n\n")
    #print(Li_array)
    for i in range(len(Li_array)): #compute  lyapunov exponent
        sum_value += math.log2(Lip_array[i]/Li_array[i])
        #print(sum_value)
    print(total_counter)
    lyapunov_exponent = sum_value/(total_counter)
    print(lyapunov_exponent)




def compute_nearest_neighbor(state_space, x, index, theiler_window):
    #separate the arrays so we aren't looking at points right next to current one
    before_array = state_space[0:index - theiler_window]
    after_array = state_space[index + theiler_window + 1:len(state_space)]
    smallest_distance = math.inf
    nearest_neighbor_index = 0
    for i in range(len(before_array)): #find smallest distance in before_array using L_2 norm
        current_distance = np.sqrt((x[0]-before_array[i][0])**2 + (x[1]-before_array[i][1])**2 + (x[2]-before_array[i][2])**2)
        if current_distance < smallest_distance:
            smallest_distance = current_distance
            nearest_neighbor_index = i
    for i in range(len(after_array)): #find smallest distance in after_array using L_2 norm
        current_distance = np.sqrt((x[0]-after_array[i][0])**2 + (x[1]-after_array[i][1])**2 + (x[2]-after_array[i][2])**2)
        if current_distance < smallest_distance:
            smallest_distance = current_distance
            nearest_neighbor_index = index + theiler_window + 1 + i
    return [nearest_neighbor_index, smallest_distance]


def writetofile(data):
    timestep = 0
    for i in range(len(data)):
        timestep = timestep + 0.001
        outString = str(data[i][0]) +' ' + str(data[i][1]) + ' ' + str(data[i][2])  + "\n"
        with open('lorenz_data200000again', "a") as f:
            f.write(outString)

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


def lorenz(a, r, b, x0, y0, z0):
    def fx(x, t):
        return a*(x[1]-x[0])

    def fy(x, t):
        return r*x[0]-x[1]-x[0]*x[2]

    def fz(x, t):
        return x[0]*x[1]-b*x[2]

    f = [fx, fy, fz]
    x = [x0, y0, z0]
    timestep = 0.001
    output = rk4(0, timestep, 200000, len(f), x, f)
    writetofile(output)

lorenz(16,45,4,10, -5, 2)
#state_space = readFile()
#Wolf(state_space, 5, 50, 50)
