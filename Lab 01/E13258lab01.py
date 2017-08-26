import sys
import csv
import numpy as np

num_of_rows = 23998
num_of_col  = 5
array = np.full((num_of_rows,num_of_col), np.nan)

class Sn:
    #read file 
    def __readFile__(self):
        with open("labExercise01.csv") as fh:
            x = 0
            for line in fh:
                currentline = line.split(",")
                for i in range(num_of_col):
                    position = [int(num_of_col  * i + x)]
                    array[x][i] =  float(currentline[i])
                x = x + 1

    #take the mean of a column
    def __meanValue__(self):
        mean_value = np.mean(array, axis = 0)
        return mean_value


    #find the value of SN
    def __valueSn__(self,col):
        meanvalues = self.__meanValue__()
        total = 0
        for i in range(num_of_rows):
            array[i][col] = np.power((array[i][col] - meanvalues[col]), 2) 
            total = total + array[i][col]
        total = total / (num_of_rows - 1)    
        print np.sqrt(total)  

obj = Sn()
    
obj.__readFile__()
obj.__valueSn__(0)
obj.__valueSn__(1)
obj.__valueSn__(2)
obj.__valueSn__(3)
obj.__valueSn__(4)

