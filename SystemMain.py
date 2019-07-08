import  time
from SystemWindow import View
from UserInformation import Adminr,ChangeUser
from BooksInformation import CheckBooks,ChangeBooks,AddBooks,DleBooks

while True:
    view = View()
    view.printView()
    time.sleep(2)
    a1 = Adminr()
    a1.logging()
    def main():
        while True:
            view.printMain()
            select = input('>> :')
            if select.isdigit():
                if select == '1':
                    c1 = CheckBooks()
                    c1.check_books()
                elif select == '2':
                    c2 = ChangeBooks()
                    c2.change_books()
                elif select == '3':
                    a2 = AddBooks()
                    a2.add_books()
                elif select == '4':
                    d = DleBooks()
                    d.del_books()
                elif select == '5':
                    c3 = ChangeUser()
                    c3.change_user()
                elif select == '6':
                    print('成功退出选择界面，正在返回主窗口，请稍后...'.center(44,'-'))
                    break
                else:
                    print('指令输入错误，输入必须为整型数字[1]--[6]')
            else:
                print('指令输入错误，输入必须为整型数字！')
    main()

    if __name__ == '__main__':
        print('this is system windows!')
