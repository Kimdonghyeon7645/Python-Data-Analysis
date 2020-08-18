'''
[문제] 1~10까지의 정수를 항목으로 갖는 리스트 객체에서
filter와 람다 함수를 이용해서 짝수만 선택해 리스트를 반환 하는 프로그램을 작성하시오
    조건) append,sort 를 이용하시오
    

[출력화면]
[2, 4, 6, 8, 10]
'''

instance = [i for i in range(10, 1, -1)]
print(list(sorted(filter(lambda x: not x % 2, instance))))
