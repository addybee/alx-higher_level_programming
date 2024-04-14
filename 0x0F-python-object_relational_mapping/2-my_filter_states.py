#!/usr/bin/python3
""" displays all values in the states table of hbtn_0e_0_usa
    where name matches the argument.
"""


if __name__ == "__main__":

    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(user=argv[1], password=argv[2], database=argv[3],
                         port=3306, host="localhost")
    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name=%s
                ORDER BY id""", (argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
