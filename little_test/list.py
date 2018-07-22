#!/usr/bin/env pthon
# -*- coding:utf-8 -*-
# Author: Mr.
# 购物小程序
salary = input("input your salary:")
if salary.isdigit():
    salary = int(salary)
else:
    exit("Invaild data type...")

welcome_msg = 'welcome to my world!'.center(50, '-')
print(welcome_msg)
exit_flag = False
product_list = [
    ('Iphone', 5888),
    ('Mac Air', 6666),
    ('Tesla', 66),
    ('Bike', 888)
]
shop_car = []
while exit_flag is not True:
    for item in enumerate(product_list):
        index = item[0]
        # print(index)
        name = item[1][0]
        price = item[1][1]
        print(index, '.', name, price)
    user_choice = input("[q=quit,c=check]what do you want to buy?:")
    if user_choice.isdigit():
        user_choice = int(user_choice)
        if user_choice < len(product_list):
            p_item = product_list[user_choice]
            print(p_item)
            print(len(product_list))
            if p_item[1] <= salary:
                shop_car.append(p_item)
                salary -= p_item[1]
                print("Added [%s] into shop car,you current balance is [%s]" % (p_item, salary))
            else:
                print("Your balance is [%s],cannot afford this.." % salary)
