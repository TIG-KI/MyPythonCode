
from bs4 import BeautifulSoup
import requests

doc = open(r'C:\Users\17635\Desktop\sourcefile.txt','r',encoding='utf-8')
soup = BeautifulSoup(doc)

path =r'C:\Users\17635\Desktop\zhihu'

count = 0
for i in soup.find_all('img'):
    if str(i['src']).split('.')[-1] == 'jpg':
        count += 1
        path2 = path+'\\'+str(count)+'.jpg'
        
        with open(path2,'wb') as f:
            f.write(requests.get(str(i['src'])).content)
            print('success!')
       
print(count)