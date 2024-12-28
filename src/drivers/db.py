from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from datetime import datetime, timezone

from src.accounts.schemas import UserRegister, UserFind
from src.drivers.hasher import get_password_hash

uri = "mongodb+srv://ishan:ishan@auth.wlunjzj.mongodb.net/?retryWrites=true&w=majority&appName=Auth"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))  # type: ignore
db = client.get_database("lokdata")
accoll = db.get_collection("accounts")
sucoll = db.get_collection("surveys")

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


def get_acc(query: dict):
    q = {key: value for key, value in query.items()
         if value != None}
    user = accoll.find_one(q)
    return user


def insert_acc(data: UserRegister):
    user = data.model_dump()
    email_s = get_acc(UserFind(email=data.email).model_dump())
    pn_s = get_acc(
        UserFind(phone_number=data.phone_number).model_dump())
    if email_s is not None or pn_s is not None:
        return False
    user["disabled"] = True
    user["datetime"] = datetime.now(timezone.utc)
    # print(u := user["phone_number"])
    # print(dir(u))
    user["hashed_password"] = get_password_hash(user["password"])
    user.pop("password")
    res = accoll.insert_one(user)
    return res.acknowledged


def insert_survey(data: dict):
    res = sucoll.insert_one(data)
    return res.acknowledged
