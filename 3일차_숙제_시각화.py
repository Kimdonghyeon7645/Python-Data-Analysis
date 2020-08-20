#!/usr/bin/env python
# coding: utf-8

# ## [문제1] 성별 인구수를 나타내는 그래프를 작성하시오
# <pre>
# 1. 그래프는 plot(선)으로 하시오
# 2. gender.csv를 이용하시오
# 3. 제목과 범례 추가
#    제목: 천전동 성별 인구수
#    x축 제목: 나이
#    y축 제목: 인구수
#    범례: 남자, 여자    (남자는 파랑, 여자는 빨강)
# 4. 지역은 본인이 사는 지역 (ex. 천전동)으로 하시오   
# </pre>
# -------------------------

# ![answer1](https://user-images.githubusercontent.com/48408417/90712901-02284780-e2df-11ea-9329-feaae2c7e098.png)

# In[1]:


import csv
import matplotlib.pyplot as plt


# In[2]:


f = open('gender.csv')
data = csv.reader(f)

m = []
f = []

name = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요 : ')
for row in data :
    if name in row[0]:
        m = list(map(int, row[3:104]))
        f = list(map(int, row[106:]))
        
plt.rc('font', family='Malgun Gothic')
plt.style.use('ggplot')
plt.figure(figsize = (8,3), dpi=300)

plt.plot(range(101), m, label='남자')
plt.plot(range(101), f, label='여자')
plt.title(name + ' 성별 인구수', size=12)
plt.xlabel('나이',fontsize=10)
plt.ylabel('인구수',fontsize=10)
plt.legend(fontsize='small')


# ## [문제2] 2019년 2월 현재 지역별 인구수구하기
# 
# <pre>
# 인구수가 알고 싶은 지역을 입력하시오: 천전동
# 
# 1 ~  20세 인구수: 남자: 2965 여자: 2557
# 21 ~ 60세 인구수: 남자: 8807 여자: 8420
# 61세 이상 인구수: 남자: 3090 여자: 4165</pre>

# In[3]:


f = open('gender.csv')
data = csv.reader(f)

name = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요 : ')

for row in data :
    if name in row[0]:
        for s, l in [(0, 20), (21, 60), (61, 100)]:
            print(f'{s} ~ {l}세 인구수: 남자: {sum(map(int, row[3+s : 4+l]))} 여자: {sum(map(int, row[106+s : 107+l]))}')

