# 테스트 케이스 개수 입력
# 5 => 총테스트 횟수
# 5 50 50 70 80 100 > 각 케이스마다 평균이 넘는 % 구하기
# 7 100 95 90 80 70 60 50
# 3 70 90 80
# 3 70 90 81
# 9 100 99 98 97 96 95 94 93 91
# 강사님 답안
def over_rate() : # 각 케이스에서 평균이 넘는 비율 구하기
    ls = list(map(int, input().split())) # 공백 기준으로 입력받아 정수형 리스트로 담음
    average = sum(ls[1:]) / len(ls[1:]) # 리스트에서 맨 앞의 요소는 인원수이므로 제외, 총합 / 인원수 = 평균
    cnt = 0 # 평균이 넘는 %를 구하기 위해서는 인원에 카운트가 필요
    for i in range(1, len(ls)): # 맨 앞의 요소는 인원수이므로 제외함
        if ls[i] > average : cnt += 1
    return cnt / (len(ls)-1) * 100 # 백분율 표기로 변경

n = int(input()) # 총 테스트 횟수
rst = [] # 각 케이스에 대한 결과값을 받기 위한 리스트
for i in range(n) : # 총 테스트 횟수만큼 반복수행
    rst.append(over_rate())

for e in rst :
    print(f"{e:.3f}%")

# Chat GPT 답안 ==================================================================================
# C = int(input())
#
# for a in range(C):
#     # 학생 수와 점수를 입력받음
#     data = list(map(int, input().split()))
#     N = data[0]  # 학생 수
#     scores = data[1:]  # 점수 리스트
#
#     # 평균 계산
#     average = sum(scores) / N
#
#     # 평균을 넘는 학생들의 비율 계산
#     count = 0
#     for score in scores:
#         if score > average:
#             count += 1
#
#     # 비율 계산 및 출력
#     ratio = (count / N) * 100
#     print(f'{ratio:.3f}%')
