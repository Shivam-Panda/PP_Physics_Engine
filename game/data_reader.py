import json


def get_data(key):
    data = json.loads(open('./game/data.json', 'r').read())
    return data[key]

def set_data(key, val):
    data = json.loads(open('./game/data.json', 'r').read())
    data[key] = val
    open('./game/data.json', 'w').write(json.dumps(data, indent=4))