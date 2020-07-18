# Puente Flask Tasky
[![Build Status](https://travis-ci.com/hopetambala/puente-flask-tasky.svg?branch=master)](https://travis-ci.com/hopetambala/puente-flask-tasky)
[![codecov](https://codecov.io/gh/hopetambala/puente-flask-tasky/branch/master/graph/badge.svg)](https://codecov.io/gh/hopetambala/puente-flask-tasky)

## Description
Puente's Task and Messaging Management System built with [Flask](https://flask.palletsprojects.com/en/1.1.x/).

## Project Layout
| Key Folder | Parent Folder | Description |
| - | - | - |
| db | root | Holds the database and database creation tools |
| models | root | Holds the main models and model methods for objects created in database |
| endpoints | root | Holds the resources we use to create API endpoints |

## Build
### Install and create virtual environment library
```
cd <root-folder>/
pip install virtualenv #if you don't have virtualenv installed
```

Create virtualenv
```
virtualenv <Name_of_Virtual_Environment>
```

Activate virtualenv
```
source <Name_of_Virtual_Environment>/bin/activate
```
### Install project requirements
Install project requirements usings the requirements.text once you're inside your virtual environment
```
pip install -r requirements.txt
```

## Run
Here are some quick commands to get started after install. Make sure to run them in the root directory

- `rm db/tasky.db && python db/database.py`: Creates database and populates it with fake data
- `python app.py`: Run flask application

<!-- ## Endpoints
Active endpoints

GET /users _i.e. http://127.0.0.1:5000/users_

GET /users/name _i.e. http://127.0.0.1:5000/users/name_

DELETE /users/name

POST /register

GET /products _i.e. http://127.0.0.1:5000/products_

GET /product/name _i.e. http://127.0.0.1:5000/product/name_

POST /product/name

GET /history/name _i.e. http://127.0.0.1:5000/history/name_

POST /shopping

POST /auth -->
