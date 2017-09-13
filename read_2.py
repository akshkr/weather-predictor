import json
import numpy as np
import sys
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
import csv

#reading data from json file

def get_data(year):
	filename = './data/'+str(year)+'.json'
	with open(filename) as data_file:
		year_data = json.load(data_file)
		return year_data

#organising data for a particular year
def organize_data(year_data):
	yeararray = np.array([])
	f1 = 0.0
	f2 = 0.0
	f3 = 0.0
	f4 = 0.0
	f5 = 0.0
	y = 0.0
	for month in range(6,10):
		f1 = 0.0
		f2 = 0.0
		f3 = 0.0
		f4 = 0.0
		f5 = 0.0
		y = 0.0
		for day in range(1,31):
			i = str(month)
			j = str(day)
			f1 = f1 + year_data[i][j]['TEMP']
			f2 = f2 + year_data[i][j]['DEWP']
			f3 = f3 + year_data[i][j]['VISIB']
			f4 = f4 + year_data[i][j]['WDSP']
			f5 = f5 + year_data[i][j]['MXSPD']
			y = y + year_data[i][j]['PRCP']
			#temp1 = np.array([yn-1999, year_data[i][j]['TEMP'], year_data[i][j]['DEWP'], year_data[i][j]['VISIB'], year_data[i][j]['WDSP'], year_data[i][j]['MXSPD'], year_data[k][l]['PRCP']])
			#yeararray = np.concatenate((yeararray, temp1), axis=0)
			if day%7==0:
				temp = np.array([f1/7, f2/7, f3/7, f4/7, f5/7, y])
				yeararray = np.concatenate((yeararray, temp), axis=0)
				f1 = 0.0
				f2 = 0.0
				f3 = 0.0
				f4 = 0.0
				f5 = 0.0
				y = 0.0
	return(yeararray)


#organising data for all years in total data and reshaping them
totaldata = np.array([])
for i in range(2000, 2017):
	if i == 2014:
		continue
	y1 = get_data(i)
	y2 = organize_data(y1)
	totaldata = np.concatenate((totaldata, y2), axis = 0)

good_data = totaldata.reshape(256, 6)


#Classyfying values of y as per rainfall for high low and medium
for i in range(0,256):
	if good_data[i][5]>2.875:
		good_data[i][5] = 3
	elif good_data[i][5] > 2.00:
		good_data[i][5] = 2
	else:
		good_data[i][5] = 1

#separating X and y
X = good_data[0:256,0:5]
y = good_data[0:256,5]

#training data using Gaussian Naive Bayes
model = GaussianNB()
model.fit(X, y)
err = 0
predicted = model.predict(X)

def plot_rain2(year, mont):
	if year>2013:
		year = year-1
	n = year-2000
	xc = np.zeros(4)
	for i in range(0,4):
		xc[i] = i
	plt.bar(xc, predicted[((n*16)+(mont*4)):((n*16) + 4 + (mont*4))])
	plt.title('Plot of predicted Rainfall')
	plt.xlabel('Weeks of month')
	plt.ylabel('Intensity of Rainfall')
	plt.ylim(0, 4)
	plt.show()


def plot_rain_comp2(year, mont):
	if year>2013:
		year = year-1
	n = year-2000
	xc = np.zeros(4)
	for i in range(0,4):
		xc[i] = i
	plt.figure(1, figsize=(8,4))
	plt.subplot(121)
	plt.bar(xc, predicted[((n*16)+(mont*4)):((n*16) + 4 + (mont*4))], color='r')
	plt.title('Predicted Intensity of Rainfall')
	plt.xlabel('Weeks on month')
	plt.ylabel('Intensity of Rainfall')
	plt.ylim(0, 4)
	plt.subplot(122)
	plt.bar(xc, y[((n*16)+(mont*4)):((n*16) + 4 + (mont*4))], color='b')
	plt.title('Actual Intensity of Rainfall')
	plt.xlabel('Weeks of month')
	plt.ylabel('Intensity of Rainfall')
	plt.ylim(0, 4)
	plt.show()

def writecsv2(year, mont):
	if year>2013:
		year = year-1
	n = year-2000
	g1 = predicted[((n*16)+(mont*4)):((n*16) + 4 + (mont*4))].reshape(4,1)
	with open('predicted_data_class.csv', 'w') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		for row in g1:
			spamwriter.writerow(row)