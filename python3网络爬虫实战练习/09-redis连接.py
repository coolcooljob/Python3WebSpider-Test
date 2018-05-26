from redis import StrictRedis,ConnectionPool


redis=StrictRedis(host='localhost',port=6379,db=0,password=None)    #两种连接方式都可以
# pool=ConnectionPool(host='localhost',port=6379,db=0,password=None)
# redis=StrictRedis(connection_pool=pool)
redis.set('name','job')
redis.set('age',22)
print(redis.get('name'))
print(redis.exists('name'))
redis.delete('age')
print(type('name'))
print(redis.keys('n*'))
print(redis.randomkey())
redis.move('name',2)
# redis.flushdb()       #删除当前选择数据库中的所有的键
# redis.flushall()      #删除所有数据库中的所有的键
print(redis.dbsize())        #获取当前数据库中的所有键的数目
