'''
[문제] 다음의 출력화면과 같이 입력된 문자열의 문자 빈도수를 구하는 프로그램을 작성하십시오.
      조건1) for와 if를 이용해서 완성하시오
      조건2) dictionary에 담아 출력하시오
      조건3) dictionary의 데이터를 하나씩 추출해서 출력하시오
      조건4) formatter를 이용해서 출력하시오

[출력화면]
문자열을 입력하시오: agama
{'a': 3, 'g': 1, 'm': 1}

a==>3
g==>1
m==>1
'''

t_str = input("문자열을 입력하시오: ")
dictionary = dict()
for i in t_str:
    if i in dictionary.keys():
        dictionary[i] += 1
    else:
        dictionary.update({i: 1})
print(dictionary)
print(*[f'\n{k}==>{v}' for k, v in dictionary.items()])
