# Image Manager and Grading Application

A simple django application for uploading and grading images collected as part of medical
studies and allowing users to assign grades relating to Trachoma infection.
This application also exposes access to the images and grades through an API allowing creation
of training sets for image classification pipelines.


## Application Flow:

#### Data creation
1) User creates a study that includes a description and a region.

2) User creates a patient and assigns a study as well as uploads a set of pictures.


#### Data grading
1) user clicks on a study.
2) Patients are displayed that they have not graded yet as well as patients that they have graded.
3) User clicks on a patient.  They can issue a new grade for a new patient, or create a new grade for a patient they've already graded.


### Deployment to AWS Elastic Beanstalk

To initialize the eb local environment.
Create the eb remote environment.
Deploy and verify.
Create the database.
Configure S3 buckets.

#### Deploying local changes when developing.


## Development Environment.

Create a virtual environment for dev.  From within the /image_manager directory run:

```bash
python3 -m venv django-env -r=requirements.txt
. django-env/bin/activate
pip install -r requirements.txt
```


To set up the dev database do the following:

1) Install Docker.

2) Install Postgres (for the `psql` command line clinent): `brew install postgres`

3) Run `. dev/setup_db.sh` to stand up a docker image runnning Postgres

4) Run `python manage.py migrate` to set up the app schemas.

5) Then run `. dev/init_db.sh` to create some test data.

6) Run `. dev/runserver.sh` to start the web server. Visit the localhost:8000/ to ensure that it's running.

Create an admin user for the development application:
```bash
python manager.py createsuperuser
Username: admin
Email address:
Password: adminpass123
```


#### Testing

To run the tests, run
```bash
 . dev/run_tests.sh
```


#### TODO

- [X] Allow creation of a patient by uploading _several_ images at the same time.
- [X] Display images under each patient.
- [X] Create a user login flow and add LoginRequiredMixin to all relevant views.
- [ ] Allow users to change password.
- [ ] Add SuperuserRequiredMixin to delete views.

- [ ] Store images in S3 in production.
- [ ] Add drag and drop : https://www.calazan.com/adding-drag-and-drop-image-uploads-to-your-django-site-in-5-minutes-with-dropzonejs/
- [ ] Write functions to add grades for patients from users.
- [ ] Create a UI to grade patients.

- [ ]  Put the django server in a docker container.

