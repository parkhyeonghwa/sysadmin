#!/usr/bin/python
import MySQLdb


db = MySQLdb.connect(host="10.7.20.3", # your host, usually localhost
                     user="spincemail", # your username
                      passwd="Seb4sB9oXx", # your password
                      db="information_schema") # name of the data base

# you must create a Cursor object. It will let
#  you execute all the query you need

def monitor_cluster() :
	dict={}
	cur = db.cursor()


# Use all the SQL you like
	cur.execute("SHOW status LIKE 'wsrep%';")


	for row in cur.fetchall() :
		dict.setdefault(row[0],[]).append(row[1])
	if dict['wsrep_local_state_comment'] == ['Synced']:
		print "cluster synchronised"
	if dict['wsrep_cluster_size'] == ['2']:
		print " All node are up"
		
	if dict['wsrep_ready'] == ['ON']:
		print "Node ready for connection"
		
	
	
	
	
def check_stats() :
	dict={}
	cur = db.cursor()
	cur.execute("SHOW STATUS;")
	for row in cur.fetchall() :
		dict.setdefault(row[0],[]).append(row[1])
	if  dict['Max_used_connections'] > 0:
		print dict['Max_used_connections'] 
		
		
		
		
monitor_cluster()
check_stats()
