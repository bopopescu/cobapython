import datetime
import urllib.request as urllib2

now = datetime.datetime.now()
started = now.strftime("%Y-%m-%d %H:%M:%S")

addresses = ['177.99.206.82:8080','34.83.71.102:8080','37.120.159.64:80','118.174.46.144:45330']
# address = '37.120.159.64:80'
for address in addresses:
    try:
        proxy_handler = urllib2.ProxyHandler({'http': address})
        opener = urllib2.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib2.install_opener(opener)
        req = urllib2.Request("http://103.41.204.195/ping.php")
        sock = urllib2.urlopen(req, timeout=10)
        rs = sock.read(1000)
        print(rs)
        if rs is None:
            proxy_result = "No"
        else:
            proxy_result = "Yes"
        now = datetime.datetime.now()
        finished = now.strftime("%Y-%m-%d %H:%M:%S")
    except:
        proxy_result = "No"
        now = datetime.datetime.now()
        finished = now.strftime("%Y-%m-%d %H:%M:%S")

    print(address,proxy_result,started,finished)