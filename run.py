import glob, os
import json, re
from pydash import omit


DIR = os.path.dirname(os.path.abspath(__file__))

files = json.load(open("alamat.json"))
for i in glob.glob("data/*.json"):
    data = json.load(open(f"{DIR}/{i}"))
    for d in data:
        alamat = re.split(' ',d['alamat'], maxsplit=1)[-1:2][0].replace(" Regency", "").replace("East Java", "Jawa Timur")
        file_alamat = omit(d, 'alamat')
        file_alamat.update({
            "alamat": alamat
        })
        
        files.append(file_alamat)


with open("alamat.json", "w") as f:
    json.dump(
        files, f
    )