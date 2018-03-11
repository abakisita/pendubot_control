import numpy as np 
import matplotlib.pyplot as plt

class visualization:
    def __init__(self, l1, l2):
        '''
        '''
        self.l1 = l1
        self.l2 = l2
        plt.axis([- self.l1 - self.l2 - 0.5 , self.l1 + self.l2 + 0.5, 
                -self.l1 - self.l2 - 0.5 , self.l1 + self.l2 + 0.5])
        plt.grid(True)
        print("Visulization functionality initiated.")
    
    def plot(self, th1, th2):
        x1 = np.cos(th1) * self.l1
        y1 = np.sin(th1) * self.l1
        x2 = x1 + np.cos(th1 + th2) * self.l2
        y2 = y1 + np.sin(th1 + th2) * self.l2
        x1_seg = np.linspace(0, x1) 
        y1_seg = np.linspace(0, y1)
        x2_seg = np.linspace(x1, x2) 
        y2_seg = np.linspace(y1, y2)
        plt.scatter(x1, y1)
        plt.scatter(x2, y2)
        plt.xlabel("X-Axis")
        plt.ylabel("Y-Axis")
        plt.plot(x1_seg, y1_seg)
        plt.plot(x2_seg, y2_seg)
        plt.show()


'''
Test code
'''
if __name__ == "__main__":
    vis = visualization(1.0, 1.0)
    vis.plot(np.pi/4, np.pi/6)
