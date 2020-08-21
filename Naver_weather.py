#!/usr/bin/env python
# coding: utf-8

# ## 네이버 날씨로 동네 날씨 크롤링

# In[1]:


import requests
from bs4 import BeautifulSoup


# In[ ]:


dong = input('동네를 입력하세요: ')
url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=' + dong + '+날씨'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')
box = soup.select_one('div._mainArea')

print("현재 위치:", box.select_one('div._areaSelectLayer').em.text)
print('현재', dong, '기온은', str(box.select_one('span.todaytemp').text)+'도 입니다.')

dust_list = zip(box.select('div.sub_info dl dt a'), box.select('div.sub_info dl dd span.num'))
for dust in dust_list:
    print(f'현재 {dust[0].text}: {dust[1].text}')
print(box.select_one('p.cast_txt').text)

