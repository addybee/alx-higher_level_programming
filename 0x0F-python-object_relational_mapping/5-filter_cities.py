#!/usr/bin/python3
""" takes in the name of a state as an argument and lists all cities of that
    state, using the database hbtn_0e_4_usa """


from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = None
    cur = None
    try:

        db = MySQLdb.connect(user=argv[1], password=argv[2], database=argv[3],
                             port=3306, host="localhost")
        cur = db.cursor()
        query = """SELECT cities.name
                FROM cities
                INNER JOIN states
                ON cities.state_id = states.id
                WHERE states.name = %s
                ORDER BY cities.id"""
        size = cur.execute(query, (argv[4],))
        rows = cur.fetchall()
        for row in rows:
            if row == rows[size - 1]:
                print(row[0])
            else:
                print(row[0], end=', ')
    except MySQLdb.Error:
        pass
    finally:
        if cur:
            cur.close()
        if db:
            db.close()
