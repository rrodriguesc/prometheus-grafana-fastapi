# prometheus-grafana-fastapi

Test project for integration between Prometheus and grafana to a FastApi application using docker

To use this project first build the test api image. Check [here](./api/README.md) to see how to do it.

Copy the [Prometheus config file](./prometheus/prometheus.yml) file to `/etc/prometheus`

```bash
sudo cp ./prometheus/prometheus.yml /etc/prometheus/prometheus.yml
```

_Note:_ You can edit this yml file to add more jobs or update scrape configs.

Then simply start the services

```bash
docker-compose -d up
```
