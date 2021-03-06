'''
[문제]구구단을 파일로 저장하고 불러오는 코드를 만드시오(파일 입출력)
1. 구구단을 파일에 저장하시오(gugudan.txt)
2. 저장된 구구단을 라인 단위(readline())로 읽어서 출력하시오
3. 구구단에 저장된 데이터중 결괏값만 리스트에 담아 출력하시오

[출력 화면]
2 *  1 =  2
2 *  2 =  4
2 *  3 =  6
2 *  4 =  8
2 *  5 = 10
2 *  6 = 12
2 *  7 = 14
2 *  8 = 16
2 *  9 = 18

[2,4,6,8,10,12,14,16,18]
'''

with open('gugudan.txt', 'w') as f:
    f.writelines([f'{i} * {j} = {i*j:>2}\n' for i in range(2, 10) for j in range(1, 10)])
with open('gugudan.txt', 'r') as f:
    answer = []
    for sig in f.readlines():
        print(sig.lstrip(), end='')
        answer.append(sig.split()[-1])
    print(answer)
