import numpy as np
import time 
from visualization import visualization
from system import pendubot_dynamic_system

def main():
    m1 = 1.0
    m2 = 1.0
    l1 = 1.0
    l2 = 1.0
    q1 = np.pi/4
    q2 = np.pi/4
    initial_state = np.array([[q1],
                            [q2]])
    
    # Initializing pendubot
    pendubot = pendubot_dynamic_system(l1, l2, m1, m2, initial_state)

    # Initializing visualization
    vis = visualization(l1, l2, initial_state)

    # Running simulation
    start_time = time.time()
    print("Simulation started at ", start_time)
    ddq, dq, q = pendubot.integrate_one_step(0.0, 0.0)
    vis.plot(q)
    while True:
        time_step = time.time() - start_time
        ddq, dq, q = pendubot.integrate_one_step(0.0, 0.01)
        vis.animate(q)

if __name__ == "__main__":
    main()


