# GraphQL service

## Queries

```getDrivers```

Example request:
```
 curl -X POST -H "Auth-Token: $API_AUTH_TOKEN" -H "Content-Type: application/json" -d '{"query": "query{getDrivers(limit: 10){name surname age}}"}'  http://0.0.0.0:8000/graphql
```
Example response:
```
{"data":{"getDrivers":[{"name":"Elizabeth","surname":"Horne","age":65},{"name":"Brian","surname":"Hubbard","age":67},{"name":"Victoria","surname":"Conrad","age":23},{"name":"Edward","surname":"Mitchell","age":19},{"name":"Brian","surname":"Curtis","age":50},{"name":"Matthew","surname":"Sanders","age":54},{"name":"Andrew","surname":"Valdez","age":43},{"name":"Patricia","surname":"Ramos","age":17},{"name":"Erik","surname":"Arellano","age":37},{"name":"Mark","surname":"Morales","age":34}]}}
```

___

```getDriver```

Example request:
```
curl -X POST -H "Auth-Token: $API_AUTH_TOKEN" -H "Content-Type: application/json" -d '{"query": "query{getDriver(driverId: 1){name surname age}}"}'  http://0.0.0.0:8000/graphql
```
Example response:
```
{"data":{"getDriver":{"name":"Elizabeth","surname":"Horne","age":65}}}
```

___

```getDriverCars```

Example request:
```
curl -X POST -H "Auth-Token: $API_AUTH_TOKEN" -H "Content-Type: application/json" -d '{"query": "query{getDriverCars(driverId: 1){brand model}}"}'  http://0.0.0.0:8000/graphql
```
Example response:
```
{"data":{"getDriverCars":[{"brand":"Ford","model":"yes"},{"brand":"Opel","model":"air"},{"brand":"Opel","model":"product"},{"brand":"Opel","model":"Astra"}]}}
```

___

```getDriverTickets```

Example request:
```
curl -X POST -H "Auth-Token: $API_AUTH_TOKEN" -H "Content-Type: application/json" -d '{"query": "query{getDriverTickets(driverId: 1){fine penaltyPoints car { brand }}}"}'  http://0.0.0.0:8000/graphql

```
Example response:
```
{"data":{"getDriverTickets":[{"fine":3721,"penaltyPoints":8,"car":{"brand":"Ford"}},{"fine":4062,"penaltyPoints":7,"car":{"brand":"Opel"}},{"fine":1484,"penaltyPoints":1,"car":{"brand":"Opel"}},{"fine":972,"penaltyPoints":2,"car":{"brand":"Opel"}},{"fine":4769,"penaltyPoints":10,"car":{"brand":"Opel"}},{"fine":500,"penaltyPoints":5,"car":{"brand":"Ford"}}]}}
```


## Mutations

```generateData```

Example request:
```
curl -X POST -H "Auth-Token: $API_AUTH_TOKEN" -H "Content-Type: application/json" -d '{"query": "mutation{generateData{message}}"}'  http://0.0.0.0:8000/graphql
```
Response:
```
{"data":{"generateData":{"message":"Data generated"}}}
```

___

```createDriver```

Example request:
```
curl -X POST -H "Auth-Token: $API_AUTH_TOKEN" -H "Content-Type: application/json" -d '{"query": "mutation{createDriver(name: \"Adam\", surname: \"Taylor\", age: 40){message}}"}'  http://0.0.0.0:8000/graphql

```
Response:
```
{"data":{"createDriver":{"message":"Driver created"}}}
```

___

```createCar```

Example request:
```
curl -X POST -H "Auth-Token: $API_AUTH_TOKEN" -H "Content-Type: application/json" -d '{"query": "mutation{createCar(brand: \"Fiat\", model: \"Bravo\", yearOfProduction: 2008, mileage: 150000, color: \"black\", driverId: 2){message}}"}'  http://0.0.0.0:8000/graphql
```
Response:
```
{"data":{"createCar":{"message":"Car created"}}}
```

___

```createTicket```

Example request:
```
curl -X POST -H "Auth-Token: $API_AUTH_TOKEN" -H "Content-Type: application/json" -d '{"query": "mutation{createTicket(driverId: 2, carId: 3, fine: 1000, penaltyPoints: 10){message}}"}'  http://0.0.0.0:8000/graphql

```
Example response:
```
{"data":{"createTicket":{"message":"Ticket created"}}}
```

