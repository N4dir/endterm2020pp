#IMPORTING PYMONGO TO WORK WITH MONGODB
import pymongo
import ssl

#CONNECTING TO OUR SERVER
client = pymongo.MongoClient("mongodb+srv://nadir:pkChz2-NsnYJP6J@nadir-xtrb4.mongodb.net/test?retryWrites=true&w=majority", ssl_cert_reqs = ssl.CERT_NONE)



#CREATING A DATABASE

mydb = client['mydb']

#PRINTING ALL AVAILABLE DATABASES
print(client.list_database_names())



#CREATING  A COLLECTION

mycol = mydb['students']

#PRINTING ALL AVAILABLE COLLECTIONS
print(mydb.list_collection_names())



#IMPORTING ONE
mydict = {'name': 'Abzal', 'gpa': '3.7'}

#INSERTING A NEW DICTIONARY TO COLLECTION
x = mycol.insert_one(mydict)

#PRINTING THE INSERTED ID OF THE INSERTED DOCUMENT
print(x.inserted_id)



#IMPORTING MULTIPLE DOCS

mylist = [
  { "name": "Amy", "gpa": "2.3"},
  { "name": "Hannah", "gpa": "1.7"},
  { "name": "Michael", "gpa": "4.0"},
  { "name": "Sandy", "gpa": "3.2"},
  { "name": "Betty", "gpa": "2.1"},
  { "name": "Richard", "gpa": "1.5"},
  { "name": "Susan", "gpa": "3.4"},
  { "name": "Vicky", "gpa": "2.8"},
  { "name": "Ben", "gpa": "3.8"},
  { "name": "William", "gpa": "2.5"},
  { "name": "Chuck", "gpa": "3.1"},
  { "name": "Viola", "gpa": "2.2"}  
]

#INSERTING A NEW LIST TO COLLECTION
x = mycol.insert_many(mylist)

#PRINTING THE INSERTED IDs OF THE INSERTED DOCUMENTS
print(x.inserted_ids)



#SEARCHING OF DOCS

#FIND FIRST DOCUMENT IN THE COLLECTION
x = mycol.find_one()
print(x)

#RETURN ALL THE DOCUMENTS IN THE COLLECTION
for x in mycol.find():
   print(x)

#FINDING BY INCLUDING/EXCLUDING SOME PAPREMETERS
for x in mycol.find({},{ "name": 1 }):
   print(x)



#SEARCHING BY QUERY

#FIND ALL THE DOCUMENTS WITH GPA 3.1
myquery = {"gpa": "3.1"}
mydoc = mycol.find(myquery)
for x in mydoc:
   print (x)



#ADVANCED SEARCHING BY QUERY

#FIND ALL THE DOCUMENT WITH GPA GREATER THAN 2.0
myquery = {"gpa": {"$gt":"2.0"}}
mydoc = mycol.find(myquery)
for x in mydoc:
    print(x)



#SORT

#SORTING BY NAME FROM A TO Z
mydoc = mycol.find().sort("name")
for x in mydoc:
    print(x)

#SORTING BY NAME FROM Z TO A
mydoc = mycol.find().sort("name", -1)
for x in mydoc:
    print(x)



#DELETE

#DELETE ONE DOCUMENT
myquery = {"name": "Abzal"}
mycol.delete_one(myquery)

#DELETE MULTIPLE DOCS
myquery = { "gpa": {"$gt": "3.0"} }
x = mycol.delete_many(myquery)
print(x.deleted_count, "documents deleted.")

#DELETE ALL DOCS
x = mycol.delete_many({})
print(x.deleted_count, "documents deleted.")



#DELETING BY DROP

#WE CAN DELETE THE WHOLE COLLECTION BY FUNCTION DROP()
mycol.drop()



#UPDATE

#UPDATE ONE DOCUMENT

#SETTING NEW VALUE
myquery = {"name": "Amy"}
new_val = {"$set": {"name": "Andy"}}

#UPDATE ONE DOCUMENT FUNCTION
mycol.update_one(myquery, new_val)

#PRINTING THE RESULT AFTER UPDATING
for x in mycol.find():
    print(x)



#UPDATE MULTIPLE DOCS

#SETTING NEW VALUES
myquery = {"gpa": {"$gt": "2.0"}}
new_val = {"$set": {"gpa": "4.0"}}

#UPDATING MULTIPLE DOCS FUNCTION
x = mycol.update_many(myquery,new_val)

#PRINTING THE RESULT AFTER UPDATING
print(x.modified_count, "uptated docs")



#LIMIT THE RESULT

#LIMITS THE NUMBER OF PRINTED DOCUMENTS
myresult = mycol.find().limit(2)
for x in myresult:
    print(x)