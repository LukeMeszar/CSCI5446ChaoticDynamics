# CSCI 5446 - Assignment 2
# Name: Luke Meszar
# Date: 1/17/2017
import sys
import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt

# User-modified variables
#R = 2.5
#m = 50
#x_not = 1.1
###


def make_plot(x_label, y_label, my_x, my_y, axes):
	plt.xlabel(x_label)
	plt.ylabel(y_label)
	plt.scatter(my_x, my_y)
	plt.savefig(axes + '-' + str(R) + '-' + str(x_not) + '.png')
	plt.clf()

# X_(n+1) = R * x_n * (1-x_n)
def get_vals(m, initial_point, r, throw_away=0):
	vals = np.zeros(m)
	vals[0] = initial_point
	for i in range(1, m):
		vals[i] = r * vals[i - 1] * (1 - vals[i - 1])
	return vals[throw_away:] # default return entire array

# X_(k+1) = y_k + 1 + ax_k^2
# Y_(k+1) = bx_k
def get_vals_henon(a, b, x0, y0, steps, throw_away=0):
    xvals = np.zeros(steps)
    yvals = np.zeros(steps)
    xvals[0] = x0
    yvals[0] = y0
    for i in range(1, steps):
		yvals[i] = b * xvals[i - 1]
		xvals[i] = yvals[i - 1] + 1 - (a * xvals[i - 1]**2)
    return (xvals[throw_away:], yvals[throw_away:])


######### User Edited Variables
l = 30000
height = 10000
precision = 1800.0
###############################


def question_one():
	precision_div = 1 / precision
	r_vals = np.arange(2.8, 4, precision_div)

	data = np.zeros((len(r_vals), l))
	counter = 0


	# Loop through all R values
	for r in r_vals:
		data[counter] = get_vals(60000, 0.2, r, l)
		counter += 1


	fig = plt.figure(figsize=(16,8))
	ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
	for i in range(len(r_vals)):
		ax.scatter(np.zeros(l) + r_vals[i], data[i], s=0.1, alpha=0.2)
	plt.title('Bifurcation Plot')
	plt.xlabel(r'$R$ Value')
	plt.ylabel(r'$x_n$ Value')
	plt.xlim(2.7, 4.1)
	#plt.show()
	plt.savefig('bifurcation.png')

def question_two():

	# First bifurcation:	2.99561
	# Second bifurcation:	3.44887
	# Third bifurcation:	3.54413
	# Fourth bifurcation:	3.56453


	precision = .00006

	bifur_points = [np.arange(2.98, 3.01, precision),
	                np.arange(3.447, 3.45, precision),
	                np.arange(3.542, 3.546, precision),
	                np.arange(3.5623, 3.5665, precision),
					np.arange(3.5671, 3.5689, precision)]

	data = [np.zeros((bifur_points[0].shape[0], height)),
	        np.zeros((bifur_points[1].shape[0], height)),
	        np.zeros((bifur_points[2].shape[0], height)),
	        np.zeros((bifur_points[3].shape[0], height)),
			np.zeros((bifur_points[4].shape[0], height))]

	for i in range(5):
		for j in range(len(bifur_points[i])):
			vals = get_vals(1000, 0.2, bifur_points[i][j], height)
			data[i][j] = vals


	fig, axarr = plt.subplots(1, 5, figsize=(18,8))
	for i in range(5):
		for j in range(bifur_points[i].shape[0]):
			axarr[i].scatter(np.zeros(height) + bifur_points[i][j], data[i][j], s=0.1, alpha=0.2)
	#plt.show()
	plt.savefig("zoom1.png")


def question_twoa():
	#precision_div = 1 / precision
	r_vals = np.arange(3.44, 3.57, 0.0001)

	data = np.zeros((len(r_vals), l))
	counter = 0


	# Loop through all R values
	for r in r_vals:
		data[counter] = get_vals(1200, 0.2, r, l)
		counter += 1


	fig = plt.figure(figsize=(16,8))
	ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
	for i in range(len(r_vals)):
		ax.scatter(np.zeros(l) + r_vals[i], data[i], s=0.1, alpha=0.2)
	plt.title('Expanded Period Doubling Cascade')
	plt.xlabel(r'$R$ Value')
	plt.ylabel(r'$x_n$ Value')
	plt.xlim(3.44, 3.57)
	#plt.show()
	plt.savefig('two.png')


def question_twob():
	#precision_div = 1 / precision
	r_vals = np.arange(3.0, 3.6, 0.0001)

	data = np.zeros((len(r_vals), l))
	counter = 0


	# Loop through all R values
	for r in r_vals:
		data[counter] = get_vals(1200, 0.2, r, l)
		counter += 1

	bifurcation_vals = []
	cycle_counter = 2
	for i in range(0, len(r_vals)):
		new_data = data[i][0:cycle_counter]
		for p in range(0, len(new_data)):
			rounded_val = "%.3f" % new_data[p]
			new_data[p] = rounded_val
		set_data = set(new_data)
		#print(new_data)
		#print("length of set: {}, cycle_counter: {}".format(len(set_data), cycle_counter))
		if len(set_data) == cycle_counter:
			bifurcation_vals.append(r_vals[i])
			cycle_counter = cycle_counter*2

	for k in range(0, len(bifurcation_vals)):
		print(bifurcation_vals[k])

	#for i in range(0,len(r_vals)):
	#	print("R value: {}".format(r_vals[i]))
	#	for j in range(0,len(data[i])):
	#		print(data[i][j])

def question_three_one():
	a  = np.arange(0, 1.4, 1e-3)
	b  = 0.3
	x0 = 0.2
	y0 = 0.2

	data = np.zeros((1.4 * 1e3 + 1, 500))

	for i in range(a.shape[0]):
		data[i] = get_vals_henon(a[i], b, x0, y0, 1000, 500)[0]

	fig = plt.figure(figsize=(16,8))
	ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
	for i in range(int(1.4 * 1e3)):
		ax.scatter(np.ones(500) * a[i], data[i], s=0.1, alpha=0.2)
	plt.title('Bifurcation Plot')
	plt.xlabel(r'$a$ Values')
	plt.ylabel(r'$x_n$ Value')
	#plt.show()
	plt.savefig("henon.png")

def question_three_two():

	# First bifurcation:	2.99561
	# Second bifurcation:	3.44887
	# Third bifurcation:	3.54413
	# Fourth bifurcation:	3.56453

	a  = np.arange(0, 1.4, 1e-3)
	b  = 0.3
	x0 = 0.2
	y0 = 0.2

	bifur_points = [np.arange(0.35, 0.4, 1e-4),
	                np.arange(0.9, 0.95, 1e-4),
	                np.arange(1.0, 1.05, 1e-4),
	                np.arange(1.05, 1.054, 1e-5)]

	data = [np.zeros((bifur_points[0].shape[0], 500)),
	        np.zeros((bifur_points[1].shape[0], 500)),
	        np.zeros((bifur_points[2].shape[0], 500)),
	        np.zeros((bifur_points[3].shape[0], 500))]

	for i in range(4):
		for j in range(len(bifur_points[i])):
			vals = get_vals_henon(bifur_points[i][j], b, x0, y0, 1000, 500)[0]
			data[i][j] = vals

	fig, axarr = plt.subplots(1, 4, figsize=(18,8))
	for i in range(4):
		for j in range(bifur_points[i].shape[0]):
			axarr[i].scatter(np.ones(500) * bifur_points[i][j], data[i][j], s=0.1, alpha=0.2)
	plt.show()
	plt.savefig("zoom2.png")


def question_threea():
	a  = np.arange(0.3, 1.06, 1e-3)
	b  = 0.3
	x0 = 0.2
	y0 = 0.2

	data = np.zeros((1.4 * 1e3 + 1, 500))

	for i in range(a.shape[0]):
		data[i] = get_vals_henon(a[i], b, x0, y0, 1000, 500)[0]

	fig = plt.figure(figsize=(16,8))
	ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
	for i in range(int(1.4 * 1e3)):
		ax.scatter(np.ones(500) * a[i], data[i], s=0.1, alpha=0.2)
	plt.title('Bifurcation Plot')
	plt.xlabel(r'$a$ Values')
	plt.ylabel(r'$x_n$ Value')
	plt.savefig('three.png')


question_one()
#question_two()
#question_twoa()
#question_twob()
#question_three_one()
#question_three_two()
#question_threea()

print("logistic map")

#bifurcation points for logistic map
lb1 = 3
lb2 = 3.449
lb3 = 3.5441
lb4 = 3.5645
lb5 = 3.56887
lb6 = 3.56982

print((lb2-lb1)/(lb3-lb2)) #n=2
print((lb3-lb2)/(lb4-lb3)) #n=3
print((lb4-lb3)/(lb5-lb4)) #n=4
print((lb5-lb4)/(lb6-lb5)) #n=5


print("Henon Map")
#bifurcation points for henon map
hb1 = 0.364
hb2 = 0.9122
hb3 = 1.0266
hb4 = 1.0513
hb5 = 1.0566
hb6 = 1.0577351

print((hb2-hb1)/(hb3-hb2)) #n=2
print((hb3-hb2)/(hb4-hb3)) #n=3
print((hb4-hb3)/(hb5-hb4)) #n=4
print((hb5-hb4)/(hb6-hb5)) #n=4
