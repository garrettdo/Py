# 判断是否是一个目录

import os

dir = "/home/deploy/"
if os.path.isdir(dir):
    print('%s is a dir' % dir)
else:
    print('%s is not a dir' % dir)