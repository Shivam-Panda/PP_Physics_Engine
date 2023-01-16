import json


def get_data(key):
    try:
        f = open('./PE/game/data.json', 'r').read()
        data = (json.loads(f))
        return data[key]
    except:
        return None

def set_data(key, val):
    data = json.loads(open('./PE/game/data.json', 'r').read())
    data[key] = val
    f = open('./PE/game/data.json', 'w')
    f.write(json.dumps(data, indent=4))
    f.close()

def clear_data():
    open('./PE/game/data.json', 'w').write('{}')