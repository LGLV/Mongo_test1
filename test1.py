import pymongo
client = pymongo.MongoClient("mongodb+srv://lglv:lglvellilll@cluster0.ldfcioo.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    'name': 'luis',
    'email': 'lgermanlv@gmail.com',
    'surname': 'lopez'
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )