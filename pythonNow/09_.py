# 查看网段里有多少ip地址

import IPy

ip = IPy.IP('172.18.31.0/26')

print(ip.len())
for i in ip:
    print(i)