FROM phusion/baseimage:0.9.16

ENV LUIGI_HOME /etc/luigi
ENV APP_HOME /usr/local/app1

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN apt-get update && \
  apt-get install -y build-essential python python-dev python-pip

ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

VOLUME /var/log/luigi

RUN mkdir $LUIGI_HOME
ADD client.cfg $LUIGI_HOME/client.cfg
COPY scripts $APP_HOME/scripts
COPY workflows $APP_HOME/workflows

ENTRYPOINT ["/bin/bash", "-c"]
CMD ["$APP_HOME/scripts/run.sh"]
