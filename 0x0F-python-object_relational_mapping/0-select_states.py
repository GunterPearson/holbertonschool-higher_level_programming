#!/usr/bin/python3
"""Select states"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="127.0.0.1", port=3306, charset="utf8",
                           user=argv[1], passwd=argv[2], db=argv[3])
    Cur = conn.cursor()
    Cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    Rows = Cur.fetchall()
    for row in Rows:
        print(row)
    Cur.close()
    conn.close()
