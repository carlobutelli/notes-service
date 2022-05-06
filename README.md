# Flask Notes API
---------------------
This is a simple note api with Python Flask.

N.B. Requires Docker to be installed.

---

### Env variables
--------------------
```bash
export FLASK_APP=api
export FLASK_DEBUG=1
export APP_SETTINGS=Local
export SECRET_KEY=this-really-needs-to-be-changed
export DATABASE_URL=postgresql+psycopg2://resu:d0nt4get@localhost:5432/notes
export DATABASE_TEST_URL=postgresql+psycopg2://resu:d0nt4get@localhost:5432/notes-test
```

---

### Run the API
---------------
## Full in Docker
Start both the services (DB & API) with following commands
```bash
docker-compose build
docker-compose up -d
```
API will be available at ```localhost:8080/swagger```

## Partially in Docker
Firstly start the DB in a container
```bash
docker-compose up -d postgres
```
then create the virtual environment, install the requirements and start the API
```bash
virtualenv -p python3 venv && . venv/bin/activate
pip3 install -r requirements/dev.txt
flask run -p 8080
```
then the API will be available at ```localhost:8080/swagger```
N.B. change the hostname ```postgres``` with ```localhost``` in both ENVs DATABASE_URL and DATABASE_URL_TEST
---

### Documentation
-----------------
The Swagger documentation is available at the development stage, @```localhost:<port>/swagger```

---

### Optimizations
-----------------
A more optimized setup with [uWSGI-NGINX](https://flask.palletsprojects.com/en/1.1.x/deploying/uwsgi/).

Standalone [WSGI Containers](https://flask.palletsprojects.com/en/1.1.x/deploying/wsgi-standalone/).