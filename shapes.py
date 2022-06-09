import random
import numpy as np

START = 0.0  # defining the start of the X-axis
END = 1.0  # defining the end of the X-axis
P_IN = 0.8  # defining the percent of inlier points
P_OUT = 0.2  # defining the percent of outlier points

rnd = random.uniform


class Shape(object):
    def __init__(self, num_points, randomness):
        self.num_points = num_points
        self.randomness = randomness

    def line_space(self, start, end, p):
        return np.linspace(start, end, self.num_points * p)

    """
    return inlier and outlier arrays
    according to the defined percent of inlier points
    and outlier points
    """
    def x(self, start, end):  # return inlier and outlier arrays
        x_in = self.line_space(start, end, P_IN)
        x_out = self.line_space(start, end, P_OUT)
        return x_in, x_out, np.append(x_in, x_out)

    """ 
    return data with noise 
    """
    def y(self, y_in, x_out):
        y_in_noise = [i + rnd(min(y_in), max(y_in)) * self.randomness for i in y_in]
        y_out = [rnd(min(y_in_noise), max(y_in_noise)) for i in x_out]
        return y_out, np.append(y_in_noise, y_out)


class Line2D(Shape):
    def __init__(self, num_points, randomness):
        super().__init__(num_points, randomness)
        self.slope = rnd(-END, END*END)
        self.intercept = rnd(START, END)
        self.x_in, self.x_out, self.x = Shape.x(self, START, END)
        self.y_in = [self.slope + self.intercept * i for i in self.x_in]
        self.y_out, self.y = Shape.y(self, self.y_in, self.x_out)
        self.params = {"slope": self.slope, "intercept": self.intercept, "X": self.x, "Y": self.y}


class Circle2D(Shape):
    def __init__(self, num_points, randomness):
        super().__init__(num_points, randomness)
        self.radius = rnd(START, END)
        self.end = 2 * np.pi
        self.t_in, self.t_out, self.t = Shape.x(self, START, self.end)
        self.x_in = self.radius * np.cos(self.t_in)
        self.y_in = self.radius * np.sin(self.t_in)
        self.x_out, self.x = Shape.y(self, self.x_in, self.t_out)
        self.y_out, self.y = Shape.y(self, self.y_in, self.x_out)
        self.params = {"radius": self.radius, "X": self.x, "Y": self.y}
