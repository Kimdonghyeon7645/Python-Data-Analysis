"""
[문제8]다음과 같이 출력하시오
반지름을 입력하시오 : 5

원의 넓이 : 78.5	(반*반*3.14)
원의 둘레 : 31.4(2*반*3.14)
"""
radius = float(input("반지름을 입력하시오 : "))

print("원의 넓이 : %.1f" % (radius ** 2 * 3.14))
print("원의 둘레 : %.1f" % (2 * radius * 3.14))
