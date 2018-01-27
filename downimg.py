#-*- coding:utf-8 -*-

import re
import os
import urllib.request as r
import io
import os

def Dimg(url):
    '''下载单个页面的所有图片'''
    print(url)
    rdx = r.urlopen(url)
    html = rdx.read()
    html = html.decode("utf-8")
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
        r.urlretrieve(imgurl,os.path.join(title,str(i)+".jpg"))
        print("XD")
        i += 1
        
    
if __name__ == "__main__":
    url = input("网站")
    print("123")
    Dimg(url)
    print('33')
    
