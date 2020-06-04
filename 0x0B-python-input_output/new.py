#!/usr/bin/python3
with open('test.txt', mode='w', encoding='utf-8') as a_file:
    a_file.write('test succeeded')
with open('test.txt', mode='rb', encoding='utf-8') as a_file:
    print(str(a_file.read()))