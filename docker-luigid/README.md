# Minimal docker image for running [Luigid](http://luigi.readthedocs.org/en/latest/index.html)


	using the following command docker build -t luigid .

To run, publish luigi's default web port ( 8082 )

    docker run -d -p 8082:8082 luigid

And visit:
 - http://LUIGI_HOST:8082/
 - http://LUIGI_HOST:8082/static/visualiser/index.html#
 - http://LUIGI_HOST:8082/history
