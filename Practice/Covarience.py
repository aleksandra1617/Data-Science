# Covariance and Correlation - the measure of joint variability of two random variables. If the greater values of one
# variable mainly correspond with the greater values of the other variable, and the same holds for the lesser values,
# (i.e., the variables tend to show similar behavior), the covariance is positive.
# In the opposite case, when the greater values of one variable mainly correspond to the lesser values of the other,
# (i.e., the variables tend to show opposite behavior), the covariance is negative.
# The sign of the covariance therefore shows the tendency in the linear relationship between the variables.
#
# The magnitude of the covariance is not easy to interpret because it is not normalized
# and hence depends on the magnitudes of the variables. The normalized version of the covariance,
# the correlation coefficient, however, shows by its magnitude the strength of the linear relation.

# STEP 1
# Create a Bivariate Scatter Plot (where 2 things are compared). (X Vs Y)

# STEP 2
# Describe the shape or pattern of the data point distribution. (Random, Linear, Polynomial)

# STEP 3
# Make an assumption on the two variable's relation. (For example, when one rises does the other rise too?)

# Covariance how they change together, how do they behave as a pair.
# A positive value indicates an increasing linear relationship. /
# A negative value indicates a decreasing linear relationship. \
# When the scatter plot looks like a shotgun shot (random) the covariance is near or equal to 0.

# (SAMPLE & POPULATION) FORMULAS:
# SAMPLE:
#   Sample Breakdown: Sum of each data point for x - the x mean, times each data point for y - y mean,
#   and all of that divided by num samples - 1.
#   Pseudo formula: Sum((xi - xmean)*(yi - ymean))/n-1

# PSEUDO CODE
# STEP 1: Get all the data from the 2 columns/variables/attributes and create a scatter plot.
# STEP 2: Calculate the mean for each column/variable/attribute.
# STEP 3: Calculate (xi-xmean) and (yi-ymean)
# STEP 4: Multiply (xi-xmean) and (yi-ymean)
# STEP 5: SUM (xi-xmean)*(yi-ymean)
# STEP 6: Divide SUM (xi-xmean)*(yi-ymean) by n-1

# POPULATION:

# Example
import matplotlib.pyplot as plt
import numpy as np

x = [12, 30, 15, 24, 14, 18, 28, 26, 19, 27]
y = [20, 60, 27, 50, 21, 30, 61, 54, 32, 57]

# STEP 1: VISUALISE THE DATA - Scatter plot shows positive covariance.
plt.scatter(x, y)

# Adding Labels
plt.xlabel("x")
plt.ylabel("y")

# Render buffer
plt.show()


# STEP 2: Calculate the mean for both x and y
x_mean = sum(x)/len(x)
print("X mean: ", sum(x)/len(x))

# Mean calc using numpy
y_mean = np.mean(y)
print("Y mean: ", np.mean(y))

# STEP 3, 4, 5
summed_xy_diff = 0

for count in range(len(x)):
    # STEP 3: Calculate the difference between the current value and the attribute mean
    x_diff = x[count] - x_mean
    y_diff = y[count] - y_mean

    # STEP 4: Multiply both differences
    xy_diff = x_diff * y_diff
    print("Current Difference: ", round(xy_diff, 2))

    # STEP 5: Sum the xy difference for all pairs in the data set
    summed_xy_diff += xy_diff

print("Summed Difference: ", summed_xy_diff)

# STEP 6: Divide summed difference by n-1
print("Covariance: ", round(summed_xy_diff/(len(x)-1), 2))
# RESULT: 106.93 - positive value i.e. positive/increasing linear covariance. 
