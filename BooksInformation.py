import time
from FillChineseChar import Fill
from SystemWindow import View
from Books import Book
b = Book()
v = View()
class Books:
    books = b.book_read()
class  TouristCheckBooks(Books) :
    def tourist_checkBooks(self):
        '''
            游客查询书籍函数
            可以查询到已有的所有书籍，查询完毕则返回选择界面
            :return:
            '''
        f = Fill()
        print('===========================================')
        print('书名'.ljust(8) + '价格'.ljust(8) + '类别'.ljust(8) + '编号'.ljust(8) + '数量'.ljust(8))
        print('===========================================')
        for book1 in self.books:
            print(book1[0].ljust(10 - f.fill(book1[0])) + book1[1].ljust(10)
                  + book1[2].ljust(10 - f.fill(book1[2])) + book1[3].ljust(10) + book1[4].ljust(10))
            print('===========================================')
        print('已显示所有书籍，如果要进行其他操作请联系管理员！')
        print('正在返回注册/登录界面，请稍后...'.center(50,'-'))
        time.sleep(2)

class CheckBooks(Books):
    def check_books(self):
        '''
            查询所有书籍函数
            可以查询到已有的所有书籍，查询完毕则返回选择界面
            :return:
            '''
        f = Fill()
        print('===========================================')
        print('书名'.ljust(8) + '价格'.ljust(8) + '类别'.ljust(8) + '编号'.ljust(8) + '数量'.ljust(8))
        print('===========================================')
        for book2 in self.books:
            print(book2[0].ljust(10-f.fill(book2[0])) + book2[1].ljust(10)
                  + book2[2].ljust(10-f.fill(book2[2])) + book2[3].ljust(10) + book2[4].ljust(10))
            print('===========================================')
        v.printChangeChoicer()
        while True:
            change_choice = input('>> :')
            if change_choice.isdigit():
                if change_choice == '1' :
                    print('正在返回图书管理界面，请稍后.......'.center(50,'-'))
                    time.sleep(2)
                    return
                else:
                    print('指令输入错误，请按指令输入！')
            else:
                print('指令输入错误，输入必须为整型数字！')

class ChangeBooks(Books):
    def check_booksInformation(self):
        '''
            查询修改书籍是否存在函数
            此函数功能为：在修改之前需要判断书籍是否存在，如果存在则修改，如果不存在则重新输入
            :return:
            '''
        f = Fill()
        while True:
            print('===========================================')
            changeBookName1 = input('请输入你要修改信息的书籍的名称：')
            time.sleep(2)
            for book3 in self.books:
                if changeBookName1 in book3:
                    print('书名'.ljust(8) + '价格'.ljust(8) + '类别'.ljust(8) + '编号'.ljust(8) + '数量'.ljust(8))
                    print('===========================================')
                    print(book3[0].ljust(10 - f.fill(book3[0])) + book3[1].ljust(10)
                          + book3[2].ljust(10 - f.fill(book3[2])) + book3[3].ljust(10) + book3[4].ljust(10))
                    print('===========================================')
                    print('书籍名称存在,正在返回修改界面，请稍后....'.center(44,'-'))
                    time.sleep(2)
                    return book3
            else:
                print('书籍名称不存在，请重新输入书籍名称！')
    def change_booksName(self,books_list):
        '''
        修改书籍名称函数
        判断更改后的书籍名称是否是存在的，如果存在则重新输入，如果不存在则保存修改
        :param books_list: 书籍列表
        :return:
        '''
        while True:
            print('===========================================')
            changeBookName2 = input('请输入更改后的名称:')     #此处要判断书籍是否在系统中
            for book4 in self.books:
                if changeBookName2  in book4:
                    print('此书籍已经存在于系统中，请返回修改书籍界面重新输入')
                    break
            else:
                books_list[0] = changeBookName2
                print('恭喜你,书籍名称修改成功!')
            break
    def change_bookSprice(self,books_list):
        '''
            修改书籍价格函数
            对书籍价格进行修改
            :param books_list:书籍列表
            :return:
            '''
        while True:
            print('===========================================')
            bookSprice = input('请输入更改后的书籍价格:')
            if bookSprice.isdigit():
                books_list[1] = bookSprice
                print('恭喜你,书籍价格修改成功!')
                break
            else:
                print('输入错误！')
    def change_booksSort(self,books_list):
        '''
            修改书籍编号函数
            进行书籍编号的修改，根据需求可以选择要修改成为的书籍的类型
            :param books_list:书籍列表
            :return:
            '''
        while True:
            v.printChangeBooksSort()
            choice_sort = input('>> :')
            if choice_sort.isdigit():
                if choice_sort  ==  '1':
                    books_list[2] = '武侠类'
                elif choice_sort == '2':
                    books_list[2] = '文学类'
                elif choice_sort == '3':
                    books_list[2] = '百科类'
                elif choice_sort == '4':
                    books_list[2] = '哲学类'
                else:
                    print('输入错误，请按要求重新输入指令')
                    continue
                print('恭喜你,书籍类别修改成功!')
                break
            else:
                print('指令输入错误，输入必须为整型数字！')
    def change_booksNumber(self,books_list):
        '''
            修改书籍编号函数
            修改书籍的编号，目前对应编号只设计有1-100
            :param books_list:书籍列表
            :return:
            '''
        while True:
            print('===========================================')
            choice_number = input('请输入要选择的书籍类别编号[0000]--[9999]')
            if  choice_number.isdigit() and len(choice_number) == 4:
                books_list[3] = choice_number
            else:
                print('输入错误，请按要求重新输入类别编号!')
                continue
            print('恭喜你,书籍编号修改成功!')
            break
    def change_booksAmount(self,books_list):
        '''
        修改书籍数量函数
        对书籍的数量进行修改，
        :param books_list:书籍列表
        :return:
        '''
        while True:
            print('===========================================')
            choice_amount = input('请输入要修改成的书籍数量:')
            if choice_amount.isdigit():
                    books_list[4] = choice_amount
            else:
                print('输入错误，书籍数量必须为整型数字!')
                continue
            print('恭喜你,书籍数量修改成功!')
            break

    def change_books(self):
        '''
            修改书籍信息主函数
            包括（1-change_booksName(books_list)，2-change_bookSprice(books_list)，3-change_booksSort(books_list)，
            4-change_booksNumber(books_list)，5-change_booksAmount(books_list)，6-退出修改界面）
            查询要修改的书籍是否存在，不存在则重新输入，存在则打印此书籍并执行下层修改函数
            :return:
            '''
        self.books_list = self.check_booksInformation()
        while True:
            v.printChangeChoice()
            change_choice = input('>> :')
            if change_choice.isdigit():
                if change_choice  ==  '1':
                    self.change_booksName(self.books_list)
                elif change_choice == '2':
                    self.change_bookSprice(self.books_list)
                elif change_choice == '3':
                    self.change_booksSort(self.books_list)
                elif change_choice == '4':
                    self.change_booksNumber(self.books_list)
                elif change_choice == '5':
                    self.change_booksAmount(self.books_list)
                elif change_choice == '6':
                    b.book_write(self.books)
                    print('恭喜你,所有书籍信息保存成功,正在返回主修改界面，请稍后....'.center(40,'-'))
                    time.sleep(2)
                    break
                else:
                    print('输入不正确，请重新输入指令[1]--[6]')
            else:
                print('指令输入错误，输入必须为整型数字！')
class AddBooks(Books):
    def add_booksInformation(self):
        '''
        查询添加的书籍信息函数
        查询书籍是否已存在于系统中，如果存在要求修改，否则进行添加
        :return:
        '''
        f = Fill()
        while True:
            print('===========================================')
            addBookName = input('请输入你要添加的书籍名称：')
            for book5 in self.books:
                if addBookName in book5:
                    print('===========================================')
                    print('书名'.ljust(8) + '价格'.ljust(8) + '类别'.ljust(8) + '编号'.ljust(8) + '数量'.ljust(8))
                    print('===========================================')
                    print(book5[0].ljust(10 - f.fill(book5[0])) + book5[1].ljust(10)
                          + book5[2].ljust(10 - f.fill(book5[2])) + book5[3].ljust(10) + book5[4].ljust(10))
                    print('===========================================')
                    print('书籍名称存在，对书籍进行信息修改即可！')
                    print('正在返回修改书籍信息界面，请稍后....'.center(50,'-'))
                    time.sleep(2)
                    return True
            else:
                print('书籍名称不存在，可以进行书籍添加！')
                print('正在返回添加书籍信息界面，请稍后....'.center(50,'-'))
                time.sleep(2)
                return False
    def add_booksName(self,addBookList):
        '''
        添加书籍名称函数
        此函数的使用为：前面函数已判断此书籍不存在于系统中，直接按照名称添加即可
        :param addBookList:书籍列表
        :return:
        '''
        print('===========================================')
        addBookName = input('请再一次输入要添加的书籍的名称:')  # 此处要判断书籍是否在系统中
        addBookList[0] = addBookName
        print('恭喜你,书籍名称添加成功!')
    def add_bookSprice(self,addBookList):
        '''
        添加书籍价格函数
        对书籍价格进行添加
        :param addBookList:书籍列表
        :return:
        '''
        print('===========================================')
        addBookSprice = input('请输入本书的书籍价格:')
        if addBookSprice.isdigit():
            addBookList[1] = addBookSprice
        print('恭喜你,书籍价格添加成功!')
    def add_booksSort(self,addBookList):
        '''
        添加书籍编号函数
        进行书籍编号的添加，根据需求可以选择要添加成为的书籍的编号
        :param addBookList:书籍列表
        :return:
        '''
        while True:
            v.printAddBooksSort()
            choice_sort = input('>> :')
            if choice_sort.isdigit():
                if choice_sort  ==  '1':
                    addBookList[2] = '武侠类'
                elif choice_sort == '2':
                    addBookList[2] = '文学类'
                elif choice_sort == '3':
                    addBookList[2] = '百科类'
                elif choice_sort == '4':
                    addBookList[2] = '哲学类'
                else:
                    print('输入错误，请按要求重新输入编号指令')
                    continue
                print('恭喜你,书籍类别添加成功!')
                time.sleep(2)
                break
            else:
                print('指令输入错误，输入必须为整型数字！')
    def add_booksNumber(self,addBookList):
        '''
        添加书籍编号函数
        添加书籍的编号，目前对应编号
        :param addBookList:书籍列表
        :return:
        '''
        while True:
            print('===========================================')
            addChoiceNumber = input('请输入要添加的书籍类别编号[0000]--[9999]')
            if addChoiceNumber.isdigit() and len(addChoiceNumber) == 4:
                for i in self.books:
                    if addChoiceNumber in i:
                        print('编号已经存在，请重新输入')
                        break
                else:
                    addBookList[3] = addChoiceNumber
            else:
                print('指令输入错误，输入必须为整型数字！')
                continue
            print('恭喜你,书籍编号添加成功!')
            time.sleep(2)
            break
    def add_booksAmount(self,addBookList):
        '''
        添加书籍数量函数
        对书籍的数量进行添加，
        :param addBookList:书籍列表
        :return:
        '''
        while True:
            print('===========================================')
            addChoiceAmount = input('请输入本书要添加的书籍数量')
            if addChoiceAmount.isdigit():
                addBookList[4] = addChoiceAmount
            else:
                print('输入错误，请按要求重新输入书籍数量!')
                continue
            print('恭喜你,书籍数量添加成功!')
            time.sleep(2)
            break
    def add_books(self):
        '''
        添加书籍主函数
        添加图书管理系统没有的书籍（新增书籍）
        如果书籍存在则书籍不能添加，要求返回修改界面进行修改，如果不存在则为可添加书籍
        包括（1-add_booksName(addBookList)，2-add_bookSprice(addBookList)，3-add_booksSort(addBookList)
        4-add_booksNumber(addBookList)，5-add_booksAmount(addBookList)，6-退出添加界面）
        :return:
        '''
        addBookList = ['0','0','0','0','0']
        flag = self.add_booksInformation()
        if  flag == True:
            c4 = ChangeBooks()
            c4.change_books()
        elif flag ==False:
            while True:
                v.printAddBooks()
                add_choice = input('>> :')
                if add_choice.isdigit():
                    if add_choice  ==  '1':
                        self.add_booksName(addBookList)
                    elif add_choice == '2':
                        self.add_bookSprice(addBookList)
                    elif add_choice == '3':
                        self.add_booksSort(addBookList)
                    elif add_choice == '4':
                        self.add_booksNumber(addBookList)
                    elif add_choice == '5':
                        self.add_booksAmount(addBookList)
                    elif add_choice == '6':
                        print('恭喜你,书籍已添加成功,正在返回主选择界面，请稍后....'.center(44,'-'))
                        time.sleep(2)
                        break
                    else:
                        print('输入不正确，请重新输入指令[1]--[6]')
                        continue
                else:
                    print('指令输入错误，输入必须为整型数字！')
            self.books.append(addBookList)
            b.book_write(self.books)
class DleBooks(Books):
    def del_books(self):
        '''
        删除书籍函数--最后返回主选择界面
        先按照书籍名称查询，如果书籍已在系统中，则直接删除书籍即可，
        如果不在系统中则需要重新输入
        :return:
        '''
        f = Fill()
        while True:
            print('===========================================')
            deleteBookName = input('请输入你要删除的书籍的名称:')
            for book6 in self.books:
                if deleteBookName in book6:
                    print('书名'.ljust(8) + '价格'.ljust(8) + '类别'.ljust(8) + '编号'.ljust(8) + '数量'.ljust(8))
                    print('===========================================')
                    print(book6[0].ljust(10 - f.fill(book6[0])) + book6[1].ljust(10)
                          + book6[2].ljust(10 - f.fill(book6[2])) + book6[3].ljust(10) + book6[4].ljust(10))
                    print('===========================================')
                    while True:
                        v.printDelBooks()
                        chioceDelBook = input('>> :')
                        if chioceDelBook.isdigit():
                            if chioceDelBook == '1':
                                self.books.remove(book6)
                                b.book_write(self.books)
                                print('恭喜你，书籍已删除成功，正在返回主选择界面，请稍后...'.center(44,'-'))
                                time.sleep(2)
                                return
                            elif chioceDelBook == '2':
                                print('你已放弃删除操作，书籍保持不变，正在返回主选择界面，请稍后...'.center(40,'-'))
                                time.sleep(2)
                                return
                            else:
                                print('指令输入错误，输入必须为整型数字！')
                        else:
                            print('指令输入错误，输入必须为整型数字！')
            else:
                print('书籍名称不存在，请重新输入要删除的书籍名称')