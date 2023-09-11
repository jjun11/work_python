# 집합이란 중복 제거를 목적으로 자주 사용됨
# 순서가 보장되지않음
# 중복 불가
# mutable 특성을가짐
s1 = set([1,2,3,4,5])
s2 = set([4,5,6,7,8])
s3 = set([1,2,3,4,5,1,2,3,4,5,1,2,3])
print(s3) # {1,2,3,4,5}

# 합집합 : 양쪽에 존재하는 모두
print(s1.union(s2)) # {1, 2, 3, 4, 5, 6, 7, 8}
print(s1 | s2) # {1, 2, 3, 4, 5, 6, 7, 8}

# 교집합 : 양쪽에 공통적으로 존재하는 것
print(s1.intersection(s2)) # {4, 5}
print(s1 & s2) # {4, 5}

# 차집합 : 집합에서 앞에서 뒤를 빼서 남은 것
print(s1.difference(s2)) # {1, 2, 3}
print(s1 - s2) # {1, 2, 3}

import random
nums = set()
while True :
    num = random.randrange(1, 46)
    nums.add(num)
    if len(nums) == 6:break
print(nums)