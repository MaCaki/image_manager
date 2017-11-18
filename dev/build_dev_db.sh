echo "Building the postgres docker container for image-manger."

# https://ryaneschinger.com/blog/dockerized-postgresql-development-environment/

PGPASSWORD='dev_db_password'

# if the container is not created yet, build it.
if [ ! "$(docker ps -a -f name=image_manger_dev_db | grep image_manger_dev_db)" ]; then
    echo 'Creating new postgres container...'
    docker run --name image_manger_dev_db -p 5432:5432 -e POSTGRES_PASSWORD=$PGPASSWORD -d postgres
else
    echo 'Container is already created, restarting the postgres conainer...'
    docker start image_manger_dev_db
fi

# docker needs some time to launch boxes
while [ ! "$(docker ps -q -f name=image_manger_dev_db)" ]; do
    echo 'sleeping'
    sleep 1
done

# A hacky way to wait for the new container instance to finish starting the postgres service so that
# the db init commands below don't fail.
while [ ! "$(PGPASSWORD=$PGPASSWORD psql -h localhost -U postgres -d postgres -c 'select 1234' | grep 1234)" ]; do
    echo 'Waiting for database to recieve connections...'
    sleep 1
done


declare -a cmnds=(
    "CREATE ROLE image_manager WITH LOGIN PASSWORD 'image_manager';"
    "CREATE DATABASE image_manager_db;"
    "GRANT ALL PRIVILEGES ON DATABASE image_manager_db TO image_manager;"
)

# run all of the commands in independently, because CREATEDB cannot be
# run as part of a multiline command.
for cmnd in "${cmnds[@]}"
do
    PGPASSWORD=$PGPASSWORD psql -h localhost -U postgres -d postgres -c "$cmnd"
done


