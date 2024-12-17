from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://elm:FoundationOMEN05@virtualeventorganizer.wmum2.mongodb.net/?retryWrites=true&w=majority&appName=VirtualEventOrganizer"

client = MongoClient(uri, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)