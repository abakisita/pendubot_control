import numpy as np
from numpy import sin, cos
class pendubot_dynamic_system:

    def __init__(self, l1, l2, m1, m2, initial_state):

        self.initial_state = initial_state
        self.l1 = l1
        self.l2 = l2
        self.m1 = m1
        self.m2 = m2
        # length of center of mass from joint 
        self.lc1 = l1/2  
        self.lc2 = l2/2

        # Inertia of the links of pendubot 
        self.i1 = m1*l1**2 / 12
        self.i2 = m2*l2**2 / 12

        # Gravitaional acceleartion
        self.g = 9.81

        # System initialization
        self.q1 = initial_state[0, 0]
        self.q2 = initial_state[1, 0] + initial_state[0, 0]
        self.dq1 = 0.0
        self.dq2 = 0.0
        self.ddq1 = 0.0
        self.ddq2 = 0.0
        self.q = np.array([[self.q1],
                            [self.q2]])

        self.dq = np.array([[0.0],
                            [0.0]])

        """
        Defining some parameters in terms of system parameters (constant) 
        just to make later calculations easier.
        """
    
    def integrate_one_step(self, tau, time_step):

        th1 = self.q[0,0]
        th2 = self.q[1,0]
        j1 = self.i1
        j2 = self.i2
        l1 = self.l1 
        l2 = self.l2 
        lc1 = self.lc1
        lc2 = self.lc2
        m1 = self.m1
        m2 = self.m2 
        g = self.g

        '''
        l1= 2 # (m)Length of element 1
        lc1= 1 # (m) Distance of CM of element 1 from source end
        m1= 10 # (kg) Mass of element 1
        j1= 3 # (kg-m^2) Moment of Inertia of element 1 about its CM
        tau1= 0 # (N-m) External torque applied on element 1

        l2= 1 # (m)Length of element 2
        lc2= 0.5 # (m)Distance of CM of element 2 from source end
        m2= 6 # (kg) Mass of element 2
        j2= 2 # (kg-m^2)Moment of Inertia of element 2 about its CM
        tau2= 0 # (N-m)External torque applied on element 2

        g= 9.81 # (m/sec^2) Acceleration due to gravity
        '''

        s1=sin(th1)
        s2=sin(th2)
        c1=cos(th1)
        c2=cos(th2)
        c21=cos(th2-th1)
        s21=sin(th2-th1)

        M = np.array([[j1+m2*l1**2, m2*l1*lc2*c21],
                    [m2*l1*lc2*c21, j2+m2*lc2**2]])
        C = np.array([[0, -m2*l1*lc2*s21],
                    [m2*l1*lc2*s21, 0]])
        G = np.array([[m1*g*lc1*c1+m2*g*l1*c1],
                    [m2*g*lc2*c2]])

        self.ddq = np.linalg.inv(M).dot(np.array([[0.0],[0.0]]) - C.dot(self.dq) - G)
        self.dq = self.dq + self.ddq * time_step
        self.q = self.q + self.dq * time_step
        return self.ddq, self.dq, self.q    

        

