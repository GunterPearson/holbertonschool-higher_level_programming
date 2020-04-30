#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, div, mul
    import sys
    argv = sys.argv
    check = ['+', '-', '*', '/']
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    for x in range(len(check)):
        if argv[2] == check[0]:
            print("{} + {} = {}".format(argv[1], argv[3], add(int(argv[1]), int(argv[3]))))
            break
        elif argv[2] == check[1]:
            print("{} - {} = {}".format(argv[1], argv[3], sub(int(argv[1]), int(argv[3]))))
            break
        elif argv[2] == check[2]:
            print("{} * {} = {}".format(argv[1], argv[3], mul(int(argv[1]), int(argv[3]))))
            break
        elif argv[2] == check[3]:
            print("{} / {} = {}".format(argv[1], argv[3], div(int(argv[1]), int(argv[3]))))
            break
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
