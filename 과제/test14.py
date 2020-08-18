'''
[문제] viewScore함수의 매개변수에 값을 전달해서 viewScore함수가 출력하는 프로그램을 구현하시오
1. 입력자료
name="홍길동"
kor=90
eng=80
mat=75

2. 함수호출
viewScore(name,kor,eng,mat)

[출력화면]
홍길동의 총점은 245점이고 평균은 81.66점 입니다
'''


def viewScore(name, kor, eng, mat):
    print(f"{name}의 총점은 {sum((kor, eng, mat))}점이고 평균은 {sum((kor, eng, mat)) / 3 : .4}점 입니다")


name = "홍길동"
kor = 90
eng = 80
mat = 75
viewScore(name, kor, eng, mat)
