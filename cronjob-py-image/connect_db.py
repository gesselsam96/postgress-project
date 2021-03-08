import sqlalchemy as db
engine = db.create_engine('postgresql://postgres:mq4Jq3C8zK@postgres-postgresql:5432/postgres')
connection = engine.connect()
metadata = db.MetaData(bind=connection, reflect=True)
print(metadata)