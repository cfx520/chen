#coding:utf-8
#author:cfx
from pyspark import SparkContext

"""##demo1 统计字符数
file='README.md'
sc=SparkContext('local','firstdemo')
data=sc.textFile(file).cache()
numAs=data.filter(lambda s:'a' in s).count()
numBs=data.filter(lambda s:'b' in s).count()
print numAs,numBs"""
"""
demo2 使用map、reduce函数
以及了解rdd
"""
"""file='1.csv'
sc=SparkContext()
data=sc.textFile(file)
#print type(data)
#print data.count()
def split_text(x):
    fields=x.split(',')
    name=str(fields[0].encode('utf-8'))
    age=int(fields[1])
    yuwen=int(fields[2])
    math=int(fields[3])
    english=int(fields[4])
    return name,age,yuwen,math,english

#for i in data.collect():
#    print split_text(i)[0]
rdd=data.map(split_text)
#print rdd.collect()

## flatmap 函数
def flatmap_x(x):
    list=[]
    for i in x:
        a=(i,1)
        list.append(a)
    return list
rdd1=rdd.flatMap(flatmap_x)
#print rdd1.collect()
#rdd2=rdd.filter(lambda x:x[2]>98)
#print rdd2.collect()
"""
"""
#reduce()并行汇总所有rdd元素
""""""sc=SparkContext()
list=[2,5,4,3,8,12]
data1=sc.parallelize(list)
value=data1.reduce(lambda x,y:int(x)+int(y))"""
#print value"""

"""sc=SparkContext()
list=['a','ccc','de','gh','efddc']
data=sc.parallelize(list)
value=data.reduce(lambda x,y:x+y)
print value"""

"""
sc=SparkContext()
list=['aa','bcd','ghb','ads','bcg']
data=sc.parallelize(list)
def re(x,y):
    return x
value=data.reduce(re)
print value
"""

"""
统计各元素在rdd中出现的次数

"""
"""list=['asd','asd','ads',1,3,3,4,'cfx','cfx','cfx']
sc=SparkContext()
data=sc.parallelize(list)
value=data.countByValue()
print value"""

"""rdd3=rdd1.reduceByKey(lambda x,y:x+y)
print rdd3.collect()
print rdd1.countByKey()"""

"""sc=SparkContext()
file='1.csv'
data=sc.textFile(file)
adjust=sc.accumulator(0)
def parseline(line):
    global adjust
    adjust+=1
    return line
rdd=data.map(parseline)
print rdd.collect()
print adjust.value"""
sc=SparkContext()
broadcastvalue=sc.broadcast([12,23,14,25,16,3])
print min(broadcastvalue.value)
def parseline(line):
    fields=line.split(',')
    #rint fields
    name=str(fields[0].encode('utf-8'))
    age=int(fields[1])
    yuwen=int(fields[2])
    math=int(fields[3])
    english=int(fields[4])+int(min(broadcastvalue.value))
    return (name,age,yuwen,math,english)
data=sc.textFile('1.csv')
rdd=data.map(parseline)
print rdd.collect()

if __name__ == '__main__':
    pass