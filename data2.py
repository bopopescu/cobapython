import pymysql.cursors

# Connect to the database
conn = pymysql.connect(host='127.0.0.1',
                       user='root',
                       password='',
                       db='test',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)

try:
    with conn.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('webmain@python.org', 'very-secret'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    conn.commit()

    with conn.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('webmain@python.org',))
        result = cursor.fetchone()
        print(result)
finally:
    conn.close()