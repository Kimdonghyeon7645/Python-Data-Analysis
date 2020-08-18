"""
[문제] 리스트에 데이터를 추가/삭제/끼워넣기/꺼내기 하시오

[출력화면]
[10, 20, 30]
[10, 20, 30, 70, 80]
[10, 20, 30, 40, 50, 60, 70, 80]
[80, 70, 60, 50, 30, 20, 10]
[80, 70, 60, 50, 30]
[]
"""

lit = [10, 20, 30]
print(lit)
lit += [70, 80]
print(lit)
lit = lit[:3] + [40, 50, 60] + lit[3:]
print(lit)
lit.remove(40)
lit = list(sorted(lit, reverse=True))
print(lit)
lit = lit[:-2]
print(lit)

