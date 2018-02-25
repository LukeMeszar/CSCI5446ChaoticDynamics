import sys
import matplotlib.pyplot as plt
import numpy as np
import random
import math

def read_file():
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

def box_counting(trajectory):
    epsilon = 1000
    for i in range(2000):
        boxes_found = []
        print(epsilon)
        if epsilon > 0:
            for j in range(len(trajectory)):
                current_point = trajectory[j]
                box_in = []
                #print(current_point)
                for k in range(len(current_point)):
                    print(k)
                    if current_point[k] >= 0:
                        box_coordinate = int(current_point[k]/epsilon)*epsilon
                    else:
                        box_coordinate = int(current_point[k]/epsilon-1)*epsilon
                    box_in.append(box_coordinate)
                #print(box_in)
                if box_in not in boxes_found:
                    boxes_found.append(box_in)
            nEpsilon = len(boxes_found)
            print(nEpsilon)
            writetofile(math.log(nEpsilon), math.log(1/epsilon))
            epsilon /= 2
        else:
            break
        #print(boxes_found)

def writetofile(nEpsilon, epsilon):
    outString = str(nEpsilon) + ' ' + str(epsilon) + "\n"
    with open('fractal15000.txt', "a") as f:
        f.write(outString)

box_counting(read_file())
