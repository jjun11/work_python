# 테스트 케이스 개수 입력
C = int(input())

for a in range(C):
    # 학생 수와 점수를 입력받음
    data = list(map(int, input().split()))
    N = data[0]  # 학생 수
    scores = data[1:]  # 점수 리스트

    # 평균 계산
    average = sum(scores) / N

    # 평균을 넘는 학생들의 비율 계산
    count = 0
    for score in scores:
        if score > average:
            count += 1

    # 비율 계산 및 출력
    ratio = (count / N) * 100
    print(f'{ratio:.3f}%')
