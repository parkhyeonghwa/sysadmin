__author__ = 'pincemail'

import re
import os
import sys
from pymongo import MongoClient, ReadPreference, MongoReplicaSetClient 
import pymongo

_id = ""
host = ""
members = ""
database = "test2"
admin_user = "belisarius"
admin_passwd = "digitalaxaxx"
replicaset  = "rs0"
mongod_port = 27017
mongos_port = 27018
servers =  [ "docker-1:27017","docker-2:27017","docker-3:27017" ]

uri_mongod = "mongodb://"+admin_user+":"+admin_passwd+"@"+"localhost"+":"+str(mongod_port) + "/admin"
uri_mongos = "localhost" +":"+str(mongos_port)

#Connection to mongos and mongod
try:
    mongos = MongoClient(uri_mongos,read_preference=ReadPreference.PRIMARY_PREFERRED)
    mongod = MongoReplicaSetClient(uri_mongod ,replicaSet=replicaset ,read_preference=ReadPreference.PRIMARY_PREFERRED)


except pymongo.errors.ConnectionFailure ,e:
    sys.stderr.write("Connection %s failed: " % e)
    sys.exit(1)

try:
        #Enable the sharding for a database
        mongos.admin.command( "enableSharding" ,database)
        #add nodes to the shard
        mongos.admin.command('addShard' , servers[0] , servers[1] , servers[2])
        #initiate Sharding
        config = {_id: replicaset, members: [
        {_id: 0, host: servers[0]},
        {_id: 1, host: servers[1]},
        {_id: 2, host: servers[2]}]
        }

        mongod.admin.command("replSetInitiate" , config)

except pymongo.errors.OperationFailure ,e:
        sys.stderr.write("Operation %s" % e) 
        error_output_enabled = re.search("enabled",str(e))
        error_output_initialized = re.search("initialized",str(e))
        if error_output_enabled:
                print "sharding already enabled"
                pass

        if error_output_initialized:
                print "initialized"
                pass

try:
        #initiate Sharding
        config = {_id: replicaset, members: [
        {_id: 0, host: servers[0]},
        {_id: 1, host: servers[1]},
        {_id: 2, host: servers[2]}]
        }

        mongod.admin.command("replSetInitiate" , config)

except pymongo.errors.OperationFailure, e:
        error_output = re.search("initialized",str(e))
        if error_output:
                print "sharding already initialized"
                pass

mongod.close()
mongos.close()

