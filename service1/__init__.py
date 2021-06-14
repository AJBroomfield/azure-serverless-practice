import logging
import random
import requests
import azure.functions as func
from azure.cosmos import exceptions, CosmosClient, PartitionKey

#setting up a database
endpoint = "ENDPOINT"
key = 'PRIMARY_KEY'
client = CosmosClient(endpoint, key)

database_name = 'usrname-db'
database = client.create_database_if_not_exists(id=database_name)

container_name = 'namecontainer'
container = database.create_container_if_not_exists(
    id=container_name, 
    partition_key=PartitionKey(path="/username"),
    offer_throughput=400
)

def main(req: func.HttpRequest) -> func.HttpResponse:
    
    response_service2 = requests.get('https://usrgen.azurewebsites.net/api/service2?code=UujE1TYd8HE2b7orprlZytKYg52TRjZGef5jUB25OrAI8p1vXvtMow==')
    response_service3 = requests.get('https://usrgen.azurewebsites.net/api/service3?code=QktTMLtomxk/oA5vJWivQX0ZypOJl6Wy21jarQJRGhT02alCcB6lCw==')
    numbers = response_service2.text
    letters = response_service3.text

    
    username = numbers + letters
    username = list(username)
    random.shuffle(username)
    usr = ''.join(username)

    container.create_item(body={
        "id": str(1),
        "username": usr}
        )

    return func.HttpResponse(usr)

