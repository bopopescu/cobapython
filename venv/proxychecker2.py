import urllib.request
import socket
import urllib.error

def is_bad_proxy(pip):
    try:
        proxy_handler = urllib.request.ProxyHandler({'http': pip})
        opener = urllib.request.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)
        req=urllib.request.Request('https://www.google.com/')  # change the URL to test here
        sock=urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        print('Error code: ', e.code)
        return e.code
    except Exception as detail:
        print("ERROR:", detail)
        return True
    return False

def main():
    socket.setdefaulttimeout(120)
    # two sample proxy IPs
    proxyList = ['audisi.ruangguru.com:443', 'ruangguru.com:443','uji.ruangguru.com:443','ruangguruuji.imgix.net:443']
    # ['159.203.166.41:8080','139.59.53.107:3128','196.52.80.75:80','174.138.54.49:8080','194.228.129.189:32753','185.188.218.10', '60928','81.28.164.55:52658','196.52.58.235:80']
    #
    # ['125.76.226.9:80', '25.176.126.9:80']
    # ['194.228.129.189:32753', '185.188.218.10:60928', '81.28.164.55:52658', '196.52.58.235:80']

    for currentProxy in proxyList:
        if is_bad_proxy(currentProxy):
            print("Bad Proxy %s" % (currentProxy))
        else:
            print("%s is working" % (currentProxy))

if __name__ == '__main__':
    main()