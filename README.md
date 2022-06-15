# Generator

In this project, i created a  small system that generates noisy data that fit to
certain shape. 
The generator receives several desired shapes from a config file and generate two
types of points: inlier points with noise and outlier points.

You can change the number of points ("num_points") to be generated and the noise of the data ("randomness") in the config file.
(shape value in the config file is the number of instances per shape you want to generate)

The main is: generator.py

To be continued: Estimate the original shape from the data, and tests the estimation against
the shape.
