
import json
list = [{"name": "张学油", "age": 50}, {"name": "刘得滑", "age": 55}]
data = json.dumps(list, ensure_ascii=False)
print(type(data))
print(data)


json_data = '[{"name": "王飞", "age": 50}, {"name": "刘若鹰", "age": 55}]'
l = json.loads(json_data)
print(type(l))
print(l)

