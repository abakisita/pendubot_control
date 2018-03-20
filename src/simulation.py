import numpy as np
import time 
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from visualization import visualization
from system import pendubot_dynamic_system


class simulation:
    def __init__(self):

        # Initializing pendubot

        m1 = 1.0
        m2 = 1.0
        l1 = 1.0
        l2 = 1.0
        self.l1 = l1
        self.l2 = l2
        q1 = 3*np.pi/2 + np.pi/4
        q2 = 0.0
        initial_state = np.array([[q1],
                                [q2]])
        self.start_time = time.time()
        self.pendubot = pendubot_dynamic_system(l1, l2, m1, m2, initial_state)
        # Initializing visualization
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(1,1,1)

    def plot(self, q):
        for i in range(0,30):
            q = self.run()
        th1 = q[0,0] 
        th2 = q[1,0] - th1
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


    def run(self):
        # Running simulation
        time_step = time.time() - self.start_time
        ddq, dq, q = self.pendubot.integrate_one_step(0.0, 0.001)
        return q

    def animate(self):
        self.start_time = time.time()
        animation = anim.FuncAnimation(self.fig, self.plot, repeat=False)
        plt.show()


if __name__ == "__main__":
    sim = simulation()

    sim.animate()


