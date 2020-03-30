import threading
import pymysql.cursors
import random
import string
# from random import randint
import uuid
import json
stringLength = 8

db = pymysql.connect(host='127.0.0.1',
                     user='root',
                     password='',
                     db='test',
                     charset='utf8mb4',
                     cursorclass=pymysql.cursors.DictCursor
)
conn = db.cursor()

def randomString(stringLength):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

def main_insert():
    kata = randomString(50)
    nilai = random.randint(0, 100)
    randoma = uuid.uuid4().hex
    ket = randoma.lower()[0:stringLength]

    sql = "INSERT INTO t_test_threading(kata,nilai,ket) VALUES (%s,%s,%s)"
    data = (kata,nilai,ket)
    conn.execute(sql, data)

def exec_update(id,nilai):
    nilai_baru = nilai + 3
    sql_upt = "UPDATE t_test_threading SET nilai = %s WHERE id = %s" % (nilai_baru,id)
    conn.execute(sql_upt)
    db.commit()

def update():
    sql = "SELECT id,kata,nilai,ket FROM t_test_threading"
    conn.execute(sql)
    hasil = conn.fetchall()

    for data in hasil:
        y = json.dumps(data)
        z = json.loads(y)
        id = z["id"]
        nilai = z["nilai"]
        t = threading.Thread(target=exec_update, args=(id,nilai))
        t.start()
    # db.commit()

# for x in range(1000):
#     t = threading.Thread(target=main_insert)
#     t.start()
#     # main()
# db.commit()
update()
# conn.close()