# 定义一个布尔类型，编写代码判断是否是本公司员工
# 如果不是，提示不允许入内

is_employee = False

# 在开发中，通常希望某个条件不满足时，执行一些代码，可以使用not
# 另外，如果需要拼接复杂的逻辑计算条件，同样也可能使用到not
if not is_employee:
    print("非本公司员工，禁止入内")
else:
    print( )