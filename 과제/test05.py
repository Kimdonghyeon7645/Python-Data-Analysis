#-*- coding: utf-8 -*-
"""
[문제5] 각각의 값을 변수에 대입해서 %s, %c, %d, %f로 출력하시오
eno:101
ename:홍길동
dept:A
score:85.9 를 대입후 출력

[출력화면]
사원번호 : 101
사원이름 : 홍길동
부서코드 : A
입사성적 : 85.9점
"""
eno = 101
ename = '홍길동'
dept = 'A'
score = 85.9
print(f"사원번호: {eno}\n사원이름: {ename}\n부서코드: {dept}\n입사성적: {score}점")
