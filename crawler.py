import requests
from bs4 import BeautifulSoup
from bs4.element import Comment
from collections import deque
import os
import urllib.request
import pickle
import re

def crawler():
    queue = deque()
    url_list=[]
    crawlNum = 3500
    initialUrl="https://www.cs.uic.edu/"
    domain = "uic.edu"
    queue.append(initialUrl)
    url_list.append(domain)
    excludeExtension = [
    ".pdf",
    ".doc",
    ".docx",
    ".ppt",
    ".pptx",
    ".xls",
    ".xlsx",
    ".css",
    ".js",
    ".aspx",
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".svg",
    ".ico",
    ".mp4",
    ".avi",
    ".tar",
    ".gz",
    ".tgz",
    ".zip",
]
    pageNo=0
    pagesCrawled={}

    while(queue):
        try:
            link=queue.popleft()
            r=requests.get(link)                #Gets html content
            if(r.status_code == 200):
                filtered_text = []
                soup = BeautifulSoup(r.text,'lxml')
                textData = soup.find_all(text=True)
                for text in textData:
                    if text.parent.name not in ['style', 'script', 'head', 'meta', '[document]'] and isinstance(text, Comment)== False and re.match(r"[\s\r\n]+",str(text))==None:
                        filtered_text.append(text)
                textOutput = " ".join(term.strip() for term in filtered_text)
                pagesCrawled[pageNo]=link
                filename = "./CrawledData/"+str(pageNo)
                os.makedirs(os.path.dirname(filename), exist_ok=True)
                with open(filename, "w",encoding="utf-8") as f:
                    f.write("<DOCNO>"+str(pageNo)+"</DOCNO>\n<URL>"+link+"</URL>\n<TEXT>"+textOutput+"</TEXT>")
                       
                
                tags = soup.find_all('a')
                    
                for tag in tags:
                    l=tag.get('href')
                    if l is not None and l.startswith("http") and l not in url_list and domain in l and \
                    not any(ext in l for ext in excludeExtension):
                        l = l.lower()
                        # removing intra page anchor tags from URL
                        l = l.split("#")[0]
                        # removing query parameters from URL
                        l = l.split("?", maxsplit=1)[0]
                        # removing trailing / from URL
                        l = l.rstrip("/")
                        l = l.strip()
                        if l not in pagesCrawled and domain in l:
                            url_list.append(l)
                            queue.append(l)
                            
                if(len(pagesCrawled) > crawlNum):
                    break

                    
                pageNo += 1

        except Exception as e:
            print(e)
            print("Connection failed for", link)
            continue
        
    pickle_folder = "./PickleFiles/"
    os.makedirs(pickle_folder, exist_ok=True)
    with open(pickle_folder +'url.pickle', 'wb') as f:
        pickle.dump(pagesCrawled, f)
        
                
crawler()