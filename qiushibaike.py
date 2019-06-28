#encoding='utf-8'
import requests
from bs4 import BeautifulSoup
r=requests.get('https://www.qiushibaike.com/text/1')
#print r.text
response=BeautifulSoup(r.text,'html.parser')
con=response.find(id='content-left')
con_list=con.find_all('div',class_='article')

for i in con_list:
    author=i.find('h2').string
    content=i.find('div',class_='content').find('span').get_text()
    stats=i.find('div',class_='stats')
    vote=stats.find('span',class_='stats-vote').find('i',class_='number').string
    author_info=i.find('div',class_='articleGender')
    comment=stats.find('span',class_='stats-comments').find('i',class_='number').string
    if author_info:
        class_list=author_info['class']
        if 'womenIcon' in class_list:
            gender='nv'
        elif 'manIcon' in class_list:
            gender='nan'
        else:
            gender=''
        age=author_info.string
    else:
        gender=''
    print author,gender,age,vote,content,comment
if __name__ == '__main__':
    pass
#main()
