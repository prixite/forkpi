FROM python:3.11.1

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

WORKDIR /opt/code

COPY forkpi_proxy/requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY ./forkpi_proxy ./
