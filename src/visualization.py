import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.animation as anim

class visualization:
    def __init__(self, l1, l2, q, ax):
        '''
        '''
        self.l1 = l1
        self.l2 = l2
        self.q = q
        self.ax = ax
        print("Visulization functionality initiated.")
    
    def plot(self, q):

        print "inside animator"
        th1 = self.q[0,0] 
        th2 = self.q[1,0]
        x1 = np.cos(th1) * self.l1
        y1 = np.sin(th1) * self.l1
        x2 = x1 + np.cos(th1 + th2) * self.l2
        y2 = y1 + np.sin(th1 + th2) * self.l2
        x1_seg = np.linspace(0, x1) 
        y1_seg = np.linspace(0, y1)
        x2_seg = np.linspace(x1, x2) 
        y2_seg = np.linspace(y1, y2)
        self.ax.clear()
        self.ax.scatter(x1, y1)
        self.ax.scatter(x2, y2)
        self.ax.plot(x1_seg, y1_seg)
        self.ax.plot(x2_seg, y2_seg)
        self.ax.axis([- self.l1 - self.l2 - 0.5 , self.l1 + self.l2 + 0.5, 
                -self.l1 - self.l2 - 0.5 , self.l1 + self.l2 + 0.5])
        plt.grid(True)

    def animate(self, q):
        self.q = q
        animation = anim.FuncAnimation(self.fig, self.plot, repeat=False)
        plt.show()



'''
Test code
'''
if __name__ == "__main__":
    pass 