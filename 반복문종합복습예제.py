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

#강사님 풀이 v

# def input_age() :
#  while True :
#     age = input("나이를 입력하세요 : ")
#     if age.isdigit() : # (isdigit)입력받은 문자열이 숫자로 구성되어있는지 확인
#         age = int(age)
#         if 0 < age < 200 : return age
#     print("나이를 잘 못 입력하셨습니다.")
# def input_gender() :
#     while True :
#         gender = input("성별을 입력하세요 : ")
#         if gender == 'M' or gender == 'm' : return "남성"
#         elif  gender == 'F' or gender == 'f' : return "여성"
#         print("성별을 잘 못 입력하셨습니다.")
#
# def input_jobs() :
#     while True :
#         jobs = input("직업을 입력하세요 : ")
#         if jobs.isdigit() :
#             jobs = int(jobs)
#             if 0 < jobs < 5: return jobs
#         print("직업을 잘 못 입력하셨습니다.")
#
# def print_info(name, age, gender, jobs) :
#     jobs_str = "", "학생", "회사원", "주부", "무직"
#     print("=" * 3, "회원정보", "=" * 3)
#     return f"이름 : {name}\n나이 : {age}\n성별 : {gender}\n직업 : {jobs_str[jobs]}"
#
# # 함수는 선언 이후 호출해야 동작함
# member_info = "member.txt"
# fd = open(member_info, "wt", encoding="utf-8")
# while True:
#     name = input("이름을 입력하세요(종료하려면 quit) : ")
#     if name == 'quit' : break
#     age= input_age()
#     gender = input_gender()
#     jobs = input_jobs()
#     rst = print_info(name, age, gender, jobs)
#     fd.write(rst + "\n")
# fd.close()

# while True :
#     age = input("나이를 입력하세요 : ")
#     if age.isdigit() : # (isdigit)입력받은 문자열이 숫자로 구성되어있는지 확인
#         age = int(age)
#         if 0 < age < 200 : break
#     print("나이를 잘 못 입력하셨습니다.")
#
# while True :
#     gender = input("성별을 입력하세요 : ")
#     if gender == 'M' or gender == 'm' or gender == 'F' or gender == 'f' : break
#     print("성별을 잘 못 입력하셨습니다.")
#
# while True :
#     jobs = input("직업을 입력하세요 : ")
#     if jobs.isdigit() :
#         jobs = int(jobs)
#         if 0< jobs < 5 : break
#         print("직업을 잘 못 입력하셨습니다.")
#
# if gender == 'M' or gender == 'm' : gen_str = "남성"
# else : gen_str = "여성"
#
# jobs_str = "", "학생", "회사원", "주부", "무직" # 튜플
#
# print("="*3, "회원정보", "="*3)
# print(f"""이름 : {name}
# 나이 : {age}
# 성별 : {gen_str}
# 직업 : {jobs_str[jobs]}
# """)
#================================================================================
# 핸드폰요금 계산하기
# 영식 요금제 : 30초에 10원
# 민식 요금제 : 60초에 15원
# n = int(input()) # 통화 횟수
# call = list(map(int, input().split())) # 통화 횟수에 대한 통화시간
# y_pay = m_pay = 0
# for i in range(n) :
#     y_pay += (call[i] // 30) * 10 + 10
#     m_pay += (call[i] // 60) * 15 + 15
#
# if y_pay > m_pay:
#     print('M', m_pay)
# elif y_pay < m_pay:
#     print('Y', y_pay)
# else :
#     print('Y M', y_pay)

# 대소문자 바꾸기
# 영어 소문자와 대문자로 이루어진 단어를 입력받은 뒤, 대문자는 소문자로, 소문자는 대문자로 바꾸어 출력하는 프로그램을 작성하시오.

# rst = ""
# for e in input() : # 입력받는 문자열 만큼 자동순회
#     if e.islower():
#         rst += e.upper()
#     else :
#         rst += e.lower()
# print(rst)

# 숫자의 개수
# A= 150, B = 266, C = 427 이라며 A x b x c = 150 * 266 * 427 = 17037300
# 1부터 9까지의 숫자가 각각 몇번 쓰였는지 차례로 한 줄에 하나씩 출력
a, b, c = map(int,input("정수 3개 입력 : ").split())
total_val = str(a * b * c) # a * b * c 결과를 문자열로 변환
for i in range(10) :
    print(total_val.count(str(i)))