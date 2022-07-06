import requests
from tq import *
 
#downloads file
def download(filename, url):
   r = requests.get(url, allow_redirects=True)
 
   if filename.find(".") != -1:
       open(filename, 'wb').write(r.content)
       return filename
 
   else:
       index = url.rfind(".")
 
       i = index
       substring = []
       while i<len(url):
           substring.append(url[i])
           i+=1
 
       substring = "".join(substring)
 
       newFilename = filename+substring
       open(newFilename, 'wb').write(r.content)
       return newFilename
     
#runs download and collects inputs
def mainDownload(theFakeActualURL):
   userFilename = "tweetFile"
    
   #the url is retrieved from twenty questions as "theURL"
   theFile = download(userFilename,theFakeActualURL)
   return theFile
