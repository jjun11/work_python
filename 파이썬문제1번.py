# 1. 정해진 형식으로 시간을 입력받아서 출력하기
# 입력 형식 : 22:5:5 = > 오후 10시 05분 05초

# 내 풀이
# hour, min, sec = map(int, input("시간 입력(h:m:s) : ").split(":"))
# if(hour > 12):
#     hour -= 12
#     print(f"오후{hour:02}시{min:02}분{sec:02}초")
# else:
#     print(f"오후{hour:02}시{min:02}분{sec:02}초 입니다.")
# 2. 3개의 정수를 입력받아 최대값과 최소값 구하기

# num1 = int(input("첫번째 정수를 입력하세요. : "))
# num2 = int(input("두번째 정수를 입력하세요. : "))
# num3 = int(input("세번째 정수를 입력하세요. : "))
# sum = num1 + num2 + num3
# print(f"세 정수의 합은 {sum} 입니다.")

# 3번. 주민등록번호를 입력받아 생년월일, 성별, 나이 출력
# jumin = input("주민등록번호를 입력해주세요 : ")
#
# gender = int(jumin[7])
# year = int(jumin[:2])
# ymd = int(jumin[0:6]) # 생년월일
# if gender < 3 : age = (2024-1900-year)
# else : age = (2024-2000-year)
# if gender %2 == 0 : gender = "여자"
# else : gender = "남자"
# print("생년월일 :", ymd)
# print("성별 :", gender)
# print("나이 : ", age)

#강사님풀이
# from datetime import datetime
#
# curr_year = datetime.today().year
# jumin = input("주민등록번호 : ")
# year = int(jumin[:2])
# gender = int(jumin[7])
# month = int(jumin[2:4])
# day = int(jumin[4:6])
#
# if gender == 1 or gender == 2:
#     age = curr_year - 1900 - year
# else :
#     age = curr_year - 2000 - year
# if gender == 1 or gender == 3:
#     gender_str = "남성"
# else:
#     gender_str = "여성"
#
# print(f"생년월일 : {year:02}년 {month:02}월 {day:02}일")
# print(f"성별 : {gender_str}")
# print(f"나이 : {age}")


# 4번. 정해지지 않은 여러개의 정수를 입력받아 합계와 평균 구하기

# 강사님풀이
score = list(map(int, input("정수 : ").split()))
print(score)
print(f"총점 : {sum(score)}")
print(f"평균 : {sum(score)/len(score)}")

