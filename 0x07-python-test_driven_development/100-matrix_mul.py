#!/usr/bin/python3
"""
100-matrix module
files in this mod:
matrix_mul
"""


def matrix_mul(m_a, m_b):
    """
    multiplies matrix
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if type(m_a[0]) is not list:
        raise TypeError("m_a must be a list of lists")
    if type(m_b[0]) is not list:
        raise TypeError("m_b must be a list of lists")
    r = all(type(y) in [int, float] for row in m_a for y in row)
    if not r:
        raise TypeError("m_a should contain only integers or floats")
    r = all(type(y) in [int, float] for row in m_b for y in row)
    if not r:
        raise TypeError("m_b should contain only integers or floats")
    r = all(len(row) == len(m_a[0]) for row in m_a)
    if not r:
        raise TypeError("each row of m_a must be of the same size")
    r = all(len(row) == len(m_b[0]) for row in m_b)
    if not r:
        raise TypeError("each row of m_b must be of the same size")
    holder = []
    new = []
    t = 0
    for x in range(len(m_a)):
        for y in range(len(m_b[0])):
            for z in range(len(m_b)):
                t += m_a[x][z] * m_b[z][y]
            holder.append(t)
            t = 0
        new.append(holder)
        holder = []
    return new
