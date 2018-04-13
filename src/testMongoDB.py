# 测试连接mongodb数据库
import pymongo
client=pymongo.MongoClient('localhost',27017)
mydb=client['mydb']
test=mydb['test']
test.insert({'name':'Jan','sex':'男','grade':'89'})