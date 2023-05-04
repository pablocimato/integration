FROM alpine:3.14

COPY test.sh /root
COPY . /app
WORKDIR /app
RUN apk update && apk upgrade && apk add --no-cache python3 py3-pip bash
# echo '*  *  *  *  *    python3 /app/app/main.py'
RUN echo '*  *  *  *  *    python3 /app/app/main.py' > /etc/crontabs/root
CMD ["crond", "-l", "8", "-f"]
# ENTRYPOINT ["./docker/api/entrypoint.sh"]