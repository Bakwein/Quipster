FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1 \ 
    PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

COPY ./requirements.txt ./requirements.txt

RUN pip3 install --upgrade pip
RUN pip3 install -r ./requirements.txt

ADD . /code
