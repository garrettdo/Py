#字符串的常见操作

mystr = "hi this is guangtong, this my honey"

print(mystr)
#左边开始查找,查不到返回-1
result = mystr.find("this")
print(result)
#右边开始查找,查不到返回-1
result = mystr.rfind("this")
print(result)

#左边开始查找,查不到时报异常
result = mystr.index("is")
print(result)
#右边开始查找,查不到时报异常
result = mystr.rindex("is")
print(result)

#统计个数
result = mystr.count("this")
print(result)

#替换
result = mystr.replace("this","THIS")
print(result)
result = mystr.replace("this","THIS",1)
print(result)

#切割
result = mystr.split(" ")
print(result)

#首字母大写
result = mystr.capitalize()
print(result)

#所有单词的首字母大写
result = mystr.title()
print(result)
