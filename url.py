# import urllib2
try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen
import threading

def get_content_len(url):
    response = urlopen(url)
    content = response.read()
    print(len(content))

urls = [
    "http://www.codepolitan.com", 
    "http://www.codepolitan.com/articles",
    "http://www.codepolitan.com/upcoming-event",
    "http://www.codepolitan.com/course",
    "http://www.codepolitan.com/statistics"
]

for url in urls:
    t = threading.Thread(target=get_content_len, args=(url,))
    t.start()
    print ("Mengambil panjang halaman web sudah selesai...")