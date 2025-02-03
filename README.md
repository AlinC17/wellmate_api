# wellmate_api

## Start up
`docker compose up --build`

## Configuration
```
DB_HOST=127.0.0.1
DB_NAME=<Database name>
DB_USER=<User name>
DB_PASSWORD=<User password>
DB_PORT=<Database port on which is running postgres instance>

SECRET_KEY=<For feature implementation of JWT auth and other security features> 
```

The project is using postgres. Tu run it smoothly you have to add all these params to you  `.env` file inside progect directory. Enjoy!

## Useful project urls

`/docs` - swagger documentation for easy overview of available endpoints
`/redoc` - redoc documentation(alternative to swagger)


> A test backend api with a clean project structure. Built on top of tech stack: FastAPI, SQLAlchemy, Alembic, PostgreSQL, Docker, Docker compose
