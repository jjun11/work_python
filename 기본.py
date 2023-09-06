print("Hello, world")
print('Hello, world')
print(100)
print(33.33)
print(100+23)
# 주석
# 범위주석 """("3개) ~~~~ """
""""
여기는 범위 주석구간 입니다.
dflwkefnsdkfkdsk
"""

# 변수를 선언하고 값을 대입
num = 100 + 254  # 데이터형은 값이 대입되는 순간에 결정남
print(num) # 354
num = "100"
print(num) # 100

# 변수 활용
name = "곰돌이사육사"
email = ("jks2024@gmail.com")
age = 25
addr = '서울시 강남구 역삼동 KH정보교육원'

print(f""""
이름 : {name}
이메일 : {email}
나이 : {age}
주소 : {addr}
""")

print("""
이름 : {name}
이메일 : {email}
나이 : {age}
주소 : {addr}""")

# 파이썬은 불리언 값이 대문자로 시작
isAdult = True

if isAdult :
    print("나는 성인 입니다.")
else :
    print("나는 성인이 아닙니다.")


"""
        작성자 : 곰돌이사육사
        수정날짜 : 2023.09.06    
"""

'''
            작성자 : 곰돌이사육사
            수정날짜 : 2023.09.06    
'''

print([1,2,3]) #리스트 출력
