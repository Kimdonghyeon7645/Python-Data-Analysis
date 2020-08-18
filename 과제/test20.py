"""
[문제] 다음 데이터를 분리해서 결과를 만드시오
txt='10*20*30*40*50'

[출력화면]
10+20+30+40+50=150
"""
txt = '10*20*30*40*50'

if __name__ == '__main__':
    print('+'.join([i for i in txt.split('*')]), '=', sum(map(int, txt.split('*'))), sep='')
