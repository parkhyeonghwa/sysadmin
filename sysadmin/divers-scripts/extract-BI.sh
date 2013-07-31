#!/bin/bash

USER=dba
PASSWD=N2O6V6E4M
REQUETE="SELECT * FROM PRODUCTION.ITEMS_test INTO OUTFILE 'bi-extract.txt' FIELDS TERMINATED BY '|' ENCLOSED BY '' LINES TERMINATED BY '\n';"
PORT=13815
HOST=10.10.6.5
FILE="/var/lib/mysql/sandboxes/multi_msb_5_5_13/node2/data/bi-extract.txt"
SUBJECT="BI.txt"
TO="pincemail.sebastien@gmail.com"

function cleaner_extract {

if [ -f $FILE ];

        then rm $FILE

fi

extract_csv
}


function extract_csv {
        mysql  -u$USER -p$PASSWD -h$HOST -P$PORT -e "$REQUETE"

mail_to_client
 }


function mail_to_client {

/usr/bin/mail -s "$SUBJECT"  $TO

}

function main {

        cleaner_extract
}
            
main 
