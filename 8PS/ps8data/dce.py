import sys
import matplotlib.pyplot as plt
import numpy as np

def dividedDifferences(theta_data, time_data):
    omegas = []
    for i in range(1,len(theta_data)-1):
        fp = (float(theta_data[i+1])-float(theta_data[i-1]))/(2*(float(time_data[i+1])-float(time_data[i])))
        omegas.append(fp)
    plot(theta_data[0:len(theta_data)-2], omegas)

def embed(theta_data, time_data, tau, m, j, k):
    embedded_data = []
    delta_t = float(time_data[1])-float(time_data[0])
    array_step_size = int(tau/delta_t)
    for h in range(len(theta_data)-(m-1)*array_step_size):
        m_vec = []
        for i in range(m):
            #print("h: {}, i: {}, array_step_size: {}, h+i*array_step_size: {}".format(h,i,array_step_size,h+i*array_step_size))
            m_vec.append(theta_data[h+i*array_step_size])
        embedded_data.append(m_vec)
    x_vals = []
    y_vals = []
    for i in range(len(embedded_data)):
        x_vals.append(embedded_data[i][k])
        y_vals.append(embedded_data[i][j])
    plot(x_vals, y_vals)



def readFile():
    with open(sys.argv[1]) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    theta_data = []
    time_data = []
    for i in range(len(content)):
        split_line = content[i].split()
        theta_data.append(split_line[0])
        time_data.append(split_line[1])
    return [theta_data, time_data]

def plot(x_values, y_values):
    print("here")
    plt.plot(x_values,y_values, '-b', markersize = 1)
    plt.xlabel(r'$\tau$')
    #plt.ylabel(r'$\omega$')
    plt.ylabel('Average Mutual Information')
    #plt.ylabel('Average Mutual Information')
    plt.savefig('problem3amutual.png')
    plt.clf()

def mutual(data):
    plot("here")
    plot(data[0], data[1])

data = readFile()

#dividedDifferences(data[0][0::10], data[1][0::10])
#problem2a
#embed(data[0][0::1],data[1][0::1], 0.15, 3, 0, 2)
tau = 0.5
#problem2b
#embed(data[0][0::1],data[1][0::1], tau, 25, 0, 1)
#problem4a
print("here")
mutual(data)
