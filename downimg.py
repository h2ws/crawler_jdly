#-*- coding:utf-8 -*-
import re
import os
#from urllib.request import urlopen,urlretrieve
import urllib.request as r
import io
import gzip

def Dimg(url):
    req = r.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36", "Accept-Encoding": "gzip"})
    bs = r.urlopen(req).read()
    print(type(bs))
    bi = io.BytesIO(bs)
    gf = gzip.GzipFile(fileobj = bi,mode = 'rb')
    html = gf.read().decode("utf-8")
    #print(html)
    imgbody = re.compile(r'<div class="main-body">(.*?)</div>')
    body = imgbody.findall(html)[0]
    pa = re.compile(r'href="(.*?)"')
    
    #print(type(body),body)
    imglist = pa.findall(body)


    pa = re.compile(r'<title>(.*?)&')
    title = pa.findall(html)[0]
    print(title,"以创建")
    os.mkdir(title)
    i = 1
    for imgurl in imglist:
        r.urlretrieve(imgurl,title+'\\'+str(i)+".jpg")
        print("XD")
        i += 1
        
    
if __name__ == "__main__":
    url = input("网站")
    print("123")
    Dimg(url)
    print('33')
    
