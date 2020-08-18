'''
[문제] 1~10까지의 정수를 항목으로 갖는 리스트 객체에서
짝수만을 선택해 리스트를 반환하는 프로그램을 작성하십시오.
    조건) append,sort 를 이용하시오
    

[출력화면]
[2, 4, 6, 8, 10]
'''
lit = [2, 5, 7, 3, 9, 10, 1, 4, 6, 8]
answer = []
for i in lit:
    if not i % 2:
         answer.append(i)
answer.sort()
print(answer)
