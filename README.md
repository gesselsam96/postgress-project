# postgress-project
# postgress-project
1. Quickly deploy postgres database. 

2. Setup automated backup per cronjob schedule.

3. Restore from known backup giving backup date as parameter.

Helpful commands:

helm install --replace postgress C:\Users\Gilbert\Desktop\projects\github\postgress-project\postgresql

helm install backup C:\Users\Gilbert\Desktop\projects\github\postgress-project\cronjobs\backup-chart

Helpful links:
https://www.postgresqltutorial.com/postgresql-backup-database/
https://hub.docker.com/layers/bitnami/postgresql/11.11.0-debian-10-r24/images/sha256-9cefdf31c72124a5cb73c4eee46dde94f008f330acfcbef1ce6a42433f16f259?context=explore
https://sandeepbaldawa.medium.com/basic-postgres-database-in-kubernetes-23c7834d91ef
https://pynative.com/python-postgresql-insert-update-delete-table-data-to-perform-crud-operations/