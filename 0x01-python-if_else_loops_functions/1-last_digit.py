#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
new = abs(number) % 10
contain = ["and is greater than 5", "and is 0", "and is less than 6 and not 0"]
if number < 0:
    new = -new
if new > 5:
    temp = contain[0]
if new == 0:
    temp = contain[1]
if new < 6 and new != 0:
    temp = contain[2]
print("Last digit of", number, "is", new, temp)
