import pickledb
import sys


def merge(db_list):
    #db_list = ["amr_2.db", "amr_3.db"]
    temp = {}
    for db in db_list:
        print(db)
        if db.endswith(".db"):
            db = pickledb.load(db, False)
            for key in db.getall():
                temp[key] = db.get(key)
        elif db.endswith(".json"):
            f = open(db)
            data = json.load(f)
            for i in data:
                temp[i] = data[i]
        else:
            for key, value in db.items():
                temp[key] = value
    return temp


if __name__ == "__main__":
    import argparse
    import json
    CLI = argparse.ArgumentParser()
    CLI.add_argument(
        "--lista",
            nargs="*")
    args = CLI.parse_args()
    n = args.lista
    res = merge(n)
    print(len(res))
    with open('amr.json', 'w') as json_file:
        json.dump(res, json_file)


