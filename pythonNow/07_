# 系统内存与磁盘检测

import psutil

def memissue():
    print('内存信息：')
    mem = psutil.virtual_memory()
    memtotal = mem.total/1024/1024
    memused = mem.used/1024/1024
    membaifen = str(mem.used/mem.total*100) + '%'

    print('%.2fMB' % memused)
    print('%.2fMB' % memtotal)
    print(membaifen)

def cuplist():
    print('磁盘信息：')
    disk = psutil.disk_partitions()
    diskuse = psutil.disk_usage('/')
    diskused = diskuse.used / 1024 / 1024 / 1024
    disktotal = disktotal.total / 1024 / 1024 / 1024
    diskbaifen = diskused / disktotal * 100

    print('%.2fGB' % diskused)
    print('%.2fGB' % disktotal)
    print(diskbaifen)


memissue()
print('*************')
cuplist()