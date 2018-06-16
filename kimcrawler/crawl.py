from urllib.request import urlopen, Request
import requests
from bs4 import BeautifulSoup
url = "http://kimcartoon.me/"

headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36',
        'host' : url
    };


page = ""

request = Request(url,
                    headers=headers,
                    data=None);
web_page = requests.get('http://104.25.205.29', headers).content
web_page = urlopen(request).read()
#soup = BeautifulSoup(web_page)
print(web_page)
    
