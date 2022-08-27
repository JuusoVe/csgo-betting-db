# API

This consists of a [PostgreSQL](https://www.postgresql.org/) database and [Flask app](https://palletsprojects.com/p/flask/) that serves as the entrypoint to the database and manages the data model.

## The API

## Setting up the database

## Running the app locally

## Env-variables

## Hosting and Deploying

## The database

If you wan't to set up a local database for development I recommend using the [official Postgres Docker image](https://hub.docker.com/_/postgres) for super quick set up.

```
docker run --name csgo-bettinb-db -e POSTGRES_PASSWORD=mysecretpassword -d postgres
```

TODO: Finish this doc

### Settings up a new database

If using a new db for dev or any other purpose:

```
flask db init
flask db migrate
flask db upgrade
```

These will bring your db up to speed with the DB models defined in code.
Any changes to DB models will require you to run migrate and update again. Automating this in deployment pipeline to be added.

#### The app

**Running the flask app in dev mode**

```
flask run
```

**Creating a docker image from the latest src**
Requires [Docker](https://www.docker.com/get-started/) to be installed.

```
docker build -t flask-api . --no-cache
```

**Running the Docker image locally**
Replace the latter port with something else in case it's reserved.

```
docker run -p 5000:5000 flask-api
```

I recommend running the app locally only if testing changes packages etc. Otherwise just run the flask app in dev mode to benefit from hot reload on code changes.

### Hosting and deployment

The flask API is hosted in a AWS Lightsail container.

These scripts assume you have [AWS cli](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) and [lightsail plugin](https://lightsail.aws.amazon.com/ls/docs/en_us/articles/amazon-lightsail-install-software) for it installed and configured.

**Creating a container service in lightsail**

```
aws lightsail create-container-service --service-name csgo-betting-db-api --power nano --scale 1
```

**Pushing an image to the container**

```
aws lightsail push-container-image --region eu-central-1 --service-name csgo-betting-db-api --label v1 --image flask-api:latest
```

If you create a new version, change the label and then replace image reference in containers.json with the image reference string you get in the response of this command.

**Deplying code to the container**

```
aws lightsail create-container-service-deployment --service-name csgo-betting-db-api --containers file://containers.json --public-endpoint file://public-endpoint.json
```

**Polling for container service status**

```
aws lightsail get-container-services --service-name csgo-betting-db-api

```

Possible responses include a state in the JSON, to avoid confusion: "READY" means nothing is running in the service but it is ready to accept deployments. "RUNNING" means the deployment was successfull and the app has succesfully started.
