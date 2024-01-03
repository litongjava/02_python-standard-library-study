# -*- coding:utf-8 *-

import json

results = []
with open('result.json', 'r') as f:
  json_object = json.load(f)
  # print(type(json_object))
  if "result" in json_object:
    result = json_object.get("result")
    for sentence in result:
      # print(type(sentence))
      sentence = "{}->{}:{}".format(sentence['t0'], sentence['t1'], sentence['sentence'])
      results.append(sentence)
      # print(sentence)

for sentence in results:
  print(sentence)
