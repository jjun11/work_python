# 이름과 나이 정보가 기록된 sample02.txt 파일이 있음
# 이 파일을 이용해 미성년자 여부를 체크하는 프로그램 작성
# 프로그램 데이터를 저장할 파일 객체 myfile2 생성
# 반복문을 사용하여 split(',') 함수 사용하여 데이터 분리
# 2번째 열 정보가 나이를 의미하므로 19세 이상인지 아닌지에 따라 '성인', '미성년'으로 분기처리
# 결과 내용 슬래시(/) 사용하여 문자열 결합
# 최종결과를 mylife2 객체에 저장 후 close() 함수를 사용해 파일을 종료

with open("sample02.txt", "r", encoding="utf-8") as myfile1, \
   open("result02.txt", "w", encoding="utf-8") as myfile2:

   for line in myfile1:
    name, ag = line.strip().split(',')

    age = int(ag)

    if age >= 19:
     adult = "성인"

    else:
     adult = "미성년"

    result = f"{name}/{age}/{adult}\n"
    myfile2.write(result)
    print(result)