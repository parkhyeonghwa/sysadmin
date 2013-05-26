# -*- coding: UTF-8 -*-
import sys, commands, time, os, connect, MySQLdb
from db_config import db_list
import functions
from imailer import iMailer

LOG_PATH = '/usr/local/tools/backup/'
BACKUP_PATH = '/var/lib/mysql/DB-BACKUP/'

MYSQL_SCHEMAS_PRODUCTION = 'PRODUCTION mysql'
MYSQL_SCHEMAS_IPROD = 'iprod_amq iprod_core iprod_events iprod_renderer mysql'


def backups():

    for db_infos in db_list:
        
            IP = ''
            USER = ''
            PASSWORD = ''
            DATABASE = ''
            PORT = ''
            RETURNS = ''
            ISBACKUP = ''
            HOSTNAME = ''
            DB_TYPE = ''
            CMD = ''
            CMD_STATUS = ''
            CMD_PIGZ = ''
            BACKUPNAME = ''
            DAY = ''
            DATE = ''
            BIN_LOG_FILE_NAME = ''
            BIN_LOG_POSITION = ''
            TEMPS_DEBUT = ''
            TEMPS_FIN = ''
            TEMPS_PROCESS = ''
            FILE_SQL_SIZE = 0
            FILE_ZIP_SIZE = 0
            BACKUPNAME = ''
            BACKUPNAMECOMPRESS = ''
            LOGNAME = ''
            MSG_ERROR = ''
            SUBJECT_MSG = ''
            infosStatus = ''

            DB_TYPE = db_infos[1]
            IP = db_infos[2]
            USER =  db_infos[3]
            PASSWORD =  db_infos[4]
            DATABASE =  db_infos[7]
            PORT = int(db_infos[5])
            PAYS = db_infos[8]
            ISBACKUP = db_infos[9]
            HOSTNAME = db_infos[10]
            DAY = time.strftime("%A")
            DATE = time.strftime("%d/%m/%Y")

            if ISBACKUP!='':
                #print IP,' - ',USER,' - ',PASSWORD,' - ',DATABASE,' - ',PORT,' - ',ISBACKUP,' - ',HOSTNAME,' - ',DAY
                print 'START DUMP FOR : ',HOSTNAME,'',time.strftime("%d/%m/%Y %H:%M:%S")     
                
                BACKUPNAME = BACKUP_PATH+'fullbackup-'+str(HOSTNAME)+'-'+str(DAY)+'.sql'
                BACKUPNAMECOMPRESS = BACKUPNAME+".gz"
                LOGNAME = LOG_PATH+'log-'+str(HOSTNAME)+'-'+str(DAY)+'.txt'
                
                LOG_PART_1 = ''
                LOG_PART_1 = LOG_PART_1+str("############################\n")
                LOG_PART_1 = LOG_PART_1+str("###  BACKUP "+str(HOSTNAME.upper())+"  ###\n")
                LOG_PART_1 = LOG_PART_1+str("###  START "+str(time.strftime("%H:%M:%S"))+"      ###\n")
                LOG_PART_1 = LOG_PART_1+str("###  DAY ---> "+str(DAY)+"   ###\n")
                LOG_PART_1 = LOG_PART_1+str("###  DATE "+str(DATE)+"     ###\n")
                LOG_PART_1 = LOG_PART_1+str("############################\n")
                LOG_PART_1 = LOG_PART_1+str("----------------------------\n")

                functions.create_log(LOGNAME,LOG_PART_1)

                ###########################################
                # START STATUS.
                ###########################################
                if DB_TYPE=='Master':
                    db_connect = connect.connect_db_MySQL_2(IP,USER,PASSWORD,'',PORT)

                    query = "SHOW MASTER STATUS"
                    cursor_mysql = db_connect.cursor()
                    cursor_mysql.execute(query)
                    infosStatus = cursor_mysql.fetchall()
                    cursor_mysql.close

                    BIN_LOG_FILE_NAME = infosStatus[0][0]
                    BIN_LOG_POSITION = infosStatus[0][1]

                    print 'BIN LOG : ',BIN_LOG_FILE_NAME,' - ',BIN_LOG_POSITION
                                    
                    db_connect.close()
                ###########################################
                # END STATUS.
                ###########################################
                 
                LOG_PART_2 = ''
                LOG_PART_2 = LOG_PART_2+str("+ BackupName : "+str(BACKUPNAME)+"\n")
                LOG_PART_2 = LOG_PART_2+str("+ Start Time : "+time.strftime("%H:%M:%S")+"\n")
                LOG_PART_2 = LOG_PART_2+str("+ BackupFile : "+str(BACKUPNAME)+"\n")
                LOG_PART_2 = LOG_PART_2+str("+ Dump MySQL start : "+str(time.strftime("%H/%M/%S"))+"\n")

                ###########################################
                # START DUMP.
                ###########################################
                TEMPS_DEBUT = time.time()

                
                print "TEST !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
                
                if DATABASE == 'PRODUCTION':
                    CMD = "mysqldump -h "+str(IP)+" -u "+str(USER)+" -p"+str(PASSWORD)+" -P"+str(PORT)+" --quick --single-transaction --add-drop-table --complete-insert --databases "+str(MYSQL_SCHEMAS_PRODUCTION)+" > "+str(BACKUPNAME)+""

                if DATABASE == 'iprod':
                    CMD = "mysqldump -h "+str(IP)+" -u "+str(USER)+" -p"+str(PASSWORD)+" -P"+str(PORT)+" --quick --single-transaction --add-drop-table --complete-insert --ignore-table=iprod_amq.ACTIVEMQ_LOCK --databases "+str(MYSQL_SCHEMAS_IPROD)+" > "+str(BACKUPNAME)+""

                """
                if DATABASE == 'PRODUCTION':
                    CMD = "/usr/local/mysql/bin/mysqldump -h "+str(IP)+" -u "+str(USER)+" -p"+str(PASSWORD)+" -P"+str(PORT)+" \
                           --quick \
                           --lock-all-tables \
                           --master-data=2 \
                           --add-drop-table \
                           --complete-insert \
                           --databases "+str(MYSQL_SCHEMAS_PRODUCTION)+" > "+str(BACKUPNAME)+""

                if DATABASE == 'iprod':
                    CMD = "/usr/local/mysql/bin/mysqldump -h "+str(IP)+" -u "+str(USER)+" -p"+str(PASSWORD)+" -P"+str(PORT)+" \
                           --quick \
                           --add-drop-table \
                           --complete-insert \
                           --ignore-table=iprod_amq.ACTIVEMQ_LOCK \
                           --databases "+str(MYSQL_SCHEMAS_IPROD)+" > "+str(BACKUPNAME)+""
                """ 

                print commands.getoutput(CMD)

                TEMPS_FIN = time.time()
                
                LOG_PART_2 = LOG_PART_2+str("+ Dump MySQL done : "+str()+"\n")

                TEMPS_PROCESS = TEMPS_FIN - TEMPS_DEBUT
                ###########################################
                # END  DUMP.
                ###########################################
                
                FILE_SQL_SIZE = functions.check_file_size(BACKUPNAME)
                LOG_PART_2 = LOG_PART_2+str("+ Backup Size Uncompressed : "+str(FILE_SQL_SIZE/1024/1024)+"M\n")

                ###########################################
                # START PIGZ FILE.
                ###########################################
                functions.del_file(BACKUPNAMECOMPRESS)
                #CMD_PIGZ = "gzip "+str(BACKUPNAME)+""
                CMD_PIGZ = "pigz "+str(BACKUPNAME)+""
                commands.getoutput(CMD_PIGZ)
                FILE_ZIP_SIZE = functions.check_file_size(BACKUPNAMECOMPRESS)
                ###########################################
                # END PIGZ FILE.
                ###########################################
                
                LOG_PART_2 = LOG_PART_2+str("+ Backup Size Compressed : "+str(FILE_ZIP_SIZE/1024/1024)+"M\n")
                LOG_PART_2 = LOG_PART_2+str("+ Master File : "+str(BIN_LOG_FILE_NAME)+"\n")
                LOG_PART_2 = LOG_PART_2+str("+ Master Position : "+str(BIN_LOG_POSITION)+"\n")
                LOG_PART_2 = LOG_PART_2+str("+ Time Processing : "+str(round(TEMPS_PROCESS/60))+"s\n")
                LOG_PART_2 = LOG_PART_2+str("+ End Time : "+str(time.strftime("%H:%M:%S"))+"\n")

                functions.create_log(LOGNAME,LOG_PART_2)

                LOG_PART_3 = ''
                LOG_PART_3 = LOG_PART_3+str("----------------------------\n")
                LOG_PART_3 = LOG_PART_3+str("############################\n")
                LOG_PART_3 = LOG_PART_3+str("###  DAY ---> "+str(DAY)+"   ###\n")
                LOG_PART_3 = LOG_PART_3+str("###  END "+str(time.strftime("%H/%M/%S"))+"        ###\n")
                LOG_PART_3 = LOG_PART_3+str("###  BACKUP "+str(HOSTNAME.upper())+"  ###\n")
                LOG_PART_3 = LOG_PART_3+str("############################\n")
                

                functions.create_log(LOGNAME,LOG_PART_3)

                print 'STOP DUMP FOR : ',HOSTNAME,'',time.strftime("%d/%m/%Y %H:%M:%S")

                if FILE_SQL_SIZE <= 500 or FILE_ZIP_SIZE <= 500:
                    SUBJECT_MSG = 'ERREUR LORS DE DU BACKUP DE LA BASE : '+str(HOSTNAME)
                    MSG_ERROR = 'ERREUR LORS DE DU BACKUP DE LA BASE : '+str(HOSTNAME)+'<br>'
                    MSG_ERROR = MSG_ERROR+'IP : '+str(IP)+'<br>'
                    MSG_ERROR = MSG_ERROR+'DB : '+str(DATABASE)+'<br>'
                    MSG_ERROR = MSG_ERROR+'BACKUP FILE : '+str(BACKUPNAME)+'<br>'
                    MSG_ERROR = MSG_ERROR+'BACKUP FILE ZIP : '+str(BACKUPNAMECOMPRESS)+'<br>'
                    MSG_ERROR = MSG_ERROR+'LOG FILE : '+str(LOGNAME)+'\n'

                if MSG_ERROR!="":
                    mailer = iMailer()
                    mailer.SetTmpDir("/tmp/")
                    mailer.SetSmtp("localhost")
                    mailer.SetSrc("cougar@photoways.com")
                    mailer.SetSubject(SUBJECT_MSG)
                    mailer.AddDest("sebastien.pincemail@photobox.com")
                    mailer.SetMail(MSG_ERROR)
                    try:
                        mailer.Mailer()
                    except:
                        print 'Impossible d\'envoyer le mail'

            

do_backup = backups()











