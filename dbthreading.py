import MySQLdb
import threading

def write_good_proxies():
    local_db = MySQLdb.connect("127.0.0.1","root","","test", port=3306 )
    local_cursor = local_db.cursor (MySQLdb.cursors.DictCursor)
    sql_select = 'select http from zproxies where update_time is null order by rand() limit 10'
    local_cursor.execute(sql_select)
    records = local_cursor.fetchall()
    id_list = [f['http'] for f in records]
    print(id_list)

def worker():
    x=0
    while x< 5:
        x = x+1
        write_good_proxies()

threads = []


for i in range(5):
    print(i)
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()