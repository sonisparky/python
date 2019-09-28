# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 17:55:24 2018

@author: Payilagam
"""

a,b=0,1
while b<100:
      print(b)
      a,b = b,a+b
#another method using recursion
def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1) + fib(n-2)                        #fibonacci using recurssion
num=int(input("enter the number :"))
for i in range(num):
    print(fib(i))
