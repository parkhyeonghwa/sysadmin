_author__ = 'pincemail'


#! /usr/bin/env python

"""
 check_belisarius.py

 Author :
  - Sebastien ROHAUT, Axa Tech, for AXA.xx

 Date :
  - 01/20/2014 v0.1
  - 03/05/2014 v0.2 : rename -H to -I (host ip or fqdn), add -H for HTTP Host header : (Host: www.toto.com)

 Nagios/centreon plugin to check belisarius status

 Requirements :
  - Python 2.7.6


 Output :
  - OK : host is responding under warning time
  - UNKNOWN : Return code is not 200
  - CRITICAL :  host is responding after critical time, or not in the timeout => no access, or not healthy

 Stats :
  - Response time in seconds

"""


import logging
import argparse
import datetime
import urllib2


# Return codes for Nagios :
NAGIOS_OK        = 0
NAGIOS_WARNING   = 1
NAGIOS_CRITICAL  = 2
NAGIOS_UNKNOWN   = 3

CONSUMER_HEALTH_URL = "status-frontend-uat-consumerwall"
CONSUMER_PATH_URL = "health-check"
ERROR_COUNT = 0
t_delta = 0

def nagios_exit(status, msg):
        global t_delta

        msg = msg + '|time='+str(t_delta)+'s'
        print msg
        exit(status)

# Main function
def main(argv=None):
        __author__ = 'Slyce'
        CONSUMER_PORT = 80
        global t_delta

        logging.basicConfig()

        parser = argparse.ArgumentParser(description='Consumerwall  for Nagios/Centreon')
        parser.add_argument('-I','--ip', help='Host IP or FQDN', required=True)
        parser.add_argument('-H','--host', help='Host via Header host:', default=False )
        parser.add_argument('-p','--port', help='Port - default 80', type=long, default=CONSUMER_PORT)
        parser.add_argument('-u','--url',help='Health URL', default=CONSUMER_HEALTH_URL)
        parser.add_argument('-s','--ssl',help='SSL Check', action="store_true")
        parser.add_argument('-a','--auth',help='Basic HTTP auth, user:password', default=False)
        parser.add_argument('-k','--key',help='Key to check health', default=CONSUMER_HEALTH_URL)
        parser.add_argument('--version', action='version', version='%(prog)s 0.2')
        args = parser.parse_args()

        CONSUMER_IP = args.ip
        CONSUMER_HOST = args.host
        CONSUMER_KEY = args.key
        CONSUMER_PORT = args.port
        HTTP_AUTH = args.auth
        if args.ssl:
                consumer_scheme = "https"
        else:
               consumer_scheme = "http"


        if  HTTP_AUTH:
                if  HTTP_AUTH.find(':') != -1:
                        user , password =  HTTP_AUTH.split(':')
                else:
                        HTTP_AUTH  = False

        #print belisarius_scheme + "://" + CONSUMER_HOST + ":" + str(CONSUMER_PORT) +   '/' +  CONSUMER_PATH_URL + '/' +  CONSUMER_HEALTH_URL

        URL = consumer_scheme + "://" + CONSUMER_HOST + ":" + str(CONSUMER_PORT)  + '/' + CONSUMER_PATH_URL + '/' + CONSUMER_HEALTH_URL

        TOP_URL = consumer_scheme + '://' + CONSUMER_HOST + ':' + str(CONSUMER_PORT) +   '/' + CONSUMER_PATH_URL + '/' + CONSUMER_HEALTH_URL



        # Basic Auth
        if HTTP_AUTH:
                password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
                password_mgr.add_password(None, TOP_URL , user , password )
                handler = urllib2.HTTPBasicAuthHandler(password_mgr)

                # create "opener" (OpenerDirector instance)
                opener = urllib2.build_opener(handler)

                # Install the opener.
                # Now all calls to urllib2.urlopen use our opener.
                urllib2.install_opener(opener)

        if CONSUMER_HOST:
                request = urllib2.Request(URL, headers={ 'Host' : CONSUMER_HOST } )
        else:
                request = urllib2.Request(URL)


        # time delta start
        t_start = datetime.datetime.now()

        try:
                f = urllib2.urlopen(request)
                http_parse = f.read()
                return_code = f.getcode()

        except urllib2.HTTPError as e:
                return_code =  e.code


        # End time

        t_end = datetime.datetime.now()



        # Delta response time
        t_delta = (t_end - t_start).total_seconds()
        print return_code



        if return_code ==  200 and t_delta <= 2:
                message = "OK:HTTP return code is " + str(return_code)
                nagios_exit(NAGIOS_OK,message)


        if return_code !=  200:
                message = "CRITICAL:HTTP return code is " + str(return_code)
                nagios_exit(NAGIOS_CRITICAL,message)


        if t_delta >= 2:
                message = "WARNING:HTTP return code is " + str(return_code)
                nagios_exit(NAGIOS_WARNING,message)

        else:
                message = "UNKNOWN:HTTP return code is " + str(return_code)
                nagios_exit(NAGIOS_UNKNOWN,message)





# Start main function
if __name__ == "__main__":
        main()

        # Delta response time


