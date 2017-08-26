import sys
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

array = []

class RandomWalk:
    def __init__ (self, position):
        self.position = position

    def walk(self,steps):
        for x in range(steps):
            number = np.random.randint (0, 2)
            if number == 0:
                self.position = self.position -1
            else:
                self.position = self.position + 1
            array.append(self.position)
        plt.plot(array)    
        plt.show()


rand = RandomWalk(0)

while True:
    num = input('Enter a desired number: ');
    rand.walk(num)
    if num == 0:
        break
