import re

def upper(args):
    """每個字的開頭變大寫"""
    for i in range(len(args)):
        args[i] = args[i].title()

def count(my_input, dic):

    """處理輸入"""
    my_input = ("Republican presidential rivals Donald Trump and Ron "
             "DeSantis hold competing events in the early nominating "
        "state of Iowa on Saturday Saturday Saturday Saturday.")
    args = my_input.split(" ")

    """ *************** """
    """ 數每個單字出現次數 """
    """ *************** """

    """去掉標點符號"""
    for i in range(len(args)):
        args[i] = re.sub('[!-.]', '', args[i])

    """去掉重複字串(set的特性:不會儲存相同的字串)"""
    my_set = list(set(args))

    """利用set走訪輸入並記錄字串出現次數"""
    for i in range(len(my_set)):
        if my_set[i] in args:
            dic[my_set[i]] = args.count(my_set[i])

    print(dict(sorted(dic.items(),key=lambda x:x[0].title())))


my_dic = {}
my_input = ""

count(my_input, my_dic)