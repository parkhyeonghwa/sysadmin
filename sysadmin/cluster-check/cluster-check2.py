#!/usr/bin/python
import MySQLdb

dict={}
db = MySQLdb.connect(host="10.7.20.3", # your host, usually localhost
                     user="spincemail", # your username
                      passwd="Seb4sB9oXx", # your password
                      db="information_schema") # name of the data base

# you must create a Cursor object. It will let
#  you execute all the query you need
cur = db.cursor() 

# Use all the SQL you like
cur.execute("SHOW status LIKE 'wsrep%';")


for row in cur.fetchall() :
	dict.setdefault(row[0],[]).append(row[1])
if dict['wsrep_local_state_comment'] == ['Synced']:
	print "cluster synchronised"
if dict['wsrep_cluster_state_uuid'] == dict['wsrep_local_state_uuid']:
	print " Right state"
