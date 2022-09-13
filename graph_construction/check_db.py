
#https://pythonhosted.org/pickleDB/commands.html

import sys
n = sys.argv[1]
import pickledb
import json

db_name = "amr_" + n +".db"
print(db_name)

db = pickledb.load(db_name, False)
print(len(db.getall()))

