#회원정보 출력하기
# 회원정보를 입력 받아서 출력 하는 예제 진행
#
# - 이름 입력
# - 나이 입력 : 1 ~ 199까지 입력 받고 잘못된 값이 오면 재 입력 요청을 한다.
# - 성별 입력 : 영문자 (M과m은 남성) (F와 f는 여성)으로 입력 받고 나머지는 재 입력 요청을 한다.
# - 직업 입력 : 1(학생), 2(회사원), 3(주부), 4(무직)으로 입력 받고 나머지는 재 입력 요청 한다.
# - 결과는 마지막에 한번에 출력 한다.

# name = input("이름을 입력하세요 : ")
# while True:
#     age = int(input("나이를 입력하세요 : "))
#     if 199 < age < 0 :
#         print("잘못된 입력입니다 재 입력해주세요.")
#     else : break
# while True:
#     gen = input("성별을 입력하세요 : ")
#     if gen == "M" or gen =="m" or gen == "F" or gen == "f":
#         if gen =="M" or gen =="m" : gender = "남성"
#         else : gender = "여성"
#         break
#     else :
#         print("잘못된 입력입니다. 재 입력해주세요")
#         continue
# while True:
#     j = input("직업을 입력하세요 [1]학생 [2]회사원 [3]주부 [4]무직 : ")
#     if j == "1" or j == "2" or j == "3" or j == "4":
#         if j == "1" : job = "학생"
#         if j == "2" : job = "회사원"
#         if j == "3" : job = "주부"
#         if j == "4" : job = "무직"
#         break
#     else :
#         print("잘못된 입력입니다 재 입력해주세요.")
#         continue
# print(f"이름 : {name}")
# print(f"나이 : {age}세")
# print(f"성별 : {gender}")
# print(f"직업 : {job}")

#핸드폰요금 계산하기

n = int, input("통화 횟수를 입력하시오. : ")
print(n)
