# ----- Example Python program to insert data into a PostgreSQL database table

import psycopg2

# Open a DB session

dbSession       = psycopg2.connect("dbname='postgres' user='postgres' password='jYFuBuNX6S'");

# Open a database cursor

dbCursor = dbSession.cursor();

 

# SQL statement to create a table

sqlCreateTable  = "CREATE TABLE Cities(id bigint, cityname varchar(128), latitude numeric, longitude numeric);";

 

# Execute CREATE TABLE command

dbCursor.execute(sqlCreateTable);


