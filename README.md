-------------------------
SAMA WEB
-------------------------
## Project health
[![Build Status](https://travis-ci.org/neodark/samaweb.svg?branch=master)](https://travis-ci.org/neodark/samaweb?branch=master)
[![Coverage Status](https://coveralls.io/repos/neodark/samaweb/badge.svg?branch=master&service=github)](https://coveralls.io/github/neodark/samaweb?branch=master)

##Project description

Building a website for the samaritains using [Django](https://www.djangoproject.com/).

##API

The backend has an available API which uses the [Django Rest Framework](http://www.django-rest-framework.org/)
This API is available through the **api/** urls

##Development

The development instance uses a local_settings to target a sqlite db

    $ python manage.py runserver --settings=samaweb.local_settings

##Running tests

The backend REST API has unit tests to verify it's good functionality

###Running a single test
    $ python manage.py test api.tests.TestAPITestClientSamaGroup
###Running all tests
    $ python manage.py test

##Integration of Travis CI / Coveralls

The continuous integration system integrates *Travis* to check the commits and *Coveralls*
to follow the code coverage.

####Automatic deployment via Heroku

To automate the process and avoid *Travis* storing publicly *Heroku* access keys:

    $ travis encrypt $(heroku auth:token) --add deploy.api_key

##Deployment test via Heroku

The deployment of the website cand be tested via **Heroku**

####Check website on Gunicorn webserver

Running a **Gunicorn** server instance to verify the website is working

#####Create a valid *Procfile*
`<web: gunicorn samaweb.wsgi --log-file ->`

#####Check *Procfile* validity
    $ foreman check

#####Start Gunicorn webserver
    $ foreman start

#####*(Optional)* Check Gunicorn server version 
    $ foreman version

####Connect to Heroku
    $ heroku login

####To create an app on Heroku (only if the application is not already created)
    $ heroku create

####Deploy the selected branch on Heroku 'master' (example: branch 'deploy' is pushed to Heroku 'master')
    $ git push heroku deploy:master

####Launch Heroku on your website
    $ heroku open

####Scale the dynos and check it:
    $ heroku ps:scale web=1
    $ heroku ps

####The logs can be checked 
    $ heroku logs

####Synchronize the POSTGRES database on Heroku (Note: Heroku doesn't support sqlite)
    $ heroku run python manage.py syncdb

##Populating the database

Adding test data to the database could be done using a script:

    $ python ./scripts/db_set.py --json_file scripts/dataset/test_data.json
