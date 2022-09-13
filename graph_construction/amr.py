"""
Author: Itisha Yadav
Purpose: This script takes json file [{"_id": 12334, "question": "What is the ques?"}, {}, {}]
    and writes amr parsed output in pickle db.
Place: Agra
Date: June 30th, 2022
"""
import threading
import penman
import spacy
import amrlib
import pickledb
import pandas as pd
import time



amrlib.setup_spacy_extension()
nlp = spacy.load('en_core_web_sm')
print("Spacy model loaded!.")


def amr(jdata, n):
    db_name = "amr_" + n +".db"
    print(db_name)
    db = pickledb.load(db_name, True)
    #jdata = [{"_id": 1233, "question": "What is the ques1?"}, {"_id": 1237, "question": "What is the ques2?"}]
    k = 0
    for entry in jdata:
        k += 1
        print(k)
        q = entry["question"]
        t1 = time.time()
        doc = nlp(q)
        amr = []
        graphs = doc._.to_amr()
        for graph in graphs:
            g = penman.decode(graph)
            amr.append(g.triples)
        db.set(str(entry["_id"]), (q, amr))
#        print("Time = ", time.time()-t1)
    db.dump()


if __name__ == "__main__":
    import sys
    chunk_no = sys.argv[1]
    import json
    f = open('filteredData4.json')
    jdata = json.load(f)
    chunks = [jdata[x:x + 30000] for x in range(0, len(jdata), 30000)]
    chunk_data = chunks[int(chunk_no)]
    amr(chunk_data, chunk_no)
