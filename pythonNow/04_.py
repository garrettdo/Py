print('\n'.join([''.join([('Love'[(x-y)%4]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y in range(15,-15,-1)]))

f1 = open('db','r')
data = f1.read()
f1.close()

# 1.格式化数据

user_info_list = []
user_str_list = data.split('\n')
for item in user_str_list:
    temp = item.split('|')
    v = {
        'name': temp[0],
        'pwd': temp[1],
        'times': int(temp[2])
    }
    user_info_list.append(v)
print(user_info_list)

user_login= []
flag = True
exit_flag = 3

while flag:
    username = input('请输入账号：')
    for item  in user_info_list:
        if  username == item['name']:
            if int(item['times']) < exit_flag:
                password = input('请输入密码:')
                if password == item['pwd']:
                    print('欢迎登陆！')
                    item['times'] = 0
                    flag = False
                    user_login = item
                    break
                else:
                    print('账号或密码错误，请重新输入')
                    item['times'] = int(item['times']) + 1
                    break
            else:
                print('账号已经锁定。')
                exit()
        else:
            print('账号不存在，请重新输入')
            break