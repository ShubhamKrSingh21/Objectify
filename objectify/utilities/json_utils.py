import numpy as np
class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        
        return super(NpEncoder, self).default(obj)

def writeJSON(newdict, json_path = 'static/result.json'):
    x = json.dumps(newdict, cls=NpEncoder,indent=4)
    # print(x)
    with open(json_path, 'w') as fp:
        fp.write(x)
    return True