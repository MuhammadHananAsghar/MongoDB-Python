import pymongo

# Create Connection
client = pymongo.MongoClient("mongodb://localhost:27017/")
# Create MyDB
mydb = client["database"]
# Get list of Databases
dblist = client.list_database_names()
if "database" in dblist:
  	print("The database exists.")
else:
	print("Not exists database.")
# Create Collection Like table in SQL Databases
col = mydb["customers"]
# Get list of Collections in Database
collist = mydb.list_collection_names()
if "customers" in collist:
	print("The collection exists.")
else:
	print("Not exists collection.")

# Insert Data in Database 
mydict = { "name": "John", "address": "Highway 37" }
# Inserting one value
x = col.insert_one(mydict)
# Checking the id of inserted value
print(x.inserted_id)


# If you want to insert many values use list of dictionaries
mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]

x = col.insert_many(mylist)

#print list of the _id values of the inserted documents:
print(x.inserted_ids) 

# If you do not want MongoDB to assign unique ids for you document, you can specify the _id field when you insert the document(s).

#mylist = [
 # { "_id": 1, "name": "John", "address": "Highway 37"},
  #{ "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
  #{ "_id": 3, "name": "Amy", "address": "Apple st 652"},
  #{ "_id": 4, "name": "Hannah", "address": "Mountain 21"},
  #{ "_id": 5, "name": "Michael", "address": "Valley 345"},
  #{ "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
  #{ "_id": 7, "name": "Betty", "address": "Green Grass 1"},
  #{ "_id": 8, "name": "Richard", "address": "Sky st 331"},
  #{ "_id": 9, "name": "Susan", "address": "One way 98"},
 # { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
 # { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
 # { "_id": 12, "name": "William", "address": "Central st 954"},
 # { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
 # { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
#]

#x = col.insert_many(mylist)

#print list of the _id values of the inserted documents:
#print(x.inserted_ids) 


# Get one value from databse
x = col.find_one()
print(x)

# Get many values from database
for y in col.find():
  print(y) 

# Return Only Specific values
for g in col.find({},{"_id":0, "name":1}):
	print(g)

# Search from mongo
myquery = { "address": "Park Lane 38" }

mydoc = col.find(myquery)

for x in mydoc:
  print(x) 


#Sort the result alphabetically by name:
mydoc = col.find().sort("name")

for x in mydoc:
  print(x) 

# Sort the result reverse alphabetically by name:
mydoc = col.find().sort("name", -1)

for x in mydoc:
  print(x) 


# Delete the document with the address "Mountain 21":

myquery = { "address": "Mountain 21" }

col.delete_one(myquery) 

# Change the address from "Valley 345" to "Canyon 123":

myquery = { "address": "Valley 345" }
newvalues = { "$set": { "address": "Canyon 123" } }

col.update_one(myquery, newvalues)
