# 题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
# 程序分析：在10万以内判断，先将该数加上100后再开方，再将该数加上268后再开方，如果开方后的结果满足如下条件，即是结果。请看具体分析：

# include "math.h"
#
# main()
# {
# long int i,x,y,z;
# for (i=1;i<100000;i++)
#     {
#     x=sqrt(i+100);
#     y=sqrt(i+268);
#         if( x*x==i+100&&y*y==i+268)
#             print("\n%ld\n",i);
#     }
# }
#
# import math
# for i in range(10000):
#     x = int(math.sqrt(i + 100))
#     y = int(math.sqrt(i + 268))
#     if (x * x == i +100) and (y * y == i + 268):
#         print(i)


def perfect_square():
    for i in range(1, 85):
        if 168 % i == 0:
            j = 168 / i;
            if i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0:
                m = (i + j) / 2
                n = (i - j) / 2
                x = n * n - 100
                print(x)


print('\n'.join([''.join([('Love'[(x-y)%4]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y in range(15,-15,-1)]))

print('\n'.join([' '.join(['%s*%s=%-2s' % (y,x,x*y) for y in range(1,x+1)]) for x in range(1,10)]))

user = 'admin'
paswd = 123456
username = input("请输入用户名：")
password = input("请输入密码:")
for i in range(3):
  if username == user and int(password) == paswd: #判断用户名和密码是否都匹配
    print("欢迎您的到来")
    break
  elif i < 2:
    username = input("请输入用户名：")
    password = input("请输入密码")
  elif i == 2:
    print("账户已锁定")
    break