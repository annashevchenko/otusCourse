FROM python:3.8-alpine

RUN apk update && apk upgrade && \
    apk add --no-cache bash git openssh

WORKDIR /home/anna

RUN git clone https://github.com/annashevchenko/otusCourse.git

WORKDIR otusCourse

RUN ["pip", "install", "-r", "requirements.txt"]

CMD ["python", "--version"]
