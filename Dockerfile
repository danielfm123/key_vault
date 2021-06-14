# Ejemplo de dockerfile
FROM ubuntu:20.04

MAINTAINER Daniel Fischer "dfischer@anasac.cl"

ARG DEBIAN_FRONTEND=noninteractive

#BASELINE
RUN apt-get update \
  && apt-get install -y apt-utils \
  && apt-get -y install wget bash gnupg2 software-properties-common locales

#LOCALES
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

#Python
RUN apt install -y python3 python3-pip
RUN pip3 install --target=/usr/local/lib/python3.8/dist-packages wheel

# otros paquetes python
RUN pip3 install uwsgi flask

# instalar app
RUN mkdir /opt/app
COPY . /opt/app/
#COPY ["global.R","init.R","ui.R","server.R","main_proc.R", "/opt/poc_dureza"]

WORKDIR /opt/app
CMD ["/bin/sh","./run.sh"]

# para shinyproxy
EXPOSE 8081
# WORKDIR /opt/poc_dureza
# CMD ["R", "-e", "shiny::runApp('/opt/poc_dureza',port=3838,host = '0.0.0.0')"]
