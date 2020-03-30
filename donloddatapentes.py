import mysql.connector

db = mysql.connector.connect(
    host="103.41.204.195",
    user="brofist",
    passwd="brofist19#",
    database="nsam_tools"
)

conn = db.cursor()

sql = "SELECT id,ip_address,url,port " \
      "FROM t_fraud_test_progress_detail " \
      "WHERE url IS NULL " \
      "AND modem = 'modem-1' " \
      "AND test_type = 'proxy tunneling' "
conn.execute(sql)
result = conn.fetchall()
for data in result:
    id = data[0]
    ip = data[2]
    if ip is None or ip == "":
        ip = data[1]
    port = data[3]
    if port is None:
        port = 1080
    print(id,ip,port)
    hasills = ip + ":" + port
    f = open("testingiphost.txt", "a")
    f.write(hasills + "\n")
    f.close()