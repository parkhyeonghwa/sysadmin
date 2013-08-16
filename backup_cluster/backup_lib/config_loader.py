__author__ = 'sype'

import ConfigParser
import commands
import os
import time
import gzip
import glob
import MySQLdb



Config = ConfigParser.ConfigParser()
Config.read("/home/sype/PycharmProjects/backup_cluster/backup_config.ini")
date = time.strftime("%d-%m-%Y")





def ConfigSectionMap(section):
    """

    :param section:
    :return:
    """
    if section != 'BackupConfig':
        hostname = Config.get(section, 'Hostname')
        user = Config.get(section, 'User')
        passwd = Config.get(section, 'Password')
        databases = Config.get(section, 'Schemas')
        ip = Config.get(section, 'IP')
        log = ''
        command = ''
        option = ''
        retention = ''
        path = ''


    else:

        command = Config.get('BackupConfig', 'Command')
        path = Config.get('BackupConfig', 'Path')
        option = Config.get('BackupConfig', 'Option')
        retention = Config.get('BackupConfig', 'Retention')
        log = Config.get('BackupConfig', 'Log')
        databases = ''
        hostname = ''
        user = ''
        passwd = ''
        ip = ''

    #backup_file = "{} {} str(date)+'.sql".format(str(path),str(hostname))
    #backup_file = "%s %s %s .sql" % (path, hostname)
    return command, hostname, ip, passwd, user, path, option, databases, retention, log


def backup_node(node):
    #Choose the cluster node to backup
    FILE_SQL_SIZE = 0
    FILE_GZ_SIZE = 0
    if node == 'node02':
        section = 'NodeTwo'
    else:
        section = 'NodeOne'
    param = ConfigSectionMap(section)
    config = ConfigSectionMap('BackupConfig')
    state = get_cluster_state(section)
    backed_file = "{path}{hostname}-{date}.sql".format(path=config[5],
                                                       hostname=param[1],
                                                       date=str(date))
    #debug
    #backed_file=backup_file
    backup_exec = "{command} -h{host} -u{user} -p{passwd} {option} {databases} > {backed_file}".format(
        command=config[0],
        host=param[1],
        user=param[4],
        passwd=param[3],
        option=config[6],
        databases=param[7],
        backed_file=backed_file)

    try:
        backup_result = commands.getstatusoutput(backup_exec)
        backup_status = "Backup executed"
        FILE_SQL_SIZE = check_file_size(backed_file)
        code_error = backup_result[0]
    except:
        backup_status = "Backup failed!"
        code_error = backup_result[0]

    else:
        compress_file_in = open(backed_file, 'rb')
        compress_file_out = gzip.open(backed_file + '.gz', 'wb')
        compress_file_out.writelines(compress_file_in)
        compress_file_in.close()
        compress_file_out.close()

    #logging process to improve
    backup_log(state[0])
    backup_log(state[1])
    backup_log(str(code_error))
    return code_error, backup_status, FILE_SQL_SIZE, state




def cleaner(retention=Config.get('BackupConfig', 'Retention')):

#Delete all sql files and archives above the retention policy
    path = Config.get('BackupConfig', 'Path')
    CMD = "find {path} -name '*.gz' -ctime +{retention} {delete}".format(path=str(path),
                                                                         retention=str(retention),
                                                                         delete="-exec rm {} \;")
    suppression_archive = os.system(CMD)
    #debug
    print CMD

    sql_file = glob.glob(path + '/*.sql')
    if len(sql_file) > 1:
        for files in sql_file:
            os.remove(files)
    else:
        os.remove(sql_file[0])
    if suppression_archive != 0:
        delete_error = "Error while deleting files"
    else:
        delete_error = "All archives create before {retention} days have been erased".format(retention=str(retention))
        #debug
    print sql_file
    return delete_error


def connection(node, schema):
    """

    :param node:
    :return:
    """
    param = ConfigSectionMap(node)

    try:

        db = MySQLdb.connect(host=(param[1]), user=(param[4]), passwd=(param[3]), db=schema)
        print "Connection sucess"
        connection_status = "Connection sucess"




        return db

    except MySQLdb.ProgrammingError:

        print "Problem with connection"
        connection_status = "Problem with connection"



    return connection_status

def get_cluster_state(node):
    db = connection(node, "information_schema")
    dict = {}
    cur = db.cursor()


 # Use all the SQL you like
    cur.execute("SHOW status LIKE 'wsrep%';")


    for row in cur.fetchall() :

        dict.setdefault(row[0], []).append(row[1])
        for key, value in dict.items():

            if key == "wsrep_cluster_state_uuid":
                cluster_state = "\nPosition du cluster"+" "+value[0]+"\n"


            if key == "wsrep_local_state_uuid":
                local_state = "\nPosition du node"+" "+value[0]+"\n"

    return cluster_state, local_state




def check_file_size(path_file):
    size_file = 0
    if path_file != '':
        if os.path.exists(path_file):

            size_file = str(os.path.getsize(path_file)/1048576) + "MB"
        else:
            print 'Path file is not a file : ', path_file

    else:
            print 'Path file is empty : ', path_file
    backup_log(str(size_file))
    print size_file





def backup_log(info):


    config = ConfigSectionMap('BackupConfig')
    log = config[9]
    if os.path.exists(log):
        f = open(log, 'a+')
        f.write(info)
    else:
        f = open(log, 'wb')
        f.write(info)
    f.close()














            #print key, value[0]
        #print dict['wsrep_local_state_uuid']

























        #return backup


if __name__ == '__main__':

    conf = ConfigSectionMap('NodeOne')
    status = backup_node('node01')
    cleaner()

    #state = get_cluster_state('NodeOne')
    #backup_log(status[1])
    #backup_log(state[0])
    #backup_log(state[1])
    print status[1]











