import sys
import pandas as pd
import numpy as np
import unittest
 

class pandaLib:
	def __readFile__(self, filename):
		df = pd.read_csv(filename, names = ['col_1', 'col_2', 'col_3', 'col_4', 'col_5' ])
		df = df.fillna(df.mean())
		return df
	
	
	def __retColumns__(self, filename):
		df = self.__readFile__(filename)
		d = [df.col_1, df.col_2, df.col_3, df.col_4, df.col_5]
		return d
    

	def __covariance__(self, filename, col1, col2):
		df      = self.__readFile__(filename)
		d       = self.__retColumns__(filename)
		columns =  df.mean()
		X       = d[col1]
		Y       = d[col2]
		x       = columns[col1]
		y       = columns[col2]

		cov     = 0
		for i in range(df.shape[0]):
			cov = cov + (X[i] - x)* (Y[i] - y)
		cov  = cov/(df.shape[0] - 1)  
		return cov


	def __std__(self, filename, col):
		df      = self.__readFile__(filename)
		d       = [df.col_1, df.col_2, df.col_3, df.col_4, df.col_5]
		X       = d[col]
		x       = X.mean()
		
		std = 0
		std = ((X - x)**2).sum()/(X.count() - 1)
		return np.sqrt(std) 		
 

	def __corelation__(self, filename, col1, col2):
		cov =  self.__covariance__(filename, col1, col2)
		std1 = self.__std__(filename, col1)
		std2 = self.__std__(filename, col2)
		cor  = cov /(std1 * std2)
		return cor     

	def __variance__(self, filename, col):
		return pow(self.__std__(filename, col), 2)


	def __covarianceMatrix__(self,filename):
		matrix = np.full((5,5), np.nan)
		df = self.__readFile__(filename)
		for i in range(df.shape[1]):
			for j in range(df.shape[1]):
				if i == j:
			 		matrix[i][j] = self.__variance__(filename, j)
				else:
					cov          = self.__covariance__(filename, i, j)
					matrix[i][j] = cov
					matrix[j][i] = cov
		return matrix


	def __corelationMatrix__(self,filename):
		matrix = np.full((5,5), np.nan)
		df = self.__readFile__(filename)
		for i in range(df.shape[1]):
			for j in range(df.shape[1]):
				cor          = self.__corelation__(filename, i, j)
				matrix[i][j] = cor
				matrix[j][i] = cor
		return matrix	


class PandasTest(unittest.TestCase):

	def setUp(self):
		self.panda = pandaLib()

	def testVaraince(self):
		self.assertEqual(np.around(self.panda.__variance__('lab03Exercise.csv', 1), decimals = 5), 0.01672)

	def testCovaraince(self):	
		self.assertEqual(np.around(self.panda.__covariance__('lab03Exercise.csv', 1, 2), decimals = 5), 0.01390)

	def testCorelation(self):
		self.assertEqual(np.around(self.panda.__corelation__('lab03Exercise.csv', 1, 2), decimals = 5), 0.85785)

	def testStandardDevtion(self):
		self.assertEqual(np.around(self.panda.__std__('lab03Exercise.csv', 1), decimals = 5), 0.12929)



	


if __name__ == "__main__":
	obj = pandaLib()
	print "=========================Covariance Matrix==================================="
	print obj.__covarianceMatrix__('lab03Exercise.csv')
	print '=============================================================================\n'
	print "=========================Corelation Matrix==================================="
	print obj.__corelationMatrix__('lab03Exercise.csv')


	unittest.main()



'''
2. Corelation Matrix
__________________________________________________________________________
   		| col - 1	 |	col - 2	  |	col - 3	   |	col - 4	|	col - 5  |  
col - 1 | 1.         | 0.82980428 | 0.79626113 | 0.7932761  | 0.41763765]|
col - 2 | 0.82980428 | 1.         | 0.85784608 | 0.84038982 | 0.56332764]|
col - 3 | 0.79626113 | 0.85784608 | 1.         | 0.90304617 | 0.60849677]|
col - 4 | 0.7932761  | 0.84038982 | 0.90304617 | 1.         | 0.72771774]|
col - 5 | 0.41763765 | 0.56332764 | 0.60849677 | 0.72771774 | 1.        ]|

From the corelation matrix above corelation vary among each column,
column (1 - 2), (1 - 3), (1 - 4), (2 - 3), (2 - 4), (3 - 4) > column (2 ,5), (3 ,5), (4 ,5)  > column (1, 5)   

'''

'''
3. It gives two values (0 or 1) relavant to the condition satisfied. But this is 
not have a higher accuracy to split the dataset. Also it will give a higher accuracy 
if use row data than column data. 

'''


