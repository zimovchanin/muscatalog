FROM python:3.10-slim-buster

RUN apt-get -y update
RUN apt-get -y upgrade
RUN mkdir /muscatalog
COPY . /muscatalog
WORKDIR /muscatalog

RUN pip install --upgrade pip && pip install -r requirements.txt
ENTRYPOINT ["sh", "/muscatalog/entrypoint.sh"]
