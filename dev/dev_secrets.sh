# Explictly state that we are in the dev environment so that we can
# appropriately configure the database and file storage.
export IM_ENV=dev

export IM_POSTGRES_NAME=image_manager_db
export IM_POSTGRES_USER=image_manager
export IM_POSTGRES_PASSWORD=image_manager
export IM_POSTGRES_HOST=localhost