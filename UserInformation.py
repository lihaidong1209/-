import time
from SystemWindow import View
from BooksInformation import TouristCheckBooks
from FillChineseChar import Exit
from Users import User
u = User()
v = View()
class Tourist:
    def tourist(self):
        '''
        游客登录函数
        不需要验证，只有查询书籍功能
        :return:
         '''
        print('你是游客身份，只有查看数据信息资格！')
class Adminr(Tourist):
    def __init__(self):
        self.old_user = u.user_read()
    def register(self):
        '''
            用户注册函数
            判断注册的用户名是否存在，
            存在则重新输入新的用户名，不存在则用户名可以使用并进行输入密码操作
            :return:
            '''
        while True:
            while True:
                v.printRegister()
                chioceRegister = input('>> :')
                if chioceRegister.isdigit():
                    if chioceRegister == '1':
                        regist_name = input('开始注册，请输入要注册的用户名:')
                        if regist_name in self.old_user:
                            print('此用户名已存在，请重新选择操作指令！')
                        else:
                            regist_pwd = input('此用户名可用,请输入注册用户名密码:')
                            u.user_write('\r'+regist_name + ' '+ regist_pwd)
                            self.old_user.update({regist_name:regist_pwd})
                            print('恭喜你，新用户名注册成功啦！')
                            print('正在返回图书管理系统窗口登录界面，请稍等.....'.center(44,'-'))
                            time.sleep(2)
                            break
                    elif chioceRegister == '2':
                        print('放弃注册，返回注册/登录界面！'.center(44,'-'))
                        break
                    else:
                        print('输入错误，请重新选择操作指令！')
                        continue
                else:
                    print('指令输入错误，输入必须为整型数字！')
                    continue
            break
    def loginer(self):
        '''
            用户登录函数
            判断输入的用户名是否存在，不存在则重新输入，存在则输入密码
            :return:
            '''
        while True:
            while True:
                v.printLoginer()
                chioceLoginer = input('>> :')
                if chioceLoginer.isdigit():
                    if chioceLoginer == '1':
                        while True:
                            name = input('请输入你的用户名（name）:')
                            if name in self.old_user:
                                pwd = input('此用户名可以使用,请输入你的密码（pwd）:')
                                if pwd == self.old_user[name]:
                                    print('密码正确,恭喜你登录成功！')
                                    print('正在进入图书管理系统，请稍等.....'.center(44,'-'))
                                    time.sleep(2)
                                    return True
                                else:
                                    print('密码输入错误，返回选择界面重新选择!'.center(44,'-'))
                                    break
                            else:
                                print('此用户名不存在，请重新选择操作指令')
                                v.printChioceLoginersr()
                                chioceLoginers = input('>> :')
                                if chioceLoginers.isdigit():
                                    if chioceLoginers == '1' :
                                        continue
                                    elif chioceLoginers == '2' :
                                        print('放弃登录，正在返回注册/登录界面，请稍后..'.center(44,'-'))
                                        return
                                    else:
                                        print('输入错误，请重新输入！')
                                        break
                                else:
                                    print('输入错误，请重新输入！')
                                    break
                    elif chioceLoginer == '2':
                        print('放弃登录，正在返回注册/登录界面，请稍后...'.center(44,'-'))
                        time.sleep(2)
                        return False
                    else:
                        print('输入错误，请重新选择操作指令！')
                        continue
                else:
                    print('指令输入错误，输入必须为整型数字！！')
    def logging(self):
        '''
        登录注册主函数
        进行选择注册或者登录或者游客进入
        :return:
        '''
        while True:
            v.printLogging()
            choiceLogging = input('>> :')
            if choiceLogging.isdigit():
                if choiceLogging == '1':
                    self.register()
                elif choiceLogging == '2':
                    flag1 = self.loginer()
                    if flag1 == True:
                        break
                    else:
                        continue
                elif choiceLogging == '3':
                    self.tourist()
                    t = TouristCheckBooks()
                    t.tourist_checkBooks()
                elif choiceLogging == '4':
                    e = Exit()
                    e.exiting()
                else:
                    print('指令不正确，请按照要求输入正确的指令！')
            else:
                print('指令输入错误，输入必须为整型数字！')

class ChangeUser(Adminr):
    def change_userName(self):
        '''
        修改用户名函数
        对用户名信息进行修改（先判断要修改的用户名是否存在，如果存在则进行修改，如果不存在则重新输入）
        此处注意：字典的键不能修改，所以先将键取出保存，然后删掉值（也就是删除了键值对），
                  然后将键入的新的键和保存下来的值重新添加到字典中完成用户名的修改
        :return:
        '''
        while True:
            print('===========================================')
            changeName1 = input('请输入旧用户名（old_user）:')
            for name1 in self.old_user:
                if changeName1 ==  name1:
                    name1_pwd = self.old_user.get(name1)
                    self.old_user.pop(name1)
                    newName2 = input('旧用户名输入正确，请输入新用户名（new_user）:')
                    self.old_user[newName2] = name1_pwd
                    u.user_writedict(self.old_user)
                    print('恭喜你，用户名修改成功！')
                    break
            else:
                print('用户名不存在，请重新输入用户名!')
            break
    def change_userPassword(self):
        '''
        修改用户密码函数
        先输入用户名和密码进行判断（如果密码和用户名匹配，则对密码进行修改没否则重新输入）
        :return:
        '''
        while True:
            print('===========================================')
            changeName2 = input('请输入旧用户名（old_userName）:')
            changePwd2 = input('请输入旧密码（old_userPwd）:')
            for name2 in self.old_user:
                if changeName2 == name2 and changePwd2 == self.old_user[name2]:
                    print('用户名和密码正确')
                    newPwd = input('旧用户名和密码输入正确，请输入新密码:')
                    self.old_user[name2] = newPwd
                    u.user_writedict(self.old_user)
                    print('恭喜你，密码修改成功！')
                    break
            else:
                print('用户名或密码输入错误，请重新输入用户名和密码（old_user））:')
            break
    def change_user(self):
        '''
        修改用户信息函数
        2.然后对密码进行修改，先判断密码是否正确，正确则更改（需要与原密码不同），如果错误则重新输入）
        :return:
        '''
        while True:
            v.printChangeUser()
            chioceChangeUser = input('>>:')
            if chioceChangeUser.isdigit():
                if chioceChangeUser  ==  '1':
                    self.change_userName()
                elif chioceChangeUser == '2':
                    self.change_userPassword()
                elif chioceChangeUser == '3':
                    print('用户信息修改完成，返回主选择界面！'.center(44,'-'))
                    break
                else:
                    print('输入不正确，请重新输入！')
            else:
                print('指令输入错误，输入必须为整型数字！')