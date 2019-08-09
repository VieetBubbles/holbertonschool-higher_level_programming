#!/usr/bin/python3
# Write a script that lists all states from the database hbtn_0e_0_usa

import MySQLdb

db = MySQLdb.connect(host="localhost", port=3306,      # your host, usually localhost
                     user="root",                      # your username
                     passwd="root",                    # your password
                     db="hbtn_0e_0_usa",               # name of the data base
                     charset="utf8")

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database

# print all the rows in the table
query_rows = cur.fetchall()

if __name__ == '__main__':
    for row in query_rows:
        if row[1][0] == "N":
            print(row)

cur.close()
db.close()
