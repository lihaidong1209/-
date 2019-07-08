
class Book:
    def book_read(self):
        '''
        书籍读取函数
        对所有文本书籍进行读入
        :return:
        '''
        list1 = []
        bookInfor = open('Books.txt', 'r+', encoding='utf-8')
        book = bookInfor.readlines()
        n = 1
        for i in book:
            if n < len(i):
                i = i[0:len(i)-1]
            i = i.split(',')
            list1.append(i)
        n += 1
        for i in list1:
            print(i)
        return list1

    def book_write(self,s):
        '''
        书籍写入函数
        将书籍写入对应的文本保存，包括更改，删除，增加等，覆盖
        :param s: 接受书籍列表，二维列表
        :return:
        '''
        del s[0]
        bookInfor = open('Books.txt', 'w', encoding='utf-8')
        bookInfor.writelines(['哈利波特'+',', '100'+',','科幻类' + ',', '0000'+',','100'])
        for i in s:
            bookInfor.write('\r'+i[0]+',')
            bookInfor.write(i[1]+',')
            bookInfor.write(i[2]+',')
            bookInfor.write(i[3]+',')
            bookInfor.write(i[4])
        bookInfor.close()
