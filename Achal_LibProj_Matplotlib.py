#Step1: Import required libraries
import numpy as np
import matplotlib as plt
from matplotlib import pyplot, style
from sklearn.datasets import load_boston #Dataset for Histogram and Scatterplot



randArr = np.random.rand(10) #Step2: Create an array with random numbers
print(randArr) #View random array created
plt.pyplot.plot(randArr) #Step3: Set the plot parameters
plt.pyplot.show() #Step4: Display the created graph

#Website traffic data, number of users on website
#10 hours of hourly traffic data for Website on Monday
userMon = [123,645,950,1290,1630,1450,1034,1295,465,205,80]
#10 hours of hourly traffic data for Website on Tuesday
userTue = [95,680,889,1145,1670,1323,1119,1265,510,310,110]
#10 hours of hourly traffic data for Website on Wednesday
userWed = [105,630,700,1006,1520,1124,1239,1380,500,610,230]
#Time distribution (hourly)
timeArr = np.arange(7,18,1)

#select the style of the plot
style.use('ggplot')
#plot website traffic data (X-axis hrs and Y-axis as number od users)
#plot monday web traffic with Red colour
plt.pyplot.plot(timeArr, userMon,'r',label='Monday',linewidth=1)
#plot monday web traffic with Green colour
plt.pyplot.plot(timeArr, userTue,'g',label='Tuesday',linewidth=1.5)
#plot monday web traffic with Blue colour
plt.pyplot.plot(timeArr, userWed,'b',label='Wednesday',linewidth=2)
#define range of values on X and Y axis
plt.pyplot.axis([6.5,17.5,50,2000])
#set the title of graph
plt.pyplot.title('Hourly Website Traffic')
#set label for x axis
plt.pyplot.xlabel('Hours')
#set label for Y axis
plt.pyplot.ylabel('Number of Users')
plt.pyplot.legend()
plt.pyplot.show()
#
# #job data in percentile
# jobList = ['40','20','17','8','5','10']
# #job domains, used as labels in Pie chart
# domainList = ['IT','Finance','Marketing','Admin','HR','Operations']
# #define parameters for Pie chart
# plt.pyplot.pie(jobList,labels=domainList,autopct='%1.0f%%')
# #display graph
# plt.pyplot.show()
#
#load boston dataset
bostonRealEstate = load_boston()
#view the description of boston dataset
print(bostonRealEstate.DESCR)
#define x axis for the data
xval = bostonRealEstate.data
#define y axis for the data
yval = bostonRealEstate.target

#use ggplot style for the graph
style.use('ggplot')
#define parameters for histogram
plt.pyplot.hist(yval,bins=50)
#set X-axis label
plt.pyplot.xlabel('Price in 1000s USD')
#set Y-axis label
plt.pyplot.ylabel('Number of Houses')
#display the graph
plt.pyplot.show()

#use ggplot style for the graph
style.use('ggplot')
#define parameters for Scatterplot
plt.pyplot.scatter(bostonRealEstate.data[:,5],bostonRealEstate.target)
#set X-axis label
plt.pyplot.xlabel('Number of Houses')
#set Y-axis label
plt.pyplot.ylabel('Price in 1000s USD')
#display the graph
plt.pyplot.show()


