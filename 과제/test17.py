'''
[문제] 계산기 프로그램을 완성하시오
1. 구현함수 (파일명: calc.py)
    sum(a,b)
	sub(a,b)
	multi(a,b)
	div(a,b)

2. 실행파일(파일명: test16.py)

[출력화면]
5 + 4 = 9
5 - 4 = 1
5 * 4 = 20
5 / 4 = 1.25
'''
import calc

a, b = 5, 4
print(calc.sum(a, b))
print(calc.sub(a, b))
print(calc.multi(a, b))
print(calc.div(a, b))
