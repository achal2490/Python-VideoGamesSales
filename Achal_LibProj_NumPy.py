import numpy as np

#define a 1-D array
firstArr = np.array([10,20,30,40,50])
print(firstArr)

#define arrays with all zeros
zeroArr = np.zeros((3,3))
print(zeroArr)

#define array with all ones
oneArr = np.ones((4,4))
print(oneArr)

#define a 1-D array
oneDArr = np.arange(20)
print(oneDArr)

#define a 2-D array
twoDArr = np.arange(15).reshape(3,5)
print(twoDArr)

#define a 3-D array
threeDArr = np.linspace(1,100,27).reshape(3,3,3)
print(threeDArr)

# Identify dimensions of various arrays and create a new array using those.
dimArr = np.array([np.ndim(oneDArr), np.ndim(twoDArr), np.ndim(threeDArr)])
print(dimArr)

# Identify shape of various arrays and create a new array using those.
shapeArr = np.array([np.shape(oneDArr), np.shape(twoDArr), np.shape(threeDArr)])
print(shapeArr)

# Identify size of various arrays and create a new array using those.
sizeArr = np.array([np.size(oneDArr), np.size(twoDArr), np.size(threeDArr)])
print(sizeArr)

# Perform mathematical multiplication on two arrays
hrsWorked = np.array([7,8,5,6,10,4,0])
rate = np.array([10,10,10,10,10,12,12])
earnings = hrsWorked * rate
print(earnings) #daily earning
print(sum(earnings)) #weekly earning

weekday = np.arange(1,8,1) #define day number for the week
print(weekday[hrsWorked>8]) #print weedays where hours worked is greater than 8

# Use logical and function to compute weedays where hours worked is between 0 and 8
print(weekday[np.logical_and(hrsWorked>0, hrsWorked<8)])

# using slice function to select specific rows and columns
sliceArr = np.linspace(1,15,15).reshape(3,5)
print("Printing 2nd and 3rd column data \n",sliceArr[:,2:4])

# define a random array and find out the mean of all values
randArr = np.random.randint(-100,100,10)
meanArr = np.mean(randArr)

# generates boolean array. Value will be true when value is greater than Mean
greatMean = randArr>meanArr
print(randArr)
print(meanArr)
print(greatMean)

# define a random array and use floor function to calculate floor values of all elements.
uniArr = np.random.uniform(1.0,10.5,10)
print(uniArr)
print(np.floor(uniArr))








