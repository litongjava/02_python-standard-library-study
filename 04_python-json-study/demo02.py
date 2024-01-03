import json

list_ = [1, 2, 3, 4]
dict_ = {"key1": {"k1": "v1", "k2": "v2"}, "key2": {"k1": "v1", "k2": "v2"}}

list_json = json.dumps(list_)
dict_json = json.dumps(dict_)

print(list_json)
print(type(list_json))

print(dict_json)
print(type(dict_json))
