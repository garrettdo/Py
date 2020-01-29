# 一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

tour = []
height = []

sheight = 100.0#起始高度
tim = 10#次数
for i in range(1, tim + 1):
    if i == 1:
        tour.append(sheight)
    else:
        tour.append(2 * sheight)
    sheight /=2
    height.append(sheight)

print('球在第10次落地时共经过tour={0}米'.format(sum(tour)))
print('第10次反弹时球的高度为height={0}米'.format(height[-1]))