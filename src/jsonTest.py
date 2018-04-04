# 测试json

import json
jsonstring='{"user_man":[{"name":"Peter"},{"name":"xiaoming"}],"user_woman":[{"name":"Anni"},{"name":"zhangsan"}]}'
json_data=json.loads(jsonstring)
print(json_data.get("user_man"))
print(json_data.get("user_woman"))
print(json_data.get("user_man")[0].get("name"))
print(json_data.get("user_woman")[1].get("name"))