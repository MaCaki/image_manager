. dev/dev_secrets.sh

echo 'Restarting the postgres conainer...'
docker start image_manger_dev_db
    
python manage.py runserver