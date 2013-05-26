# -*- coding: UTF-8 -*-
from db_config import *

OS="linux"

if OS=="windows":
	import mx.ODBC.Windows
	import MySQLdb
else:
	#import cx_Oracle
	import MySQLdb
	
import string
import time,sys

#####################################
# Fonction Conection à la DB ORACLE.
#####################################
def connect_db_ORACLE():
	while 1:
		try:
			print "connection DB Oracle\n"
			if OS=="windows":
				db = mx.ODBC.Windows.DriverConnect('DSN='+CONFIG_ORACLE_DSN+';UID='+CONFIG_ORACLE_USER+';PWD='+CONFIG_ORACLE_PWD+'')
			else:
				db = cx_Oracle.connect(CONFIG_ORACLE_USER, CONFIG_ORACLE_PWD, CONFIG_ORACLE_TNS)
			print "Connection reussie\n"
			return db
		except:
			print "Attend la connection DB ORACLE\n"
 			time.sleep(15)
			print "Attend la connection DB ORACLE\n"


#####################################			
# Fonction Conection à la DB MySQL Local .
#####################################
def connect_db_MySQL_2(MYSQL_HOST,MYSQL_USER,MYSQL_PASSPWD,MYSQL_DB='',MYSQL_PORT=3306):
        #print "connection a la DB MySQL\n"
	db = MySQLdb.connect(host=MYSQL_HOST,user=MYSQL_USER,passwd=MYSQL_PASSPWD,db=MYSQL_DB,port=MYSQL_PORT)
	#print "Connection reussie\n"
	return db
        """
	while 1:
		try:
			#print "connection a la DB MySQL\n"
			db = MySQLdb.connect(host=MYSQL_HOST,user=MYSQL_USER,passwd=MYSQL_PASSPWD,db=MYSQL_DB)
			#print "Connection reussie\n"
			return db
		except:
			print "Attend la connection de MySQL\n"
			time.sleep(15)
			print "Attend la connection de MySQL\n"
        """                			
#####################################			
# Fonction Conection à la DB MySQL Local .
#####################################
def connect_db_MySQL():   
	while 1:
		try:
			print "connection a la DB MySQL\n"
			db = MySQLdb.connect(host=CONFIG_MYSQL_HOST,user=CONFIG_MYSQL_USER,passwd=CONFIG_MYSQL_PASSPWD,db=CONFIG_MYSQL_DB)
			print "Connection reussie\n"
			return db
		except:
			print "Attend la connection de MySQL\n"
			time.sleep(15)
			print "Attend la connection de MySQL\n"

#####################################			
# Fonction Conection à la DB MySQL Local .
#####################################
def connect_db_MySQL_Master():   
	while 1:
		try:
			print "connection a la DB MySQL\n"
			db = MySQLdb.connect(host=CONFIG_MYSQL_HOST_1,user=CONFIG_MYSQL_USER_1,passwd=CONFIG_MYSQL_PASSPWD_1,db=CONFIG_MYSQL_DB_1)
			print "Connection reussie\n"
			return db
		except:
			print "Attend la connection de MySQL\n"
			time.sleep(15)
			print "Attend la connection de MySQL\n"
			
#####################################			
# Fonction Conection à la DB MySQL Local 2.
#####################################
def connect_db_MySQL_Slave():   
	while 1:
		try:
			print "connection a la DB MySQL 2 - "+CONFIG_MYSQL_HOST_2+"\n"
			db = MySQLdb.connect(host=CONFIG_MYSQL_HOST_2,user=CONFIG_MYSQL_USER_2,passwd=CONFIG_MYSQL_PASSPWD_2,db=CONFIG_MYSQL_DB_2)
			print "Connection reussie\n"
			return db
		except:
			print "Attend la connection de MySQL 2\n"
			time.sleep(15)
			print "Attend la connection de MySQL 2\n"
			

#####################################			
# Fonction Conection à la DB MySQL Spooler.
#####################################
def connect_db_MySQL_Spooler():   
	while 1:
		try:
			print "connection a la DB MySQL Spooler - "+CONFIG_MYSQL_HOST_3+"\n"
			print "user="+CONFIG_MYSQL_USER_3+" passwd="+CONFIG_MYSQL_PASSPWD_3+" db="+CONFIG_MYSQL_DB_3
			db = MySQLdb.connect(host=CONFIG_MYSQL_HOST_3,user=CONFIG_MYSQL_USER_3,passwd=CONFIG_MYSQL_PASSPWD_3,db=CONFIG_MYSQL_DB_3)
			print "Connection reussie\n"
			return db
		except:
			print "Attend la connection de MySQL Spooler\n"
			sys.exit(0)
			time.sleep(15)
			print "Attend la connection de MySQL Sploore\n"
			
			
#####################################
#	recuperation de la liste
#####################################
def get_list_order(fichier):
	list_order=list()
	f = open(fichier,'r')
	
	while 1 :
		ligne = f.readline()
		if not ligne:
			break
		else:
			list_order.append(ligne)
	f.close()
	return list_order
