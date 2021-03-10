import sqlalchemy as db
import psycopg2
engine = db.create_engine('postgresql://postgres:mq4Jq3C8zK@postgres-postgresql:5432/postgres')
connection = engine.connect("dbname=postgres user=postgres password=iQqsxUly9A")
metadata = db.MetaData(bind=connection, reflect=True)
print(metadata)

# Open a database cursor
dbCursor = dbSession.cursor();

# SQL statement to create a table

sqlCreateTable  = "CREATE TABLE Cities(id bigint, cityname varchar(128), latitude numeric, longitude numeric);";

# Execute CREATE TABLE command

dbCursor.execute(sqlCreateTable);
