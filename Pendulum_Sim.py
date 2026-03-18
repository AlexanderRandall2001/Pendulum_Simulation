import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Pendulum:
    """
    Create a pendulum simulation using equation of motion derived from Lagrangian.
    """

    def __init__(self, theta, g, l, dt):
        self.theta = theta
        self.initial_theta = theta
        self.theta_dot = 0
        self.g = g
        self.l = l
        self.dt = dt
        self.x = self.compute_x()
        self.y = self.compute_y()
        self.start = (self.x, self.y)
    
    def update_theta_dot(self):
        self.theta_dot = self.theta_dot - ((self.g / self.l) * np.sin(self.theta)) * self.dt
    
    def update_theta(self):
        self.theta = self.theta + self.theta_dot * self.dt
    
    def compute_x(self):
        return self.l * np.sin(self.theta)
        
    def compute_y(self):
        return -self.l * np.cos(self.theta)
    
    def swing(self):
        """
        Main loop
        """

        self.trajectory = [self.start]

        while True:
            self.x = self.compute_x()
            self.y = self.compute_y()
            self.update_theta_dot()
            self.update_theta()

            self.trajectory.append([self.x, self.y])
            if abs(self.theta - self.initial_theta) <= 0.01:
                break
    
    def animate(self):
        interval = 1000 * self.dt
        fig = plt.figure()
        axes = fig.add_subplot(111)

        axes.set_xlim(-self.l * 1.1, self.l * 1.1)
        axes.set_ylim(-self.l * 1.1, self.l * 1.1)

        line, = axes.plot([], [], ".-", lw=4, color='#66FF66')

        def update(frame):
            x, y = self.trajectory[frame]
            xs, ys = (0, x), (0, y)
            return line.set_data(xs, ys)
        
        fig.ani = FuncAnimation(fig, update, frames = len(self.trajectory), interval = interval, blit = False)
        fig.ani.save('pendulum.gif', writer='pillow', fps=20)

        plt.show()

pendulum = Pendulum(-0.7, 9.8, 0.5, 0.05)
pendulum.swing()
pendulum.animate()
        
        

