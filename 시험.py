from mpmath import mp

# 원하는 정밀도로 mp 파이 값을 설정
mp.dps = 200000  # 예: 50 자릿수의 정밀도

# mp 파이 값을 출력
pi_value = mp.pi
print(pi_value)