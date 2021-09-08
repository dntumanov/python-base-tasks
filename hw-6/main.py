from music_serialize import serializer_data
from music_deserialize import deserializer_data
from utils import TypeSerializerTo

my_favourite_groups: list[dict] = [
    {
        'name': 'Г.М.О.',
        'tracks': ['Последний месяц осени', 'Шапито'],
        'Albums': [{'name': 'Делать панк-рок', 'year': 2016},
                   {'name': 'Шапито', 'year': 2014}]
    }
]


if __name__ == '__main__':
    serializer_data(TypeSerializerTo.json, my_favourite_groups)
    serializer_data(TypeSerializerTo.pickle, my_favourite_groups)
    print(deserializer_data(TypeSerializerTo.json))
    print(deserializer_data(TypeSerializerTo.pickle))
