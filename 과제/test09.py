#-*- coding: utf-8 -*-
"""
[문제9]2개의 숫자와 연산자를 입력하여 계산
하시오 (if문이용)
    조건1) 실수인경우는 소수이하 2째자리까지 출력하시오
    조건2) 연산자가 +,-,*,/ 이외의 문자가 들어오면 "연산자 에러"출력하시오

[실행결과]
A값을 입력하시오: 25
B값을 입력하시오: 36
연산자를 입력(+,-,*,/) : +
25 + 36 = 71

A값을 입력하시오: 25
B값을 입력하시오: 36
연산자를 입력(+,-,*,/) : /
25 / 36 = 0.69

A값을 입력하시오: 25
B값을 입력하시오: 36
연산자를 입력(+,-,*,/) : #
연산자 에러
"""
#----------------------------------------------------
A = int(input("A값을 입력하시오: "))
B = int(input("B값을 입력하시오: "))
op = input("연산자를 입력(+,-,*,/) :")

if op == '+':
    result = A+B
    print("%d %c %d = %d" % (A, op, B, result))
elif op == '-':
    result = A - B
    print("%d %c %d = %d" % (A, op, B, result))
elif op == '*':
    result = A * B
    print("%d %c %d = %d" % (A, op, B, result))
elif op == '/':
    result = A / B
    if(A/B-int(A/B)>0):
        print("%d %c %d = %.2f" % (A, op, B, result))
    else:
        print("%d %c %d = %d" % (A, op, B, result))
else:
    print("연산자 에러")