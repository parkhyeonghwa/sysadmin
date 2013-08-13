__author__ = 'sype'


import ConfigParser
import commands,os, time
import gzip
import glob

Config = ConfigParser.ConfigParser()
Config.read("/home/sype/PycharmProjects/backup_cluster/backup_config.ini")
date = time.strftime("%d-%m-%Y")


def ConfigSectionMap(section):

    """

    :param section:
    :return:
    """
    if section != 'BackupConfig':
        hostname = Config.get(section,'Hostname')
        user = Config.get(section,'User')
        passwd = Config.get(section, 'Password')
        databases = Config.get(section,'Schemas')
        ip = Config.get(section,'IP')
        command = ''
        option = ''
        retention = ''
        path = ''


    else:

        command = Config.get('BackupConfig','Command')
        path = Config.get('BackupConfig','Path')
        option = Config.get('BackupConfig','Option')
        retention = Config.get('BackupConfig','Retention')
        databases = ''
        hostname = ''
        user = ''
        passwd = ''
        ip = ''

    #backup_file = "{} {} str(date)+'.sql".format(str(path),str(hostname))
    #backup_file = "%s %s %s .sql" % (path, hostname)
    return command, hostname, ip, passwd, user, path, option, databases, retention





def backup_node(node):
    #selection du noeud a backuper
    if  node == 'node02':
        section = 'NodeTwo'
    else:
        section = 'NodeOne'
    param = ConfigSectionMap(section)
    config = ConfigSectionMap('BackupConfig')
    backup_file = "{path}{hostname}-{date}.sql".format(path=config[5],
                                                             hostname=param[1],
                                                             date=str(date))
    #debug
    print backup_file
    backed_file=backup_file
    backup_exec = "{command} -h{host} -u{user} -p{passwd} {option} {databases} > {backed_file}".format(command=config[0],
                                                                                                  host=param[1],
                                                                                                  user=param[4],
                                                                                                  passwd=param[3],
                                                                                                  option=config[6],
                                                                                                  databases=param[7],
                                                                                                 backed_file=backup_file)



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
    #debug
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
    #debug
    print sql_file
    return delete_error





















    #return backup
if __name__=='__main__':

    conf = ConfigSectionMap('NodeOne')
    status = backup_node('node01')
    cleaner(2)
    print status[1]











