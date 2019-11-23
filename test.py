# A = []
# import string
# S = "123a"
# # S = string.atoi(S,base = 10)
#
# # print(float(".98"))
#
#
# # a = "1234567"
# # print(a[-1])
# #
# #
# # a = 964176192
# #
# #
# # a = bin(a)
# # a = a[2:]
# # s = a[::-1]
# # print(int(s, 2))
#
# # dic = {1:2, 2:3, 3:4}
# # print(dic.get(1), max(dic.values()))
#
# # list = [1, 2, 3]
# # print(list.pop())
#
#
# #-*-coding:utf-8-*-
# def split_new(stringstr, charstr):
#     """
#     :param stringstr: 要分割的串
#     :param charstr: 按该串分割
#     :return: 返回分割后的list
#     """
#     #stringstr = stringstr
#     tempstr = []
#     lengstring = len(stringstr)#计算串的长度
#     lengchar = len(charstr)#计算分割符的长度
#     for i in range(lengstring):
#         index = stringstr.find(charstr)#找到第一个出现charstr的坐标，如果没有找到，find返回-1
#         if index == -1:
#             tempstr.append(stringstr)
#             return tempstr
#         else:
#             tempstr.append(stringstr[:index])#取第一次出现charstr(不包含charstr)的前面部分
#             stringstr = stringstr[index+lengchar:]#把第一次出现charstr(不包含charstr)的 后面部分 重新赋值给stringstr
#
# if __name__=="__main__":
#     print (split_new(" ", "A"))


# i = 0
# # flag = 1
# # while True:
# #     i += flag
# #     if i == 100:
# #         flag = -1
# #     if i == -100:
# #         flag = 1

# from sys import maxsize
# print(maxsize)

# def f1(lIn):
#     l1 = sorted(lIn)
#     l2 = [i for i in l1 if i<0.5]
#     return [i*i for i in l2]
#
# def f2(lIn):
#     l1 = [i for i in lIn if i<0.5]
#     l2 = sorted(l1)
#     return [i*i for i in l2]
#
#
# def f3(lIn):
#     l1 = [i*i for i in lIn]
#     l2 = sorted(l1)
#     return [i for i in l1 if i<(0.5*0.5)]
#
# import random
# import cProfile
# lIn = [random.random() for i in range(100000)]
# cProfile.run('f1(lIn)')
# cProfile.run('f3(lIn)')
# cProfile.run('f2(lIn)')

# import sys
# print(sys.getrefcount(object))
#
#
# class AAB(object):
#     name = 'a'
#
#
# print(hasattr(AAB, '__init__'))
# print(getattr(AAB, "__init__"))
# print(setattr(AAB, 'setoutside', 'thisisoutside'))
# print(AAB.setoutside)


# def jiecheng(n):
#     res = 1
#     for i in range(1, n+1):
#         res *= res
#     return res
#
#
# from functools import reduce
# def jiecheng2(n):
#     return reduce(lambda x,y:x*y, range(1, n+1))
#
# import random
# import cProfile
# n = 100000
# cProfile.run('jiecheng(n)')
# cProfile.run('jiecheng2(n)')

# f = lambda x, y: x+y
# print(f(2017, 2018))
#
# class Base:
#     a = 1
#     b = 2
#     print('class defined')
#
#     def __new__(cls, *args, **kwargs):
#         print(cls.__name__, 'class instance created')
#         print(cls)
#         return super().__new__(cls)
#
#     def __init__(self):
#         print(type(self).__name__, 'class instance inited')
#         print(type(self))
#
#     def hello(self):
#         pass
#
#
# b = Base()

# class Meta(type):
#     def __new__(meta, *args, **kwargs):
#         clsname, bases, namespace = args
#         print(clsname, 'class created')
#         return super().__new__(meta, *args)
#
#     def __init__(cls, *args, **kwargs):
#         print(cls.__name__, 'class inited')
#         super().__init__(*args)
#
#     @classmethod
#     def __prepare__(meta, name, bases):
#         print(name, 'class namespace created')
#         return {}
#
#
# class Base(metaclass=Meta):
#     a = 1
#     b = 2
#
#     def __new__(cls, *args, **kwargs):
#         print(cls.__name__, 'class instance created')
#         return super().__new__(cls)
#
#     def __init__(self, *args, **kwargs):
#         print(type(self).__name__, 'class instance inited')
#
#     def hello(self):
#         pass
#
#
# b = Base('4')
# print(type(Base))
#
# import time
# from functools import wraps
#
#
# def timethis(func):
#     # 定义一个装饰器函数，函数返回执行时间
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(func.__name__, end-start)
#         return result
#     return wrapper
#
#
# # @timethis
# # def countdown(n):
# #     while n > 0:
# #         n -= 1
#
# def countdown(n):
#     while n > 0:
#         n -= 1
#
#
# countdown = timethis(countdown)
#
#
# countdown(100000)


# print([[x for x in range(1, 101)][i:i+3] for i in range(0, 100, 3)])

# def createGenerator():
#     mylist = range(3)
#     for i in mylist:
#         print('bianchengpingfang')
#         yield i*i
#
# myGenerator = createGenerator()
# print(myGenerator)
# for i in myGenerator:
#     print(i)

# class Person:
#     def __init__(self, x):
#         self.__age = x
#
#     def age(self):
#         return self.__age
#
#
# t = Person(22)
# # 虽然是只读，但是还是可以访问到
# t.__init__(100)
# print(t.age())

# class MyCls(object):
#     __weight = 50
#
#     # 以访问属性的方式来访问weight方法
#     @property
#     def weight(self):
#         return self.__weight
#
#
# if __name__ == '__main__':
#     obj = MyCls()
#     print(obj.weight)
#     obj.__weight = 12
#
#     print(obj.weight)
#     print(dir(obj))
#     # 其实还是可以访问到的，这就僵硬了
#     obj._MyCls__weight = 12
#     print(obj.weight)

# ans = ['a','b','c']
# print(''.join(ans))
# res = 1
# for i in range(1, 10):
#     res *= i
#
# print(res)


# for index num in enumerate
# print(100+300)
# print(eval('100+300'))

# compile 是 exec 和 eval的低级版本.
# 它不执行或者评估你的语句或者表达式，但返回可以执行它的代码对象。 模式如下：
#
# compile(string,'','eval') 返回将要执行的代码对象，如果你完成了 eval(string) 。
# 请注意，在这里模式下，只有用你不能使用语句( 单) 表达式是否有效。
# compile(string,'','exec') 返回将要执行的代码对象，如果你完成了 exec(string) 。
# 你可以在这里使用任意数量的语句。
# compile(string,'','single') 类似于 exec 模式，但它将忽略除第一个语句之外的所有内容。
# 注意，带有结果的if/else 语句被认为是单个语句。
#
#
# exec用于语句，但不返回任何内容。 eval用于表达式并返回表达式值。
# eval参数返回要执行的代码对象，single参数但它将忽略除第一个语句之外的所有内容。
# 注意，带有结果的if/else 语句被认为是单个语句
# eval_code = compile('100+200', '', 'eval')
# print(eval(eval_code))
#
# exec('5')




def com1(a, b):
    lens = len(a)
    tip = [0]*lens
    for i in range(len(b)):
        for j in range(lens):
            if b[i] in a:
                tip[j] += 1

    l_tag = 0
    for i in range(lens):
        if tip[i] > 0:
            l_tag += 1
        else:
            break

    r_tag = lens-1
    for i in range(lens):
        if tip[lens-1] > 0:
            r_tag -= 1
        else:
            break

    if r_tag == l_tag:
        return 0
    else:
        for i in range(l_tag, r_tag+1):
            if tip[i] == 0:
                return 0
    return 1


# def merge_search(li, item):
#     # 获取li的开始 结束
#     start = 0
#     end = len(li) - 1
#
#     # 只要start和end 还没错开 就一直找
#     while start <= end:
#         # 通过计算获取当前查找范围的中间位置
#         mid = (start + end) // 2
#         # 如果中间数就是item则返回True
#         if li[mid] == item:
#             return mid
#         # 如果mid比item大，说明item可能会出现在mid左边，对左边再查找
#         elif li[mid] > item:
#             end = mid - 1
#         # mid 比item小，说明item有可能在mid右边，对右边再查找
#         else:
#             start = mid + 1
#     # 跳出循环说明没找到 返回错误
#     return -1


if __name__ == '__main__':
    print(com1('baiyiisgreat', "yibai"))
