# 인덱싱과 슬라이싱
jumin = "991120-1234567"

gender = jumin[7] #성별
print(jumin[:2]) # -
year = jumin[:2] # 출생년도, 2번인덱스 미만
month = jumin[2:4] # 출생월, 2번인덱스부터 4번인덱스 미만
day = jumin[4:6] # 일

print("생년월일 : " + jumin[:6])
print("뒤 7자리 : " + jumin[7:]) # 7번인덱스부터 ~
print("뒤 7자리 : " + jumin[-7:]) # 뒤에서 7번인
