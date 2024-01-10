import numpy as np

# [] : 리스트
# {} : 딕셔너리
# () : 튜플, 튜플은 괄호가 없어도 튜플
data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # 리스트로 데이터 생성
a1 = np.array(data) # 리스트를 넘파이 배열로 변환
print("# a1 : ", a1) # [ 0  1  2  3  4  5  6  7  8  9 10]

data2= [0, 1, 2, 3, 4, 5, 1.56, 3, 14, 0.333]
a2 = np.array(data2)
print("# a2 : ", a2) # [ 0.     1.     2.     3.     4.     5.     1.56   3.    14.     0.333]

x = np.array([0.1, 0.2, 0.3])
print("# x : ", x) # [0.1 0.2 0.3]
print("# x.shape : ", x.shape) # 배열의 형태를 나타냄, (3,) : 1차원 배열이고 3개의 요소를 가지고 있음
print("# x.dtype : ", x.dtype) # 배열 요소의 타입 확인, float64 : 실수형 64 비트 부동소수점

y = np.array(([[1, 2, 3], [4, 5, 6]]))
print("# y : ", y) # [[1 2 3]
            #  [4 5 6]]
print("# y.shape : ", y.shape) # (2, 3) : 2차원 배열이고 2개의 행과 3개의 열을 가지고 있음
print("# y.dtype : ", y.dtype) # int32 : 정수형 32비트

# 범위를 지정해 배열 생성
a3 = np.arange(0, 10, 2) # 0부터 10미만까지 2씩 증가하는 배열 생성
print("# a3 : ", a3) # [0 2 4 6 8]

a4 = np.arange(1, 20) # 1부터 20미만까지 1씩 증가하는 배열 생성(간격을 생략했음, 기본값 1)
print("# a4 : ", a4) # [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]

# 배열 형태 변경, 0 ~ 12 미만 배열 생성
a5 = np.arange(12). reshape(4, 3) # 4행 3열로 배열 형태 변경
print("# a5 : ", a5) # [[ 0  1  2]
            #  [ 3  4  5]
            #  [ 6  7  8]
            #  [ 9 10 11]]
print("# a5.shape : ", a5.shape) # (4, 3) : 2차원 배열이고 4개의 행과 3개의 열을 가지고 있음

# 배열의 시작과 끝 지정, 그리고 데이터의 개수를 지정해 배열 생성
a6 = np.linspace(0, 10, 5) # 0부터 10까지 5개의 데이터를 생성, 시작과 끝, 범위 내에서 균등한 간격으로 데이터를 생성해 배열을 만듦
print("# a6 : ", a6) # [ 0.   2.5  5.   7.5 10. ]
a7 = np.linspace(0, np.pi, 20) # 0부터 파이까지 20개의 데이터를 생성
print("# a7 : ", a7) # [0.         0.16534698 0.33069396 0.49604095 0.66138793 0.82673491
a7_2 = np.linspace(0, 10, 5, endpoint=False) # 0부터 10까지 5개의 데이터를 생성, endpoint=False : 끝값을 포함하지 않음
print("# a7_2 : ", a7_2) # [0. 2. 4. 6. 8.]

# 특별한 형태의 배열 생성
# 1차원 배열
a8 = np.zeros(5) # 0으로 채워진 1차원 5개 배열 생성
print("# a8 : ", a8) # [0. 0. 0. 0. 0.]
a9 = np.zeros((3, 4))
print("# a9 : ", a9) # 0으로 채워진 3행 4열의 2차원 배열 생성
a10 = np.ones(5) # 1로 채워진 1차원 5개 배열 생성
print("# a10 : ", a10) # [1. 1. 1. 1. 1.]
a11 = np.ones((3, 4))
print("# a11 : ", a11) # 1로 채워진 3행 4열의 2차원 배열 생성

# 단위 행렬 생성
a12 = np.eye(4) # 4행 4열의 단위 행렬 생성
print("# a12 : " , a12) # [[1. 0. 0. 0.]
            #  [0. 1. 0. 0.]
            #  [0. 0. 1. 0.]
            #  [0. 0. 0. 1.]]

# 배열의 타입 변환: 배열은 숫자 뿐만 아니라 문자열로 요소로 가질 수 있음 (단, 배열의 요소는 모두 같은 타입이어야 함)
a13 = np.array(['1.5', '0.62', '2', '3.14', '3.141592', '-12', '+12'])
print("# a13 : ", a13) # ['1.5' '0.62' '2' '3.14' '3.141592' '-12' '+12']
print("# a13.dtype : ", a13.dtype) # <U8 : 유니코드 문자열 8자리

num_a13 = a13.astype(float) # a13 배열의 타입을  실수(float)으로 변환
print("# num_a13 : ", num_a13) # [1.5      0.62     2.       3.14     3.141592 -12.      12.     ]

# 난수 배열 생성 : 0 ~ 1 사이의 임의의 실수로 난수 발생
# 난수 : 0 ~ 1 사이의 임의의 값을 가지는 수
a15 = np.random.rand(2, 3) # 2행 3열의 난수 배열 생성
print("# a15 : ", a15)
a16 = np.random.rand(2, 3, 4) # 2면 3행 4열의 난수 배열 생성
print("# a16 : ", a16)

#배열의 연산
arr1 = np.array([1, 2, 3])
print ("# arr1 : ", arr1) # [1 2 3]
arr2 = np.array([[10, 20, 30]])
print ("# arr2 : ", arr2) # [[10 20 30]]
result = arr1 ** arr2
print("# arr1 ** arr2 : ", result) # [[          1     1048576 -1010140999]]

# 요소별 연산 : true, false로 연산
arr3 = np.array([10, 20, 30, 40, 50])
print("# arr3 > 20 : ", arr3 > 20) # [False False  True  True  True]

# 통계를 위한 연산 : 배열의 합, 평균, 표준편차, 분산, 최대값, 최소값, 중앙값, 누적합, 누적곱 등의 통계에서 많이 사용되는 메소드
arr4 = np.arange(5) # 0 ~ 5미만의 값으로 구성된 배열 생성
print("# arr4 : ", arr4) # [0 1 2 3 4]
print(f"합계 : {arr4.sum()}") # 10, 배열 내 모든 요소의 합
print(f"평균 : {arr4.mean()}") # 2.0, 배열 내 모든 요소의 평균
print(f"표준편차 : {arr4.std()}") # 1.4142135623730951, 표준편차란 평균으로부터 얼마나 떨어져 있는지를 나타내는 지표
print(f"분산 : {arr4.var()}") # 2.0, 분산이란 편차의 제곱의 평균
print(f"최대값 : {arr4.max()}") # 4, 배열 내 최대값
print(f"최소값 : {arr4.min()}") # 0, 배열 내 최소값
print(f"중앙값 : {np.median(arr4)}") # 2.0, 중앙값이란 데이터를 크기 순서대로 정렬했을 때 가장 중앙에 위치하는 값
print(f"누적합 : {arr4.cumsum()}") # [ 0  1  3  6 10], 누적합이란 배열의 각 요소를 순서대로 더한 값
print(f"누적곱 : {arr4.cumprod()}") # [0 0 0 0 0], 누적곱이란 배열의 각 요소를 순서대로 곱한 값

# 배열 인덱싱
arr5 = np.arange(1, 6)
print("# arr5 : ", arr5) # [1 2 3 4 5]
print("# arr5[0] : ", arr5[0]) # 1
# 슬라이싱
new_arr = arr5[1:3] # 1행에서 3행 인덱스 미만의 값을 슬라이싱
print("# new_arr : ", new_arr) # [2 3]

# Universal 함수 : 배열의 원소별 연산을 지원하는 함수, 배열의 각 요소에 대한 반복적인 계산을 빠르게 수행
# 산술연산 : add(), subtract(), multiply(), divide(), power(), mod(), remainder(), divmod(), fmod(), abs(), fabs(), rint(), sign(), heaviside(), conj(), exp(), exp2(), log(), log2(), log10(), expm1(), log1p(), sqrt(), square(), cbrt(), reciprocal(), gcd(), lcm()
# 삼각함수 : sin(), cos(), tan(), arcsin(), arccos(), arctan(), arctan2(), hypot(), sinh(), cosh(), tanh(), arcsinh(), arccosh(), arctanh(), deg2rad(), rad2deg(), degrees(), radians()
# 지수와 로그 :  exp(), exp2(), log(), log2(), log10(), expm1(), log1p(), logaddexp(), logaddexp2()
# 집계함수 : sum(), prod(), mean(), std(), var(), min(), max(), argmin(), argmax(), median(), percentile(), any(), all()
# 논리함수 : logical_and(), logical_or(), logical_xor(), logical_not()
# 비교함수 : greater(), greater_equal(), less(), less_equal(), not_equal(), equal()
# 기타 : copysign(), nextafter(), spacing(), modf(), ldexp(), frexp(), fmod(), floor(), ceil(), trunc(), angle(), real(), imag(), fix(), i0(), sinc()

xx = np.arange(0., 2*np.pi, 0.1)
yy = np.sin(xx)
print("# xx : ", xx) # 0부터 2파이(6.283185307179586...)까지 0.1씩 증가하는 배열 생성
print("# yy : ", yy) # xx 배열의 각 요소에 대한 sin() 함수의 결과를 저장한 배열

matrix1 = np.array([[1, 2], [4, 5]])
matrix2 = np.array([[5, 6], [7, 8]])
# 행렬 덧셈
res = np.add(matrix1, matrix2)
print("# res : ", res) # [[ 6  8]
                       #  [11 13]]

# 정렬과 탐색 : 배열의 정렬과 탐색을 위한 함수와 메소드
xxx = np.array([9,8,7,2,3,4,6,11])
print("# xxx : ", xxx) # [ 9  8  7  2  3  4  6 11]
print(np.amin(xxx)) # 배열 내 최소값 : 2
print(np.amax(xxx)) # 배열 내 최대값 : 11
print(np.max(xxx)) # 배열 내 최대값 : 11
print(np.argmin(xxx)) # 배열 내 최소값의 인덱스 : 3
print(np.sort(xxx)) # 배열 내 요소를 오름차순 정렬 : [ 2  3  4  6  7  8  9 11]
print(np.sort(xxx)[::-1]) # 배열 내 요소를 내림차순 정렬 : [11  9  8  7  6  4  3  2]))
print(np.argsort(xxx)) # 배열 내 요소의 인덱스를 오름차순 정렬 : [3 4 5 6 2 1 0 7]

# 브로드캐스팅 : 배열의 크기가 다른 배열끼리 연산을 수행할 수 있도록 배열의 크기를 동적으로 변환하는 기능
ax = np.array([1, 2, 3]) # 1차원 배열
bx = np.array([[4], [5], [6]]) # 2차원 배열 (3 * 1)로 구성된 2차원 배열
cx = ax + bx
print("# cx : ", cx) # [[5 6 7]
                     #  [6 7 8]
                     #  [7 8 9]]