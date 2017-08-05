# import sys
# #argv使用空格传入多个参数
# print(sys.argv)
#缓存池，自动垃圾回收
#1.字符串之间，最好不要用+号，最好用字符串格式化。
#list

name=[1,2,3,4]
name1=list([1,2,3,4])
print(name[1].__str__() +":"+ name1[2].__str__())
'''
list
 #'索引' # 切片 
 #   ： # 追加      append
 # 删除      del remove pop
 # 长度      len
 # 循环      for,while(foreach)          break;continue;pass(相当于占位);return;exit
 # 包含      in(查看是否在内部),_contains_
 
 #基础操作
  #'索引' # 切片 
 #   ： # 追加      append
 # 删除      del remove pop
 # 长度      len
 # 循环      for,while(foreach)          break;continue;pass(相当于占位);return;exit
 # 包含      in(查看是否在内部),_contains_
 # 元祖元素不可以修改，元祖的元素的元素是可以修改的
'''
tuples1=(11,22,33)
tuples2=(11,22,{'k1':'v1'})
tuples2[2]['k1']="hello"
print(tuples2[2])
'''
字典
索引
新增
删除
键、值、键值对
 keys values items
 for i in dict
 dict=类 这是一个类，不能起这个名字
 循环
 长度
 一切事物都是对象
'''