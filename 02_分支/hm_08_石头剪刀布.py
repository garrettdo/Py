# 导入随机工具包
# 从控制台输出拳头（石头，剪刀，布）
# 电脑随机出拳
# 比较胜负

import random

player = int(input("请输入您要出的拳 （1）石头 -（2）剪刀 - （3）布 ："))
computer = random.randint(1,3)
print("玩家选择的拳头是：%d - 电脑选择的拳头是：%d" % (player,computer))

if ((player == 1 and computer == 2)
    or (player == 2 and computer == 3)
    or (player == 3 and computer == 1)):
    print("玩家获胜")
elif player == computer:
    print("平局")
else:
    print("电脑获胜")