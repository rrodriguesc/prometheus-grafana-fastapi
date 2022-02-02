# Api built using FastApi framework

This folder contains a test api to report informations using prometheus.

First clone the intire project then in api folder build the docker image:

`docker build -t test-api .`

Then run the api using

`docker run -d --name api -p 8080:80 test-api`

Then check http://127.0.0.1:8080/api/docs

_Note:_ You can change 8080 port to any available port
