class User:
    def user_read(self):
        '''
        读取用户信息函数
        将文本中的用户信息全部读入系统
        :return:
        '''
        dict1 ={'李海东':'000000'}
        userInfor = open('Users.txt', 'r+', encoding='utf-8')
        user_pwd = userInfor.readlines()
        n = 1
        for i in user_pwd :
            if n < len(user_pwd):
                i = i[0:len(i)-1]  #字符串切片
            i = i.split(' ')
            dict1.setdefault(i[0],i[1])
            n += 1
        print('当前可用账户与密码共有{}对，具体如下:'.format(len(dict1)))
        print(dict1)
        return  dict1

    def user_write(self,s):
        '''
        用户注册写入函数
        将用户新注册的信息写入文本，追加写入
        :param s: 接受到新用户名和密码
        :return:
        '''
        userInfor = open('Users.txt', 'a+', encoding='utf-8')
        userInfor.write(s)
        userInfor.flush()
        return
    def user_writedict(self,s):
        '''
        写入用户信息修改函数
        将用户修改后的信息写入文本，覆盖
        :param s:  用户字典，所有用户信息
        :return:
        '''
        userInfor = open('Users.txt', 'w', encoding='utf-8')
        userInfor.write('李海东'+' '+'000000')
        for i in s.items():
            userInfor.write('\r'+i[0]+' '+i[1])
        userInfor.flush()
        return



