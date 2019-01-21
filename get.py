import requests
import urllib
from bs4 import BeautifulSoup


#doc = open(r'C:\Users\17635\Desktop\sourcefile.txt','r',encoding='utf-8')

url = 'https://www.zhihu.com/question/309090523/answer/576629595'

page = urllib.request.urlopen(url)

html = page.read()

html = html.decode('utf-8')

doc = BeautifulSoup(html,'lxml')

path =r'C:\Users\17635\Desktop\zhihu\zhihuPicture2' 

count = 0

for tag in doc.find_all('img'):
    if str(tag['src']).split('.')[-1] == 'jpg'or str(tag['src']).split('.')[-1] == 'gif':
        count += 1
        path2 = path+'\\'+str(count)+'.'+str(tag['src']).split('.')[-1]
        
        with open(path2,'wb') as f:
            f.write(requests.get(str(tag['src'])).content)
            print('{}'.format(count)+"save successfully!")