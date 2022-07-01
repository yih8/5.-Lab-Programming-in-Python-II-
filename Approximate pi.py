import math

import random
from tkinter import N


def calculate_number(n):
    a=0
    for i in range (0,n):
        x=random.uniform(-1,1)
        y=random.uniform(-1,1)
        r=math.sqrt(x*x+y*y)
        if r<1 :
            a+=1
            i+=1
        else:
            i+=1
    c=4*a/n 
    return c 


x= int(input("the accuracy = \n"))

print("pi=",calculate_number(x))


            



