"""
[문제10] for문을 이용해서 다음과 같이 출력하시오
 0 + 1 + 2 + 3 + 4 + 5 = 15
"""
print(' + '.join(map(str, range(0, 6))), '=', sum(range(0, 6)))     # 걍 이 한줄로 끝내요

sum = 0
for i in range(0, 6):
    sum += i
    print(i, end=' ')
    if i != 5:
        print('+', end=' ')
print('=', sum)
