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

# Running an aggregate query on mongoDB table rest_detail for average rating for each type of food in the descending order of average ratings
result= rest_detail.aggregate([{"$group" :{"_id": {'Type of Food':"$type_of_food"}, "Average_Rating":{"$avg":"$rating"}}},
                               {"$sort":{'Average_Rating':-1}}
                              ])

# Printing all the rows fetched by above query
print("Average Restaurant rating for food type are - ")
print("")
for i in result:
    print(i)