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
x = (1, 2, 3)
y = (1, 2, 3)
plt.plot(x,y)
# Use the command below to make plot appear
plt.show()

