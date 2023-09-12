# A : 고정비용
# B : 가변비용
# C : 노트북가격
# n : 생산대수
# 손익분기점 : A+(B*n) < (C*n)
# 내풀이 = 풀다말았음
# check = []
# while True :
#     check = list(map(int, input("고정비용, 가변비용, 노트북가격 입력 : ").split()))
#     A = check[0]
#     B = check[1]
#     C = check[2]
#     n = 0
#     if B > C :
#         print("노트북 가격이 너무 낮습니다.")
#         continue
#
#     for e in check :
#         e > 2100000000
#         print("각 비용은 21억을 초과할 수 없습니다.")
#         continue
#     while True :
#         n += 1
#         if A+(B*n) < (C*n) :
#             break
#     print(n)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#강사님풀이
fix, var, sell = map(int, input().split())
# cnt = 0
# while True :
#     # if fix + (var * cnt) < sell * cnt : break
#     if(cnt > fix // (sell - var)) : break # 생산대수가 1000 / 100
#     cnt +=1
# print(cnt)
if sell <= var : print(-1)
else : print(fix // (sell-var)+1)