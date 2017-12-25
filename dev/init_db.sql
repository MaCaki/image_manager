# Init commands to create the dev db for the image manager applications.

CREATE ROLE image_manager WITH LOGIN PASSWORD 'image_manager';
CREATE DATABASE image_manager_db;
GRANT ALL PRIVILEGES ON DATABASE image_manager_db TO image_manager;