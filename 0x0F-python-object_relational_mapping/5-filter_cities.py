#!/usr/bin/python3
# Write a script that takes in the name of a state as an argument and lists
# all cities of that state, using the database hbtn_0e_4_usa

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
    stemp = ""

    dig = "SELECT cities.id, cities.name, states.name FROM cities " +\
          "LEFT JOIN states ON states.id = cities.state_id " +\
          "WHERE states.name = %s ORDER BY cities.id ASC"

    # HERE I have to know SQL to grab all states in my database
    cur.execute(dig, [sys.argv[4]])

    # print all the rows in the table
    query_rows = cur.fetchall()

    for row in query_rows:
        stemp += str(row[1]) + ", "
    pcity = stemp.strip(" ,")
    print(pcity)

    cur.close()
    db.close()
