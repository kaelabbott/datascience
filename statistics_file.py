from __future__ import division
from collections import Counter
import math

# from matplotlib import pyplot as plt 

# Statistics

#s um between list
def dot(v, w):
    """v_1 * w_1 + ... + v_n * w_n"""
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

def sum_of_squares(v):
    return dot(v,v)


def range_func(x):
    return max(x) - min(x)

def mean(x):
    return sum(x) / len(x)

#print('range: %s' % range_func(num_of_grades))
#print('Mean: %s' % mean(num_of_grades) )

def median(v):

    n = len(v)
    sorted_v = sorted(v)
    midpoint = n // 2
    if n % 2 == 1:
        # if odd, return the middle value
        return sorted_v[midpoint]
    else:
    # if even, return the average of the middle values
        lo = midpoint - 1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi]) / 2

# P = percent
def quantile(x, p):
    p = p/100
    p_index = int(p * len(x))
    return sorted(x)[p_index]
# Max count
def mode(x):
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items()
    if count == max_count]
# x-x'
def de_mean(x):
    x_mean = mean(x)
    return [x_i - x_mean for x_i in x ]
# variance = (x-x_mean))**2
def variance(x):
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n-1)
    
def standard_deviation(x):
    return math.sqrt(variance(x))
# Example of list ------------------------------------------------------------
list_1do = [1.25,1.28,1.27,1.21,1.22,1.29,1.30,1.24,1.27,1.29,1.23,1.26,
            1.30,1.21,1.28,1.30,1.22,1.25,1.20,1.28,1.21,1.29,1.26,1.22,1.28,
            1.27,1.26,1.23,1.22,1.21]
list_2do = [2,4,2,3,1,2,4,2,3,0,2,2,2,3,2,6,2,3,2,2,3,2,3,3,4,
            3,3,4,5,2,0,3,2,1,2,3,2,2,3,1,4,2,3,2,4,3,3,2,2,1]
counts = Counter(list_1do)
frecuency_2 = [2,4,21,15,6,1,1]
new_list = [x/50 for x in frecuency_2]
print(new_list)
print(median(list_1do))
print(mean(list_1do))
print(mode(list_1do))
# -------------------------------------------------------------------------------

#print("QUANTILE_4: %s" % quantile_4)
#print("Max Count: %s" % mode(num_of_grades))

#print("Desviation Mean: %s" % de_mean(num_of_grades))
#print("Variance: %s" % variance(num_of_grades))
#print("Standard deviation: %s" %standard_deviation(num_of_grades))


# covariance measures how two variables vary in tandem from their means:

def covariance(x,y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1)


def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0 # if no variation, correlation is zero
# 0.25

#print("Covariance: %s" % covariance(num_of_grades,time_studying))
#print("Correlation: %s " % correlation(num_of_grades,time_studying) )