import numpy as np

""" 1. 
1차원 numpy 배열을 만들어 결과와 같이 출력하시오
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
"""
print(np.arange(0, 29, 2))


""" 2. 
2차원 numpy 배열을 만들어 결과와 같이 출력하기
[[10, 20, 30, 40],
50, 60, 70, 80]]
"""
print(np.arange(10, 90, 10).reshape(2, 4))


""" 3. 
3차원 numpy 배열을 만들어 결과와 같이 출력하기
[[ 1, 2, 3],
[ 4, 5, 6]],

[[ 7, 8, 9],
[10, 11, 12]],

[[13, 14, 15],
[16, 17, 18]],

[[19, 20, 21],
[22, 23, 24]]]
"""
print(np.arange(1, 25).reshape(4, 2, 3))


""" 4. 
아래와 같은 행렬을 이용하여 조건에 맞는 코드 작성
  1) vector = np.array(range(0, 30, 2))
  2) 값 24 출력
  3) 값 6 출력
"""
vector = np.array(range(0, 30, 2))
print(vector[12])   # 24 // 2
print(vector[3])    # 6 // 2


""" 5. 
아래와 같은 행렬을 이용하여 조건에 맞는 코드 작성
matrix = np.array([ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16] ])
1) 값 8 출력
2) 값 2 출력
3) 값 9 출력 
4) 값 15 출력
[출력 화면]
8
2
9
15
"""
matrix = np.array([ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16] ])
print(matrix[1][-1])
print(matrix[0][1])
print(matrix[2][0])
print(matrix[3][2])


""" 6. 
아래와 같은 행렬을 이용하여 조건에 맞는 코드 작성
     1) vector = np.array(range(-1, -6, -1))
        idx = [False, True, False, True, False]
     2) vector과 idx를 비교해서 True인것만 출력

[출력화면]
[-2,-4]
"""
vector = np.array(range(-1, -6, -1))
idx = [False, True, False, True, False]

print(*[n for i, n in enumerate(vector) if idx[i]])     # 방법1
print(*[a for a, b in zip(vector, idx) if b])           # 방법2
print(vector[idx])      # 방법3


""" 7. 
[[1, 2, 3], [4, 5, 6]]를 만들고 각행에 각각 10,20 입력하시오

[[1,2,3]               [[1,2,3,10]
[4,5,6]]      ==>      [4,5,6,20]]
"""
vector = np.array([[1, 2, 3], [4, 5, 6]])
print(vector)
plus_array = np.array([*[[i*10] for i in range(1, len(vector)+1)]])     # [[10] [20]]
# plus_array = np.array([[[10], [20]])      # 이와 같음

print(np.append(vector, plus_array, axis=1))    # 방법1(append 사용)
print(np.concatenate((vector, np.array([[10], [20]])), axis=1))     # 방법2-1(concatenate 사용)
print(np.concatenate((vector, np.array([[10, 20]]).T), axis=1))     # 방법2-2(concatenate 와 .T 사용)


""" 8. 
1 ~ 30 의 실수로 이루어진 5 x 6 형태의 데이터 행렬을 만든후 다음 조건에 맞는 데이터를 찾으시오
       1) 1 ~ 30 의 실수로 이루어진 5 x 6 형태의 데이터 행렬
       2) 가장 큰수 출력
       3) 행별 합계(sum)
       4) 열별 평균(mean)

[출력화면]
[[ 1  2  3  4  5  6]
 [ 7  8  9 10 11 12]
 [13 14 15 16 17 18]
 [19 20 21 22 23 24]
 [25 26 27 28 29 30]]
30
[ 21  57  93 129 165]
[13. 14. 15. 16. 17. 18.]
"""
hang = np.arange(1, 31).reshape(5, 6)
print(hang)
print(hang.max())
print(np.array([hang[i, :].sum() for i in range(len(hang))]))   # [n,:] n행의 모든 원소 슬라이싱
print(np.array([hang[:, i].mean() for i in range(len(hang))]))  # [:,n] n열의 모든 원소 슬라이싱

