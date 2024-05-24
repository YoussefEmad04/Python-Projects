import math
from turtle import *

def heart1(k):
    return 15 * math.sin(k)**3

def heart2(k):
    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

speed(1000)
bgcolor('black')

for i in range(6000):
    goto(heart1(i) * 20, heart2(i) * 20)
    for j in range(5):
        color("red")
        # Additional correction: Add the following line to fill the heart shape with red color
        begin_fill()
    end_fill()

done()

    