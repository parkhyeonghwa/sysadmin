#!/bin/bash







while read line
do server=$(echo $line | cut -d ' ' -f1)
   ip=$(echo $line | cut -d ' ' -f2)

   echo "$server replicated"  
   mysql -uspincemail -pSeb4sB9oXx -h$ip -e "show slave status\G;"
done < "slaves.txt"
