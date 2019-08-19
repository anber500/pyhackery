++++++++ Build the image create container
$ docker build -t my-python-app .

++++++++ Run the application
$ docker run -it --rm --name my-running-app my-python-app