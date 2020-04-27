import os
import mysql.connector
import threading
import time

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="",
    database="brofistool"
)

conn = db.cursor()
hasil_test = []

def dns_check(id,link):
    # dig (domain information groper)
    print(link, threading.currentThread().getName(), 'Starting')
    perintah = "dig %s"% link
    with os.popen(perintah) as f:
        if 'ANSWER SECTION' in f.read():
            dns_result = "Yes"
        else:
            dns_result = "No"
    isi_test = (id,dns_result)
    hasil_test.append(isi_test)
    print(threading.currentThread().getName(), 'Exiting')

def escapeshellarg(arg):
    return "\\'".join("'" + p + "'" for p in arg.split("'"))

if db.is_connected():
    query_apn = "SELECT apn FROM t_fraud_test_progress_detail GROUP BY apn"
    conn.execute(query_apn)
    apns = conn.fetchall()
    for apn in apns:
        query_proxy = "SELECT id,ip_address,url,port " \
                      "FROM t_fraud_test_progress_detail " \
                      "WHERE suspect_fraud IS NULL " \
                      "AND modem = 'modem-1' " \
                      "AND apn = '%s' " \
                      "AND test_type = 'dns tunneling' " \
                      "ORDER BY id ASC " \
                      "LIMIT 100" % apn[0]
        conn.execute(query_proxy)
        proxies = conn.fetchall()
        for data in proxies:
            id = data[0]
            ip = data[1]
            if ip == "" or ip is None:
                ip = data[2]
            t = threading.Thread(target=dns_check, args=(id,ip))
            t.start()
t.join()
time.sleep(10)
print(hasil_test)
