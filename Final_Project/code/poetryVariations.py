import sys
import matplotlib.pyplot as plt
import numpy as np
import random
import math
import re
from collections import namedtuple
from operator import itemgetter
from pprint import pformat
import scipy.spatial as spatial

def readFileLine():
    with open(sys.argv[1]) as f:
        content = f.readlines()
    return content

def readFilePeriod():
    text = ''.join(open(sys.argv[1]).readlines())
    sentences = re.split(r' *[\.\?!][\'"\)\]]* *', text)
    return sentences

def readFileComma():
    text = ''.join(open(sys.argv[1]).readlines())
    commas = re.split(r' *[\,\?!][\'"\)\]]* *', text)
    return commas

def readFileStanza():
    text = ''.join(open(sys.argv[1]).readlines())
    stanzas = re.split('\n\s*\n', text)
    return stanzas


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
        trajectory.append(tuple(x))
        t += h
    return trajectory

def writetofile(data):
    timestep = 0
    for i in range(len(data)):
        timestep = timestep + 0.001
        outString = str(data[i][0]) +' ' + str(data[i][1]) + ' ' + str(data[i][2])  + "\n"
        with open('output', "a") as f:
            f.write(outString)

def lorenz(a, r, b, x0, y0, z0, chunks):
    def fx(x, t):
        return a*(x[1]-x[0])

    def fy(x, t):
        return r*x[0]-x[1]-x[0]*x[2]

    def fz(x, t):
        return x[0]*x[1]-b*x[2]

    f = [fx, fy, fz]
    x = [x0, y0, z0]
    timestep = 0.05
    output = rk4(0, timestep, 30000 + len(chunks), len(f), x, f)
    modifiedOutput = output[30000:len(output)]
    return modifiedOutput[0::1]
    #writetofile(output)
def computeNearestNeighbor(currentPoint, trajectory):
    smallestDistance = math.inf
    smallestDistanceIndex = -1
    for i in range(len(trajectory)):
        #distance = math.sqrt((currentPoint[0]-trajectory[i][0])**2 +(currentPoint[1]-trajectory[i][1])**2)+(currentPoint[2]-trajectory[i][2])**2))
        distance = math.sqrt((currentPoint[0]-trajectory[i][0])**2+(currentPoint[1]-trajectory[i][1])**2+(currentPoint[2]-trajectory[i][2])**2)
        if distance < smallestDistance:
            smallestDistance = distance
            smallestDistanceIndex = i
    return smallestDistanceIndex

def plot(xValues1, yValues1, xValues2, yValues2, xlab, ylab):
    plt.plot(xValues1, yValues1, "o", label='Initial Trajectory')
    plt.plot(xValues2, yValues2, "o", label='New Trajectory')
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.legend()
    plt.savefig('output.png')
    plt.clf()

def poetryVariations(chunkMethod):
    if chunkMethod == "commas":
        chunks = readFileComma()
    elif chunkMethod == "periods":
        chunks = readFilePeriod()
    elif chunkMethod == "stanzas":
        chunks = readFileStanza()
    elif chunkMethod == "lines":
        chunks = readFileLine()
    usedChunks = [0 for x in range(len(chunks))]
    initialTrajectory = lorenz(16,45,4,10,-5,2, chunks)
    xValues1 = [x[0] for x in initialTrajectory]
    yValues1 = [x[1] for x in initialTrajectory]
    #kdTree = spatial.KDTree(initialTrajectory)
    #newTrajectrory = lorenz(16,45,4,random.uniform(-20,20),random.uniform(-20,20),random.uniform(-20,20), chunks)
    newTrajectrory = lorenz(16,45,4,10.5,-4.5,2.2, chunks)
    xValues2 = [x[0] for x in newTrajectrory]
    yValues2 = [x[1] for x in newTrajectrory]
    newPoem = []
    print(len(chunks))
    plot(xValues1, yValues1, xValues2, yValues2, r'$x$', r'$y$')
    for i in range(len(newTrajectrory)):
        nearestNeighborIndex = computeNearestNeighbor(newTrajectrory[i], initialTrajectory)
        #print(nearestNeighborIndex)
        newPoem.append(chunks[nearestNeighborIndex])
        del(initialTrajectory[nearestNeighborIndex])
        del(chunks[nearestNeighborIndex])



    # for i in range(len(newTrajectrory)):
    #     possiblePoints = kdTree.query_ball_point(newTrajectrory[i], 20)
    #     if len(possiblePoints) == 0:
    #         sys.exit("no nearest neighbor")
    #     for i in range(len(possiblePoints)):
    #         if usedChunks[possiblePoints[i]] == 0:
    #             newPoem.append(chunks[possiblePoints[i]])
    #             usedChunks[possiblePoints[i]] = 1
    #     #newPoem.append(chunks[kdTree.query(newTrajectrory[i])[1]])
    for i in range(len(newPoem)):
         print("{}".format(newPoem[i]))

poetryVariations("periods")
