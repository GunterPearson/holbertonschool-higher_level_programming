#!/usr/bin/python3
""" show cities and states """
import MySQLdb as mysql
import sys

if __name__ == "__main__":
    conn = mysql.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name\
    FROM cities, states WHERE states.id=cities.state_id")
    for row in cur.fetchall():
        print(row)
