import numpy as np

class pendubot_dynamic_system:

    def __init__(self, l1, l2, m1, m2, initial_state):

        self.initial_state = initial_state
        # length of center of mass from joint 
        lc1 = l1/2  
        lc2 = l2/2

        # Inertia of the links of pendubot 
        i1 = m1*l1**2 / 12
        i2 = m2*l2**2 / 12

        # Gravitaional acceleartion
        self.g = 9.8

        # System initialization
        self.q1 = initial_state[0, 0]
        self.q2 = initial_state[1, 0]
        self.dq1 = 0.0
        self.dq2 = 0.0
        self.ddq1 = 0.0
        self.ddq2 = 0.0
        self.q = initial_state
        self.dq = np.array([[0.0],
                            [0.0]])

        """
        Defining some parameters in terms of system parameters (constant) 
        just to make later calculations easier.
        """
        self.p1 = m1*lc1**2 + m2*l1**2 + i1
        self.p2 = m2*lc2**2 + i2
        self.p3 = m2*l1*lc2
        self.p4 = m1*lc1 + m2*l1
        self.p5 = m2*lc2

    def integrate_one_step(self, tau, time_step):

        # Inertial matrix
        m = np.array([[self.p1 + self.p2 + 2*self.p3*np.cos(self.q2), self.p2 + self.p3*np.cos(self.q2)],
                    [self.p2 + self.p3*np.cos(self.q2), self.p2]], dtype='float')
        
        # Coriolis and centripetal terms 
        c = np.array([[-self.p3*np.sin(self.q2) * self.dq2, -self.p3*np.sin(self.q2)*(self.dq2 + self.dq1)],
                    [self.p3*np.sin(self.q2)*self.dq1, 0.0]])

        # Gravitational terms
        g = np.array([[self.p4*self.g*np.cos(self.q1) + self.p5*self.g*np.cos(self.q1 + self.q2)],
                    [self.p5*self.g*np.cos(self.q1 + self.q2)]])

        self.ddq = np.linalg.pinv(m).dot(np.array([[0.0],[0.0]]) - c.dot(self.dq) - g)
        self.dq = self.dq + self.ddq * time_step
        self.q = self.q + self.dq * time_step
        return self.ddq, self.dq, self.q

        

