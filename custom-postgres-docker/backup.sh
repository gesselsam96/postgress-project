#!/bin/bash

file_name=backup.pgsql
current_time=$(date "+%Y.%m.%d")
##Change directory to script
#cd /opt/script

pg_dump --no-password -U postgres postgres > /opt/bitnami/scripts/postgresql/$current_time-$file_name

echo "Backup successful"

### delete files older than 5 days
find /opt/bitnami/scripts/postgresql/ -mtime +5 -exec rm {} \;