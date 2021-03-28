#!/bin/bash

#parse which file to use for restore
current_time=$1
file_name=backup.pgsql

psql -U postgres -d postgres < /opt/bitnami/scripts/postgresql/$1-$file_name

echo "Restore successful"