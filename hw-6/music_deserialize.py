import json
import pickle
from utils import TypeSerializerTo


def deserializer_data(des_type: TypeSerializerTo):
    """Deserializers data to need format"""
    groups = None
    if des_type == TypeSerializerTo.json:
        with open(f'data.json', 'r', encoding='utf-8') as file:
            groups = json.load(file)
    elif des_type == TypeSerializerTo.pickle:
        with open(f'data.pickle', 'rb') as file:
            groups = pickle.load(file)
    return groups

