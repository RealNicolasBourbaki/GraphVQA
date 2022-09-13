import json

from pymongo import MongoClient
import pandas as pd

c = MongoClient(port=27017)
db = c.GraphVQA
collection = db.train_all_questions

temp = []
docs = collection.find()
k = 0
for doc in docs:
    k += 1
    print(k)
    temp.append([doc["question"], doc["dep_tree"]])
df = pd.DataFrame(temp, columns=['question', "dep_tree"])
df.to_json("./parsed_questions.json")