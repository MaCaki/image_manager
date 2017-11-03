# Image Manager and Grading Application

A small django application for the managing images collected as part of medical
studies and allowing users to assign grades relating to Trachoma infection.


## Application Flow:

#### Data creation
1) User creates a study that includes a description and a region.

2) User creates a patient and assigns a study as well as uploads a set of pictures.


#### Data grading
1) user clicks on a study.
2) Patients are displayed that they have not graded yet as well as patients that they have graded.
3) User clicks on a patient.  They can issue a new grade for a new patient, or create a new grade for a patient they've already graded.



## Development Environment.

Create a virtual environment for dev.  From within the /image_manager directory run:

```
python3 -m venv django-env -r=requirements.txt
. django-env/bin/activate
pip install -r requirements.txt
```


To set up the dev database do the following:

1) Install Docker.

2) Install Postgres (for the `psql` command line clinent): `brew install postgres`

3) Run `. dev/setup_db.sh`

4) Run `python manage.py migrate`

5) Run `. dev/runserver.sh`

#### Testing

To run the tests, run
```bash
 . dev/run_tests.sh
```


#### TODO

1) create some sample studies when initializing the db.
2) Put the django server in a docker container.
3) Enable upload of images.
4) Create a user login flow.

