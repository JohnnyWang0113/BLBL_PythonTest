# 创建redis连接
# import redis
#
# r = redis.Redis(
#     host='localhost',
#     port=6379,
#     passowrd='123456',
#     db=0
# )
#
# # 创建连接池
# pool = redis.ConnectionPool(
#     host="localhost",
#     port=6379,
#     password="123456",
#     db=0,
#     max_connections=20
# )
#
# r = redis.Redis(
#     connection_pool=pool
# )
# # 数据操作
# r.set("name", "Lisa")
# r.set("gender", "男")
# name = r.get("city").decode("utf-8")
# print(name)
# # 关闭连接
# del r

import redis

# decode_responses=True保证取出的数据不带b（byte）
r = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)
# 清除所有key
r.flushdb()
r.set('name1','zhangsan')
r.set('name2','lisi')

i = 1
# 获取所有key
print(r.keys('*'))
m = r.keys('*')
print(m[i]+' '+r.get(m[i]))
