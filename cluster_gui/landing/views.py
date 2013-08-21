# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext
import MySQLdb


db = MySQLdb.connect(host="10.7.20.3", # your host, usually localhost
                     user="spincemail", # your username
                     passwd="Seb4sB9oXx", # your password
                     db="information_schema") # name of the data base


def monitor_cluster(request):
        dict={}
        cur = db.cursor()
        message = "NODE01"


 # Use all the SQL you like
        cur.execute("SHOW status LIKE 'wsrep%';")


        for row in cur.fetchall():
            dict.setdefault(row[0],[]).append(row[1])
            #if dict["wsrep_local_state_comment"] == ['Synced']:
                #sync_state =  "cluster synchronised"
            #if dict['wsrep_cluster_size'] == ['2']:
             #   size_cluster =  " All node are up"

            #if dict['wsrep_ready'] == ['ON']:
             #    connection_state = "Node ready for connection"

        return render_to_response('landing.html', {'dict': dict,'cluster_name':message}, context_instance=RequestContext(request))





def home(request):
    message = "cluster_monitoring"

    return render_to_response('base2.html', {'title': message}, context_instance=RequestContext(request))


