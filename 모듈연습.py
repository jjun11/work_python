#import math # math 모듈을 사용하기 위해서 import 함

# print(math.sin(1))
# print(math.cos(1))
# print(math.tan(1))
 #  모듈 내에 특정 함수(메서드) 특정한 함수만 가져오고자 하는 경우-----------------------------------------------------------
# from math import sin, cos, tan
# print(sin(1)) # from 을 통해 모듈안의 특정함수를 가져온 경우는 math. 처럼 앞의 모듈이름은 생략가능
# print(cos(1))
# print(tan(1))
# 모듈을 가져 올 때 충돌이나 긴 이름을 간결하게 사용하기 위해 별칭 부여 (별칭을 부여하면 원래 이름은 사용안됨)----------------------
# import math as m
# print(m.sin(1))
# # print(math.cos(1)) # 에러
#
# # sys 모듈 : 시스템과 관련된 정보를 가지고 있는 모듈---------------------------------------------------------------------
# import sys
# print("명령 줄 인수 : ", sys.argv ) # 명령 줄 인수 :  ['D:\\dev\\work_python\\모듈연습.py']
# print("실행 경로 : ", sys.path[0] ) # 실행 경로 :  D:\dev\work_python
# sys.stdout.write("Hello, world!!!\n") # Hello, world!!!
# sys.exit(0) # 강제 종료

# os 모듈 : 운영체제와 상호 작용하기위한 기능을 제공 (파일 시스템 접근, 환경 변수 제어, 프로세스 관리 등)---------------------------
import os
cwd = os.getcwd() # 현재 작업 디렉터리
print("현재 작업 디렉터리 : ", cwd) # 현재 작업 디렉터리 :  D:\dev\work_python
# 디렉터리 생성
is_dir = os.path.isdir("testDir")
# os.mkdir("testDir") # 디렉터리 생성, 이미 같은이름의 디렉터리가 있는경우 죽음
if not is_dir : os.mkdir("testDir") # if not is dir 로 같은이름이 없는경우만 생성, 즉 같은디렉터리가 있어도 죽지않음
is_file = os.path.isfile("score.txt")
print(is_file) # True

os.system("pwd")