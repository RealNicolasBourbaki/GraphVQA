import json

f = open('dataComplete.json')
jdata = json.load(f)

newData = []
f1 = open('amr.json')
amrData = json.load(f1)
print(len(amrData))
k = 0
for i in jdata:
    k += 1
    if i["_id"] not in amrData:
        newData.append(i)
print("Filtered data = ", len(newData))

with open('filteredData4.json', 'w') as json_file:
    json.dump(newData, json_file)

