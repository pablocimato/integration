FROM alpine:3.14

COPY . /app
WORKDIR /app
RUN apk update && apk upgrade && apk add --no-cache python3 py3-pip bash

# ARG requirements=/app/requirements.txt
RUN pip install -r /app/requirements.txt

RUN echo '*  *  *  *  *    python3 /app/app/main.py' > /etc/crontabs/root
CMD ["crond", "-l", "8", "-f"]
