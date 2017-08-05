'''
执行的py文件 __name__="__main__"，主py文件引用的py文件，name=文件名。
py中的所有可操作的，都是对象。由类生成的。

int 二进制的位数：bit_length

python 中常用的功能，会写在内置函数里。__abs___():绝对值
1+1 执行的时候，先创建1然后调用add方法，去添加另一个1

int.__divmod 方法，返回的就是，商和余数。
'''

'''

if __name__=="__main__":
    print("this is %s" %(__name__))

age=int(-18)
print(type(age))
print(age.bit_length())

print(age.__abs__())
print(abs(age))
'''

'''
type() 获取类型
dir() 是获取的类里面的说有成员
contain等于in
'''
name="wang"
name1=str("wang1 {0}")
print(type(name))
#print(dir(name))
print(str.format(name1,"sss"))
print(8*"*")
print(name.center(20))
print(name.center(20,'*'))

#str.count() 字符串子序列出现的次数
name3='sefr:festdesdesed'
print(name3.count('s'))
print(name3.count('s',0,10))

#encode 转码
print(name.encode('gbk'))
print(name.encode('utf-8'))
#endswith 判读是否含有某个字符
name4='wang'
print(name4.endswith('g'))
print(name4.endswith('wsg',0,3))
print(name4.endswith('w',0,3))

name5='w\tang'
print(name5)
print(len(name5))

print(name5.find('j'))#如果不存在，返回-1
print(name5.index('g'))# 如果不存在报错

'''
format 字符串的格式化
'''
name7='my {0} is {1}'
print(name7.format('name','wang'))
name8='my {ward} is {myname}'
print(name8.format(ward='name',myname='wang_'))

#join
li=['w','n','g']
print(''.join(li))
print('_'.join(li))

#lower 变成小写
#ltrip 去掉左边的空格
# maketrans 可以做一个对应表
#translate 结合做替换
#partition 分割
print('hahawiwos'.partition('i'))#将字符串分割成三部分
#replace 替换
#rsplit() 从右开始分割字符
#split()
#splitlines() 根据换行符分割
#startswish
#swapcase(0 大小写转换，将大写转换为小写，小写转换为大写
#title

#with 管理上下文，不用再打开和关闭文件。