### YOUR CODE HERE - Write method that returns Euclidean distance between two points, last element in point array is class 
from array import array
from dis import dis
from scipy.spatial import distance
import numpy as np
def getDistance(p1, p2):
    """ 
    p1:  a numpy array, last element of the array is the class of the point
    p2:  a numpy array, last element of the array is the class of the point
    Calculates the Euclidean distance between two points. Returns dist float
    """
    return distance.euclidean(p1[:-1],p2[:-1])#using the scipy libruary to get fast.

data1 = np.array([2, 2, 2, 'a'])
data2 = np.array([4, 4, 4, 'b'])
# distance = getDistance(data1, data2)
# print(type(distance))
# print(distance)
distance.euclidean(data1[:-1],data2[:-1])