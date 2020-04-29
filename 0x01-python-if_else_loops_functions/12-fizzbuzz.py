#!/usr/bin/python3
def fizzbuzz():
    for x in range(1, 101):
        if x % 3 == 0 and x % 5 == 0:
            print('FizzBuzz', end=' ')
            x += 1
        elif x % 3 == 0:
            print('Fizz', end=' ')
            x += 1
        elif x % 5 == 0:
            print('Buzz', end=' ')
            x += 1
        else:
            print(x, end=' ')
            x += 1
