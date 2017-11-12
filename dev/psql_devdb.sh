# Access the dev db using psql shell cmnd.
. dev/dev_secrets.sh

PGPASSWORD=$IM_POSTGRES_PASSWORD psql -h $IM_POSTGRES_HOST -U $IM_POSTGRES_USER -d $IM_POSTGRES_NAME