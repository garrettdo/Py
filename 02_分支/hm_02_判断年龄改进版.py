# 1.定义一个整数变量记录年龄
age = int(input("请输入年龄："))

# 2.判断是否满18岁
if age >= 18:
    # 3.如果满了18岁，可以进网吧嗨皮
    print("你已经成年，可以进网吧")
    print("欢迎欢迎，热烈欢迎！")

else:
    print("你还未成年！回家写作业！")

# 无论条件是否满足，都会执行
print("这句什么时候执行")