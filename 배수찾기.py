# num = []
# while True:
#     n = int(input("수 입력 : "))
#     if 1000 < n or n < 0:
#      print("수를 잘못 입력하셨습니다.")
#      continue
#     if n == 0:
#      break
#     num.append(n)
#     print(num)
#
# for e in range(1, len(num)):
#     if num[e] % num[0] == 0:
#         print(f"{num[e]} is a multiple of {num[0]}")
#     else:
#         print(f"{num[e]} is NOT a multiple of {num[0]}")

#강사님풀이 ----------------------------------------------------------------
n = int(input()) #문자열로 반환되기 때문에 정수타입으로 변환
ls = [] # 빈 리스트 생성
while True : # 0 입력되기 전까지 반복수행
    x = (int(input())) # 목록의 수를 입력받음
    if x == 0 : break # 0이 입력되면 탈출
    ls.append(x)

for e in ls :
    if e % n == 0 : print(f"{e} is a multiple of {n}.")
    else : print(f"{e} is NOT a multiple or {n}.")