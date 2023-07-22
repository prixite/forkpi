From forkpi-forkpi_proxy

RUN apt update && apt install -y cron
COPY ./cron/crontab /etc/cron.d/crontab
RUN chmod 0644 /etc/cron.d/crontab
RUN /usr/bin/crontab /etc/cron.d/crontab

WORKDIR /opt/cron
COPY ./cron ./
COPY ./.env /opt/code

CMD ["cron", "-f"]
