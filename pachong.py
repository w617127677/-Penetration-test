import requests
from lxml import etree
headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }
h1 = input('输入域名:')
pages = input('输入页数:')
subdomain = []
for i in range(1,int(pages)+1):
    url="https://cn.bing.com/search?q={}&go=Search&qs=ds&first={}&FORM=PERE".format(h1,str((int(pages)-1)*10))
    response = requests.get(url,headers=headers)

    # print(response.text)
    content = response.content
    html = etree.HTML(content)

    a = html.xpath('//ol[@id="b_results"]/li')
    for i in a:
        domain = i.xpath('./h2/a/@href')
        if domain:
            subdomain.append(domain)
        else:
            pass
for i in subdomain:
    print(i)


