# FastAPI service

## Requests

```POST http://0.0.0.0:7000/generate_data```

Creates sample data: drivers, cars and tickets (by default 100 drivers, 150 cars and 200 tickets - default values can be changed in ```config/env.py```).

Example request:
```
curl -X POST -H "Auth-Token: $API_AUTH_TOKEN" http://0.0.0.0:7000/generate_data
```

Response:
```
{"message":"Data generated"}
```

___

```POST http://0.0.0.0:7000/drivers/```

Creates a driver with given name, surname and age.

Example request:
```
curl -X POST -H "Auth-Token: $API_AUTH_TOKEN" -H "Content-Type: application/json" -d '{"name": "John","surname": "Smith","age": "35"}' http://0.0.0.0:7000/drivers/
```

Example response:
```
{"name":"John","surname":"Smith","age":35}
```

___

```GET http://0.0.0.0:7000/drivers/?limit=10```

Returns list of drivers from the database (by default 10 random).

Example request:
```
curl -X GET -H "Auth-Token: $API_AUTH_TOKEN" http://0.0.0.0:7000/drivers/?limit=10
```

Example response:
```
[{"name":"Elizabeth","surname":"Horne","age":65},{"name":"Brian","surname":"Hubbard","age":67},{"name":"Victoria","surname":"Conrad","age":23},{"name":"Edward","surname":"Mitchell","age":19},{"name":"Brian","surname":"Curtis","age":50},{"name":"Matthew","surname":"Sanders","age":54},{"name":"Andrew","surname":"Valdez","age":43},{"name":"Patricia","surname":"Ramos","age":17},{"name":"Erik","surname":"Arellano","age":37},{"name":"Mark","surname":"Morales","age":34}]
```

___

```POST http://0.0.0.0:7000/drivers/```
```POST http://0.0.0.0:7000/cars/```
```POST http://0.0.0.0:7000/tickets/```

Creates a driver, car or ticket.

Example requests:
```
curl -X POST -H "Auth-Token: $API_AUTH_TOKEN" -H "Content-Type: application/json" -d '{"name": "John","surname": "Smith","age": "35"}' http://0.0.0.0:7000/drivers/
```
```
curl -X POST -H "Auth-Token: $API_AUTH_TOKEN" -H "Content-Type: application/json" -d '{"brand": "Opel","model": "Astra","year_of_production": "2005","mileage":"200000","color":"silver","driver_id":"1"}' http://0.0.0.0:7000/cars/
```
```
curl -X POST -H "Auth-Token: $API_AUTH_TOKEN" -H "Content-Type: application/json" -d '{"driver_id": "1","car_id": "1","fine": "500","penalty_points":"5"}' http://0.0.0.0:7000/tickets/
```

Example responses:
```
{"name":"John","surname":"Smith","age":35}
```
```
{"brand":"Opel","model":"Astra","year_of_production":2005,"mileage":200000,"color":"silver","driver_id":1}
```
```
{"driver_id":1,"car_id":1,"fine":500,"penalty_points":5}
```

___
```GET http://0.0.0.0:7000/drivers/{driver_id}```
```GET http://0.0.0.0:7000/drivers/{driver_id}/cars```
```GET http://0.0.0.0:7000/drivers/{driver_id}/tickets```

Returns information about driver, cars or tickets based on ```driver_id```.

Example requests:
```
curl -X GET -H "Auth-Token: $API_AUTH_TOKEN" http://0.0.0.0:7000/drivers/1

```
```
curl -X GET -H "Auth-Token: $API_AUTH_TOKEN" http://0.0.0.0:7000/drivers/1/cars

```
```
curl -X GET -H "Auth-Token: $API_AUTH_TOKEN" http://0.0.0.0:7000/drivers/1/tickets

```

Example responses:
```
{"name":"Elizabeth","surname":"Horne","age":65}
```
```
[{"brand":"Ford","model":"yes","year_of_production":2020,"mileage":420655,"color":"silver","driver_id":1},{"brand":"Opel","model":"air","year_of_production":2012,"mileage":221423,"color":"silver","driver_id":1},{"brand":"Opel","model":"product","year_of_production":2015,"mileage":455047,"color":"red","driver_id":1},{"brand":"Opel","model":"Astra","year_of_production":2005,"mileage":200000,"color":"silver","driver_id":1}]
```
```
[{"driver_id":1,"car_id":17,"fine":3721,"penalty_points":8},{"driver_id":1,"car_id":22,"fine":4062,"penalty_points":7},{"driver_id":1,"car_id":22,"fine":1484,"penalty_points":1},{"driver_id":1,"car_id":22,"fine":972,"penalty_points":2},{"driver_id":1,"car_id":22,"fine":4769,"penalty_points":10},{"driver_id":1,"car_id":1,"fine":500,"penalty_points":5}]
```
