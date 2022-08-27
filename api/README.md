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

```
docker build -t flask-api . --no-cache
```

**Running the Docker image locally**
Replace the latter port with something else in case it's reserved.

```
docker run -p 5000:5000 flask-api
```

I recommend running the app locally in Docker only if testing changes to packages etc. Otherwise just run the flask app in dev mode to benefit from hot reload on code changes.

