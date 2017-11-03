. dev/dev_secrets.sh
.  django-env/bin/activate

echo 'Restarting the postgres conainer...'
docker start image_manger_dev_db
    
python manage.py runserver