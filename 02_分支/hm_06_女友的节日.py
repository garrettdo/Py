# 定义变量记录节日名称
# 如果是情人节，买买玫瑰，看电影
# 如果是平安夜，买苹果，吃大餐
# 如果是生日，买蛋糕
# 其他的日子，每天都是节日...

#holiday_name = "情人节"
holiday_name = str(input("请输入节日："))

if holiday_name == "情人节":
    print("买玫瑰")
    print("看电影")
elif holiday_name == "平安夜":
    print("买苹果")
    print("吃大餐")
elif holiday_name == "生日":
    print("买蛋糕")
    print("啪啪啪")
else:
    print("每天都是节日")