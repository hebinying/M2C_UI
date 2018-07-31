import requests
import urllib
import urllib2

def GetWebPage(url):
    req=urllib2.Request(url)
    pageContent=urllib2.urlopen(req).read()
    print pageContent



if __name__=='__main__':
    url = "http://b.m2c2017test.com"
    GetWebPage(url)





'''usr_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
rq=urllib.request.Request(url)
rq.add_header("User-Agent",usr_agent)

content=urllib.request.urlopen(rq)

print content

res=requests.get(url)
res.encoding='utf-8'
print(res.text)'''

