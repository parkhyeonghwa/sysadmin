#!/bin/bash



DATE=$(date +"%m-%d-%Y")
BACKUPDIR=/var/lib/backup
BACKUPLOG=/var/log/pg_backup
DATABASE=consulting

if [ ! -d "$BACKUPDIR" ]; then
mkdir $BACKUPDIR 
fi

if [ ! -d "$BACKUPLOG" ]; then
mkdir $BACKUPLOG
fi

pg_dump -Ft  -b $DATABASE >   $BACKUPDIR/dump-consulting-$DATE.tar  
