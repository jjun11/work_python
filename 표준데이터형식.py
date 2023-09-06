# 값을 할당하는 방법
a = b = c = 1
print(a, b, c)

a, b, c = 1, False, "곰돌이사육사" # 여러개의 변수를 한번에 대입
print(a, b, c)

# 타입 확인
# age=input("나이를 입력 하세요 : ")
# print(type(age))

value = 0O20
print(value)
# 0o : 8진수 // 0x : 16진수 // 0b : 2진수(대소문자 구분X)''

# 불리언 타입 : 참과 거짓의 값을 가짐
print(bool(1)) # 참
print(bool(0)) # 거짓
print(bool(-1000)) # 참
print(bool("")) # 거짓
print(bool(None)) # 거짓

# 문자열 타입 :