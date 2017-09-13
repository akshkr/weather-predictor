import json
import numpy as np
import sys
import matplotlib.pyplot as plt
import csv

from scipy.optimize import minimize

#The following function get the data from the json files
def get_data(year):
	filename = './data/'+str(year)+'.json'
	with open(filename) as data_file:
		year_data = json.load(data_file)
		return year_data
#keys -> TEMP	DEWP	VISIB	WDSP	PRCP=y

#This will take input as the output of above function
#JUNE -> SEPTEMBER
def organize_data(year_data, yn):
	yeararray = np.array([])
	for month in range(6,10):
		for day in range(1,31):
			i = str(month)
			j = str(day)
			if day>0:
				k = str(month)
				l = str(day)
			else:
				k = str(month-1)
				l = str(30-day)
			temp1 = np.array([yn-1999, year_data[i][j]['TEMP'], year_data[i][j]['DEWP'], year_data[i][j]['VISIB'], year_data[i][j]['WDSP'], year_data[i][j]['MXSPD'], year_data[k][l]['PRCP']])
			yeararray = np.concatenate((yeararray, temp1), axis=0)

	return(yeararray)

#prepares the total data for all the years in form of single array which is later reshaped and 
#training set and test set are derived from the data
training_data = np.array([])
for i in range(2000, 2017):
	year = get_data(i)
	temp = organize_data(year, i)
	training_data = np.concatenate((training_data, temp), axis=0)

#data variable stores the total data which can be later parsed to separate training set and test set
data = training_data.reshape(2040, 7)

#X and y separates the input features and output
X = np.c_[np.ones(data.shape[0]), data[:,0:7]]
y = np.c_[data[:,6]]


#returns the cost of the test set or training set according to build hypothesis
def computeCost(X, y, theta=[[0],[0],[0],[0],[0],[0],[0],[0]]):
    m = y.size
    J = 0
    
    h = X.dot(theta)
    
    J = 1/(2*m)*np.sum(np.square(h-y))
    
    return(J)

print(computeCost(X,y))


#gradient descent for linear regression used for optimising weights
def gradientDescent(X, y, theta=[[0],[0],[0],[0],[0],[0],[0],[0]], alpha=0.0001, num_iters=1500):
    m = y.size
    J_history = np.zeros(num_iters)
    
    for iter in np.arange(num_iters):
        h = X.dot(theta)
        theta = theta - alpha*(1/m)*(X.T.dot(h-y))
        J_history[iter] = computeCost(X, y, theta)
    return(theta, J_history)

theta , Cost_J = gradientDescent(X, y)
print('theta: ',theta.ravel())

print(Cost_J)

#The following function is to plot the rainfall for the year_rain and COMPARE
def plot_rain_comp(year_rain, theta = theta):

	#calculating index of data
	n = year_rain - 2000

	#initialising test set
	X_test = X[n*120:(n*120)+120,:]

	#multiplying with theta and evaluating results
	g1 = (theta.T.dot(X_test.T)).T

	xc = np.zeros(120)

	g2 = data[n*120:(n*120)+120,6]

	for i in range(0,120):
		xc[i] = i
	plt.figure()
	plt.plot(xc, g1, label='Predicted')
	plt.scatter(xc, g2, s=30, c='r', marker='x', linewidths=1, label='Actual')
	plt.title('Plot for Actual vs Predicted Rainfall')
	plt.xlabel('days in Monsoon')
	plt.ylabel('Rainfall')
	plt.grid(True)
	plt.ylim(0,4)
	plt.legend()
	plt.show()


#The following function is used to plot simple PREDICTION
def plot_rain(year_rain, theta = theta):

	#calculating index of data
	n = year_rain - 2000

	#initialising test set
	X_test = X[n*120:(n*120)+120,:]

	#multiplying with theta and evaluating results
	g1 = (theta.T.dot(X_test.T)).T

	xc = np.zeros(120)

	g2 = data[n*120:(n*120)+120,6]

	for i in range(0,120):
		xc[i] = i
	plt.figure()
	plt.plot(xc, g1, label='Predicted')
	plt.xlabel('days in Monsoon')
	plt.ylabel('Rainfall')
	plt.title('Plot for Predicted Rainfall')
	plt.grid(True)
	plt.legend()
	plt.ylim(0,3)
#	plt.scatter(xc, g2, s=30, c='r', marker='x', linewidths=1)
	plt.show()

#The following function used to write data into csv

def writecsv(year_rain, theta = theta):

	#calculating index of data
	n = year_rain - 2000

	#initialising test set
	X_test = X[n*120:(n*120)+120,:]

	#multiplying with theta and evaluating results
	g1 = (theta.T.dot(X_test.T)).T

	with open('predicteddata1.csv', 'w') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		for row in g1:
			spamwriter.writerow(row)