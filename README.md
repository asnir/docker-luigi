# Minimal docker image for running [Luigi](http://luigi.readthedocs.org/en/latest/index.html)

- Built on [baseimage-docker](http://phusion.github.io/baseimage-docker/)

Reference: https://github.com/akursar/docker-luigid


At this repository you will find:
1) sample luigi-monitor (Luigi central planner - the webapp).
2) Sample luigi worker.

To run, publish luigi's default web port ( 8082 )

    docker run -d -p 8082:8082 akursar/luigid

And visit http://LUIGI_HOST:8082/





	
It's uses [Crane](https://github.com/michaelsauter/crane) to easily deploy the docker containers.


Use the following cli commands:

```bash

#Build the image 'luigi-worker'
crane provision luigi-worker

#Build the image 'luigi-monitor'
crane provision luigi-monitor

#Show the status of the current running containers 
docker ps

#Lift the luigi monitor (provision & run the 'central planner' image)
crane lift luigi-monitor

#Lift the luigi monitor (provision & run the 'luigi-worker' image)
crane lift luigi-worker

#Show the logs of 'luigi-worker' container
docker logs luigi-worker

```	


