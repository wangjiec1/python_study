# f=open("test.log","w")
# f.write("this is the first line\n")
# f.write("this is the second line\n")
# f.close()

# f=open("test.log","r")
# print(f.read())
# f.close()
#
# f=open("test.log","r")
# for line in f:
#   print(line)
# f.close()
#
# f=open("test.log","r")
# for line in f:
#     print(line)
# f.close()
#
# #a 追加
# f=open("test.log","a")
# f.write("3\n")
# f.write("4\n")
# f.close()
# w+ 读写
f=open("test.log","w+")
print(f.readline())
f.write("new line\n")

f.close()