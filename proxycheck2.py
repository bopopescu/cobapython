import pycurl
import mysql.connector

db = mysql.connector.connect(
    host="103.41.204.195",
    user="brofist",
    passwd="brofist19#",
    database="nsam_tools"

)

def process_checker(ip,port):
    ch = pycurl.Curl()
    # ch.setopt(pycurl.URL, ip)
    ch.setopt(pycurl.PROXY, ip)
    ch.setopt(pycurl.PROXYPORT,port)
    ch.setopt(pycurl.CONNECTTIMEOUT, 10)

    tanggapan = ch.perform()
    print(tanggapan)

if db.is_connected():
    print("Connected Succesfully!")
    cursor = db.cursor()
    sql = "SELECT ip_address,url,port,apn FROM t_fraud_test_progress_detail WHERE modem = 'modem-1'"
    cursor.execute(sql)
    results = cursor.fetchall()

    for data in results:
        ip = data[0]
        if ip is None:
            ip = data[1]
        port = data[2]
        print(ip,":",port)
        # process_checker(ip,port)


# proxy = []

