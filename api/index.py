from flask import Flask
from flask import jsonify
import os, json, random, compress_json, re
from pydash import omit

app = Flask(__name__)
DIR = os.path.dirname(os.path.abspath(__file__))


def randomData():
    nama    = compress_json.load(f"{DIR}/nama.json.lzma")
    alamat  = compress_json.load(f"{DIR}/alamat.json.lzma")
    devices = compress_json.load(f"{DIR}/devices.json.lzma")
    
    random_nama = nama[random.randint(0, len(nama) -1)]
    random_alamat = alamat[random.randint(0, len(alamat) -1)]
    random_devices = devices[random.randint(0, len(devices) -1)]
    list_rt = [
        f"Rt.{random.randrange(1, 30)}/Rw.{random.randrange(2, 44)}",
        f"rt.{random.randrange(1, 30)}/rw.{random.randrange(2, 44)}",
        f"RT.{random.randrange(1, 30)}/RW.{random.randrange(2, 44)}",
        f"Rt.{random.randrange(1, 30)} Rw.{random.randrange(2, 44)}",
        f"Rt.{random.randrange(1, 30)} rw.{random.randrange(2, 44)}",
        f"RT.{random.randrange(1, 30)} RW.{random.randrange(2, 44)}"
    ]
    random_rt = [list_rt[random.randint(0, len(list_rt)-1)] for _ in range(10)]
    alamatFake = random_alamat['alamat']
    print(alamatFake)
    try:
        assert re.search(r'(rt.|RT.|Rt.)', alamatFake) == True
        jsonAlmat = random_alamat
    except:
        base = re.split(",", alamatFake,maxsplit=3)
        a1, a2 = base[0:3], base[-1]
        data_alamat = ','.join(a1) + f",{random.choice(random_rt)}"
        data = data_alamat.split(",")
        random.shuffle(data)
        jsonAlmat = ",".join([
            ", ".join(
                data
            ),a2
        ])
    
    return {
        "nama": random_nama,
        "alamat": jsonAlmat.strip(),
        "devices": random_devices
    }




@app.route("/generate")
def random_props():
    return jsonify(
        randomData()
    )


if __name__ == '__main__':
    app.run(debug=True)

