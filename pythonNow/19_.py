# 暂停一秒输出，并格式化当前时间。
# 程序分析：使用 time 模块的 sleep() 函数。



import time

# 输出当前时间
print(time.strftime('%Y-%M-%D %H:%M:%S',time.localtime(time.time())))

time.sleep(10)

# 输出10秒后的时间
print(time.strftime('%Y-%M-%D %H:%M:%S',time.localtime(time.time())))

