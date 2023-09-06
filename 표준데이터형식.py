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
str1 = "Hello Python!!!!"
print(str1)
print(str1[0]) #인덱싱
print((str1[2:5])) # 2번 인덱스에서 5번 인덱스 미만
print(str1[2:])
print(str1 * 3)
print(str1 + "TEST")

# 형변환 : 파이선은 값이 할당되는 순간 형이 결정됨, 이후 데이터형을 변경하고자 할 때 형변환을 사용
print(10+int("10"))
print("나이 : " + str(30))
print(1+3.141592+float("4.44"))