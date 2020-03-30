import mysql.connector as mysql
import threading
import datetime

db_cloud = mysql.connect(
    host="103.41.204.195",
    user="brofist",
    passwd="brofist19#",
    database="nsam_tools"
)

db_local = mysql.connect(
    host="127.0.0.1",
    user="root",
    passwd="",
    database="research"
)

conn_cloud = db_cloud.cursor()
conn_local = db_local.cursor()
limit = 1000

def pull():
    sql_pull = "SELECT * " \
               "FROM t_fraud_test_progress_detail " \
               "WHERE suspect_fraud IS NULL " \
               "ORDER BY id ASC " \
               "LIMIT %s" % limit
    conn_cloud.execute(sql_pull)
    result = conn_cloud.fetchall()
    for data in result:
        t = threading.Thread(target=insert_pull, args=[data])
        t.start()
    t.join
    db_local.commit()

def insert_pull(frauds):
    print(threading.currentThread().getName(), 'Starting')
    for data in frauds:
        # code = int([data[1]])
        print(data)
        print(data)
        exit()
        # created = data[2]
        # ip = data[5]
        # url = data[6]
        # port = data[7]
        # category = data[9]
        # suspect = data[11]
        # modem = data[13]
        # msisdn = data[14]
        # apn = data[15]
        # test_type = data[16]
        sql = "INSERT INTO t_fraud_test_progress_detail(code,created_at,ip_address,url,port,category,suspect_fraud,modem,msisdn,apn,test_type) " \
              "VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
        data = (code,created,ip,url,port,category,suspect,modem,msisdn,apn,test_type)
        conn.execute(sql, data)
    print(threading.currentThread().getName(), 'Exiting')

# def push():
#     sql_push = ""

pull()