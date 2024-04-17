#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
from sys import argv

# The code should not be executed when imported
if __name__ == '__main__':

    # make a connection to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
     # It gives us the ability to have multiple seperate working environments
    # through the same connection to the database.
    cur = db.cursor()
    sql = """SELECT c.id, c.name, s.name
          FROM states s, cities c
          WHERE c.state_id = s.id
          ORDER BY c.id ASC"""
    cursor.execute(sql)

    data = cursor.fetchall()

    for row in data:
        print(row)

    cursor.close()
    db.close()
