# CS:GO betting db

## What is this?

This is a monorepo for a study and hobby project that collects betting-related data about the
esports game Counter-Strike: Global Offensive from multiple sources and combines it into insights
not publicly available otherwise.

## Settings up local dev env

1. Make sure you have python 3 installed
2. Go to project root and start virtual env
   Windows

```
$venv\Scripts\activate
```

Unix-based

```
$source venv/bin/activate
```

3. Run the flask app (inside the virtual env)

```
flask run
```

### Required environment variables

Example:

```
ENV_SETTINGS=config.DevelopmentConfig
SECRET_KEY=add_some_top_secret_key_here
DATABASE_URI=postgresql://csgo-betting-db-devabcdefgh.eu-north-1.rds.amazonaws.com:5432?user=postgres&password=yourpasswordhere
```

### Settings up a new database

If using a new db for dev or any other purpose:

```
flask db migrate
flask db upgrade
```

These will bring your db up to speed with the DB models defined in code.
Any changes to DB models will require you to run this again. Automating this in
deployment pipeline to be added.

# TODO

-Everything
