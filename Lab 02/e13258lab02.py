import sys
import unittest
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

array = []

class GDC:
    def __init__(self, e1, e2, e3):
        self.e1 = e1
        self.e2 = e2
        self.e3 = e3
        
    def __plotFunction__(self, Range, steps):
        
        for x in range(steps):
            _e1 = self.e1 % 5
            _e2 = self.e2 % 5
            _e3 = self.e3 % 5
            f_x = self.e2 * pow(Range[x] , _e1) - self.e3 * pow(Range[x] , _e2 ) - self.e1 * pow(Range[x] , _e3) + self.e3
            array.append(f_x)
            
        plt.plot(Range, array)
        plt.ylabel('f(x)')
        plt.xlabel('x values')
        plt.title('f(x) = e2 * pow(x , _e1) - e3 * pow(x , _e2 ) - e1 * pow(x , _e3) + e3')
        plt.grid()
        plt.show()

    def __GradX__(self, x):

        grad = 10 * x - 6* pow(x, 2.0)  
        return grad
            
    def __minimumvalue__(self, initial, learningRate, Precision):
        
        currentX = initial   
        while True:
            previousX = currentX
            currentX  = currentX - learningRate *self.__GradX__(currentX)
            previousStepsize = np.abs(currentX - previousX)
            if previousStepsize > Precision:
                break    
        return currentX    

            
'''======================Test============================'''
            
class GDCTest(unittest.TestCase):
    def setUp(self):
        print '======Testing GDC class====='
        self.gdc = GDC(2,5,8)

    def testStartPositin(self):
        expected = [ -200.0, -136.0, -84.0, -44.0, -16.0, 0.0, 4.0, -4.0,-24.0,-56.0, -100.0]
        index = [-5,-4,-3,-2,-1,0,1,2,3,4,5] 
        for i in range(len(expected)):
            self.assertEqual(self.gdc.__GradX__(index[i]), expected[i])

gdc= GDC(2,5,8)

print 'Local minimal Value:  ',int(gdc.__minimumvalue__(-0.01,1,2.0000000000131024e-05))


'''===============Answers===================='''

''' Excercise 1 '''
x = range(-100, 100)
gdc.__plotFunction__(x, 200)

if __name__ == '__main__':
    unittest.main()



