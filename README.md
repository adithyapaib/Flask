
# Pizza-House 🍕

A simple Flask API to accept and fetch Pizza orders 




## Installation

Install this project with Github

```bash
  git clone 
  cd Flask
  pip3 install -r requirements.txt
  sudo apt-get update && apt-get install -y rabbitmq-server
  python3 app.py
```
#### ❕ Make sure mongodb is running before running the Application
## API Reference

### welcome

```http
  GET /welcome
```

Returns a welcome JSON Message




### Send Orders

```http
  POST /order
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `order`      | `Array` | **Required**. The JSON body with Pizza orders |


#### Sample POST BODY JSON
``
 {"order": ["Pizza1", "Pizza2"]}
``

### Get all Orders

```http
  GET /getorders
```
  Returns a JSON with all the Pizza Orders

### Get Particular Order

```http
  GET /getorders/<order_id> 
```
  Returns Order details of a given order id , 404 Not found if record not present.

  
## Appendix
Make sure MongoDB is running locally or else the user can also run a MongoDB Docker container using the following command for the application to run.

```bash
docker run -d -p 27017:27017 --name mongo mongo:latest
```



## Testing

The project can be tested using with the follwing command.

```bash
  python3 -m pytest
```


## Todo
- Dockerize container and deploy to Dockerhub
- Write dockercompose file to combine mongo and flask app deployments

