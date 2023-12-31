# 내장함수 : 파이썬이 기본적으로 제공, import 가 필요 없음
# 외장함수 : 파이썬이 기본적으로 제공, import 가 필요함

# 큰값, 작은값 찾기
# print(max(1,2,3,4,45,56,7,777,88,99,100)) # 제일 큰값
# print(min(1,2,3,4,45,56,7,777,88,99,100)) # 제일 작은값
#
# # 총 합 구하기
# print(sum([1,2,3,4,45,56,7,777,88,99,100])) # 리스트에 대한 총합
# print(sum((1,2,3,4,45,56,7,777,88,99,100))) # 튜플에 대한 총합

# num = list(map(int, input("정수값 입력 : ").split()))
# print(f"입력받은 수의 총합 : {sum(num)}")
# print(f"입력받은 수의 평균 : {sum(num)/len(num)}")

# 몫과 나머지 구하기
# print(f"몫과 나머지 : {divmod(10, 4)}") # 튜플의 동작 원리, 두개의 반환값으로 받음

#정렬
# print(sorted([1, 3, 5, 67, 45, 34, 3124, 1123, 4, 23], reverse=True)) # 내림차순
# print(sorted([1, 3, 5, 67, 45, 34, 3124, 1123, 4, 23],)) # 오름차순

# 여러개의 값을 한번에 입력받아 리스트로 만들기
# 최대값, 최소값, 합계, 평균

num = list(map(int, input("값 입력 : ").split()))
print(f"""최대값 : {max(num)}
최소값 : {min(num)}
합계 : {sum(num)}
평균 : {sum(num)/len(num):.2f}
합계에 대한 몫과 나머지 : {divmod(sum(num), 5)}""")