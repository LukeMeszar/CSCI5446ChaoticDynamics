import math


# t0 - initial time
# delta_t - timestep
# input vec - initial state vector at time = 0
# n_dims - number of dimensions
# system_deriv - ???
#
# rkn does single step, multiple steps handled by iterator()

def rkn(t0, delta_t, input_vec, n_dims, function_array):
    k1 = []
    k2 = []
    k3 = []
    k4 = []
    helper = []

    for i in range(n_dims):
        k1.append(function_array[i](input_vec)*delta_t)
    for i in range(n_dims):
        helper.append(input_vec[i] + k1[i]*0.5)
    for i in range(n_dims):
        k2.append(function_array[i](helper)*delta_t)
    for i in range(n_dims):
        helper[i] = input_vec[i] + k2[i]*0.5
    for i in range(n_dims):
        k3.append(function_array[i](helper)*delta_t)
    for i in range(n_dims):
        helper[i] = input_vec[i] + k3[i]
    for i in range(n_dims):
        k4.append(function_array[i](helper)*delta_t)
    for i in range(n_dims):
        helper[i] = (input_vec[i] + (k1[i] + 2*(k2[i] + k3[i]) + k4[i])/6)

    return helper



def iterator(initial_t, timestep, num_iterations, input_state_vec, output_file_name, n_dims, function_array):

    input_vec = input_state_vec[0]
    delta_vec = input_state_vec[1]

    func_array = function_array[0]
    h = function_array[1]

    cur_time = initial_t
    remaining_iterations = num_iterations
    output_vec = []

    while (remaining_iterations > 0):

        output_vec = rkn(cur_time, timestep, input_vec, n_dims, func_array)

        delta_vec_temp = h(output_vec, delta_vec)

        delta_vec = delta_vec_temp
        input_vec = output_vec
        cur_time += timestep
        remaining_iterations -= 1


        print("Iteration: ", 100-remaining_iterations)
 #       print(delta_vec[0])
 #       print(delta_vec[1])
 #       print(delta_vec[2])
        print(" ")



    #with open("problem_3c.txt", "a") as f:
    #    f.write(str(delta_vec[0]))
    #    f.write(str(delta_vec[1]))
    #    f.write(str(delta_vec[2]))

#    print(delta_vec[0])
#    print(delta_vec[1])
#    print(delta_vec[2])

    return


#  USER-EDITED AREA
#####################
#
# Put functions here

def fx(x):
    a = 16
    return a*(x[1]-x[0])

def fy(x):
    r = 45
    return ((r*x[0])-x[1]-(x[0]*x[2]))

def fz(x):
    b = 4
    return ((x[0]*x[1])-(b*x[2]))

def h(x,delta):
    delta_prime = [[0,0,0],[0,0,0],[0,0,0]]

    print(delta[0])
    print(delta[1])
    print(delta[2])

    a = 16
    r = 45 
    b = 4
    # positions:
    #
    #   1   2   3
    #   4   5   6
    #   7   8   9
    #
    pos1 = delta[0][0]
    pos2 = delta[0][1]
    pos3 = delta[0][2]
    pos4 = delta[1][0]
    pos5 = delta[1][1]
    pos6 = delta[1][2]
    pos7 = delta[2][0]
    pos8 = delta[2][1]
    pos9 = delta[2][2]

    delta_prime[0][0] = ((-a*pos1)+(a*pos4))
    delta_prime[0][1] = ((-a*pos2)+(a*pos5))
    delta_prime[0][2] = ((-a*pos3)+(a*pos6))
    delta_prime[1][0] = ((r-x[2])*pos1)-pos4-(x[0]*pos7)
    delta_prime[1][1] = ((r-x[2])*pos2)-pos5-(x[0]*pos8)
    delta_prime[1][2] = ((r-x[2])*pos3)-pos6-(x[0]*pos9)
    delta_prime[2][0] = (x[1]*pos1)+(x[0]*pos4)-(b*pos7)
    delta_prime[2][1] = (x[1]*pos2)+(x[0]*pos5)-(b*pos8)
    delta_prime[2][2] = (x[1]*pos3)+(x[0]*pos6)-(b*pos9)

    print(delta_prime[0])
    print(delta_prime[1])
    print(delta_prime[2])

    return delta_prime


# Put arrays here
# 
# Function array
func_array = [[fx, fy, fz], h]
# Intiial conditions array
# Theta, omega

identity_matrix = [[1,0,0],[0,1,0],[0,0,1]]
x0 = [0,-1,2]

x0_array = [x0, identity_matrix]
# Timestep
timestep = .001
# Initial time
t0 = 0
# Number of iterations
num_iterations = 100
# Filename
fn = "problem_3_a.csv"
#
#####################


num_dims = 3

counter = 0

iterator(t0, timestep, num_iterations, x0_array, fn, num_dims, func_array)
