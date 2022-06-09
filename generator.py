import json
from matplotlib import pyplot as plt
import shapes
import serialization

config_path = 'config.json'
output_path = 'output.json'
debug = False

rf = open(config_path, 'r')
config = json.load(rf)

for shape in config['shapes']:
    for i in range(config['shapes'][shape]):
        if shape == 'Line2D':
            s = shapes.Line2D(config['num_points'], config['randomness'])
        if shape == 'Circle2D':
            s = shapes.Circle2D(config['num_points'], config['randomness'])
        serialization.output(output_path, s.params)
        if debug:
            plt.scatter(s.x, s.y, c='g', s=2)
            plt.show()

