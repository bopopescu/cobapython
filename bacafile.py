import urllib.request as urllib2

f = open("testingiphost.txt", "r")
for address in f:
  # address.replace("\n", "")

  ads = address.lstrip()
  addr = ads.rstrip()
  try:
    proxy_handler = urllib2.ProxyHandler({'http': addr})
    opener = urllib2.build_opener(proxy_handler)
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    urllib2.install_opener(opener)
    req = urllib2.Request("https://www.google.com/")
    # 103.41.204.195/ping.php
    sock = urllib2.urlopen(req, timeout=10)
    rs = sock.read(1000)
    if rs is None:
      proxy_result = "No"
    else:
      proxy_result = "Yes"
  except:
    proxy_result = "No"
  print(addr,proxy_result)