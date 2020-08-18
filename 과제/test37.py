'''
[문제] 리스트 내포 기능을 이용해 다음 문장으로부터 모음('aeiou')을 제거하십시오.
'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
       조건) 문자를 연결 할때 join()을 이용하시오

[출력 화면]
Pythn s pwrfl... nd fst; plys wll wth thrs; rns vrywhr; s frndly & sy t lrn; s Opn.
'''

data_str = \
    'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
serch = 'aeiou'
print(''.join([i for i in data_str if i not in serch]))
