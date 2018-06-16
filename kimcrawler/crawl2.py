import pycookiecheat
import cfscrape
import re
import json
import time
from bs4 import BeautifulSoup

base_url = "http://kimcartoon.me"
url = base_url + "/CartoonList"
current_page = 1
json_path = "./kimcartoonlist"

def main():
    global url, current_page
    soup = soupify(url)
    ul = soup.find("ul", {"class": "pager"})
    link = ul.find("a", text= re.compile("Last"))
    pages = int(link['page'])
    while (current_page != pages):
        try:
            print("Getting page" + str(current_page))
            getCartoons(current_page, pages+1)
        except:
            print("Stopped at " + str(current_page))
            print("Sleeping for three minutes and trying again")
            time.sleep(180) 

def getCartoons(start,end):
    global current_page
    for i in range(start,end):
        current_page = i
        appendToJson(getCartoonList(i))
        time.sleep(20)
         
def appendToJson(json_data):
    global json_path
    with open(json_path, "a") as data:
        data.write(json.dumps(json_data))
        data.close()

def getCartoonList(cartoon_list_page):
    global url;
    new_url = url + "?page=" + str(cartoon_list_page)
    soup = soupify(new_url)
    return getCartoonNameUrls(soup)

def getCartoonNameUrls(soup):
    global base_url
    data = {}
    cartoon_list = soup.find("div", {"class": "list-cartoon"})
    cartoons = cartoon_list.findAll("div")
    for cartoon in cartoons:
        link = base_url + cartoon.find("a")['href']
        title = BeautifulSoup(cartoon['title'], "html.parser")
        title = title.find("p").text
        data[title] = link

    return data
        
def soupify(url):
    return BeautifulSoup(scrapeURL(url), "lxml") 

def scrapeURL(url):
    cookies = pycookiecheat.chrome_cookies(url)
    return cfscrape.create_scraper().get(url, cookies = cookies).content


if __name__ == "__main__":
        main();
