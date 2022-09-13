train = "/mount/arbeitsdaten61/studenten3/advanced-ml/2022/gogirlspower/nicole/GraphVQA/questions/backup/train_balanced_programs.json"
test = "/mount/arbeitsdaten61/studenten3/advanced-ml/2022/gogirlspower/nicole/GraphVQA/questions/backup/testdev_balanced_programs.json"

import json
with open(train) as obj:
    train_data = json.load(obj)

with open(test) as obj2:
    test_data = json.load(obj2)

def stats(obj):
    stats_dict = {}
    for d in obj:
        type = d[-1]["structural"]
        if type in stats_dict:
            stats_dict[type] = stats_dict[type]+1
        else:
            stats_dict[type] = 1
    return stats_dict

print("train", stats(train_data))
print("test", stats(test_data))

