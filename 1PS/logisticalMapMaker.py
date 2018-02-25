# CSCI 4446 - Assignment 1
# Name: Derek Gorthy
# Date: 1/17/2017

import matplotlib.pyplot as plt

# User-modified variables
R = 2.5
m = 100
x_not = .2
###


def make_plot(x_label, y_label, my_x, my_y, axes):
	plt.xlabel(x_label)
	plt.ylabel(y_label)
	plt.scatter(my_x, my_y)
	plt.savefig(axes + '-' + str(R) + '-' + str(x_not) + '.png')
	plt.clf()

# X (n+1) = R * xn * (1-xn)


x_values = [] # "y"
n_values = [] # "x"

x_values.append(x_not)
n_values.append(0)

for value in range(1, m+2):
	n_values.append(value)
	prev_value = x_values[value-1]
	x_values.append(R * prev_value * (1-prev_value))

# Plot A
make_plot('n', 'x_n', n_values[0:m], x_values[0:m], 'x_n-vs-n')
make_plot('x_n', 'x_(n+1)', x_values[0:m], x_values[1:m+1], 'x_(n+1)-vs-x_n')
make_plot('x_n', 'x_(n+2)', x_values[0:m], x_values[2:m+2], 'x_(n+2)-vs-x_n')
