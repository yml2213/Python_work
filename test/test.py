import json

data = {"name": '小白', "age": 20}
print(data, type(data))
dic_str = json.loads(str(data).replace("'", "\""))
print(dic_str)
