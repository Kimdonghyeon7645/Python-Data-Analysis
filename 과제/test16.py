'''
[문제] 값을 입력받고 함수를 호출해서 프로그램을 구현하시오.
1.계산방법
   금액 = 수량 * 단가

2.처리조건
    ①__main__ 에서 품명과 수량, 단가를 입력 받으시오
    ②compute() 함수로 값을 전달하여 계산과 출력하시오
    ③함수 구현 :   compute(item, qty, price)

3. 입.출력화면
품명을 입력하시오 : apple
수량을 입력하시오 : 10
단가를 입력하시오 : 1200

품명 : apple                            <---compute()에서 처리
금액 : 12000원
'''


def compute(item, qty, price):
    print(f"품명: {item}")
    print(f"금액 : {qty * price}원")


i = input("품명을 입력하시오 : ")
q = int(input("수량을 입력하시오 : "))
p = int(input("단가를 입력하시오 : "))
compute(item=i, qty=q, price=p)
