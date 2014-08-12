__author__ = 'pincemail'

import re
import sys
from pymongo import MongoClient, ReadPreference
import pymongo

_id = ""
host = ""
members = ""
master_node = "docker-2"
admin_user = "belisarius"
admin_passwd = "digitalaxaxx"

mongod_port = 27017
mongos_port = 27018

uri_mongod = "mongodb://"+admin_user+":"+admin_passwd+"@"+master_node+":"+str(mongod_port) + "/admin"
uri_mongos = master_node +":"+str(mongos_port)

#Connection to mongos and mongod
try:
    s = MongoClient(uri_mongos,read_preference=ReadPreference.SECONDARY)
    d = MongoClient(uri_mongod ,read_preference=ReadPreference.SECONDARY)
#    s.admin.authenticate(admin_user,admin_passwd)
except pymongo.errors.ConnectionFailure ,e:
    sys.stderr.write("Connection %s failed: " % e)
    sys.exit(1)


try:
        #Enable the sharding for a database
        s.admin.command( "enableSharding" ,'test2')
        #add nodes to the shard
        s.admin.command('addShard' , "docker-1:27017" , "docker-2:27017" ,"docker-3:27017")
        #initiate Sharding
        config = {_id: 'rs0', members: [
        {_id: 0, host: 'docker-1:27017'},
        {_id: 1, host: 'docker-2:27017'},
        {_id: 2, host: 'docker-3:27017'}]
        }

        d.admin.command("replSetInitiate" , config)

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

                #sys.exit(0)

try:
#initiate Sharding
        config = {_id: 'rs0', members: [
        {_id: 0, host: 'docker-1:27017'},
        {_id: 1, host: 'docker-2:27017'},
        {_id: 2, host: 'docker-3:27017'}]
        }

        d.admin.command("replSetInitiate" , config)

except pymongo.errors.OperationFailure, e:
        #sys.stderr.write("Connection %s failed: " % e)
        error_output = re.search("initialized",str(e))
        if error_output:
                print "sharding already initialized"
                pass
