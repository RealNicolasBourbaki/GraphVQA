"""
What is dependency tree?

A dependency tree for a sentence is a directed acyclic graph with words as nodes and relations as edges. Each word in
the sentence either modifies another word or is modified by a word. The root of the tree is the only entry that is
modified but does not modify anything else.

An Dependency tree should meet few constraints:
- Single-head
- Connected
- Acyclic

Taken together, these constraints ensure that each word has a single head, that the dependency structure is
connected, and that there is a single root node from which one can follow a unique directed path to each of the words
in the sentence

"""

from spacy import displacy
from pymongo import MongoClient
import spacy

nlp = spacy.load("en_core_web_sm")


def get_dependency_tree(question):
    triples = []
    doc = nlp(question)
    #print(f"{'Node (from)-->':<15} {'Relation':^10} {'-->Node (to)':>15}\n")
    for token in doc:
        # print("{:<15} {:^10} {:>15}".format(str(token.head.text), str(token.dep_), str(token.text)))
        triples.append([str(token.head.text), str(token.dep_), str(token.text)])
    # displacy.render(doc, style='dep')
    return triples


if __name__ == "__main__":
    c = MongoClient(port=27017)
    db = c.GraphVQA
    collection = db.train_all_questions
    docs = collection.find()
    k = 0
    for doc in docs:
        k += 1

        if k >= 920082:
            ques = doc["question"]
            print(k, ques)
            dep_tree_triples = get_dependency_tree(ques)
            collection.update_one({"_id": doc["_id"]}, {"$set": {"pipe": 11, "dep_tree": dep_tree_triples}})

print("Mongo Updated !")
# store


#