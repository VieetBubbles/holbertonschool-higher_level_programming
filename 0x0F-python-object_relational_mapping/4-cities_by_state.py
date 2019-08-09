#!/usr/bin/python3
# Write a script that lists all cities from the database hbtn_0e_4_usa

if __name__ == '__main__':
    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost", port=3306,      # your host
                         user="root",                      # your username
                         passwd="root",                    # your password
                         db=sys.argv[3],               # name of database
                         charset="utf8")

    # you must create a Cursor object. It will let
    #  you execute all the queries you need
    cur = db.cursor()

    # HERE I have to know SQL to grab all states in my database
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities " +
                "LEFT JOIN states ON states.id = cities.state_id ORDER BY" +
                " cities.id ASC")

    # print all the rows in the table
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    db.close()
