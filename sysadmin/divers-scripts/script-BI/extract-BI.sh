#!/bin/bash

USER=dba
PASSWD=N2O6V6E4M
PORT_FR=13815
PORT_UK=5513
HOST=10.10.6.5
SUBJECT="BI.txt"
TO="pincemail.sebastien@gmail.com"


function cleaner_extract {

while read i; do rm -rf $i; done < list.txt
extract_csv_fr
}



function extract_csv_uk {
while read REQUETE; do	mysql  -u$USER -p$PASSWD -h$HOST -P$PORT_UK -e "$REQUETE"; done < query_uk.txt 
#mail_to_client
format_csv
 }


function extract_csv_fr {
while read REQUETE; do  mysql  -u$USER -p$PASSWD -h$HOST -P$PORT_FR -e "$REQUETE"; done < query_fr.txt
extract_csv_uk
#mail_to_client
 }

function format_csv {

while read i; do sed -i 's/w/\n/g' $i;done < list.txt
}

function mail_to_client {

/usr/bin/mail -s "$SUBJECT"  $TO	

}

function main {

	cleaner_extract
}

main
