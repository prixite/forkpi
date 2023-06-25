FROM ubuntu:20.04

RUN apt-get update && \
	apt-get install -y \
	build-essential \
	zlib1g-dev \
	libncurses5-dev \
	libgdbm-dev \
	libnss3-dev \
	libssl-dev \
	libreadline-dev \
	libffi-dev \
	wget && \
	mkdir /python && cd /python && \
	wget https://www.python.org/ftp/python/3.2.4/Python-3.2.4.tgz && \
	tar -xvf Python-3.2.4.tgz && \
	cd Python-3.2.4

RUN ./configure --enable-optimizations && \
  make && \
	make install

#WORKDIR /opt/code
#
#COPY forkpi/requirements.txt requirements.txt

#RUN pip install -r requirements.txt
#
#COPY ./forkpi ./
