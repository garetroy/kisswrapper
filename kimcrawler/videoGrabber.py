import re
import requests
import json
import time
import urllib
from kimconnectionwrapper import KimConnection
from bs4 import BeautifulSoup


class VideoGrabber:
    
    def __init__(self, url, path, name):
        self.connection = KimConnection(url)
        self.soup = self.connection.getBeautifulSoup()
        self.path = path
        self.name = name

    def grabVideoUrl(self):
        iframes = self.soup.find_all('iframe')
        videoiframe = [x for x in iframes if str(x).find('openload') != -1]
        return KimConnection(videoiframe[0]['src']


    def download_file(self):
        url = self.grabVideoUrl()
        local_filename = url.split('/')[-1]
        r = requests.get(url, stream=True)
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024): 
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
        return local_filename 

if __name__ == '__main__':
    vg = VideoGrabber('http://kimcartoon.me/Cartoon/South-Park-Season-07.t85/Episode-009?id=1572&s=openload','/Users/garett/Desktop/','Episode15')
    print(vg.grabVideoUrl()) 
    vg.download_file()
