#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Mr.ZhangJc
# def send(text,subject,xx):
#     print("邮件内容为：",text,subject)
#     return True
# while True:
#     em=input("请输入邮件人姓名：")
#     result = send(em,'SB',"OK!")
#     if result == True:
#         print("发送成功！")
#     else:
#         print("发送失败！")

# s="I am {0},I am from {1}".format("zjc","shandong")
# print(s)
#
# def f1(a1,a2):
#     return a1+a2
#
# def f1(a1,a2):
#     return a1*a2
#
# ret = f1(8,8)
# print
#
# def f1(li):
#     li.append(111)
# li=[11,22,33,44]
# f1(li)
# print(li)

# #登录
# def login(username, password):
#     f=open("db",'r')
#     for line in f:
#         line_list=line.strip().split("|")
#         if line_list[0] == username and line_list[1] == password:
#             return True
#     return False
#
#
# def register():
#     pass
#
#
# def main():
#     t = input("1:登录;2:注册")
#     if t=="1":
#         user = input("请输入用户名：")
#         pwd = input("请输入密码：")
#         r=login(user,pwd)
#         if r:
#             print("登陆成功！")
#         else:
#             print("登陆失败！")
#     elif t=="2":
#         print("注册")
#
# main()

# def f1(a1):
#     return a1+100
# ret = f1(10)
# print(ret)
#
# f2 = lambda a1:a1*a1
#
# r2=f2(3)
# print("结果为：",r2)


#
# print(bin(5))  #二进制
# print(oct(8))  #八进制
# print(hex(19)) #十六进制


# print(bool(1))


# 字符串转换字节类型
#
# s = "张建超"
# n = bytes(s,encoding="utf-8")
# print(n)

#
# #文件操作
# f = open('db','r') #只读
# f = open('db','w') # 只写，先清空源文件
# f = open('db','a') #追加
# f = open('db','x') #如果这个文件存在，报错。不存在，创建并只写

# f = open('db', 'r+', encoding="utf-8") # b 代表字节方式。如果打开模式无b，则read按字符读取。
# data = f.read() # read() 雾草朱，读全部；有参数，有 b，按字节；无 b， 按字符。
# print(data)
# f.seek(1)   #开始的位置
# f.write("xw|333") # write 写数据，b 字节；无 b ，字符。
# print(f.tell()) #定位当前指针的位置（字节）
# print(data)
# f.close()


# #强制刷入
# f = open("db", 'a', encoding="utf-8")
# print(f)
# f.write("123")
# f.flush()
# input("adssafsadf")
# #print(f)

# truncate 截断，指针为后的清空
# f.seek(3)
# f.truncate() 字符3的位置开始截断。
#
# with open('db', 'r', encoding="utf-8") as f1, open('db2', 'w', encoding="utf-8") as f2:
#     for line in f1:
#         f2.write(line)
#     print(f2)

# 随机生成字母
# import random
# i = random.randrange(65,91)
# c = chr(i)
# print(c)
# print(i)

# import random
# li = []
# for i in range(6):
#     temp = random.randrange(65,91)
#     c = chr(temp)
#     # li.append(c)
#     print(li)
# result = "".join(li)
# print(result)


# import keyword
# a = keyword.kwlist
# print(a)


# input("\n\n按下Enter 键后退出。")

# 不换行输出
# x = 'a'
# y = 'b'
# print(x , end=" ")
# print(y , end=" ")
# print()

# import sys
# print('命令行参数为：')
# for i in sys.argv:
#     print(i)
# print('\n python 路径为',sys.path)
#
# from sys import argv,path
# print('path:',path)


# 有误！！！
# import os
# count = os.system("grep '123' db| wc -l'")
# print(count)
# if ["$count" == 0]:
#     print("0")
# elif ["$count" > 5]:
#     print("$count")
# else:
#     print("0")


# print("hello world!")

# num = input("请输入一个幸运数字：")
# guess = int(num)
# if guess == 8:
#     print("you are very nice!")
# else:
#     print("you are wrong!")


# name = input("请输入你的名字：")
# print("welcome " + name)
#
# print('Let\'s go')
# str = """
# 你好啊!
# 宁静的夏天...
# """
# print(str)


# import random
# secret = random.randint(1 ,10)
# print(secret)

#
# a = 5
# b = a ** 2
# print(b)

#
# list = ['zhang','jian','chao']
# for i in list:
#     print(i,len(i))

# a = range(5)
# for i in a:
#     print(i)


#
# for i in range(10):
#     if i%2 != 0:
#         print(i)
#         continue


# 列表
# num = ["小甲鱼:nihao",'黑夜']
# for i in num:
#     print(i)
# num.extend(['北京欢迎您！'])
# print(num)
# num.insert(1,'牡丹')
# num.remove('黑夜')
# print(num)
# del num[0]
# print(num)

# 元组
#
# print('a',end=' ')
# print('b',end=' ')
# print('c')


# a = '%c %c %c ' % (97,98,99)
# print(a)

# a
# i = 5
# print('value is',i)
# print('I repeat, the value is', i)


# daxiao
#
# def fun(a,b):
#     if a>b:
#         print("big num is ",a)
#     elif a<b:
#         print("small num is ",a)
#     else:
#         print("end")
#
# a = input("A 的值为：")
# b = input("B 的值为：")
# fun(a,b)


#
# def fun(x,y):
#     '''
#     :param x: this is part1
#     :param y: this is part2
#     :return:
#     '''
#     x = int(x)
#     y = int(y)
#     if x>y:
#         print("最大值为：",x)
#     else:
#         print("最大值为：",y)
# fun(3,5)
# print(fun.__doc__)


# 通过函数来获取文档
# def print_max(x, y):
#     '''Prints the maximum of two numbers.打印两个数值中的最大数。
#     The two values must be integers.这两个数都应该是整数'''
#     # 如果可能，将其转换至整数类型
#     x = int(x)
#     y = int(y)
#     if x > y:
#         print(x, 'is maximum')
#     else:
#         print(y, 'is maximum')
# print_max(3, 5)
# print(print_max.__doc__)


# 函数参数及路径打印
# import sys,os
# print("The command line arguments are:")
# for i in sys.argv:
#     print(i)
# print('\n\nThe PYTHONPATH is',sys.path,'\n')
# print(os.getcwd())
#

# 模块引用方法一
# import if_else
# if_else.say_hi()
# print('Auth By:',if_else._auth_)
#
# #模块引用方法二
# from if_else import say_hi,_auth_
# say_hi()
# print('Auth By',_auth_)


# 列表
# list = ['zhang','jian','chao']
# print('my name is so lang:',len(list))
# # print('These item are:',end=' ')
# print('These item are:',end=' ')
# for item in list:
#     print(item,end=' ')
# list.sort()
# print('\nnew list is:',list)

#
# #元组
# list=('zhang','jian','chao')
# print('old list is:',list)
# new_list='welcome',list
# print('new list is:',new_list)


# #字典
# email={
#     'zhangjianchao':'zhangjianchao@linkcircle.cn',
#     'xuyunfei':'xuyunfei@linkcircle.cn'
# }
# print("xuyunfei's email is:",email['xuyunfei'])
# print('There are {} contacts in the email\n'.format(len(email)))
# for name,email_address in email.items():
#     print('name {} email is {}'.format(name,email_address))
#
# email['baifan'] = 'baifan@linkcircle.cn'
# print(email["baifan"])
# del email['zhangjianchao']
# print(email.items())


# #集合
# print('Simple Assignment')
# shoplist = ['zhang','jian','chao']
# mylist = shoplist
# del shoplist[0]
# print('shoplist is ',shoplist)
# print('mylist is',mylist)


# 函数
# g = lambda x,y:x + y
# print(g(2,3))


# 类
# class myself:
#     def zhang(self):
#         print("This is The test...")
# p = myself()
# p.zhang()


# _init_方法：
# class person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def say_hi(self):
#         print(' hello my name is',self.name,',age is',self.age)
# p = person('zhang',12)
# p.say_hi()


# class test:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def zhang(self):
#         print("my name is " + self.name + ".my age is " + self.age)
# p = test('chao','21')
# p.zhang()


# def zhang(name,age):
#     quan = name + ' ' + age
#     return quan.title()
# haha = zhang('chao','21')
# print(haha)
#
#
#
# def greet_user(username):
#     print('Hello ,',username.title())
# greet_user('zhangjianchao')

# 输入名字，返回欢迎语！
# def name_format(xing,ming):
#     full_name = xing +' '+ming
#     return full_name.title()
# while True:
#     print("Please input your name:")
#     xing_name = input("请输入你的姓氏:")
#     ming_name = input("请输入你的名字:")
#     full_name_format = xing_name + ming_name
#     print("Hello ," + full_name_format + '!')


# #传递列表
# def list(names):
#     for i in names:
#         print("hello:" + i + '!')
# usernames = ['zhang','jian','chao']
# list(usernames)


# 在函数中修改列表
# listone = ['zhang','jian','chao']
# listnone = []
# while listone:
#     currentlist = listone.pop()
#     print('now delete num is:',currentlist)
#     listnone.append(currentlist)
# print('\nnow new list is:')
# for j in listnone:
#     print(j)

# b = lambda x: x * 5 + 2
# print(b(3))


# filter 函数
# a = list(filter(lambda x : x % 2,range(10)))
# print(a)

# map 函数的用法：
# a = list(map(lambda x : x * 2,range(10)))
# print(a)

# 阶乘
# def jiecheng(n):
#     result = n
#     for i in range(1,n):
#         result *= i
#     return result
# num = int(input("请输入一个整数："))
# result = jiecheng(num)
# print("%d 的阶乘为：%d" %(num,result))


# 全数返回
# num1 = "请告诉我一些东西，我将原本返回你："
# num1 += "\n如果你什么都不想说，那就‘quit’退出吧！"
# message = ""
# while message != 'quit':
#     message = input(num1)
#     if message != 'quit':
#         print(message)


# num1 = "请告诉我一些东西，我将原本返回你："
# num1 += "\n如果你什么都不想说，那就‘quit’退出吧！"
# while True:
#     city = input(num1)
#     if city == 'quit':
#         break
#     else:
#         print("I love you!" + '\t' + city.title() + '!')


# 递归
# def digui(n):
#     if n < 1:
#         print("输入的数值有误！")
#         return -1
#     if n == 1 or n ==2:
#         return 1
#     else:
#         return digui(n-1)+digui(n-2)
# num = int(input("请输入您要统计的月份："))
# result = digui(num)
# if result != -1:
#     print("共有%d对小兔子诞生！" % result)


# 汉诺塔游戏
# def hnt(n,a,b,c):
#     if n == 1:
#         print(a,'-->',c)
#     else:
#         hnt(n-1,a,c,b)
#         #print(x,'-->',z)
#         hnt(1,a,b,c)
#         hnt(n-1,b,a,c)
# n = int(input("请输入汉诺塔的层数："))
# hnt(n,'A','B','C')


# # 矩阵交换
# mylist = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# mylist2 = [[row[i] for row in mylist] for i in range(3)]
# print(mylist2)


# 遍历多个列表
# questions=['name','quest','favorite color']
# answers=['qinshihuang','the holy','blue']
# for q,a in zip(questions,answers):
#     print('what is your %s? it is %s' %(q,a))
#     print('what is your {0}? it is {1}'.format(q,a))


# import sys
# for i in sys.argv:
#     print(i)
# print('路径为：',sys.path)


# 斐波那契数列
# def fi(n):
#     a,b = 0,1
#     while b < n:
#         print(b,end=' ')
#         a, b = b, a+b
#     print()
# def fi2(n):
#     result = []
#     a, b = 0, 1
#     while b < n:
#         result.append(b)
#         a,b = b, a + b
#     print(result)
# fi(1000)
# fi2(1000)


# #调用if_else.py模块
# from if_else import PI,main
# def area(redius):
#     return PI * (redius ** 2)
# def main2():
#     print("round area:",area(2))
# main2()
# main()

# 字符串
# s = 'hello ,zhangjianchao\n'
# print(repr(s)) # repr函数可以转译字符串中的特殊字符。
# print(s)


# 输出平方与立方的值
# for x in range(1,11):
#     print(repr(x),repr(x*x),repr(x**3),end='\n')
# print("*********************")
# for x in range(1,11):
#     print('{0:2d}是我本人："我是平方：{1:3d}""我是立方：{2:4d}"'.format(x,x*x,x**3))


# 格式化输出
# table = {'zhang':5,'jian':4,'chao':3}
# for name, num in table.items():
#     print('name:{0:5},num:{1:d}'.format(name,num))

#
# f = open("db2","a+")
# f.write("'zhang':5\n")
# f.close()
# f = open("db2",'r')
# # for str in f:
# #     print(str)
# # print(f.tell())
# print(f.readlines())
# f.close()

# from urllib import request
# response = request.urlopen("http://www.baidu.com")
# fi = open("db2",'w')
# page = fi.write(str(response.read()))
# fi.close()
# f = open("db2",'r')
# for x in f:
#     print(x)
# f.close()


# 异常处理
# while True:
#         try:
#             x = int(input("Please enter a number: "))
#             break
#         except ValueError:
#             print("Oops!  That was no valid number.  Try again   ")

# for line in open("db2",'r'):
#     "你好吗？"
#     print(line,end=' ')


"类以及类的继承"
# class Complex:
#     def __init__(self,num1,num2):
#         self.n1 = num1
#         self.n2 = num2
# x = Complex(2,3)
# print("两个数分别为：",x.n1,x.n2)

# class people:
#     name = ''
#     age = 0
#     weight = 0.0
#     def __init__(self,n,a,w):
#         self.name = n
#         self.age = a
#         self.weight = w
#     def speak(self):
#         print("本人：%s 今年 %s 体重 ：%s" %(self.name,self.age,self.weight))
#
# class jicheng(people):
#     grade = ''
#     def __init__(self,n,a,w,g):
#         people.__init__(self,n,a,w)
#         self.grade = g
#     def speak(self):
#         print("本人：%s 今年 %s 体重：%s 年级：%s" %(self.name,self.age,self.weight,self.grade))
#
#
# a = input("请输入people名字：")
# b = input("请输入people年龄：")
# c = input("请输入people体重：")
# d = input("请输入people年级：")
# p = jicheng(a,b,c,d)
# p.speak()


# 多重继承
# 类定义
# class people:
#     # 定义基本属性
#     name = ''
#     age = 0
#     # 定义私有属性,私有属性在类外部无法直接进行访问
#     __weight = 0
#
#     # 定义构造方法
#     def __init__(self, n, a, w):
#         self.name = n
#         self.age = a
#         self.__weight = w
#
#     def speak(self):
#         print("%s 说: 我 %d 岁。" % (self.name, self.age))
#
#
# # 单继承示例
# class student(people):
#     grade = ''
#
#     def __init__(self, n, a, w, g):
#         # 调用父类的构函
#         people.__init__(self, n, a, w)
#         self.grade = g
#
#     # 覆写父类的方法
#     def speak(self):
#         print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))
#
#
# # 另一个类，多重继承之前的准备
# class speaker():
#     topic = ''
#     name = ''
#
#     def __init__(self, n, t):
#         self.name = n
#         self.topic = t
#
#     def speak(self):
#         print("我叫 %s，我是一个演说家，我演讲的主题是 %s" % (self.name, self.topic))
#
#
# # 多重继承
# class sample(student, speaker):
#     a = ''
#
#     def __init__(self, n, a, w, g, t):
#         student.__init__(self, n, a, w, g)
#         speaker.__init__(self, n, t)
#
#
# test = sample("Tim", 25, 80, 4, "Python")
# test.speak()  # 方法名同，默认调用的是在括号中排前地父类的方法


# 调用父类
# class Parent:  # 定义父类
#     def myMethod(self):
#         print('调用父类方法')
#
#
# class Child(Parent):  # 定义子类
#     def myMethod(self):
#         print('调用子类方法')
#
#
# b = Child()  # 子类实例
# b.myMethod()  # 子类调用重写方法
# super(Child, b).myMethod()  # 用子类对象调用父类已被覆盖的方法


# class JustCounter:
#     __secretCount = 0  # 私有变量
#     publicCount = 0  # 公开变量
#
#     def count(self):
#         self.__secretCount += 1
#         self.publicCount += 1
#         print(self.__secretCount)
#
#
# counter = JustCounter()
# counter.count()
# counter.count()
# print(counter.publicCount)
# #print(counter.__secretCount)  # 报错，实例不能访问私有变量


# 类的私有方法
# class Site:
#     def __init__(self, name, url):
#         self.name = name  # public
#         self.__url = url  # private
#
#     def who(self):
#         print('name  : ', self.name)
#         print('url : ', self.__url)
#
#     def __foo(self):  # 私有方法
#         print('这是私有方法')
#
#     def foo(self):  # 公共方法
#         print('这是公共方法')
#         self.__foo()
#
#
# x = Site('菜鸟教程', 'www.runoob.com')
# x.who()  # 正常输出
# x.foo()  # 正常输出
# x.__foo()  # 报错


# class Vector:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __str__(self):
#         return 'Vector (%d, %d)' % (self.a, self.b)
#
#     def __add__(self, other):
#         return Vector(self.a + other.a, self.b + other.b)
#
#
# v1 = Vector(2, 10)
# v2 = Vector(5, -2)
# print(v1 + v2)


# class people:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def __str__(self,):
#         return '这个人的名字是%s,已经有%d岁了！'%(self.name,self.age)
#
# a=people('孙悟空',999)
# print(a)


# 返回值
# def test01():
#     msg = "没有返回值的函数。"
#     print(msg)
# def test02():
#     msg = "有返回值的函数。"
#     print(msg)
#     return msg
#
# a = test01()
# #b = test02()
#
# print(a)
# #print(b)


#
# def test(x,**kwargs):
#     print(x)
#     print(kwargs)
#     return 0
# a = test(5,y = 2,z = 3)
# print(a)


# 往文件里面循环插入
# f = open("db2",'w+')
# i = 1
# while i<10000:
#     f.write("'zhang':5\n")
#     i += 1
#     #print(i)
# while True:
#     lines = f.readlines(10000)
#     if not lines:
#         break
#     for line in lines:
#         print(line.strip())
# f.close()

#
# class Stack(object):
#     def __init__(self):
#         self.data_list = []
#     def init_queue(self):
#         self.data_list = []
#     def insert(self,data):
#         self.data_list.append(data)
#     def pop(self):
#         if len(self.data_list) == 0:
#             return None
#         data = self.data_list[0]
#         del self.data_list[0]
#         return data
#     def size(self):
#         return len(self.data_Stack)
#
# stack = Stack()
# stack.insert(1)
# stack.insert(2)
# stack.insert(3)
# tail = stack.pop()
# print(tail)
# tail = stack.pop()
# print(tail)
# tail = stack.pop()
# print(tail)


# 爬虫小试牛刀

# import re
#
# from urllib import request
#
# rr = request.urlopen("https://piao.damai.cn/152301.html?spm=a2o6e.home_bj.0.0.5f483d1dHK2IDp")
# html = rr.read()
# m = re.findall(r'page.setTitle(.*?);',html.decode('utf8'))
# print(m)


#
# import re
# # m = re.findall("a[bcd]m","abcabmacdacm")
# # print(m) #匹配字符集
# m1 = re.findall("\d","123wqdsad435")
# print("m1:",m1)#匹配数字
# m2 = re.findall("\D","123wqdsad435")
# print("m2:",m2)#匹配非数字
# m3 = re.findall("\s","12  23 \tndsa")
# print("m3:",m3)#匹配空白字符
# m4 = re.findall("\S","12  23 \tndsa")
# print("m3:",m4)#匹配非空白字符
# #匹配不区分大小写【"abc","abc#ABCabC",re.I】"\w":匹配字母或数字。 re.I匹配大小写   re.S 匹配换行   "ab?"：匹配一个或0个。 "ab+":至少匹配一个。"ab*":匹配0个或多个
# a = "<div>hello\nworld</div>"
# m5 = re.findall("\S",a,re.S)
# print("m5:",m5)
# #匹配org结尾的邮箱
# m6 = re.findall("\w+@\w+\.org","1182762696@qq.com;1182752696@qq.org")
# print("m6:",m6 )


# 引入模块
# from urllib import request
#
# url = "https://piao.damai.cn/152301.html?spm=a2o6e.home_bj.0.0.5f483d1dHK2IDp"
#
# # 第一种下载网页的方法
# print("第一种方法:")
# # request = urllib.urlopen(url)  2.x
# response1 = request.urlopen(url)
# #print("状态码:", response1.getcode())
# # 获取网页内容
# html = response1.read()
# # 设置编码格式
# print(html.decode("utf8"))
# # 关闭response1
# response1.close()

# 糗事段子
# import requests
# import html
# import time
# import re
# def wangye(page=1):
#     url = "https://www.qiushibaike.com/8hr/page/" + str(page)
#     res = requests.get(url)
#     pattern = re.compile("<div class=\"article block untagged mb15.*?<div class=\"content\">.*?</div>",re.S)
#     body = html.unescape(res.text).replace("<br/>","\n")
#     m = pattern.findall(body)
#     user_pattern = re.compile("<div class=\"author clearfix\">.*?<h2>(.*?)</h2>",re.S)
#     #content_pattern = re.compile("<div class=\"content\">(.*?)</div>",re.S)
#     content_pattern = re.compile("<span>(.*?)</span>",re.S)
#     for joke in m:
#         user = user_pattern.findall(joke)
#         output = []
#         if len(user) > 0:
#             output.append(user[0])
#         content = content_pattern.findall(joke)
#         if len(content) > 0:
#             output.append(content[0].replace("\n",""))
#         print("\t".join(output))
#     time.sleep(1)
# if __name__ == '__main__':
#     for i in range(1,10):
#         wangye(i)


# map1 = [1,2,3,4,5]
# map2 = [2,2,2,2,2]
#
# def map(array):
#     dis = []
#     for i in array:
#         dis.append(i**2)
#     print(dis)
# map(map1)
# map(map2)


# 变量传递函数和变量
# map = [1,2,3,4,5,6]
# def fun(func,array):
#     ret = []
#     for i in array:
#         res = func(i)
#         ret.append(res)
#     return ret
# print(fun(lambda x:x+1,map))


# num1 = [1,2,3,4,5,6]
# ret = []
# for i in num1:
#     ret.append(i**2)
# print(ret)
#
# def del_one(x):
#     return x-1
#
# def map_test(func,array):
#     rett = []
#     for i in array:
#         res = func(i)
#         rett.append(res)
#     print(rett)
# map_test(del_one,num1)


# class Test(object):
#     def __init__(self,name,age):
#         self.__name = name
#         self.__age = age
#     def get_name(self):
#         return self.__name
#     def get_age(self):
#         return self.__age
#     def set_score(self,score):
#         if 0 <= score <= 100:
#             self.__score = score
#             print("score:",score)
#         else:
#             raise ValueError('bad score')
# fo = Test('zhang',24)
# print("name:%s,age:%s" %(fo.get_name(),fo.get_age()))
# fo.set_score(33)


# class cat(object):
#     pass
#
#
# class Black_cat(cat):
#     def catch_mouse():
#         return True
#
#
# class White_cat(cat):
#     def catch_mouse():
#         return True
#
#
# class Pet_cat(cat):
#     def catch_mouse():
#         return False
#
#
# class dog(object):
#     def catch_mouse():
#         return True
#
#
# def good_cat(cat):
#     if cat.catch_mouse():
#         print('It\'s a good cat')
#     else:
#         print('It\'s a bad cat')
#
# good_cat(Black_cat)
# good_cat(White_cat)
# good_cat(Pet_cat)
# good_cat(dog)


# class Student(object):
#     count = 0
#
#     def __init__(self, name):
#         self.name = name
#         if(name):
#             Student.count += 1
#             print(Student.count)
# if Student.count != 0:
#     print('测试失败!')
# else:
#     print('第一步Student.count = 1!')
#     bart = Student('Bart')
#     if Student.count != 1:
#         print('测试失败!')
#     else:
#         lisa = Student('Bart')
#         if Student.count != 2:
#             print('测试失败!')
#         else:
#             print('Students:', Student.count)
#             print('测试通过!')


# 线程
# import threading
# import time
#
# exitFlag = 0
#
# class myThread (threading.Thread):
#     def __init__(self, threadID, name, counter):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.counter = counter
#     def run(self):
#         print ("开始线程：" + self.name)
#         print_time(self.name, self.counter, 5)
#         print ("退出线程：" + self.name)
#
# def print_time(threadName, delay, counter):
#     while counter:
#         if exitFlag:
#             threadName.exit()
#         time.sleep(delay)
#         print ("%s: %s" % (threadName, time.ctime(time.time())))
#         counter -= 1
#
# # 创建新线程
# thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(2, "Thread-2", 2)
#
# # 开启新线程
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()
# print ("退出主线程")


# #filter函数
# movie_people = ['sb_1','sb_2','sb_3','xiaoming','xiaowang']
# def show_test(p):
#     return p.endswith('g')
# def filter_test(func01,array):
#     ret = []
#     for i in array:
#         if not func01(i):
#             ret.append(i)
#     return ret
# result = filter_test(show_test,movie_people)
# print(result)
# print(filter_test(lambda n:not n.endswith('2'),movie_people))


# num01 = [2,3,4,5,6]
# def reduce_test(func,array,init = None):
#     if  init is None:
#         res = array.pop(0)
#     else:
#         res = init
#     for num in array:
#         res = func(res,num)
#     return res
# print(reduce_test(lambda x,y:x*y,num01,100))


# reduce 函数
# from functools import reduce
# num1 = [1,2,3,4,5]
# print(reduce(lambda x,y:x+y,num1))
# print(reduce(lambda x,y:x*y,num1,100)) #100代表的是传入的默认值。


# 编码、解码
# name = '你好'
# print(bytes(name,encoding='utf8').decode('utf8'))

# a = [1,2,3,4,5]
# print(max(a))
# print(list(zip(('a','b','c'),(1,2,3))))


# 比较年龄的最大值、最小值
# age_dis = {'age1':1,'age2':20,'age3':24,'age4':3}
# print("name:%s,age:%s" %(max(age_dis),max(age_dis.values())))


# 取字典中年龄最大者
# people = [
#     {'name':'zhang','age':24},
#     {'name':'jian','age':25},
#     {'name':'chao','age':26},
#     {'name':'wupei','age':100}
# ]
# print(max(people,key=lambda dic:dic['age']))


# 各省并发
# import json
# f = open("db",'r',encoding='utf8')
# data = f.read()
# # print(json.dumps(data,sort_keys=True,ensure_ascii=False,indent=2).replace(',','\n').replace('\\','').replace(':{','{\n'))
# b = json.loads(data)
# print(b)
# f.close()

# with open('db2','r+',encoding='utf8') as f:
#     p =f.readlines()
# with open('db3','w',encoding='utf8') as f2:
#     p2 = f2.write(p[1])


# 读取二进制文件内容并将其打印
# with open('db3','rb') as f:
#     b = f.read()
#     print(b)
#     print(b.decode())


# with open('db3', 'r+', encoding='utf-8',newline='') as f:   #newline=''读取文件中真正的换行符号。
#     # f.write('123\n')
#     c = f.read(3)
#     print(c)
#     # print(c.rstrip())  # 打印时删除多余的空行
#     # print(f.closed)
#     # print(f.encoding)
#     print(f.seek(0))   #表示指定光标的位置
#     print(f.readlines())
#     print(f.tell())


# with open('seek.txt','r',encoding='utf-8',newline='') as f:
#     ff = f.read()
#     print(ff)
#     print(ff.replace('\r\n','\n'))
#     # f.seek(10,1)
#     # print(f.tell())
#     # f.seek(13,1)  #1位置表示从上次光标所在的位置开始操作。使用seek最好以‘rb模式‘打开文件（’seek.txt‘，‘rb’）
#     # print(f.tell())


# 读取日志文件最后一行的数据
# with open('日志文件.txt','rb') as f:
# # with open('db','rb') as f:
#     for i in f:
#         doce = -5
#         while True:
#             f.seek(doce,2) # 2代表倒序查找。
#             data = f.readlines()
#             print(data)
#             print(len(data))
#             if len(data) > 1:
#                 print("文件的最后一行是：%s" %(data[-1].decode('utf-8')))
#                 break
#             doce *=2


# 迭代器协议
# l = [1,2,3,4,5,6,6]
# index = 0
# while index < len(l):
#     print(l[index])
#     index += 1


# with open('db3','r+') as f:
#     iter = f.__iter__()
#     # while f.readline() != None:
#     while True:
#         try:
#             print(iter.__next__(),end='')
#         except StopIteration:
#             #print("迭代出错了！")
#             break


# list = []
# for i in range(10):
#     list.append(i)
#     print("第%s个鸡蛋！\n" % i,end='')


# while True:
#     name = input("请输入你的名字：")
#     res = [name + '帅哥！' if name == 'zhangjianchao' or name =='zjc' else  name + '傻冒!']
#     print(res)


# print(sum(i for i in range(100000000)))


# #yield 与 return 作用类似   不同的是 yield 可以返回多个值
# def test():
#     yield 1         #可以返回多个数值
#     yield 2
#     yield 3
#     yield 4
#     yield 5
# a = test()
# while True:
#     try:
#         print(a.__next__())
#     except StopIteration:
#         break


# def chibaozi():
#     ret = []
#     for i in range(100):
#         ret.append('包子：%s' %i)
#     return  ret
# print(chibaozi())


# def  product_baozi():
#     for i in range(100):
#         print("正在生产第%s个包子..." %i)
#         yield '一屉包子',i   #下次运行就从yield位置开始运行
# ret = product_baozi()
# while True:
#     try:
#         print(ret.__next__())
#     except StopIteration:
#         break


# def baozi():
#     for i in range(10000):
#         yield '鸡蛋%s' %i
# ret = baozi()
# for i in ret:
#     print(i)


# 人口普查
# def get_population():
#     with open('人口普查','r',encoding='utf-8',newline='') as f:
#         for i in f:
#             yield i
# g = get_population() #获取到的值为字符串
#
# while True:
#     try:
#         print(eval(g.__next__().replace('\n',''))['name']) #eval函数将字符串转换成字典形式
#     except StopIteration:
#         break
#
# gg = get_population()
# def all_num_people():
#     num = sum(eval(i)['population'] for i in gg)
#     print("全国总人口为：%s" % num)
# all_num_people()
#
# ggg = get_population()
# while True:
#     try:
#         for i,j in eval(ggg.__next__()).items():
#             print(i + ":" + str(j))
#     except StopIteration:
#         break


# enumerate函数     可遍历的数据对象组合为一个索引序列，同事列出数据和数据下标。一般用在for循环当中。
# import time
# def producer():
#     ret = []
#     for i in range(10000):
#         # time.sleep(0.1)
#         ret.append(i)
#     return ret
# def consumer(res):
#     for index,baozi in enumerate(res):
#         time.sleep(0.1)
#         print('第%s个人，吃了第%s个包子！' %(index,baozi))
# res = producer()
# consumer(res)


# 生产者与消费者(吃包子)
# import time
# def shengchan(name):
#     print("我是生产者：%s,接下来由我为大家生产产品..." %name)
#     while True:
#         chanpin = yield
#         print("%s正在消费第%s件产品..." %(name,chanpin))
# def xiaofei():
#     res = shengchan("小张")
#     res2 = shengchan("小wang")
#     res.__next__()
#     res2.__next__()
#     for i in range(100):
#         res.send("%s" %i)
#         res2.send("%s" %i)
#         time.sleep(1)
# xiaofei()


# 装饰器原则：1、不改变被修饰函数的源代码；2、不修改被调用函数的调用方式。
# # 函数闭包 && 装饰器
# import time
# def timmer(func):
#     def wapper(*args,**kwargs):
#         start_time = time.time()
#         res = func(*args,**kwargs)
#         stop_time = time.time()
#         print('运行时间是%s' %(stop_time-start_time))
#         return res
#     return wapper
# #第一种
# def test(name,age):
#     time.sleep(3)
#     print("test函数运行完毕！名字是:%s,年龄是：%s" %(name,age))
#     return "这是test函数的返回值！"
# #第二种
# def test2(name,age,gender):
#     time.sleep(3)
#     print("test2函数运行完毕！名字是:%s,年龄是：%s,性别是：%s" %(name,age,gender))
#     return "这是test2函数的返回值！"
# #两种调用方式
# ff = timmer(test) #返回的是wapper的地址
# print(ff('zhang',123))  #执行的是wapper函数
# fff = timmer(test2)
# print(fff('zhang',123,'女'))


# l = [1,2,3,4,5,6,7,8,9,0]
# a,*_,b = l
# print(a)
# print(b)
# print(l[0])
# print(l[-1])


# 京东购物
# user_list = [
#     {'name':'xiaozhang','passwd':'xiaozhang'},
#     {'name':'xiaowang','passwd':'xiaowang'},
#     {'name':'xiaoli','passwd':'xiaoli'},
#     {'name':'xiaochen','passwd':'xiaochen'},
# ]
# current_dic = {'username':None,'login':False}
#
# def auth(auth_type='filedb'):
#     def auth_func(func):
#         def wapper(*args,**kwargs):
#             print('认证类型是：',auth_type)
#             if auth_type == 'filedb':
#                 # if username == 'sb' and passwd =='123':
#                 if current_dic['username'] and current_dic['login']:
#                     res = func(*args,**kwargs)
#                     return res
#                 username = input('用户名：').strip()
#                 passwd = input('密码:').strip()
#                 for index,user_dic in enumerate(user_list):
#                     if username == user_dic['name'] and passwd == user_dic['passwd']:
#                         current_dic['username'] = username
#                         current_dic['login'] = True
#                         res = func(*args, **kwargs)
#                         return res
#                 else:
#                     print("用户名或密码错误，请重新登录！")
#             elif auth_type == 'ldap':
#                 print('不会玩。。。')
#             else:
#                 print('米西米西......')
#
#         return wapper
#     return auth_func
# @auth(auth_type='filedb')
# def index():
#     print("欢迎来到京东主页！")
#
# @auth(auth_type='ldap')
# def home(name):
#     print("欢迎'%s'回家!" %name)
#
# @auth(auth_type='sss')
# def shopping_car(name):
#     print("[%s]的购物车里有[%s,%s,%s]" %(name,'奶茶','妹妹','娃娃'))
#
#
# print('before-->',current_dic)
# index()
# print('after-->',current_dic)
# home('产品经理')
# shopping_car('产品经理')


# 函数的运行时间
# import time
#
# def timer(func):
#     def wapper():
#         print(func)
#         start_time = time.time()
#         res = func()
#         stop_time = time.time()
#         print("函数的运行时间是%s" %(stop_time-start_time))
#         return res
#     return wapper
#
#
# @timer
# def test():
#     time.sleep(3)
#     print('test函数运行完毕！')
#     return '这是test的返回值'
#
# res = test()
# print(res)


# 对传入的参数进行检查
# def recoder(strname,age):
#     if not isinstance(age,(int,str)):
#         raise TypeError('bad operand type')
#     print('姓名：',strname,'年纪：',age)
#
# recoder('xiaozhang',age=1.2)


#
# def fetch(data):
#     # print("\033[1;43m这是查询功能\033[0m")
#     # print("\033[1;43m用户数据是：\033[0m", data)
#     backend_data = 'backend %s' % data
#     with open('haproxy.conf', 'r') as read_f:
#         tag = False
#         ret = []
#         for read_line in read_f:
#             if read_line.strip() == backend_data:
#                 tag = True
#                 continue
#             if tag and read_line.startswith('backend'):
#                 break
#             if tag:
#                 # print("%s" % read_line, end='')
#                 ret.append(read_line)
#     return ret
#
#
# def add():
#     print("\033[1;43m这是添加功能\033[0m")
#
#
# def change(data):
#     print("\033[1;43m这是修改功能\033[0m")
#     # print("用户输入的数据是：",data)
#     backend = data[0]['backend']
#     old_server_record ='%sserver %s %s weight %s maxconn %s' %(' '*8,data[0]['record']['server'],data[0]['record']['server'],data[0]['record']['weight'],data[0]['record']['maxconn'])
#     print("原文件中要修改的数据是：",old_server_record)
#
#     res = fetch(backend)
#     print("查询到的原文件数据为：",res)
#     if not res or old_server_record not in res:
#         return "你要修改的数据不存在..."
#
#
#
#
#
# def delete():
#     print("\033[1;43m这是删除功能\033[0m")
#
#
# def quit():
#     print("退出！")
#
#
# if __name__ == '__main__':
#     msg = """
#     1：查询
#     2：添加
#     3：修改
#     4：删除
#     5：退出
#     """
#     msg_dic = {
#         '1': fetch,
#         '2': add,
#         '3': change,
#         '4': delete,
#         '5': quit
#     }
#     while True:
#         print(msg)
#         choice = input('请输入你的选项：').strip()
#         if not choice: continue
#         if choice == '5': break
#         data = input("请输入用户数据：").strip()
#         if choice != '1':
#             data = eval(data)
#         if not data: continue
#         res = msg_dic[choice](data)
#         print("最终结果是：",res)
#
#
#
#
# # [{'backend':'www.oldboy1.org','record':{'server':'2.2.2.5','weight':30,'maxconn':4000}},{'backend':'www.oldboy1.org','record':{'server':'2.2.2.6','weight':60,'maxconn':8000}}]


# with open('123','r') as f:
#     linelist = f.readlines()
#     # for i in range(len(linelist)):
#     for i in range(80,len(linelist)):
#         print("aliyun%s,num%s,em2" %(linelist[i].strip(),str(i)) )


# for i in range(50):
#     list_str = ['avg','dtr','min','max','lo']
#     for t in range(len(list_str)):
#         print("num%s-%s" %(i,list_str[t]))


# list1 = [['num94', '117.91.180.136'], ['num91', '117.91.180.132'], ['num85', '117.91.180.124'], ['num82', '117.91.180.120'], ['num88', '117.91.180.128'], ['num80', '175.22.55.255'], ['num238', '117.91.182.36'], ['num241', '117.91.182.40'], ['num247', '117.91.182.48'], ['num235', '117.91.182.32'], ['num244', '117.91.182.44'], ['num256', '117.91.182.60'], ['num253', '117.91.182.56'], ['num250', '117.91.182.52'], ['num271', '117.91.182.80'], ['num277', '117.91.182.88'], ['num259', '117.91.182.64'], ['num274', '117.91.182.84'], ['num268', '117.91.182.76'], ['num262', '117.91.182.68'], ['num265', '117.91.182.72'], ['num280', '117.91.182.92']]
# list2 = [1, 2, 3, 4, 5, 6, 7]
#
# # print("list1[0]: ", list1[0])
# # print("list2[1:5]: ", list2[1:5])
# for i in range(len(list1)):
#     print(list1[i][0])
# a = [['num94', '117.91.180.136'], ['num91', '117.91.180.132'], ['num85', '117.91.180.124'], ['num82', '117.91.180.120'], ['num88', '117.91.180.128'], ['num80', '175.22.55.255'], ['num238', '117.91.182.36'], ['num241', '117.91.182.40'], ['num247', '117.91.182.48'], ['num235', '117.91.182.32'], ['num244', '117.91.182.44'], ['num256', '117.91.182.60'], ['num253', '117.91.182.56'], ['num250', '117.91.182.52'], ['num271', '117.91.182.80'], ['num277', '117.91.182.88'], ['num259', '117.91.182.64'], ['num274', '117.91.182.84'], ['num268', '117.91.182.76'], ['num262', '117.91.182.68'], ['num265', '117.91.182.72'], ['num280', '117.91.182.92']]
#
# for i in range(len(a)):
#     print("Error name :%s ==> Error ip :%s " % (a[i][0], a[i][1]))


# from if_else import *
#
# print(add(3,4))
# print(sub(3,4))


# aa = "([a,b],[c,de])"


# 将两个列表 顺序合并
# a = [1,2,3]
# b = [11,22,33]
# c = [[a,b] for a,b in zip(a,b)]
# print(c)


# # 时间转换
# import time
# t = time.localtime()
# print(t)
# print(t.tm_wday)
# print(time.time())
# print(time.localtime(time.time()))     #time.localtime()   时间戳转换成结构化时间
# print(time.mktime(time.localtime()))   #time.mktime()   结构化时间转换成时间戳
# print(time.strftime("%Y-%m-%d %X",time.localtime()))   #time.strftime()   将结构化时间转换成字符串时间
# print(time.strptime("2008:08:08:20:00:00","%Y:%m:%d:%X"))   #time.strptime() 将字符串时间转换成结构化时间
# print(time.asctime())
# print(time.ctime())


# import datetime
# print(datetime.datetime.now())


# import re
# print(re.findall(r'123','123456'))


#
#
# t = random.random() #返回[0-1]浮点数
#
# t1 = random.randint(1,7) #返回值包括 [1-7]整数
#
# t2 = random.randrange(1,7)  #返回值不包括 7整数
#
# t3 = random.choice([11,22,33,44,55,66,77])  #返回列表中的一个数
#
# t4 = random.sample([11,22,33,44,55,66,77],2)   #返回列表中的两个数
#
# t5 = random.uniform(1,3)   #返回[1-3]浮点数

# 洗牌
# t6 = [1,2,3,4,5,6,7]
# random.shuffle(t6)
# print(t6)


# 二维码
# import random
# def v_code():
#     ret = ""
#     for i in range(5):
#         num = random.randint(0,9)
#         print("num:%s" %num)
#         alf = chr(random.randint(65,122))
#         print("alf:",alf)
#         s = str(random.choice([num,alf]))
#         print("s:%s" %s)
#         ret+=s
#     return ret
# print(v_code())


# import sys,os
#
# print(os.path.dirname(os.path.abspath(__file__))) # abspath 绝对路径; dirname 相对路径
# print(os.path.dirname(__file__))
#
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# sys.path.append(BASE_DIR)
#
# print(os.listdir())


# import os         #路径拼接
# a = "zhangjian"
# b = "chao"
# c = os.path.join(a,b)
# print(c)


#
# import sys
# print(sys.argv)


# 进度条
# import sys,time
# for i in range(100):
#     sys.stdout.write("#")
#     time.sleep(0.1)
#     sys.stdout.flush()


#  将字符串进行字典处理
# a = '{"zhang":"chao"}'
# b=eval(a)
# print(b)
# print(type(b))
# print(b["zhang"])


# import json

# dic = {"name":"zhang"}
# data = json.dumps(dic)
# print(data)
# a='{"济南acd1-2":{"JNACD\u003c-\u003eYZACD5":"342","把枪":"0","行圆汽车-JN":"0","江苏联通-JN":"8","VIPKID-JN03-150M":"63","freeswitch":"48","拒绝":"0","行圆汽车2":"0","95066广州移动-JN":"972","95066北京联通2-JN":"0","95066北京联通-JN":"155","JNACD1-2\u003c-\u003eYZACD1-4":"0","滴滴-JN":"550","顺丰专线-JN":"281","95753内蒙联通-JN":"2","VIPKID-JN02":"0","VIPKID-JN01":"327"},"扬州acd7-8":{"南京acd1-4\u003c-\u003eYZACD7-8":"2","拒绝":"0","扬州acd1-4\u003c-\u003eYZACD7-8":"12","扬州ACD5-6\u003c-\u003eYZACD7-8":"2"},"南京测试机":{"珏焱-TEST":"0","NJTEST\u003c-\u003eYZACD01":"0","NJTEST\u003c-\u003eNJACD01":"2","沈崇坤-TEST":"0","德塔思维-TEST":"0","同程网络-TEST":"0","NJTEST\u003c-\u003eYZACD05":"0","尼罗河-TEST":"0","测试":"0","NJTEST\u003c-\u003eYZCC":"0","度言软件-TEST":"0","上海钉钉TO-TEST":"0","南京钉钉TO-TEST":"0","guangdongCT":"0","福建电信117.27.144.98":"0","弘益通盈-TEST":"0","苏宁-TEST":"0","jiangsuCT":"0","途牛-TEST":"0","智语-TESST":"0","beijingCT":"0","银联-TEST":"0","顺丰-TEST":"0","京东咚咚-TEST":"0","移动透传":"0","统一通信-TEST":"0","shanghaiCT":"0","58非注册-TEST":"0","京东FS/苏宁电话会议-TEST":"0","云趣-TEST":"0","声网-TEST":"0","网易七鱼-TEST":"0","杭州钉钉TO-TEST":"0"},"扬州云":{"扬州acd5":"0","扬州1-4":"0","DECLINE":"0"},"自建扬州":{"测试-YZZJ":"0","黑龙江-伊春-YZZJ":"1","黑龙江-齐齐哈尔-YZZJ":"0","贵州-遵义-YZZJ":"1","吉林-长春-YZZJ":"22","贵州-黔东南-YZZJ":"0","黑龙江-大兴安岭-YZZJ":"0","湖南-YZZJ":"432","四川-YZZJ":"364","江西-YZZJ":"184","贵州-铜仁-YZZJ":"0","新疆-乌鲁木齐-YZZJ":"5","上海云信-YZZJ":"0","河北-中兴-YZZJ":"202","内蒙-华为-YZZJ":"157","河北-张家口-YZZJ":"17","河南-华为-YZZJ":"72",,"河北-承德-YZZJ":"5","山东-青岛-YZZJ":"183","用友嘟嘟-YZZJ":"748","贵州-安顺-YZZJ":"0","陕西-西安-YZZJ":"381","河北-唐山-YZZJ":"62","辽宁-中兴-YZZJ":"156","福建-YZZJ":"112","吉林-四平-YZZJ":"3","贵州-黔南-YZZJ":"0","山东-济南-YZZJ":"213","阿里通信6秒-YZZJ":"493","甘肃-YZZJ":"108","贵州-黔西南-YZZJ":"0","海南-YZZJ":"21","黑龙江-绥化-YZZJ":"0","新疆-阿泰勒-YZZJ":"4","河北-秦皇岛-YZZJ":"11","重庆-YZZJ":"141","上海-YZZJ":"689","贵州-毕节-YZZJ":"1","浙江-YZZJ":"818","内蒙-中兴-YZZJ":"86","山西-太原-YZZJ":"195","黑龙江-大庆-YZZJ":"4","中天网景-YZZJ":"0","辽宁-华为-YZZJ":"86","贵州-贵阳-YZZJ":"38","北京-中兴-YZZJ":"1069","贵州-六盘水-YZZJ":"0","吉林-中兴-YZZJ":"7","天津-YZZJ":"114","英孚教育-YZZJ":"1","安徽-YZZJ":"192","阿里通信-YZZJ":"5306","河北-廊坊-YZZJ":"16","北京-华为-YZZJ":"1","黑龙江-黑河-YZZJ":"0","黑龙江-中兴-YZZJ":"106","河南-中兴-YZZJ":"132"},"自建南京":{"用友云主机-NJZJ":"0","广东沃云-NJZJ":"1280","黑龙江-齐齐哈尔-NJZJ":"5","黑龙江-黑河-NJZJ":"0","测试-NJZJ":"0","八爪鱼-NJZJ":"0","河北-张家口-NJZJ":"14","黑龙江-绥化-NJZJ":"1","贵州-铜仁-NJZJ":"0","海南-NJZJ":"26","四川-NJZJ":"371","上海-NJZJ":"251","九州盈丰-NJZJ":"0","广汇汽车-NJZI":"0","天津-NJZJ":"80","第五大道-NJZJ":"141","安徽-NJZJ":"214","内蒙-华为-NJZJ":"197","贵州-毕节-NJZJ":"0","河南-华为-NJZJ":"99","广汇汽车-NJZJ":"0","中天网景-NJZJ":"0","江西-NJZJ":"165","阿里通信-NJZJ":"4550","食在鲜-NJZJ":"0","贵州-黔西南-NJZJ":"0","河南-中兴-NJZJ":"160","吉林-中兴-NJZJ":"11","山西-太原-NJZJ":"192","贵州-黔南-NJZJ":"0","吉林-四平-NJZJ":"3","重庆-NJZJ":"103","陕西-西安-NJZJ":"167","黑龙江-伊春-NJZJ":"1","贵州-贵阳-NJZJ":"44","河北-中兴-NJZJ":"226","河北-廊坊-NJZJ":"16","辽宁-中兴-NJZJ":"119","新疆-乌鲁木齐-NJZJ":"0","山东-济南-NJZJ":"333","方正-NJZJ":"88","黑龙江-中兴-NJZJ":"104","河北-承德-NJZJ":"2","浙江-NJZJ":"665","贵州-遵义-NJZJ":"1","黑龙江-大兴安岭-NJZJ":"0",,"鼐威欣-NJZJ":"234","新疆-阿泰勒-NJZJ":"0","Udesk-NJZJ":"0","贵州-黔东南-NJZJ":"0","四方教育-NJZJ":"0","贵州-六盘水-NJZJ":"0","内蒙-中兴-NJZJ":"47","福建-NJZJ":"131","北京-华为-NJZJ":"1","阿里通信6秒-NJZJ":"0","河北-唐山-NJZJ":"48","世纪融云-NJZJ":"683","辽宁-华为-NJZJ":"82","甘肃-NJZJ":"108","河北-秦皇岛-NJZJ":"8","吉林-长春-NJZJ":"15","北京-中兴-NJZJ":"643","湖南-NJZJ":"358","贵州-安顺-NJZJ":"0","黑龙江-大庆-NJZJ":"1","上海云信-NJZJ":"0","山东-青岛-NJZJ":"338"},"扬州acd5-6":{"云平台-京东预发布环境（建沿）":"0","拒绝":"0","YZACD5-6-\u003eYZcc":"0","内蒙古联通95753-YZACD05":"1","测试":"0","扬州二期云主机35.51【号码解析预发】":"0","江苏联通-YZACD5":"0","山东移动-YZACD5":"0","FS49-50测试":"0","滴滴-YZACD5":"543","95338XX江苏联通-YZACD5":"121","原易车网（荒废中）":"0","扬州电信9533885":"0","YZACD5-6\u003c-\u003eYZACD7-8":"2","话务转呼叫中心":"0","顺丰公网-YZACD5":"0","sai认证（星宇）":"0","YZACD5-6\u003c-\u003eNJTESTACD":"0","废弃":"0","YZACD5-6\u003c-\u003eNJACD1-4":"3","顺丰专线-YZACD5":"0","云平台呼叫中心51.50":"0","YZACD5-6\u003c-YZCC":"0","SIP对接测试3":"0","SIP对接测试4":"0","95078广东移动-YZACD5":"509","薄富帅01":"0","YZACD5-6\u003c-\u003eJNACD1-2":"340","扬州移动-YZACD5":"0","95078扬州电信-YZACD5":"331","YZACD5-6\u003c-YZACD1-4":"33","VIPKID-YZ03":"6","95066北京联通2-YZACD5":"71","扬州电信95184":"0","广州移动-YZACD5":"0","原阿里通信（荒废中）":"0","95066北京联通1-YZACD5":"68","VIPKID-YZ02":"0","VIPKID-YZ01":"43","95078江苏联通-YZACD5":"116","云平台呼叫中心51.24":"0"},"南京acd1-4":{"NJACD1-4\u003c-\u003eNJTESTACD":"2","今日头条-NJ":"681","食在鲜-NJ":"53","中大互联-NJ":"0","青海-NJCZW":"34","四川平安-NJ":"469","贵州-铜仁-NJCZW":"2","八爪鱼-NJ":"113","用友云总机-NJ":"26","贵州-黔南-NJCZW":"5","新疆-阿泰勒博州-NJCZW":"7","江西-NJCZW":"87","吉林-长春通化-华为-NJCZW":"23","吉林-四平延吉-华为-NJCZW":"4","上海-NJCTW":"0","度言-NJ":"5","苏州平安（测试）-NJ":"0","南京鼐威欣-NJ":"0","河北-中兴-NJCZW":"136","河南-中兴-NJCZW":"117","移动透传-NJ":"0","电信通道-NJ":"0","中智未来-NJ":"1","贵州-贵阳-NJCZW":"73","内蒙古-中兴-NJCZW":"12","贵州-六盘水-NJCZW":"3","苏宁-NJ":"143","上海太保/平安-NJ":"428","广东-对等-NJCZW":"0","山东-济南-NJCZW":"238","广西-NJCZW":"66","河南-华为-NJCZW":"89","钉钉FROM-NJ":"31","江苏-二号线-NJCTW":"0","携程-NJ":"0","贵州-毕节-NJCZW":"12","第五大道-NJ":"0","京东咚咚-NJ":"2","四川-NJCTW":"0","四方教育-NJ":"0","CTD\u003c-\u003e上海阿里通信-NJ":"405","天润（沪江网）-NJ":"644","智云呼叫-NJ":"0","NJACD1-4\u003c-\u003eJNACD1-2":"0","NJACD1-4\u003c-\u003eYZCC":"0","黑龙江-伊春-NJCZW":"0","广东沃云-NJ":"12","钉钉TO-NJ":"80","河北-张家口-NJCZW":"10","NJACD1-4\u003c-\u003eYZACD7-8":"3","辽宁-华为-NJCZW":"27","FS对接-NJ":"0","NJACD1-4\u003c-\u003eYZACD5-6":"1","北京-华为-NJCZW":"313","黑龙江-中兴-NJCZW":"33","湖南-NJCZW":"165","黑龙江-大庆-NJCZW":"5","四川-NJCZW":"208","位置网-NJ":"0","黑龙江-大兴安岭-NJCZW":"0","云南-NJCZW":"0","重庆-NJCZW":"195","福建-NJCZW":"123","贵州-黔西南-NJCZW":"1","自建平台":"1392","海南-NJCZW":"20","吉林-中兴-NJCZW":"5","九州盈丰-NJ":"80","方正-NJ":"0","河北-秦皇岛-NJCZW":"8","贵州-遵义-NJCZW":"11","甘肃-江宁-NJCZW":"24","黑龙江-齐齐哈尔-NJCZW":"2","二六三-NJ":"0","辽宁-中兴-NJCZW":"44","世融软件-NJ":"0","山东-青岛-NJCZW":"132","江苏-NJCTW":"2105","河北-唐山-NJCZW":"33","NJACD1-4\u003c-\u003eYZACD1-4":"372","天津-NJCZW":"46","黑龙江-黑河-NJCZW":"0","新疆-乌鲁木齐喀什-NJCZW":"26","华为云-NJ":"12","用友嘟嘟-NJ":"0","黑龙江-绥化-NJCZW":"0","湖北-NJCZW":"476","苏州平安-NJ":"1","途牛-NJ":"89",,"科讯嘉联-NJ":"0","云南-高新-NJCZW":"12","宁夏-西藏-NJCZW":"58","饿了么-NJ":"34","华拓金服-NJ":"182","58同城01-NJ":"0","捷骏汽车-NJ":"2","图贝创达-NJ":"0","内蒙古-华为-NJCZW":"69","北京-中兴-NJCZW":"275","陕西-NJCZW":"243","上海一潇测试":"0","VIPKID-NJ":"0","今日头条（big_data）-NJ":"92","贵州-安顺-NJCZW":"3","甘肃-河西兰州-NJCZW":"30","安徽-NJCZW":"118","京东电话会议":"5","阿里测试":"0","河北-承德-NJCZW":"6","京东咚咚转FreeSWITCH-NJ":"0","上海-NJCZW":"739","星宇测试-NJ":"0","山西-NJCZW":"47","北京-NJCTW":"0","云南-南天-NJCZW":"21","安邦财险-NJ":"28","移网小号-NJ":"3","58同城02-NJ":"0","广汇汽车-NJ":"18","浙江-NJCZW":"902","陕西华为智能电话-NJ":"26","河北-廊坊-NJCZW":"16","上海银联专线-NJ":"6","京东FS":"0","世纪融云-NJ":"14","贵州-黔东南-NJCZW":"0"},"扬州acd1-4":{"内蒙古-华为-YZCZW":"19","中天网景-YZ":"4","浙江钉钉FROM-YZ":"0","安徽银联2-YZ":"0","拒绝":"0","河北-中兴-YZCZW":"81","山东-济南-YZCZW":"148","河北-秦皇岛-YZCZW":"4","云南-YZCZW":"0","辽宁-中兴-YZCZW":"21","贵州-贵阳-YZCZW":"6","YZACD1-4\u003c-\u003eYZCESHI":"0","海南-YZCZW":"17","青海-YZCZW":"10","江苏-二号线-YZCTW":"0","贵州-遵义-YZCZW":"0","云南-高新-YZCZW":"0","上海钉钉TO-YZ":"0","山东-青岛-YZCZW":"72","河北-廊坊-YZCZW":"8","新疆-乌鲁木齐喀什-YZCZW":"7","携程-YZ":"0","吉林-四平延吉-华为-YZCZW":"1","黑龙江-中兴-YZCZW":"8","YZACD1-4\u003c-\u003eNJ_TEST01":"0","58测试-YZ":"0","重庆-YZCZW":"67","天润（沪江网）-YZ":"659","上海银联-YZ":"0","江西-YZCZW":"56","云南-南天-YZCZW":"7","电信通道":"0","YZACD1-4\u003c-\u003eJNACD":"0","吉林-长春通化-华为-YZCZW":"7","辽宁-华为-YZCZW":"10","新疆-阿勒泰博州昌吉-YZCZW":"0","天津-YZCZW":"18","上海云信":"0","EF英孚教育-YZ":"1","湖南-YZCZW":"143","贵州-铜仁-YZCZW":"0","黑龙江-齐齐哈尔-YZCZW":"1","山西-YZCZW":"20","甘肃-河西兰州-YZCZW":"22","九霄祥云-YZ":"0","河南-华为-YZCZW":"39","YZACD1-4\u003c-\u003eSFACD":"31","西安辉腾-YZ":"3","黑龙江-大庆-YZCZW":"2","宁夏测试":"0","广东-对等-YZCZW":"0","上海拍拍贷-YZ":"0","吉林-中兴-YZCZW":"1","苏州平安-YZ":"0","上海-YZCTW":"0","安徽银联-YZ":"31","饿了么-YZ":"10","四川-YZCTW":"0","移网小号-YZ":"0","内蒙古-中兴-YZCZW":"6","YZACD1-4\u003c-\u003eNJACD1-4":"32","杭州钉钉TO-YZ":"0","上海-YZCZW":"281","甘肃-江宁-YZCZW":"0","黑龙江-大兴安岭-YZCZW":"0","移动透传-YZ":"0","安徽-YZCZW":"20","用友嘟嘟-上海-YZ":"0","贵州-黔西南-YZCZW":"0","贵州-毕节-YZCZW":"0","宁夏-西藏-YZCZW":"40","江苏-YZCTW":"848","YZACD1-4\u003c-\u003eYZCC":"0","上海尚仪02-YZ":"3","云呼叫中心35.121-YZ":"0","贵州-安顺-YZCZW":"0","黑龙江-黑河-YZCZW":"0","中天网景2-YZ":"0",,"上海平安/太保-YZ":"501","珍爱网-YZ":"0","测试-YZCZW":"0","河北-唐山-YZCZW":"21","四川-YZCZW":"113","上海钉钉FROM-YZ":"75","自建话务01":"737","上海一潇测试":"0","CTD\u003c-\u003e阿里通信-YZ":"0","北京-华为-YZCZW":"386","浙江-YZCZW":"212","YZACD1-4\u003c-\u003eYZACD7-8":"12","贵州-黔东南-YZCZW":"0","上海尚仪01-YZ":"309","福建-YZCZW":"103","今日头条-YZ":"648","上海银联专线-YZ":"0","广西-YZCZW":"59","YZACD1-4\u003c-\u003eSFACD6":"0","河北-张家口-YZCZW":"2","河北-承德-YZCZW":"5","河南-中兴-YZCZW":"71","徐州北京鑫彭-YZ":"0","北京-中兴-YZCZW":"198","58-YZ":"0","贵州-六盘水-YZCZW":"2","淮安升学教育-YZ":"6","湖北-YZCZW":"300","黑龙江-绥化-YZCZW":"0","北京-YZCTW":"3","黑龙江-伊春-YZCZW":"0","贵州-黔南-YZCZW":"0","华云讯通-YZ":"77","用友嘟嘟-北京-YZ":"10","京东FS":"4","陕西-YZCZW":"100"}}'
# dir = open("db3",'w')
# dir.write(json.dumps(a))
# dir.close()
# with open('db3') as file:
#     file = json.loads(file.read())
#     print(file)


# 正则匹配
#
# import re
#
# print(re.findall("alex+?","mandsaujaaalexalexalexalexalexalexxxxaaab"))


#  生成随机密码
# import random
# import string
# My_List = []
# User = input("请您输入您的姓名：")
# Password = input("请您选择你要设置几位数的密码：")
# for i in range(int (Password)):
#     Method = random.choice(string.ascii_letters + string.digits )
#     print(random.choice(string.ascii_letters+string.digits))
#     My_List.append(Method)
# result = "".join(My_List)
# total = "您的用户名为：%s  您的密码为：%s" %(User,result)
# print(total)


# import re
# print(re.findall(r"c\\l","c\ln nnn"))
# print(re.search("(?P<name>[a-z]+)(?P<age>\d+)","zhang24jian23chao22").group())
# print(re.search("(?P<name>[a-z]+)(?P<age>\d+)","zhang24jian23chao22").group("name"))
# print(re.search("(?P<name>[a-z]+)(?P<age>\d+)","zhang24jian23chao22").group("age"))
# print(re.split("[ |]","a b c|d|fjjj")) #空格或管道符分割
#
#
# com = re.compile("\d+")
# print(com.findall("zhang24hahahha")) #提前编译
#
# #去掉优先级,下面默认有限匹配（）里面的字符。
# print(re.findall("www.(baidu|sina).com","nbzcinsdwww.baidu.comdmaosid"))
# print(re.findall("www.(?:baidu|sina).com","nbzcinsdwww.baidu.comdmaosid"))


# day23 05


# 异常处理
# try:
#     f = open('db2','wb+')
#     f.write('nihao')
# except Exception as e:
#     print(e)
#     f.write(b'haha')
# finally:
#     print('End')
#     f.close()
