#!/usr/bin/python3
# Write a script that takes in an argument and displays all values in the
# states table of hbtn_0e_0_usa where name matches the argument.

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
    cur.execute("SELECT * FROM states WHERE name = '{}' ORDER BY id ASC"
                .format(sys.argv[4]))

    # print all the rows in the table
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    db.close()
