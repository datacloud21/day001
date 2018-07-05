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
#             f.seek(doce,2)
#             data = f.readlines()
#             print(data)
#             print(len(data))
#             if len(data) > 1:
#                 print("文件的最后一行是：%s" %(data[-1].decode('utf-8')))
#                 break
#             doce *=2
