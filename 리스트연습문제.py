# 상근날드
# 햄버거는 총 3종류 상덕버거, 중덕버거, 하덕버거가 있고, 음료는 콜라와 사이다 두 종류가 있다.
# 세트로 구매하면 가격의 합계에서 50원을 뺀 가격이 세트의 가격이 됨
# 햄버거 = []
# 음료수 = []
# for hbg in range(3):
#     hbg = int(input("햄버거 값 입력 : "))
#     햄버거.append(hbg)
# for drk in range(2):
#     drk = int(input("음료수 값 입력 : "))
#     음료수.append(drk)
# print(f" 가장 저렴한 세트의 가격은 {min(햄버거)+min(음료수)-50} 입니다.")
#--------------------------------------강사님 풀이 -------------------------------------------------
# ls = list(map(int, input().split()))
# min_b = min(ls[:3])
# min_d = min(ls[3:5])
# print(f"{min_b + min_d - 50}")
#==================================================================================================
#저항
# color = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
# count = []
# for c in range(3):
#     c = input("색깔 입력 : ")
#     count.append(c)
# print(f"{((color.index(count[0])*10)+(color.index(count[1])))*10**(color.index(count[2]))}")
#---------------------------------------강사님 풀이 -------------------------------------------------
# color = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
# f_name = color.index(input()) # input() 으로 입력받은 문자열이 color 튜플내의 인덱스로 반환
# s_name = color.index(input())
# t_name = color.index(input())
# print(int(str(f_name)+str(s_name)))*(10**t_name)
#==================================================================================================
# PC방 알바, 중급에서 검색
# 1 ~ 100번까지의 컴퓨터가 있음
# 손님은 자신이 앉고 싶어하는 자리를 선택하고자 합니다. 이미 예약된 자리는 선택할 수 없으므로 거절
seat_num = list(map(int, input().split()))
pc = [0] * 100 # 0으로 초기화 된 100개의 리스트 생성
cnt = 0
for e in seat_num : # 향상된 for문 이므로 e값은 고객이요청한 좌석번호
    if pc[e-1] != 0: cnt += 1
    else : pc[e -1] =1
print(cnt)

# 4번 : Knuth-Mrris-Pratt => KMP, Mirko-Slavko => MS
upper_str = ""
for r in input() : # 입력받는 개수만큼 자동 순회
    if e.isupper() : upper_str += e
print(upper_str)