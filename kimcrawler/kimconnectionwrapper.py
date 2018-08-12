import pycookiecheat
import cfscrape
import urllib.request as req
import json
from bs4 import BeautifulSoup

class KimConnection:
    
    def __init__(self, url):
        self.url = url
        self.cookies = pycookiecheat.chrome_cookies(url)
        self.scraper = cfscrape.create_scraper()
        self.content = None;
    
    def getContent(self):
        if(self.content == None):
            self.content = self.scraper.get(self.url, cookies = self.cookies).content

        return self.content

    def getBeautifulSoup(self):
        return BeautifulSoup(self.getContent(), "lxml")

class OpenLoadWrapper(KimConnection): 

    def __init__(self,url):
        super(OpenLoadWrapper, self).__init__(url)
        self.ticketurl = "https://api.openload.co/1/file/dlticket?file={0}"
        self.downlaodurl = "https://api.openload.co/1/file/dl?file={0}&ticket={1}&captcha_response={2}"
        self.file = url.split("embed/")[1]
        self.ticket = None
        self.response = None

    def getTicket(self):
        with req.urlopen(self.ticketurl.format(self.file)) as url:
            self.ticket = json.loads(url.read().decode())

        return self.ticket
 
olw = OpenLoadWrapper('https://openload.co/embed/Tu1yTJrHuuk/1575-15751442662083_1495692783.mp4')
print(olw.getTicket())
