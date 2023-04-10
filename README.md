# APIs

The same API created using:
- FastAPI
- GraphQL
- Django (to be done)
- Flask (to be done)

## How to run each service?

There are 4 services specifies in ```docker-compose.yaml``` (there are 4 associated subfolders named after these services).

Examples for ```fastapi_api``` service:

&nbsp;
    Build service: ```docker-compose build fastapi_api```

&nbsp;
    Run service shell: ```docker-compose run fastapi_api bash``` (or ```bin/run fastapi_api```)

&nbsp;
    Run service: ```docker-compose up fastapi_api```

Each service allows to:
 - generate data about drivers, their cars and tickets (and save it to the database)
 - create new drivers/cars/tickets
 - get lists of existings drivers
 - get list of cars/tickets for a selected driver 

Examples of requests can be found in each service subfolder.


## Before push

Before pushing code changes to remote check if it requires linting and whether all tests pass

```
bin/pre-push
```
