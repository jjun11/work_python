# all = []
# while True:
#  a = list(map(int,input("변 길이 : ").split()))
#  if a == [0, 0, 0]:
#   break
#  if len(a) !=3:
#   print("숫자는 세 가지만 입력 가능합니다.")
#   continue
#  all.append(a)
#
# for e in range(0, len(all)):
#  if all[e][0]**2 + all[e][1]**2 == all[e][2]**2 :
#   print("right")
#  else:
#   print("wrong")

# 강사님풀이 -----------------------------------------------------------------
rst = [] # 결과를 출력하기 위한 빈 리스트
while True :
 li = list(map(int, input().split()))
 li.sort()
 if li[0] == 0 and li[1] == 0 and li[2] == 0 : break
 elif li[2] ** 2 == li[1] ** 2 + li[0] ** 2 :
    rst.append("right")
 else : rst.append("wrong")

for e in rst : print(e)