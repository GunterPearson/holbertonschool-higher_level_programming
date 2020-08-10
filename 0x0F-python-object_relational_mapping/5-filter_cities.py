#!/usr/bin/python3
""" show cities and states """
import MySQLdb as mysql
import sys

if __name__ == "__main__":
    conn = mysql.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT cities.name FROM cities\
    LEFT JOIN states ON cities.state_id = states.id\
    WHERE states.name = '{}'".format(sys.argv[4]))
    rows = cur.fetchall()
    for i in range(len(rows)):
        print(rows[i][0], end="" if i == len(rows) - 1 else ", ")
    print()
