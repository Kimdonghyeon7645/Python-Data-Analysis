'''
[문제]성적처리프로그램
     중간고사,기말고사,레포트,출석점수를 입력받아서 계산하시오

조건1) (중간+기말)/2   ---> 60%
       과제           ---> 20%
       출석           ---> 20%

조건2)  90이상 'A'학점         (3)A,B학점  ---->"excellent"
       80이상 'B'학점            C,D학점  ---->"good"
       70이상 'C'학점            F학점    ---->"poor"
       60이상 'D'학점            (if~else if문이용)
       나머지 'F'학점
       (if문이용)


[입.출력화면]
중간고사를 입력하시오: 90
기말고사를 입력하시오: 89
과제점수를 입력하시오: 99
출석점수를 입력하시오: 100

성적=93.50      <---소수이하 2째자리까지
학점=A
평가=excellent
'''

mid = int(input("중간고사를 입력하시오: "))       # 중간고사
fin = int(input("기말고사를 입력하시오: "))       # 기말고사
rep = int(input("과제점수를 입력하시오: "))       # 레포트
att = int(input("출석점수를 입력하시오: "))       # 출석
avg = (mid + fin) / 2 * (60/100) + rep * (20/100) + att * (20/100)                  # 성적
print(-1 if avg//10 < 6 else 10-avg//10)
grade = ['A', 'A', 'B', 'C', 'D', 'E'][-1 if avg//10 < 6 else 10-int(avg//10)]      # 학점
result = 'excellent' if grade in 'AB' else ('good' if grade in 'CD' else 'foor')    # 평가
print(f'성적={avg:.4}\n학점={grade}\n평가={result}')
