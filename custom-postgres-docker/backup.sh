#!/bin/bash

file_name=backup.pgsql
current_time=$(date "+%Y-%m-%d:%H")
##Change directory to script
#cd /opt/script

pg_dump --no-password -U postgres postgres > /home/backups/$current_time-$file_name

echo "Backup successful"
