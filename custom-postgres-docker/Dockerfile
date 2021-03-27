FROM bitnami/postgresql:11.11.0-debian-10-r24

USER root
RUN mkdir /home/customscripts
COPY backup.bash /home/customscripts
COPY restore.bash /home/customscripts

RUN chmod +x /home/customscripts/backup.bash
RUN chmod +x /home/customscripts/restore.bash