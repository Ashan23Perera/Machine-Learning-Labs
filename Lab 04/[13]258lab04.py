import sys
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

class Regression:

	def __readFile__(self):
		#Take the Channels
		channelList = pd.read_csv('lab04ExerciseChannels.csv', names = ['channel1', 'channel2', 'channel3', 'channel4', 'channel5'])
		#Take the angels
		angleList   = pd.read_csv('lab04ExerciseAngles.csv', names = ['angle1', 'angle2', 'angle3'])
		#Merge angles and channels
		mergeList   = pd.DataFrame({'angle': [angleList], 'channel':[channelList]})
		return mergeList
	
	def __linearRegression__(self):
		mergeList = self.__readFile__()
		X_train, X_val, Y_train, Y_val = train_test_split(mergeList.channel[0], mergeList.angle[0].angle1, test_size = 0.2)
		lin_reg = LinearRegression()
		lin_reg.fit(X_train, Y_train)
		Test = lin_reg.predict(X_val.values)

		print "====================Expected==================="
		print Y_val.values
		print "=========Output Of Linear Regression==========="
		print Test
		print "=====================Error====================="
		print Test - Y_val.values 

	def __logisticRegression__(self):
		mergeList = self.__readFile__()
		X_train , X_val , Y_train , Y_val = train_test_split (mergeList.channel[0], mergeList.angle[0].angle1, test_size = 0.2)
		log_reg = LogisticRegression ()
		log_reg.fit( X_train , Y_train )
		y_proba = log_reg.predict (X_val)
		
		print "===================Expected===================="
		print Y_val.values
		print "=========Output of Logistic Regression========="
		print y_proba
		print "===================Error======================="
		print y_proba - Y_val.values
          

obj = Regression()
print obj.__linearRegression__()
#print obj.__logisticRegression__()


''' 
part 3 - 
  
  Linear Regression is not an issue for this case.
  Because most outputs are in floats data type.
  In logistic regression some issues when the output 
  data type is in float. When logistic Regression used 
  the error it given is in attached image (Fig 01).  
  Linear Regression is the suitable one

'''
'''

part 4 -
	
	Basically here there are two types of data angle and channels.
	So there is no big impact on those data to accuracy. Because of 
	that all channels are chosen as features. 

'''
'''

part 5 -
     
     The accuracy vary when the code run again and again.
     Because data is selected randomly. The selected data
     is not same for everymoment that code runing. 

'''