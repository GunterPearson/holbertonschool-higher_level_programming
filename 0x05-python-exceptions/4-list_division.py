#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    quot = 0
    for i in range(list_length):
        try:
            quot = my_list_1[i] / my_list_2[i]
        except IndexError:
            print("out of range")
            quot = 0
        except TypeError:
            print("wrong type")
            quot = 0
        except ZeroDivisionError:
            print("division by 0")
            quot = 0
        finally:
            new_list.append(quot)
    return new_list
