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
2) Patients are displayed that they have not graded yet as well as patients that
    they have graded.
3) User clicks on a patient.  They can issue a new grade for a new patient,
    or create a new grade for a patient they've already graded.


## Architecture of applications

The `core` app defines models for studies, patients belonging to those studies,
and images belonging to those patients.  The core views are responsible for
displaying all studies, creating, editing, and inspecting those studies, and
likewise with patients.  The core views also handle uploading files, allowing
study administrator users and image collectors to add images to studies.
Additionally user account management is handled by the core application.

The `grade` app defines models that define the structure of a grade type. These
are administrator defined questions with a static set of options that graders
can chose from.  The grading views are distinct from the core views so that
they the logic of how the images are exposed during a 'grading session' is
isolated from the normal list view.

A user is 'sent to' the grade app through from the core app when they start
grading a study. The study object has a `GradeTypes` assigned to it
through a one to many foreign key relationship from the `grade.GradeType`.
The grading app then constructs forms for each grade type assigned to that
study and sends them to the user alongside samplings of images for that
study.

When the user fills out and submits the form, the data is parsed into
`GradeEntry` objects, one for each `GradeField` assigned to the `GradeType`
and is saved along with a `Grade` object, which unifies all the entries through
 a foreign key relationship.


### Deployment to AWS Elastic Beanstalk

#### Fresh start
If you want to start with a fresh environment configuration, you will need to
do the following:
Install the EBCLI
```
pip install awsebcli --upgrade --user
```
being sure to add `~/Library/Python/X.Y/bin` to your bash $PATH.

To initialize the eb local environment.
```
eb init -p python3.6 image-manager
```
then `eb init` one more time to generate ssh keys to login to the machines that
AWS creates.

Create the eb remote environment.
```
eb create image-manager
```

Within the Elastic Beanstalk console, configure the following environment
variable:
```
IM_ENV = 'prod'
```

Initialize the production application and create a superuser adming account.
Run `eb ssh` inside of the root of the local application directory then run
inside of the EB launched instance:
```
# get all of the production environment env variable and activate python env.
source /opt/python/current/env
source /opt/python/run/venv/bin/activate
cd /opt/python/current/app
python manage.py createsuperuser
```
(You will probably need to `sudo su` to be able to execute the above. )


#### From Saved Configuration

Included in this repository is an up to date saved configuration that specifies
the correct database, environment variable, python installation etc.  To deploy
the application using this saved config run
```bash
eb config get image-manager-stage
eb create --cfg  image-manager-stage
```
NOTE: check the elastic beanstalk console to verify the name of the latest
saved configuration.
Once the changes are verified, repeat for prod.

#### Verification

Once the application is deployed navigate to the eb generate url using
`eb open` then use the above generated super user credentials to login
and create other users.


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
- [X] Allow users to change password.
- [X] Store images in S3 in production.
- [X] Change Study creation to allow for creation of Region at the same time.

----- Release 0
- [x] Set up an SMTP server using aws.ses.
- [X] Allow users to modify their profile.
- [ ] Create a grading app with models for user defined grade types.
- [ ] Attach a grade to a image.
- [ ] Write functions to add grades for patients from users.
- [X] Stub out API and install django rest api.
- [ ] Write a test suite.

---- Release 1
- [ ] Write a function around the eyelid images that extracts the full file path.
- [ ] Fill in EyeLidKeyGradeList with basic list functionality and params (
        limit, graded/ungraded
    )
- [ ] Verify that non-expiring s3 keys can be extracted from the Image model.
- [ ] Show all images that a user has graded with opportunity to modify.
- [ ] Add api endpoint to request images filenames and grades with API key.


#### Cool features
- [ ] [Add drag and drop](https://www.calazan.com/adding-drag-and-drop-image-uploads-to-your-django-site-in-5-minutes-with-dropzonejs/)

Deploy and Dev Infrastructure

- [ ] Deploy from Github using [CodeDeploy](https://aws.amazon.com/blogs/devops/automatically-deploy-from-github-using-aws-codedeploy/)
- [ ] Put the django server in a docker container.

Domain name stuff

- [ ] Verify registration of ucsfproctorgrading.center.
- [ ] Verify the domain with AWS SES to send emails.
- [ ] Route ucsfproctorgrading.center [to EB deploy](http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-beanstalk-environment.html)
