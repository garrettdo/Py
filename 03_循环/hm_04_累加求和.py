# 计算 0-100 所有数的累计和结果
# 0、定义最终结果的变量
result = 0

# 1、定义一个整数的变量记录循环次数
i = 0

# 2、开始循环
while i <= 100:
    #print(i)

    # 每次循环都让result这个变量和i相加
    result += i
    i += 1
print("0-100直接的数字求和结果=%d" % result)

print(i)