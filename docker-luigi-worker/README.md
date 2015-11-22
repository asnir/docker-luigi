# Luigi [Luigi](http://luigi.readthedocs.org/en/latest/index.html) worker samle


Sample Luigi worker.

```bash
#Building the image
docker build -t luigi_worker .

#Lifting up container.
docker run -it --rm --name luigi_worker1 luigi_worker
```
