#!/usr/bin/python3
""" takes in the name of a state as an argument and lists all cities of that
    state, using the database hbtn_0e_4_usa """


from sys import argv
import MySQLdb

if __name__ == "__main__":
    try:

        db = MySQLdb.connect(user=argv[1], password=argv[2], database=argv[3],
                             port=3306, host="localhost")
        cur = db.cursor()
        query = """SELECT cities.name
                FROM cities
                WHERE state_id = (SELECT id FROM states WHERE name = %s)
                """
        cur.execute(query, (argv[4],))
        rows = cur.fetchall()
        size = len(rows)
        for idx in range(size):
            if rows[idx] == rows[size - 1]:
                print(rows[idx][0], end="")
            else:
                print(rows[idx][0], end=', ')
        print()
        cur.close()
        db.close()
    except MySQLdb.Error as e:
        print(e)
