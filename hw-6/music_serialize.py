import json
import pickle
from utils import TypeSerializerTo

def serializer_data(type_serializer: TypeSerializerTo, groups: list[dict]) -> None:
    """Serializer Data to json or pickle"""
    if type_serializer == TypeSerializerTo.json:
        with open('data.json', 'w', encoding='utf-8') as file:
            json.dump(groups, file)
            print('Success Serialize')
    elif type_serializer == TypeSerializerTo.pickle:
        with open('data.pickle', 'wb') as file:
            pickle.dump(groups, file)
            print('Success Serialize')
    else:
        print('Error')
