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

# Running an aggregate query on mongoDB table rest_detail which receives type of food of the restaurant
# as arguments and returns count of restaurants in the zip code
result= rest_detail.aggregate([{"$match":{'type_of_food':n[1]}},
                               {"$group" :{"_id": {'zip':"$zipcode"}, "count":{"$sum":1}}},
                               {"$sort":{'count':-1}}
                              ])

# Printing all the rows fetched by above query
print("Restaurant count for food type: %s in the zipcodes are - " %(n[1]))
print("")
for i in result:
    print(i)