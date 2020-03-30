import random
import string
import uuid
import threading
import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="",
    database="test"
)

conn = db.cursor()
stringLength = 8
data = []

def randomString(stringLength):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

def susun():
    kata = randomString(50)
    nilai = random.randint(0, 100)
    randoma = uuid.uuid4().hex
    ket = randoma.lower()[0:stringLength]
    isi_data = [kata,nilai,ket]
    data.append(isi_data)

for x in range(1000):
    t = threading.Thread(target=susun)
    t.start()
    t.join()
    # susun()

for isi in data:
    sql = "INSERT INTO t_test_threading(kata,nilai,ket) VALUES (%s,%s,%s)"
    data = (isi[0], isi[1], isi[2])
    conn.execute(sql, data)
db.commit()