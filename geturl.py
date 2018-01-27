#-*- coding:utf-8 -*-
import re
import urllib.request as r
from downimg import Dimg

def start(url):
    '''初始大页面的url'''
    print(url)
    rdx = r.urlopen(url)
    html = rdx.read()
    html = html.decode("utf-8")
    #获取当期页面

    pa = re.compile(r"title='最后页'.*href='(.*)' title='下一页'")
    exiturl = pa.findall(html)[0]
    #下一个页面的url

    pazi = re.compile(r'<a href="(.{10,50})" class="(viewsButton|/d*?)" title="阅读"')
    pageurl = pazi.findall(html)
    print(pageurl,'-'*30)
    #图片页面 列表

    for purl in pageurl:
        Dimg(purl[0])

    return exiturl
def main(url):
    '''主方法'''
    while True:
        n = start(url)
        url = n

if __name__ == "__main__":
    url = input("输入网站")
    main(url) 
    
    
