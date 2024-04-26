import os
import json

data_structure = {
    "productos": [],
    "ventas": []
}


def read_data():
    if not os.path.isfile('data.json'):
        with open('data.json', 'w') as doc:
            json.dump(data_structure, doc)
    
    with open('data.json', 'r') as doc:
        data = json.load(doc)

    return data

def write_json(data):
    with open('data.json', 'w') as doc:
        json.dump(data, doc)

def lista_productos():
    return read_data()['productos']

