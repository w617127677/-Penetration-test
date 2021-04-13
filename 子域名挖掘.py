import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import sys
from lxml import etree

def bing_serch(site,pages):
    subdomain = []
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }
    for i in range(1,int(pages)+1):
        url="https://cn.bing.com/search?q=site%3a"+site+"&go=Search&qs=ds&first="+str((int(i)-1)*10) + "&FORM=PERE"
        conn =requests.session()
        conn.get('https://cn.bing.com',headers=headers)
        html = conn.get(url,stream=True,headers=headers,timeout=8)
        # print(html.content.decode().encode())
        with open ('gg.html','w',encoding='utf-8') as f:
            f.write(html.text)
        content = html.content
        html = etree.HTML(content)

        a = html.xpath('//ol[@id="b_results"]/li')
        for i in a:
            domain = i.xpath('./h2/a/@href')
            subdomain.append(domain)
            print(domain)

        print(subdomain)
        # soup = BeautifulSoup(html.content,'html.parser')
        # job_bt = soup.findAll('h2')
        # for i in job_bt:
        #     link =i.a.get('href')
        #     domain = str(urlparse(link).scheme+"://"+urlparse(link).netloc)
        #     if domain in subdomain:
        #         pass
        #     else:
        #         subdomain.append(domain)
        #         print(domain)
if __name__ == '__main__':
    subdomain = bing_serch(site, page)
    if len(sys.argv)==3:
        site = sys.argv[1]
        page = sys.argv[2]
    else:
        print('gg'+sys.argv[0])
        sys.exit(-1)
    # site = 'baidu.com'
    # page = 5


