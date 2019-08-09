#!/usr/bin/python3
# Write a script that lists all states from the database hbtn_0e_0_usa

if __name__ == '__main__':
    import MySQLdb

    db = MySQLdb.connect(host="localhost", port=3306,      # your host
                         user="root",                      # your username
                         passwd="root",                    # your password
                         db="hbtn_0e_0_usa",               # name of database
                         charset="utf8")

    # you must create a Cursor object. It will let
    #  you execute all the queries you need
    cur = db.cursor()

    # HERE I have to know SQL to grab all states in my database
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # print all the rows in the table
    query_rows = cur.fetchall()

    for row in query_rows:
        if row[1][0] == "N":
            print(row)

    cur.close()
    db.close()
