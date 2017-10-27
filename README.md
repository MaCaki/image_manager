

Setting up the dev env.

1) install postgres
2) run `initdb` to create the database cluster.
3) run `createdb image_manager_db` to create the app database.
4) Create app user: run `psql postgres` then execute:
    CREATE ROLE image_manager WITH LOGIN PASSWORD 'image_manager'
    GRANT ALL PRIVILEGES ON DATABASE image_manager_db TO image_manager;