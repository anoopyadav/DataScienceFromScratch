from collections import Counter
from random import randint
from matplotlib import pyplot as plt
from LinearAlgebra.vectors import sum_of_squares, dot
from math import sqrt

num_friends = [randint(1, 101) for x in range(200)]
friend_counts = Counter(num_friends)

""" Plot the friend-count vs number of people
"""
x_axis = range(101)
y_axis = [friend_counts[x] for x in x_axis]

plt.bar(x_axis, y_axis)
plt.axis([0, 101, 0, 25])
plt.title("Histogram of friend counts")
plt.xlabel('Number of friends')
plt.ylabel('Number of people')
plt.show()

""" Get some statistics going
"""
num_points = len(num_friends)
largest_value = max(num_friends)
smallest_value = min(num_friends)

""" Basic statistics methods
"""


def mean(x):
    return sum(x) / len(x)


def median(v):
    length = len(v)
    sorted_v = sorted(v)
    midpoint = length // 2

    if length % 2 is not 0:
        return sorted_v[midpoint]
    else:
        low = midpoint - 1
        high = midpoint
        return (sorted_v[low] + sorted_v[high]) / 2


def quantile(x, p):
    index = int(p * len(x))
    return sorted(x)[index]


def mode(x):
    """ Returns a list of most common values """
    counts = Counter(x)
    max_count = max(counts.values())

    return [x for x, count in counts.items()
            if count == max_count]


print("Mean: " + str(mean(num_friends)))
print("Median: " + str(median(num_friends)))
print("Mode: " + str(mode(num_friends)))

""" The following methods calculate the Variance and the Standard Deviation for a set of values"""


def de_mean(x):
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]


def variance(x):
    n = len(x)
    deviations = de_mean(x)

    return sum_of_squares(deviations) / (n - 1)


def standard_deviation(x):
    return sqrt(variance(x))


print("Standard Deviation: " + str(standard_deviation(num_friends)))


def interquantile_range(x):
    """ Return the difference between the 75th persentile and 25th percentile of a dataset """
    return quantile(x, 0.75) - quantile(x, 0.25)


print("Interquantile range: " + str(interquantile_range(num_friends)))


""" Methods to determine correlation
"""


def covariance(x, y):
    """ +ve value : X is large when Y is large
        -ve value: X is small when Y is small
        Hard to interpret units since they're the product of the two datasets
    """
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1)


def correlation(x, y):
    """ Correlation is unitless, so more meaningful"""
    stddev_x = standard_deviation(x)
    stddev_y = standard_deviation(y)

    if stddev_x > 0 and stddev_y > 0:
        return covariance(x, y) / stddev_x / stddev_y
    else:
        return 0


daily_minutes = [randint(1, 30) for x in range(len(num_friends))]
print("Correlation: " + str(correlation(num_friends, daily_minutes)))
