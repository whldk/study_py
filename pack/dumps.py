# coding:utf-8

import json

data = {
    'no':1,
    'name':'rr',
    'url':'www'
}

#讲字典
print(data, type(data))
json_str = json.dumps(data)

print(json_str, type(json_str), repr(data))