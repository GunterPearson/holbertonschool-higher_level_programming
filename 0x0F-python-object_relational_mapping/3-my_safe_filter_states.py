#!/usr/bin/python3
""" safe file"""
import MySQLdb as mysql
import sys

if __name__ == "__main__":
    conn = mysql.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states")
    for row in cur.fetchall():
        if row[1] == sys.argv[4]:
            print(row)
