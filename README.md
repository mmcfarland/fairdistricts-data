# Fair Districts Data processing

Automate the data processing of PA district geometries from PASDA to individual
files appropriate for a static web app.

#### Requirements
* Docker https://docs.docker.com/engine/installation/
* Docker Compose https://docs.docker.com/compose/install/

#### Usage
```bash
docker-compose run data
```

Processed geoJSON files will be in the `dist/` directory.
