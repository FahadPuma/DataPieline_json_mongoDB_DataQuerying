#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import sys
from pymongo import MongoClient

client = MongoClient()

#Fetching database Restaurant and table rest_detail to run the query on the data
db = client['Restaurant']
rest_detail=db.rest_detail

# Collecting all arguments into a variable
n=sys.argv

# Running an aggregate query on mongoDB table rest_detail which receives type of food and zipcode of the restaurant
# as arguments and returns top 5 restaurants in the descending order of ratings
result= rest_detail.aggregate(
   [
     { "$match": { "$text": { "$search":n[1] } } },
     { "$sort": { "score": { "$meta": "textScore" } } },
     { "$project": {
                                                "_id": 0,
                                                "name": 1,
                                                "address": 1,
                                                "address_line2":1,
                                                "rating":1
                                            }}
   ]
)

# Printing all the rows fetched by above query for top 5 restaurants
print("Top 5 restaurants for food type: %s in the zipcode: %s are - " %(n[1],n[2]))
print("")
for i in result:
    print(i)