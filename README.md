# CS:GO betting db

## What is this?

This is a monorepo for a study and hobby project that collects betting-related data about the
esports game Counter-Strike: Global Offensive from multiple sources and combines it into insights
not publicly available otherwise.

### Required environment variables

TODO: Split these into modules' READMEs

ENV_SETTINGS: Which object from config file to use.  
SECRET_KEY: A secret key.  
DATABASE_URI: DB connection URI.  
UNI_API_ID: Id to Unibet API.  
UNI_API_KEY: Key to Unibet API.  
FLASK_ENV: Flask mode to run.  

Example:

```
ENV_SETTINGS=config.DevelopmentConfig
SECRET_KEY=add_some_top_secret_key_here
DATABASE_URI=postgresql://csgo-betting-db-devabcdefgh.eu-north-1.rds.amazonaws.com:5432?user=postgres&password=yourpasswordhere
UNI_API_ID=ca12345
UNI_API_KEY=12345qwertyuiop
FLASK_ENV=development

```

### Settings up a new database

If using a new db for dev or any other purpose:

```
flask db init
flask db migrate
flask db upgrade
```

These will bring your db up to speed with the DB models defined in code.
Any changes to DB models will require you to run migrade and update again. Automating this in
deployment pipeline to be added.

### Hosting and Deploying

#### The flask API

The flask API is hosted in a AWS Lightsail container.

These scripts assume you have [AWS cli](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) and [lightsail plugin](https://lightsail.aws.amazon.com/ls/docs/en_us/articles/amazon-lightsail-install-software) for it installed and configured.

**Running the flask app in dev mode**
```
flask run
```

**Creating a docker container from the latest src**
Requires [Docker](https://www.docker.com/get-started/) to be installed.
```
docker build -t flask-api .
```

**Running the Docker image**
Replace the latter port with something else in case it's reserved.
```
docker run -p 5000:5000 flask-api
```
I recommend running the app locally only if testing changes packages etc. Otherwise just run the flask app in dev mode to benefit from hot reload on code changes.


**Creating a container service in lightsail**
```
aws lightsail create-container-service --service-name csgo-betting-db-api --power nano --scale 1
```

**Pushing an image to the container**
```
aws lightsail push-container-image --region eu-central-1 --service-name csgo-betting-db-api --label v1 --image flask-app:latest
```
If you create a new version, change the label and then replace image reference in containers.json with the image reference string you get in the response of this command.


**Deplying code to the container**
```
aws lightsail create-container-service-deployment --service-name csgo-betting-db-api --containers file://containers.json --public-endpoint file://public-endpoint.json
```

**Polling for container serveice status**
```
aws lightsail get-container-services --service-name csgo-betting-db-api

```
Possible responses include a state in the JSON, to avoid confusion: "READY" means nothing is running in the service but it is ready to accept deployments. "RUNNING" means the deployment was successfull and the app has succesfully started.


## TODO
- CI/CD Pipeline
- Infra as code set up
- All tests
- Unibet fetching module
- Scheduling
- hltv_scraper module hosting
- Web UI
