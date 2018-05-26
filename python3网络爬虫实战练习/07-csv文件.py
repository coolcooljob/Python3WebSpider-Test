import csv
import pandas as pd        #利用pandas读取csv数据文件

#csv，其文件以纯文本的形式存储表格数据，相当于一个结构化表的纯文本形式
#写入
with open('data.csv','w') as csvfile:            #打开csv文件，获得文件句柄
    writer=csv.writer(csvfile)                   #初始化传入对象，传入该句柄
    writer=csv.writer(csvfile,delimiter=' ')     #可以修改数据之间的分隔符，默认是逗号
    writer.writerow(['id','name','age'])         #以writerow()传入每行的数据
    writer.writerow(['1','job','20'])
    writer.writerow(['2','jack','22'])


#写入字典格式的数据
with open('data1.csv','w',encoding='utf-8') as csvfile:
    fieldnames=['id','name','age']                              #先定义三个字段，用filenames表示
    writer=csv.DictWriter(csvfile,fieldnames=fieldnames)        #将字段传入给Dictwriter来初始化一个字典写入对象
    writer.writeheader()                                        #写入头信息
    writer.writerow({'id':'100','name':'job','age':22})         #传入相应字段
    writer.writerow({'id':'101','name':'tom','age':32})
    writer.writerow({'id':'102','name':'mary','age':25})

#读取
with open('data1.csv','r',encoding='utf-8') as csvfile:
    reader=csv.reader(csvfile)
    for row in reader:
        print(row)



df=pd.read_csv('data1.csv')
print(df)
