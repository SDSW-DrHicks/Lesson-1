# To perform certain functions and make plots, you must install the "matplotlib" package
# To do this, first:
# 1. Go to the "Python Packages" tab on the bottom of the window
# 2. Go to the search par and search for "matplotlib," make sure you select the most recent update, 3.6.2
# 3. Click the "install package."
# 4. After a moment, the package should be installed. To verify, select the "python packages" tab again
# and confirm that "matplotlib" is now on the list.

# Once matplotlib is installed, you must still import it into your operating file.
import matplotlib.pyplot as plt

# Here is an example plot.
x1 = [1, 2, 3]
y1 = [1, 2, 3]
plt.plot(x1,y1)
# Use the command below to make plot appear
plt.show()

# numpy is useful for manipulating arrays and functions
import numpy as np
# linspace is used to generate an values from (lefthand side, righthand side, number of
# Evenly distributed values within the left- and righthand bounds).

# Make a set of values for input, x
x = np.linspace(-np.pi, np.pi, 201)
# Use plt.plot to plot the input againt the output of a function, sine.
plt.plot(x, np.sin(x))
# Format plots with axis titles.
plt.xlabel('Angle [rad]')
plt.ylabel('sin(x)')
plt.axis('tight')
plt.show()
# special format options in matplotlib
plt.plot(x1,y1, 'bo') # this allows for making discrete point with blue "b" color and "o" cicular shape.
plt.show()
plt.plot(x1,y1,"r+") # plot with red, "r" plus signs "+."
plt.grid(True) # adds a grid to the plot
plt.show()