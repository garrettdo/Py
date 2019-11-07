# 定义字符串变量 name，输出我的名字叫小明，请多多关照；
name = "小明"
print("我的名字叫%s，请多多关照！" % name)

# 定义整数型变量 student_no，输出我的学号是 10040
student_no = 10040
print("我的学号是%d" % student_no)

# 定义小数，price，weight，money，输出苹果单价，重量，总价；
price = 8.5
weight = 7.5
money = price * weight
print("苹果单价是%f元，苹果重量是%f千克，苹果总价是%f" % (price,weight,money))

# 定义一个小数 scale，输出数据比例是10.00%
scale = 0.25
print("数据比例是%.2f%%" % scale)