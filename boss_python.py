# -*- coding: utf-8 -*-
#author cfx
#2019-05-10
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import time,re
import pandas as pd
url='https://www.zhipin.com/c101280600/e_104-d_203-y_3-h_101280600/'
"""
构造请求头
"""
headers={
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer':'https://login.zhipin.com/',
    'Cookie':'astCity=101280600; __a=72686344.1560832848..1560832848.116.1.116.20; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1560832848,1561442469,1561536522; _uab_collina=156083284788174294934936; __c=1560832848; __g=sem_pz_bdpc_dasou_title; __l=l=%2Fwww.zhipin.com%2F&r=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DE-SCWS2xSDB0gaR9avTyqKV_S1gVQvp-NG2GRonyQ2KOZrsbd-3k9n-nQRMDZOBZ%26wd%3D%26eqid%3Dd3b677c70000ce7b000000065d086bb0&g=%2Fwww.zhipin.com%2F%3Fsid%3Dsem_pz_bdpc_dasou_title; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1561555175; t=bGagBuweWhVJgWjs; wt=bGagBuweWhVJgWjs; sid=sem_pz_bdpc_dasou_title',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
}
"""
读取html代码
"""
def get_one_page(url,headers,params):
    try:
        response = requests.get(url,headers=headers,params=params)
        time.sleep(2)
        if response.status_code==200:
            return response.text
        return None
    except Exception:
        return None
"""
利用beautifulsoup查找div节点，找到需要的数据
"""
def get_detail_info(html):
    soup=BeautifulSoup(html,"html.parser")
    #print soup
    mains=soup.find(id='main')
    job_list=mains.find('div',class_='job-list').find('ul')
    #print job_list.select('li')
    joblist=[]
    for li in job_list.select('li'):
        job={}
        #print job_list.find('div',class_='job-primary')
        job['position'] = li.find('div', class_='job-primary').find('div', 'info-primary').find('h3',class_='name').find('a')\
                .find('div',class_='job-title').string.encode('utf-8')
                #.find('div',class_='detail-top-title')
        job['companys']=li.find('div',class_='info-company').find('h3',class_='name').find('a').get_text().encode('utf-8')
        job['salary']=li.find('div',class_='info-primary').find('h3',class_='name').find('span',class_='red').get_text()
        exper=li.find('div',class_='info-primary').find('p')
            #reg = r'<p>深圳 南山区 科技园<em class="vline"></em>1-3年<em class="vline"></em>本科</p>'
        reg=r'<p>(.*?)<em class="vline">'###贪婪匹配
        loca = re.findall(reg, str(exper))
        for i in loca:
            job['location']=''.join(i)
        reg1=r'</em>(.*?)<em class="vline">'
        experi=re.findall(reg1, str(exper))
        for ii in experi:
            job['experience']=''.join(ii)
        joblist.append(job)
    return joblist


def main(url, headers, params):
    html = get_one_page(url, headers=headers, params=params)
    joblist= get_detail_info(html)
    position_data_zhipin = pd.DataFrame(joblist)
    return (position_data_zhipin)
if __name__ == '__main__':
    for page in range(1, 3):
        params = {
            'query': 'python',
            'page': page,
            'ka': 'page-{}'.format(page)
        }
        print main(url,headers,params)

