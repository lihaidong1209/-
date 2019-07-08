import sys
from SystemWindow import View
v = View()
class Fill:
    def fill(self,chinese):
        '''
        中文字符长度判断函数
        判断中文字符的数量并返回长度
        :param chinese:
        :return:
            '''
        n = 0
        for i in str(chinese):
            if self.ischinese(i):
                n += 1
        return n
    def ischinese(self,word):
        '''
            判断是否是中文函数
            :param word:
            :return:
            '''
        if '\u4e00' <= word <= '\u9fff':
            return True
        return False
class Exit:
    def exiting(self):
        '''
        退出系统函数
        此函数结束所有登录操作，可实现用户信息保密
        :return:
        '''
        v.printLogOut()
        sys.exit()