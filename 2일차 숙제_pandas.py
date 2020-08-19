import pandas as pd
import numpy as np

""" 1.
랜덤으로 5개의정수를 만들어 시리즈로 생성하기
[출력화면]
0    8
1    7
2    3
3    1
4    6
dtype: int64
"""
print(pd.Series(np.random.randint(1, 10, 5)))


""" 2. 
랜덤으로 5개의 실수를 만들어 시리즈로 생성하기
랜덤으로 실수 값으로 1부터 9까지 랜덤으로 5개 뽑기
[출력화면]
0    2.0
1    5.0
2    3.0
3    2.0
4    1.0
dtype: float64
"""
print(pd.Series(np.random.randint(1, 9, size=5).astype('float64')))


""" 3.
혈액형 통계 수치를 이용하여 인덱스를 가지는 시리즈 생성하기
blood = ['A형', 'B형', 'O형', 'AB형']
st = [34.2, 27.1, 26.7, 11.5]

[출력화면]
A형     34.2
B형     27.1
O형     26.7
AB형    11.5
dtype: float64
"""
blood = ['A형', 'B형', 'O형', 'AB형']
st = [34.2, 27.1, 26.7, 11.5]
print(pd.Series(st, index=blood))


""" 4. 
1 ~ 25숫자를 가지는 DataFrame 만들기

[출력화면]
    a   b   c   d   e
1   1   2   3   4   5
2   6   7   8   9  10
3  11  12  13  14  15
4  16  17  18  19  20
5  21  22  23  24  25
"""
print(pd.DataFrame(np.arange(1, 26).reshape(5, 5), columns=['a', 'b', 'c', 'd', 'e']))


""" 5. 
아래와 같은 형태의 DataFrame 만들기
[{'번호':101, '이름':'kim',  '점수':100}
{'번호':102, '이름':'lee',  '점수':90}
{'번호':103, '이름':'park', '점수':80}
{'번호':104, '이름':'hong', '점수':70}]
(1)자료를 데이터프레임으로 만들어서 출력하시오
(2)user.xls로 저장하시오


[출력화면]
  번호  이름  점수
0 101  kim   100
1 102  lee   90
2 103  park  80
3 104  hong  70
"""
data = [{'번호': 101, '이름': 'kim',  '점수': 100},
        {'번호': 102, '이름': 'lee',  '점수': 90},
        {'번호': 103, '이름': 'park', '점수': 80},
        {'번호': 104, '이름': 'hong', '점수': 70}]
df = pd.DataFrame(data)
print(df)
df.to_excel('user.xls', sheet_name='Sheet1.xls', encoding='utf-8')
