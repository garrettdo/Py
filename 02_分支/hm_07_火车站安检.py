# 定义布尔类型表示是否有车票
# 定义整型变量表示刀的长度，单位厘米
# 首先检查是否有车票，如果有，才允许进行安检
# 安检时，需要检查刀的长度，判断是否超过20厘米
# 如果超过20厘米，提示刀的长度，不允许上车
# 如果不超过20里面，安检通过
# 如果没有车票，不允许安检

has_ticket = True
knife_length = 18

if has_ticket:
    print("车票检查通过，准备进行安检")
    if knife_length > 20:
        print("您携带的刀太长了！有%d公分长" % knife_length)
    else:
        print("安检通过！")
else:
    print("大佬，请先买票")