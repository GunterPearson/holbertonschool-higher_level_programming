#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == '':
        list = [len(sentence), None]
    else:
        list = [len(sentence), sentence[0]]
    return tuple(list)
