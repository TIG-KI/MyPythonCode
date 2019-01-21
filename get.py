import requests
import urllib
from bs4 import BeautifulSoup


#doc = open(r'C:\Users\17635\Desktop\sourcefile.txt','r',encoding='utf-8')

url = 'https://www.zhihu.com/question/49441554/answer/540280872' #要爬取的网页

page = urllib.request.urlopen(url)

html = page.read()

html = html.decode('utf-8')

doc = BeautifulSoup(html,'lxml') # 用beautifulsoup 解析request的网站

path =r'C:\Users\17635\Desktop\zhihu\zhihuPicture3'  #图片将要保存的路径

count = 0

for tag in doc.find_all('img'):   #find_all()为beauifulsoup 内置的筛选函数
    if str(tag['src']).split('.')[-1] == 'jpg'or str(tag['src']).split('.')[-1] == 'gif':
        count += 1
        path2 = path+'\\'+str(count)+'.'+str(tag['src']).split('.')[-1]  #文件的路径+名称，此时只是一个定义
        
        with open(path2,'wb') as f:           
            f.write(requests.get(str(tag['src'])).content)     # wb 表示 二进制文件
            print('{}'.format(count)+"save successfully!")

