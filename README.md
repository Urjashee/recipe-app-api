# recipe-app-api
Recipe API project

## Commands to run

### To build our python project
```
docker build .
```

#### or

```
docker-compose build
```

#### with flake

```
docker-compose run --rm app sh -c "flake8"
```

```
docker-compose up
docker-compose up -d # in detach mode
```

### Docker hub
#### docker hub login
```
docker login -u your-username # Please replace the username from your docker hub account
```

#### to run test
```
docker-compose run --rm app sh -c "python manage.py test"
```