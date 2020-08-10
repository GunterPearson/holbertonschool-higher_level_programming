#!/usr/bin/python3
""" lists all states from hbtn_0e_0_usa """
import MySQLdb as mysql
import sys

if __name__ == "__main__":
    conn = mysql.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name REGEXP '^[n]'\
ORDER BY id ASC")
    for row in cur.fetchall():
        print(row)
