import pandas as pd
import numpy as np

# 판다스 : 데이터 분석과 조작을 위한 라이브러리, 데이터를 구조화하고 저장, 처리, 분석을 수행

s1 = pd.Series([10, 20, 30, 40, 50])
print("# s1 : ", s1)
print("# s1.index : ", s1.index)
print("# s1.values : ", s1.values)
print("# s1.dtype : ", s1.dtype)

# 판다스는 원소의 데이터 타입이 달라도 가능
s2 = pd.Series(['a', 'b', 'c', 1, 2, 3])
print("# s2 : ", s2)
print("# s2.dtype : ", s2.dtype)

# 데이터가 없는 경우 np.nan 으로 표시 가능
s3 = pd.Series([np.nan, 10, 30])
print("# s3 : ", s3)

# Series 데이터 생성 시 인덱스 추가 기능
index_date = ['2023-09-15', '2023-09-16', '2023-09-17', '2023-09-18']
s4 = pd.Series([200, 195, np.nan, 205], index=index_date)
print("# s4 : ", s4)

# 파이썬의 딕셔너리 이용
s5 = pd.Series({'국어': 100, '영어': 95, '수학': 90})
print("# s5 : ", s5)