FROM bitnami/postgresql:11.11.0-debian-10-r24

USER root
RUN mkdir /home/customscripts
COPY backup.sh /home/customscripts
COPY restore.sh /home/customscripts

RUN chmod +x /home/customscripts/backup.sh
RUN chmod +x /home/customscripts/restore.sh