try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

def get_content_len(url):
    print(url)
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
    get_content_len(url)