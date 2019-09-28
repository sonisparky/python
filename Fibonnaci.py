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
def fact(n):
    if n==0:
        return 1
    else:                                                  #Factorial using recursion
        return n*fact(n-1)
