def socks_adadeh(host,port,timeout):
    print(host, port)
    # HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
    # PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
    port2 = int(port)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port2))
        s.listen(1)
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)

def socks_adalagi():
    target_host = "103.41.204.195" # "www.google.com"

    target_port = 80  # create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect the client
    client.connect((target_host, target_port))

    # send some data
    request = "GET /ping.php HTTP/1.1\r\nHost: 103.41.204.195\r\n\r\n"
    client.send(request.encode())
    # client.sendall(b'Hello, world')
    # receive some data
    response = client.recv(4096)
    http_response = repr(response)
    http_response_len = len(http_response)
    print(response)
    eheh = response.splitlines()
    hehe = eheh[0].split()
    print(hehe[1])

    # display the response
    # gh_imgui.text("[RECV] - length: %d" % http_response_len)
    # gh_imgui.text_wrapped(http_response)





    #     s = socks.socksocket() # socket.AF_INET, socket.SOCK_STREAM
    #     # t = socks.PROXY_TYPE_SOCKS4
    #     t = socks.SOCKS4
    #     url = "https://www.google.com/"
    #     s.settimeout(timeout)
    #     s.setproxy(t, host, int(port))
    #     s.connect((url, 80))
    #     # s.listen()
    #     # s.sendall("GET / HTTP/1.1 ...")
    #     print(s.recv(4096))
    #     # print(s)
    #
    #     s.shutdown()
    #     s.close()
    #     s = None
    #     t = None
    #
    # except socks.GeneralProxyError:
    #     socks.set_default_proxy(socks.SOCKS4, host, int(port))
    #     s.send(b'GET http://103.41.204.195/ping.php HTTP/1.1\n')

    # socket.socket = socks.socksocket # connect socket
    # baca = urllib.urlopen("https://www.google.com/", timeout=timeout)
    # res = baca.read(1000)
    # if res is None:
    #     res2 = requests.get("https://www.google.com/", timeout=timeout)
    #     if res2.text is None:
    #         print("No")
    #     else:
    #         print("Yes")
    # else:
    #     print(res)
    #     print("Yes")
    # except urllib.error.URLError:
    #     s = socks.socksocket()
    #     t = socks.SOCKS4
    #     s.settimeout(timeout)
    #     s.setproxy(t, host, int(port))
    #     socket.socket = s
    #     baca = urllib.urlopen("https://www.google.com/", timeout=timeout)
    #     res = baca.read(1000)
    #     if res is None:
    #         res2 = requests.get("https://www.google.com/", timeout=timeout)
    #         if res2.text is None:
    #             print("No")
    #         else:
    #             print("Yes")
    #     else:
    #         print(res)
    #         print("Yes")
    #
    #     s.shutdown()
    #     s.close()
    #     s = None
