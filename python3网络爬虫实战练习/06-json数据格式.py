import json

#json.loads()可以将文本字符串转化为json对象，可以是列表，也可以使是符串
#json.dumps()可以将json对象转化为文本字符串
#json的数据需要用双引号来包围，不能使用单引号，否则loads()方法会解析失败

str='''[{
    "name":"job",      #注意数据必须是以双引号包围，不然json.loads()则会出现解析错误
    "age":"20",
    "gender":"boy"
    },{
    "name":"jack",
    "age":"22",
    "gender":"boy"
    }]'''
print(type(str))
data=json.loads(str)
print(type(data))
print(data)
