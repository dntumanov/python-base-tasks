## 6. Working with files. Encodings
1: Create a module music_serialize.py. In this module, define a dictionary for your favorite music group, for example
```python
my_favourite_group = {
'name': 'Г.М.О.',
'tracks': ['Последний месяц осени', 'Шапито'],
'Albums': [{'name': 'Делать панк-рок','year': 2016},
{'name': 'Шапито','year': 2014}]}
```
Use the json and pickle modules to serialize this dictionary in json and in bytes, output the results to the terminal. Write the results to group files.json, group. pickle, respectively. In the group file.json specify utf-8 encoding.
2: Create a module music_deserialize.py. In this module, open the group files.json and group. pickle, read the information from them. And get the object: dictionary from the previous task.