import json

list_json = '[1,2,3,4]'
dict_json = '{"key1":{"k1":"v1","k2":"v2"},"key2":{"k1":"v1","k2":"v2"}}'

list_ret = json.loads(list_json)
dict_ret = json.loads(dict_json)

print(list_ret)
print(type(list_ret))

print(dict_ret)
print(type(dict_ret))
