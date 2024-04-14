#!/usr/bin/python3
""" displays all values in the states table of hbtn_0e_0_usa
    where name matches the argument.
"""


from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], password=argv[2], database=argv[3],
                         port=3306, host="localhost")
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name='{}' ORDER BY id".format(argv[4])
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
