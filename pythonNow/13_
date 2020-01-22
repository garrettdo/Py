# tomcat健康检查失败自行重启

import os
import urllib
import commands
import time
import socket

# 定义时间变量
date_now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
# 定义启动脚本路径
StartTomcat = "/home/tomcat/bin/startup.sh"
# 定义测试URL
WebUrl = "http://127.0.0.1:8080/kafka/"
# 获取进程ID，里面多了个grep -V check_tomcat，是因为脚本名里面有tomcat关键字，会多检测出一个进程出来，要排除掉。
process_id = commands.getoutput("ps -ef|grep tomcat |grep -v check_tomcat|grep -v grep|awk '{print $2}'")

# 设置URL超时时间
socket.setdefaulttimeout(5)

def tart_tomcat(pid):  # 定义重启方法
    pid = int(pid)
    try:
        print (date_now, "reboot-tomcat:")
        os.kill(pid, 9)
        time.sleep(5)
        print ("开始执行startup.sh")
        os.system(StartTomcat)
    except (ValueError,IOError) as err:
    # except IOError, e:
        print (err)

# def check_tomcat():  # 定义检查tomcat方法
#     print ("----------------------------")
#     print (date_now, "开始检查 tomcat...")
#     if process_id:  # 如果存在进程ID则往下执行
#         print ("进程已存在，检测url是否能访问...")
#             # 判断是否返回200，另外有可能有其他报错，所以这里用try来写，防止有别的错误。
#             try:
#             response_code = urllib.urlopen(WebUrl).getcode()
#             if response_code == 200:
#                 print ("URL访问正常无需重启tomcat...")
#             else:
#                 restart_tomcat(process_id)
#         # except IOError:
#         except (ValueError, IOError) as err:
#
#             restart_tomcat(process_id)
#     else:
#         print ("进程不存在,开始执行startup.sh")
#         os.system(StartTomcat)
#
# check_tomcat()
