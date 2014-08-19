#!/bin/bash



DATE=$(date +"%m-%d-%Y")
BACKUPDIR=$(hostname)/backup
BACKUPLOG=$(hostname)/log
DATABASE=consulting
CurrentUser=$(whoami)
username="sd-49600"
password="gallis1780"
servername="dedibackup-dc2.online.net"

if [ $CurrentUser != postgres ]; then
echo " Script must be run by postgres"
fi

if [ ! -d "$BACKUPDIR" ]; then
mkdir $BACKUPDIR
fi

if [ ! -d "$BACKUPLOG" ]; then
mkdir $BACKUPLOG
fi

pg_dump -Ft  -b $DATABASE >   $BACKUPDIR/dump-$DATABASE-$DATE.tar

ftp -in -u ftp://username:password@servername/ $BACKUPDIR/dump-$DATABASE-$DATE.tar