# import turtle as t
# from random import random

# for i in range(100):
#     steps = int(random() * 100)
#     angle = int(random() * 360)
#     t.right(angle)
#     t.fd(steps)


#-----------------------------------

import turtle
import time as t
skk = turtle.Turtle() 
k = 90
l = 10
for j in range(100):
    skk.right(5)
    for i in range(4): 
        skk.forward(l) 
        skk.right(90) 
    
    l+=1
      
turtle.done() 