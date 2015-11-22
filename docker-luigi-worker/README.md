# Minimal docker image for running [Luigi](http://luigi.readthedocs.org/en/latest/index.html)

- Built on [baseimage-docker](http://phusion.github.io/baseimage-docker/)

Sample Luigi worker.


docker build -t luigi_worker .
 docker run -it --rm --name luigi_worker1 luigi_worker