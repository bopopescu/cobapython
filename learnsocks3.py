import socket
    import urllib2
    import threading
    import sys
    import Queue
    import socket

    socket.setdefaulttimeout(7)

    print("Bobng's proxy checker. Using %s second timeout"%(socket.getdefaulttimeout()))

    #input_file = sys.argv[1]
    #proxy_type = sys.argv[2] #options: http,s4,s5
    #output_file = sys.argv[3]
    input_file = 'proxylist.txt'
    proxy_type = 'http'
    output_file = 'proxy_alive.txt'

    url = "www.seemyip.com" # Don't put http:// in here, or any /'s

    check_queue = Queue.Queue()
    output_queue = Queue.Queue()
    threads = 20

    def writer(f,rq):
        while True:
            line = rq.get()
            f.write(line+'\n')

    def checker(q,oq):
        while True:
            proxy_info = q.get() #ip:port
            if proxy_info == None:
                print("Finished")
            #quit()
                return
            #print "Checking %s"%proxy_info
            if proxy_type == 'http':
                try:

            listhandle = open("proxylist.txt").read().split('\n')

            for line in listhandle:
                saveAlive = open("proxy_alive.txt", 'a')

                details = line.split(':')
                email = details[0]
                password = details[1].replace('\n', '')


                proxy_handler = urllib2.ProxyHandler({'http':proxy_info})
                opener = urllib2.build_opener(proxy_handler)
                opener.addheaders = [('User-agent','Mozilla/5.0')]
                urllib2.install_opener(opener)
                req = urllib2.Request("http://www.google.com")
                sock=urllib2.urlopen(req, timeout= 7)
                rs = sock.read(1000)
                if '<title>Google</title>' in rs:
                    oq.put(proxy_info)
                    print('[+] alive proxy' , proxy_info)
                    saveAlive.write(line)
                    saveAlive.close()
                except urllib2.HTTPError,e:
                    print('url open error? slow?')
                    pass
                except Exception,detail:
                    print('[-] bad proxy' ,proxy_info)

            else:
                # gotta be socks
                try:
                    s = socks.socksocket()
                    if proxy_type == "s4":
                        t = socks.PROXY_TYPE_SOCKS4
                    else:
                        t = socks.PROXY_TYPE_SOCKS5
                    ip,port = proxy_info.split(':')
                    s.setproxy(t,ip,int(port))
                    s.connect((url,80))
                    oq.put(proxy_info)
                    print proxy_info
                except Exception,error:
                    print proxy_info

    threading.Thread(target=writer,args=(open(output_file,"wb"),output_queue)).start()
    for i in xrange(threads):
        threading.Thread(target=checker,args=(check_queue,output_queue)).start()
    for line in open(input_file).readlines():
        check_queue.put(line.strip('\n'))
    print "File reading done"
    for i in xrange(threads):
        check_queue.put(None)
    raw_input("PRESS ENTER TO QUIT")
    sys.exit(0)