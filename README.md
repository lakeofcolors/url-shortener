# url-shortener

### First set up documentation
 - docker-compose up -d --build
 - docker-compose exec web flask db init
 - docker-compose exec web flask db migrate -m "Initial migration."
 - docker-compose exec web flask db upgrade

### After

    -docker-compose up

### TEST API DOCUMETATION

    You can visit http://127.0.0.1:8080/apidocs/ url for get swagger
    api documentation
