# Flask Notes API
---------------------
This is a simple notes api with Python Flask and PostgreSQL.

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

N.B. change the hostname ```localhost``` with ```postgres``` in both ENVs DATABASE_URL and DATABASE_URL_TEST 

Start both the services (DB & API) with following commands
```bash
docker-compose build
docker-compose up -d
```

## Only Database in Docker and API locally
Firstly start the DB:
```bash
docker-compose up -d postgres pg-admin
```
this command also creates a PG-Admin instance to control Postgres over WEB at ```http://localhost:5050```

N.B. 
use the container name as Database Name 

To create DB's tables and/or updated them run the following:
```bash
flask init db
flask db migrate
flask db update
```

then create the virtual environment, install the requirements and start the API
```bash
virtualenv -p python3 venv && . venv/bin/activate
pip3 install -r requirements/dev.txt
flask run -p 8080
```

API  will be available at ```localhost:8080```
API's docs will be available at ```localhost:8080/swagger```

N.B.
Database can be created from scratch by
```bash
docker pull postgres
docker run --name postgres -e POSTGRES_USER=resu -e POSTGRES_PASSWORD=d0nt4get -p 5432:5432 -d notes
```

Connect to DB:
```bash
docker exec -it <container_id> psql -h localhost -p 5432 -U resu -d notes -W
```

---

### Documentation
-----------------
The Swagger documentation is available at the development stage, @```localhost:<port>/swagger```

---

### Optimizations
-----------------
A more optimized setup with [uWSGI-NGINX](https://flask.palletsprojects.com/en/1.1.x/deploying/uwsgi/).

Standalone [WSGI Containers](https://flask.palletsprojects.com/en/1.1.x/deploying/wsgi-standalone/).