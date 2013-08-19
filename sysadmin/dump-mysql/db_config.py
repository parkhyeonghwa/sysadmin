CONFIG_MYSQL_HOST_1 = '10.10.6.1'
CONFIG_MYSQL_USER_1 = 'purge'
CONFIG_MYSQL_PASSPWD_1 = 'B4tc4e'
CONFIG_MYSQL_DB_1 = 'PRODUCTION'
CONFIG_MYSQL_HOST_2 = '10.16.6.2'
CONFIG_MYSQL_USER_2 = 'dba'
CONFIG_MYSQL_PASSPWD_2 = '8PUJ6BV7'
CONFIG_MYSQL_DB_2 = 'PRODUCTION'
CONFIG_MYSQL_HOST_3 = '10.16.9.1'
CONFIG_MYSQL_USER_3 = 'purge'
CONFIG_MYSQL_PASSPWD_3 = 'Spooler'
CONFIG_MYSQL_DB_3 = 'Spooler'
USER_DB = 'dba'
PASWWORD_DB = 'N2O6V6E4M'
db_list = [['Cougar DB FR Master',
  'Master',
  '10.10.6.1',
  USER_DB,
  PASWWORD_DB,
  '3306',
  '10_10_6_1.txt',
  'PRODUCTION',
  'FR',
  'ISBACKUP',
  'cougar-bd01'],
 ['Cougar DB FR Slave 1',
  'Slave',
  '10.10.6.2',
  USER_DB,
  PASWWORD_DB,
  '3306',
  '10_10_6_2.txt',
  'PRODUCTION',
  'FR',
  '',
  'cougar-bd02'],
 ['Cougar DB FR Backup',
  'Slave',
  '10.10.6.3',
  USER_DB,
  PASWWORD_DB,
  '3306',
  '10_10_6_3.txt',
  'PRODUCTION',
  'FR',
  '',
  'cougar-bd03'],
 ['Cougar DB FR Slave 2',
  'Slave',
  '10.7.9.1',
  USER_DB,
  PASWWORD_DB,
  '3306',
  '10_7_9_1.txt',
  'PRODUCTION',
  'FR',
  '',
  'cougar-bd-101'],
 ['Cougar DB UK Master',
  'Master',
  '10.16.6.1',
  USER_DB,
  PASWWORD_DB,
  '3306',
  '10_16_6_1.txt',
  'PRODUCTION',
  'UK',
  'ISBACKUP',
  'cougar-uk-bd01-d'],
 ['Cougar DB UK Backup',
  'Slave',
  '10.16.6.2',
  USER_DB,
  PASWWORD_DB,
  '3306',
  '10_16_6_2.txt',
  'PRODUCTION',
  'UK',
  '',
  'cougar-uk-bd02'],
 ['Cougar DB UK Slave 1',
  'Slave',
  '10.16.6.3',
  USER_DB,
  PASWWORD_DB,
  '3306',
  '10_16_6_3.txt',
  'PRODUCTION',
  'UK',
  '',
  'cougar-uk-bd03'],
 ['IProd DB UK Master',
  'Master',
  '10.16.60.1',
  USER_DB,
  PASWWORD_DB,
  '3306',
  '10_16_60_1.txt',
  'iprod',
  'UK',
  'ISBACKUP',
  'iprod-db-uk-01'],
 ['IProd DB UK Slave 1',
  'Slave',
  '10.16.60.2',
  USER_DB,
  PASWWORD_DB,
  '3306',
  '10_16_60_2.txt',
  'iprod',
  'UK',
  '',
  'iprod-db-uk-02'],
 ['IProd DB FR Master',
  'Master',
  '10.10.20.1',
  USER_DB,
  PASWWORD_DB,
  '3306',
  '10.10.20.1_FR.txt',
  'iprod',
  'FR',
  'ISBACKUP',
  'iprod-db-fr-01'],
 ['IProd DB FR Slave',
  'Slave',
  '10.10.20.2',
  USER_DB,
  PASWWORD_DB,
  '3306',
  '10.10.20.2_FR.txt',
  'iprod',
  'FR',
  '',
  'iprod-db-fr-02'],
 ['IProd DB AU Master',
  'Master',
  '10.7.20.1',
  USER_DB,
  PASWWORD_DB,
  '3306',
  '10.7.20.1_AU.txt',
  'iprod',
  'FR_AU',
  'ISBACKUP',
  'iprod-db-au-01'],
 ['IProd DB AU Slave',
  'Slave',
  '10.7.20.2',
  USER_DB,
  PASWWORD_DB,
  '3306',
  '10.7.20.2_AU.txt',
  'iprod',
  'FR_AU',
  '',
  'iprod-db-au-02'],
 ['BI DB UK Slave',
  'Slave',
  '10.10.6.5',
  USER_DB,
  PASWWORD_DB,
  '5513',
  '10_16_60_5_FR.txt',
  'PRODUCTION',
  'UK',
  'ISBACKUP',
  'bi-stage01-UK'],
 ['BI DB FR Slave',
  'Slave',
  '10.10.6.5',
  USER_DB,
  PASWWORD_DB,
  '13815',
  '10_16_60_5_UK.txt',
  'PRODUCTION',
  'FR',
  'ISBACKUP',
  'bi-stage01-FR']]
# okay decompyling db_config.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2013.04.02 09:10:51 CEST

Le 28 mars 2013 12:35, Marc JOUSSEMET <marc.joussemet@photobox.com> a écrit :
##################################### 
# Accès base de donnée MySQL local 
##################################### 
CONFIG_MYSQL_HOST         = "10.10.6.1" 
#CONFIG_MYSQL_HOST         = "10.10.2.27" 
CONFIG_MYSQL_USER          = "dpozega" 
CONFIG_MYSQL_PASSPWD     = "Dj3los2" 
CONFIG_MYSQL_DB         = "PRODUCTION" 
 
 
##################################### 
# Accès base de donnée MySQL local 
##################################### 
#CONFIG_MYSQL_HOST_2     = "srv_web" 
#CONFIG_MYSQL_USER_2      = "rainbow" 
#CONFIG_MYSQL_PASSPWD_2     = "rainbow" 
#CONFIG_MYSQL_DB_2         = "db_offline" 
 
CONFIG_MYSQL_HOST_2     = "srv_base" 
CONFIG_MYSQL_USER_2      = "rainbow" 
CONFIG_MYSQL_PASSPWD_2     = "rainbow" 
CONFIG_MYSQL_DB_2         = "SC" 
 
 
##################################### 
# Accès base de donnees ORACLE 
##################################### 
CONFIG_ORACLE_TNS  = "PWDB" 
CONFIG_ORACLE_DSN  = "base-distante" 
CONFIG_ORACLE_USER = "photo" 
CONFIG_ORACLE_PWD  = "photo" 

