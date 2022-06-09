from json import JSONEncoder
import json
import numpy as np


# Serialization
class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)


# Serializing json and
# Writing json file
def output(output_path, shape_params):
    with open(output_path, 'w') as write_file:
        json.dump(shape_params, write_file, cls=NumpyArrayEncoder)

