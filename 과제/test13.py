'''
[문제] show함수를 호출하고 show함수에서 "Hello Python"을 10번 출력하시오(call by name)
      조건)while문이용해서 "Hello Python" 반복출력
'''


def show():
    i = 0
    while i < 10:
        print("Hello Python")
        i += 1


show()
