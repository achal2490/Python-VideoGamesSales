import numpy as np


from scipy import linalg, stats, constants
import matplotlib as mp

#define a 2-D array
mat = np.array([[10, 6], [2, 7]])
#print the array
print(mat)
#find the inverse of the array using inv function
mat_inv = linalg.inv(mat)
#print inverse of the array
print(mat_inv)

#Solving a system of linear equation
#define a 2-D array with values of x,y,z in three equations
numArr = np.array([[2,3,1],[-1,5,4],[3,2,9]])
#define another array with values on right of equal sign
numArrValue = np.array([21,9,6])
#use solve function to solve the linear equation
ans = linalg.solve(numArr,numArrValue)
#display the values of x,y,z
print(ans)

#generate an array of normally distributed random variates with meano f 0 and standard deviation of 1
normArr = stats.norm.rvs(loc=0, scale=1, size=10)
print(normArr)

#generates an array of normally distributed values and calculates the cumulative density
normCDF = stats.norm.cdf(5,loc=1,scale=2)
print(normCDF)

#generates an array of normally distributed values and calculates the probability density
normPDF = stats.norm.pdf(9,loc=0,scale=1)
print(normPDF)

# retreive values of various constants like speed of light etc. stored in scipy package.
arrConst = np.array([['pi', 'speed of light', 'Planck\'s constant' ],[constants.pi,constants.speed_of_light,constants.h]])
print(arrConst)

