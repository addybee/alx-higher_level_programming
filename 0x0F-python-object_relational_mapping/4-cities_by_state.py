#!/usr/bin/python3
""" displays all values in the states table of hbtn_0e_0_usa
    where name matches the argument.
"""


from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = None
    cur = None
    try:

        db = MySQLdb.connect(user=argv[1], password=argv[2], database=argv[3],
                             port=3306, host="localhost")
        cur = db.cursor()
        query = """SELECT cities.id, cities.name, states.name
                FROM cities
                INNER JOIN states
                ON cities.state_id = states.id
                ORDER BY cities.id"""
        cur.execute(query)
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except MySQLdb.Error:
        pass
    finally:
        if cur:
            cur.close()
        if db:
            db.close()
