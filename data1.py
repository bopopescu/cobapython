import mysql.connector

db = mysql.connector.connect(
    host="103.41.204.195",
    user="brofist",
    passwd="brofist19#",
    database="nsam_tools"

)

if db.is_connected():
    print("Connected Succesfully!")
    cursor = db.cursor()
    sql = "SELECT ip_address,url,port,apn FROM t_fraud_test_progress_detail WHERE modem = 'modem-1' AND test_type = 'proxy tunneling' LIMIT 10"
    cursor.execute(sql)
    results = cursor.fetchall()

    for data in results:
        ip = data[1]
        port = data[2]
        print(ip)

    # sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    # values = [
    #     ("Doni", "Jakarta"),
    #     ("Ella", "Surabaya"),
    #     ("Fani", "Bandung"),
    #     ("Galih", "Depok")
    # ]
    #
    # for val in values:
    #     cursor.execute(sql, val)
    #     db.commit()
    #
    # print("{} data ditambahkan".format(len(values)))