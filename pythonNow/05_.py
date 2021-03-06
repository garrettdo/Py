print('\n'.join([''.join([('Love'[(x-y)%4]
    if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')
        for x in range(-30,30)])
        for y in range(15,-15,-1)]))

import socket
# import os
# import subprocess


# 判断网络是否正常
# server='baidu.com'
# # 检测服务器是否能ping通，在程序运行时，会在标准输出中显示命令的运行信息
# def pingServer(server):
#     result=os.system('ping '+server+' -c 2')
#     if result:
#         print('服务器%s ping fail' % server)
#     else:
#         print('服务器%s ping ok' % server)
#     print(result)
#
# # 把程序输出定位到/dev/null,否则会在程序运行时会在标准输出中显示命令的运行信息
# def pingServerCall(server):
#     fnull = open(os.devnull, 'w')
#     result = subprocess.call('ping '+server+' -c 2', shell = True, stdout = fnull, stderr = fnull)
#     if result:
#         print('服务器%s ping fail' % server)
#     else:
#         print('服务器%s ping ok' % server)
#     fnull.close()

# 用于检测程序是否正常
def check_aliveness(ip, port):
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.settimeout(1)
    try:
        sk.connect((ip,port))
        print('server %s service %d is connect!' %(ip,port))
        return True
    except Exception:
        print('server %s service %d is not connect!' %(ip,port))
        return False
    finally:
        sk.close()
    return False

if __name__=='__main__':
    # pingServerCall(server)
    # pingServer(server)

    check_aliveness('172.18.62.100', 6798)
    check_aliveness('172.18.62.100', 12798)


