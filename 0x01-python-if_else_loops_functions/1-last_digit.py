#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    newnum = -number
else:
    newnum = number
num = newnum % 10
contain = ["and is greater than 5", "and is 0", "and is less than 6 and not 0"]
if num > 5:
    temp = contain[0]
if num == 0:
    temp = contain[1]
if num < 6 and num != 0:
    temp = contain[2]
print("Last digit of", number, "is", num, temp)
