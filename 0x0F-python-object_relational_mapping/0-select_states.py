#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa
"""
if __name__ == "__main__":
	import MySQLdb
	from sys import argv

	db = MySQLdb.connect(user=argv[1], password=argv[2], database=argv[3],
			port=3306, host="localhost")
	cur = db.cursor()
	cur.execute("SELECT name FROM hbtn_0e_0_usa ORDER BY id")
	rows = cur.fetchall()
	for row in rows:
		print (row)
	cur.close()
    	db.close()
        