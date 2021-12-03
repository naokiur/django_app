FROM python:3.8

RUN mkdir /code
WORKDIR /code

RUN apt-get update \
    && apt-get install -y \
    && pip install --upgrade pip \
    && pip install --upgrade setuptools \
