FROM python:3.7-alpine

# Install cron
# RUN apk update \ && apk add curl openrc

RUN crond
# RUN apk update && apk add busybox-initscripts
# RUN rc-service crond start && rc-update add crond
COPY . /app
WORKDIR /app
RUN chmod +x ./docker/api/entrypoint.sh

ENTRYPOINT ["sh", "./docker/api/entrypoint.sh"]
