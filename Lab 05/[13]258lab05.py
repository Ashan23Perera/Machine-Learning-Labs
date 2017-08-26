import sys
import math
import unittest
import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.metrics import accuracy_score
 

class Classification:
	 
    #Read the file and fill the missing value with mean value
	def __readFile__(self, filename) :
		df = pd.read_csv(filename)
		df = df.fillna(df.mean())
		return df

    #Rest of the lab task
	def __decisionTree__(self, filename):
		dataset = ['INCOMEPERPERSON','ALCCONSUMPTION', 'ARMEDFORCESRATE' ,'CO2EMISSIONS' ,'INTERNETUSERATE','LIFEEXPECTANCY','OILPERPERSON','POLITYSCORE','RELECTRICPERPERSON','SUICIDEPER100TH','EMPLOYRATE',  'urbanrate' ]
        
        #Take the dataset with filling missing data
		df  = self.__readFile__(filename)  
 

        #Convert the response variable (class attribute) breastcancerper100th to binary
		newdf = df['BREASTCANCERPER100TH'].shape[0]  
		for i in range(newdf):
			if df['BREASTCANCERPER100TH'][i] > 20 :
				df.loc[i, 'BREASTCANCERPER100TH'] = 1
			else:
 				df.loc[i, 'BREASTCANCERPER100TH'] = 0
		for i in range(len(dataset)):
			df[dataset[i]] = pd.cut(df[dataset[i]], 3, labels =[1, 2, 3])

                
		target = df ['BREASTCANCERPER100TH'].as_matrix()
		array = ['BREASTCANCERPER100TH','COUNTRY','FEMALEEMPLOYRATE','HIVRATE']
		data  = df.drop(array, axis=1).as_matrix()
		lengthTrainData = int(data.shape[0] * 2/3)

		#Construct a tree 
		Tree   = tree.DecisionTreeClassifier()
		decision = Tree.fit(data[0: lengthTrainData], target[0: lengthTrainData])
		
        #After being fitted, the model can then be used to predict the class of samples
		length  =  data.shape[0]
		final   =  Tree.predict(data[lengthTrainData:length])
		
		#Calculate a prediction accuracy for test data set
		correctness = str(accuracy_score(target[lengthTrainData:length], final, normalize = False)) #Correctly Prdicted       
		total = str(length - lengthTrainData)     #Total used to predict

		info = [correctness,total]
		return info 
 
	


if __name__ == "__main__":
	obj = Classification()
	output = obj.__decisionTree__('breaset-cancer.csv')
	print "Total: ", output[1]
	print "Correctly Predicted: ", output[0]
	
