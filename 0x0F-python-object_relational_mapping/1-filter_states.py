#!/usr/bin/python3
""" lists all states with a name starting with N (upper N)
    from the database hbtn_0e_0_usa
"""


if __name__ == "__main__":

    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(user=argv[1], password=argv[2], database=argv[3],
                         port=3306, host="localhost")
    query = "SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY id"
    db.query(query)
    rows = db.store_result().fetch_row(maxrows=0)
    for row in rows:
        print(row)
    db.close()
