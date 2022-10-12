#!/usr/bin/python3
"""
Module that lists all cities and their state from
the database hbtn_0e_0_usa
"""
import sys
import MySQLdb


def connectToDB():
    # Connecting to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         password=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * \
                 FROM cities \
                 ORDER BY cities.id")
    rows = cur.fetchall()
    for item in rows:
        print(item)


if __name__ == "__main__":
    connectToDB()
