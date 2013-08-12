__author__ = 'sype'


import ConfigParser
import commands, os, time
import gzip
import glob

Config = ConfigParser.ConfigParser()
Config.read("/home/sype/PycharmProjects/backup_cluster/backup_config.ini")

def ConfigSectionMap(section):

    hostname = Config.get(section,'Hostname')
    date = time.strftime("%d-%m-%Y")
    ip = Config.get(section,'IP')
    user = Config.get(section,'User')
    passwd = Config.get(section, 'Password')
    command = Config.get('BackupConfig','Command')
    path = Config.get('BackupConfig','Path')
    option = Config.get('BackupConfig','Option')
    databases = Config.get(section,'Schemas')
    backup_file = "{path}{hostname}-{date}.sql".format(path=str(path),
                                                             hostname=str(hostname),
                                                             date=str(date))
    retention = Config.get('BackupConfig','Retention')
    #backup_file = "{} {} str(date)+'.sql".format(str(path),str(hostname))
    #backup_file = "%s %s %s .sql" % (path, hostname)
    return command, hostname, ip, passwd, user, path, option, databases, backup_file, retention





def backup_node(node):

    if  node == 'node02':
        section = 'NodeTwo'
    else:
        section = 'NodeOne'
    param = ConfigSectionMap(section)
    backed_file=param[8]
    backup_exec = "{command} -h{host} -u{user} -p{passwd} {option} {databases} > {backed_file}".format(command=param[0],
                                                                                                  host=param[1],
                                                                                                  user=param[4],
                                                                                                  passwd=param[3],
                                                                                                  option=param[6],
                                                                                                  databases=param[7],
                                                                                                 backed_file=param[8])



    try:
        backup_result = commands.getstatusoutput(backup_exec)
        backup_status = "Backup executed"
        code_error = backup_result[0]
    except:
        backup_status = "Backup failed!"
        code_error = backup_result[0]

    else:
        compress_file_in = open(backed_file, 'rb')
        compress_file_out = gzip.open(backed_file+'.gz','wb')
        compress_file_out.writelines(compress_file_in)
        compress_file_in.close()
        compress_file_out.close()

    return code_error, backup_status





def cleaner(retention):


    path = Config.get('BackupConfig','Path')
    CMD = "find {path} -name '*.gz' -ctime +{retention} {delete}".format(path=str(path),
                                                                        retention=str(retention),
                                                                        delete="-exec rm {} \;")
    suppression_archive = os.system(CMD)

    print CMD

    sql_file = glob.glob(path + '/*.sql')
    if len(sql_file) > 1:
        for files in sql_file:
            os.remove(files)
    else:
        os.remove(sql_file[0])
    if suppression_archive != 0:
        delete_error = "Error while erasing files"
    else:
        delete_error = "All archives create before {retention} days have been erased".format(retention=str(retention))
    print sql_file
    return delete_error





















    #return backup
if __name__=='__main__':

    conf = ConfigSectionMap('NodeOne')
    status = backup_node('node01')
    cleaner(20)
    print status[1]











