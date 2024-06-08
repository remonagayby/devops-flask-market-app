import json

def load_visits():
    with open('visits.json', 'r') as file:
        data = json.load(file)
    return data['visits']

def save_visits(visits):
    with open('visits.json', 'w') as file:
        json.dump({'visits': visits}, file)

