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




## TODO
- CI/CD Pipeline
- Infra as code set up
- All tests
- Unibet fetching module
- Scheduling
- hltv_scraper module hosting
- Web UI
